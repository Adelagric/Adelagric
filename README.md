# Adel Kaleche

I write Rust and hunt silent failures: the kind where a program returns a plausible answer and nothing tells you it's wrong.

## Building

- [vivacity](https://github.com/Adelagric/vivacity) — `composer install` and `composer update`, reimplemented in Rust. Same `composer.json` in, same `vendor/` and lock file out as Composer, byte for byte. No PHP needed.
- [ocs-rs](https://github.com/Adelagric/ocs-rs) — exact, matrix-free solver for optimum contribution selection in breeding programs. It never forms the dense relationship matrix, so it runs at population sizes where the reference tool can't.
- [vector-router](https://github.com/Adelagric/vector-router) — gRPC middleware that rejects NaN, Inf and out-of-range vectors before they reach a vector database.

## Upstream

Most of my time goes into other people's code. The bugs I keep finding fall into four buckets:

- **Data dropped without an error.** Vector's file source on stale checkpoints, mem0 on partial embedding failures, one bad span discarding a whole ingestion batch in future-agi, conda leaving half-created environments on disk, OpenFisca and PolicyEngine losing memberless group entities on `restore_simulation`.
- **Corrupt state accepted as valid.** NaN vectors in Qdrant and Weaviate, checkpoints published without a directory fsync and no fail-closed latch after a failed fsync in rostam.
- **Numbers that are quietly wrong.** rust-bio's pair HMMs: gap extensions that emit no base, gaps opened with the other sequence's probability, stale cells left outside the band, column ends summed twice.
- **Tools that drift from their reference.** OpenFisca simulation clones sharing state with the original, `freebayes-parallel` disagreeing with a single run at region boundaries, Composer failing instead of explaining a security block.

Merged in rust-bio, rostam, conda, OpenFisca, varlociraptor, dna-seq-varlociraptor. Open in ClickHouse, Vector, Composer, Weaviate, mem0, freebayes, PolicyEngine, microlp, ollama.

## How I work

Reproduce first. Every issue I open ships with a standalone reproduction, every fix with a test that fails without it.

Mostly bioinformatics these days: pair HMM correctness and speed in rust-bio and varlociraptor (a linear-space forward algorithm is in review in both), freebayes, and the dna-seq-varlociraptor workflow that ties them together.

[kaleche.dev](https://kaleche.dev)
