"""Refresh the generated blocks of README.md from the GitHub and crates.io APIs."""
import json
import os
import re
import urllib.parse
import urllib.request
from collections import Counter

USER = "Adelagric"
CRATE = "vivacity"

# Display name per upstream repository; anything missing falls back to the repo name.
NAMES = {
    "rust-bio/rust-bio": "rust-bio",
    "rostamlabs/rostam": "rostam",
    "conda/conda": "conda",
    "openfisca/openfisca-core": "OpenFisca",
    "varlociraptor/varlociraptor": "varlociraptor",
    "snakemake-workflows/dna-seq-varlociraptor": "dna-seq-varlociraptor",
    "ClickHouse/ClickHouse": "ClickHouse",
    "vectordotdev/vector": "Vector",
    "composer/composer": "Composer",
    "weaviate/weaviate": "Weaviate",
    "weaviate/weaviate-github-issue-triage": "Weaviate",
    "mem0ai/mem0": "mem0",
    "freebayes/freebayes": "freebayes",
    "PolicyEngine/policyengine-core": "PolicyEngine",
    "Specy/microlp": "microlp",
    "ollama/ollama": "ollama",
}
# Draft proposals on friends' repositories, not upstream contributions.
EXCLUDED = {"Nasism/axioma"}


def get(url, headers=None):
    req = urllib.request.Request(url, headers={"User-Agent": f"{USER}-profile-stats", **(headers or {})})
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def search_prs(state):
    headers = {"Accept": "application/vnd.github+json"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    q = f"author:{USER} is:pr is:{state} -user:{USER}"
    repos, page = [], 1
    while True:
        data = get(
            "https://api.github.com/search/issues?"
            + urllib.parse.urlencode({"q": q, "per_page": 100, "page": page}),
            headers,
        )
        for item in data["items"]:
            repo = item["repository_url"].split("/repos/", 1)[1]
            if repo not in EXCLUDED:
                repos.append(repo)
        if len(data["items"]) < 100:
            return repos
        page += 1


def name(repo):
    return NAMES.get(repo, repo.split("/", 1)[1])


def replace(text, marker, body):
    pattern = re.compile(rf"(<!-- {marker}:start -->\n).*?(\n<!-- {marker}:end -->)", re.S)
    if not pattern.search(text):
        raise SystemExit(f"marker {marker} not found")
    return pattern.sub(lambda m: m.group(1) + body + m.group(2), text)


merged = Counter(name(r) for r in search_prs("merged"))
open_projects = []
for project in (name(r) for r in search_prs("open")):
    if project not in merged and project not in open_projects:
        open_projects.append(project)

stars = get(f"https://api.github.com/repos/{USER}/{CRATE}")["stargazers_count"]
downloads = get(f"https://crates.io/api/v1/crates/{CRATE}")["crate"]["downloads"]

total = sum(merged.values())
ranked = sorted(merged.items(), key=lambda kv: (-kv[1], kv[0].lower()))
merged_list = ", ".join(f"{p} ({n})" if n > 1 else p for p, n in ranked)

stats = (
    f"**{total} merged pull requests** upstream, in {len(merged)} projects. "
    f"vivacity: {stars} stars, {downloads} downloads on crates.io. "
    "One of my projects ships inside someone else's product."
)
lists = (
    f"**Merged in** {merged_list}. "
    "Welcomed as a first-time contributor in conda's July 2026 release notes.\n\n"
    f"**Open in** {', '.join(open_projects)}."
)

with open("README.md") as f:
    readme = f.read()
readme = replace(readme, "stats", stats)
readme = replace(readme, "upstream", lists)
with open("README.md", "w") as f:
    f.write(readme)
