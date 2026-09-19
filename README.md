# Adel Kaleche

I write Rust and hunt silent failures: the kind where a program returns a plausible answer and nothing tells you it's wrong.

## Building

- [vivacity](https://github.com/Adelagric/vivacity) — `composer install` and `composer update`, reimplemented in Rust. Same `composer.json` in, same `vendor/` and lock file out as Composer, byte for byte. No PHP needed.
- [ocs-rs](https://github.com/Adelagric/ocs-rs) — exact, matrix-free solver for optimum contribution selection in breeding programs. It never forms the dense relationship matrix, so it runs at population sizes where the reference tool can't.
- [vector-router](https://github.com/Adelagric/vector-router) — gRPC middleware that rejects NaN, Inf and out-of-range vectors before they reach a vector database.

## Upstream

Most of my time goes into other people's code. The bugs I keep finding fall into three buckets:

- **Data dropped without an error.** Vector's file source on stale checkpoints, mem0 on partial embedding failures, conda leaving half-created environments on disk.
- **Corrupt state accepted as valid.** NaN vectors in Qdrant and Weaviate, checkpoints published without fsync in rostam.
- **Tools that drift from their reference.** OpenFisca simulation clones sharing state, Rector dropping imports it still needs, Composer failing instead of explaining a security block.

Merged in rust-bio, conda, rostam. Open in ClickHouse, Vector, Composer, Rector, OpenFisca, Qdrant, Weaviate, varlociraptor.

## How I work

Reproduce first. Every issue I open ships with a standalone reproduction, every fix with a test that fails without it.

Lately drifting toward bioinformatics: varlociraptor, rust-bio, the dna-seq-varlociraptor workflow.

[kaleche.dev](https://kaleche.dev)
