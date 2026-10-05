# Adel Kaleche

I write Rust and hunt silent failures: the kind where a program returns a plausible answer and nothing tells you it's wrong.

**29 merged pull requests** upstream, in rust-bio, rostam, conda, OpenFisca, varlociraptor and dna-seq-varlociraptor. One of my projects ships inside someone else's product.

## Building

- **[vivacity](https://github.com/Adelagric/vivacity)** [![crates.io](https://img.shields.io/crates/v/vivacity.svg)](https://crates.io/crates/vivacity) [![downloads](https://img.shields.io/crates/d/vivacity.svg)](https://crates.io/crates/vivacity) — `composer install` and `composer update`, reimplemented in Rust. Same `composer.json` in, same `vendor/` and lock file out as Composer, byte for byte, with no PHP.
  - **Adopted by [ePHPm](https://github.com/ephpm/ephpm)**, which embeds it as `ephpm composer` ([ephpm#523](https://github.com/ephpm/ephpm/pull/523)), keeps a fork under its org, and runs a daily CI job that bumps the pin whenever a new vivacity lands on crates.io.
  - Checked against the real thing, not assumed: on a corpus of 106 real PHP projects, 75 install natively and byte-identical down to file modes; the rest are handed to Composer before any write. **No diff on any of them.**
  - 22 releases, published on crates.io as four crates (`vivacity`, `-core`, `-resolver`, `-autoload`), installable via script, `cargo binstall` or a GitHub Action.
- **[ocs-rs](https://github.com/Adelagric/ocs-rs)** [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20746987.svg)](https://doi.org/10.5281/zenodo.20746987) [![PyPI](https://img.shields.io/pypi/v/ocs-rs.svg)](https://pypi.org/project/ocs-rs/) — exact, matrix-free solver for optimum contribution selection in breeding programs. Same optimum as optiSel, the field's exact tool, and **12–132× faster** given the relationship matrix; without it, it runs at population sizes where that matrix can't be built. Validated on wheat, pig and mouse genomic panels, with a manuscript ([PDF](https://github.com/Adelagric/ocs-rs/releases/download/v0.4.0/ocs-rs-manuscript-v0.4.0.pdf), [version française](https://github.com/Adelagric/ocs-rs/releases/download/v0.4.0/ocs-rs-manuscrit-fr-v0.4.0.pdf)) and a one-command reproduction.
- **[vector-router](https://github.com/Adelagric/vector-router)** — gRPC middleware that rejects NaN, Inf and wrong-dimension vectors before they reach Qdrant or pgvector, with per-producer Prometheus metrics. Checked under miri.
- **[moment-scale-law](https://github.com/Adelagric/moment-scale-law)** — paper and code: *How fine a change can moments see? A scale law for detecting distribution shift, with a kernel calibration rule.* [Read the PDF](https://github.com/Adelagric/moment-scale-law/blob/main/docs/paper1/paper.pdf). Every number in it maps to the script that produces it.
- **[opengatellm-rs](https://github.com/Adelagric/opengatellm-rs)** [![crates.io](https://img.shields.io/crates/v/opengatellm.svg)](https://crates.io/crates/opengatellm) — Rust client for OpenGateLLM, the French government's (DINUM / Etalab) open-source LLM gateway.

## Upstream

Most of my time goes into other people's code. The bugs I keep finding fall into four buckets:

- **Numbers that are quietly wrong.** Five bugs fixed in rust-bio's pair HMMs: gap extensions that emitted no base, stale cells left outside the band, gaps opened with the other sequence's probability, column ends summed twice, hop states that could not return to every match state. All merged and released in rust-bio 4.1.0 and 4.2.1.
- **Data dropped without an error.** conda leaving half-created environments on disk (merged), OpenFisca losing memberless group entities on `restore_simulation` (merged), Vector's file source on stale checkpoints, mem0 on partial embedding failures, one bad span discarding a whole ingestion batch in future-agi.
- **Corrupt state accepted as valid.** In rostam: checkpoints published without a directory fsync, no fail-closed latch after a failed fsync, trailing bytes accepted by the log decoder; all fixed, plus fuzzing of the network and WAL-recovery decoders (8 PRs merged). NaN vectors accepted by Weaviate.
- **Tools that drift from their spec or reference.** varlociraptor scenarios with overlapping events (now checked at compile time, merged), dna-seq-varlociraptor declaring config keys it didn't read (merged), `freebayes-parallel` disagreeing with a single run at region boundaries, OpenFisca simulation clones sharing state with the original. A wrong `channelId` docstring in the x402 spec, reported with byte-exact vectors and fixed upstream.

**Merged in** rust-bio (14), rostam (8), conda (3), dna-seq-varlociraptor (2), OpenFisca, varlociraptor. Welcomed as a first-time contributor in conda's July 2026 release notes.
**Open in** ClickHouse, Vector, Composer, Weaviate, mem0, freebayes, PolicyEngine, microlp, ollama.

## How I work

Reproduce first. Every issue I open ships with a standalone reproduction, every fix with a test that fails without it.

Mostly bioinformatics these days: pair HMM correctness and speed in rust-bio and varlociraptor (a linear-space forward algorithm is in review in both), freebayes, and the dna-seq-varlociraptor workflow that ties them together.

[kaleche.dev](https://kaleche.dev)
