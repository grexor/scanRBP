# Quick Start

## Scoring a single sequence

Give scanRBP a sequence directly on the command line, plus an output name:

```bash
scanRBP AAAGCGGCGACTTATTATATCCCCATATATTATATCTTCTTCTCTTATATATAAACCAGAGATAGATGTGTGTGGTGG example1 -heatmap example1
```

This scores the sequence against every RBP motif in the database and writes:

- `example1.tab.gz` — the log-odds score matrix (proteins × positions), gzipped TSV.
- `example1.png` / `example1.pdf` — a clustered heatmap of the scores (only produced when `-heatmap` is given).

## Scoring a FASTA file

Point scanRBP at a FASTA file instead, and it scores every sequence in it, producing one matrix (and, with `-heatmap`, one heatmap) per sequence, named after that sequence's FASTA id:

```bash
scanRBP data.fasta -heatmap data
```

## Reading the heatmap

Rows are RBPs (clustered by similarity of their binding profile across the sequence), columns are sequence positions. Warmer cells mean a stronger predicted binding signal at that position for that RBP; cooler/negative cells mean the position looks less like that RBP's motif than background.

## Next steps

- [Motif database & search](motifs.md) — which RBPs are available, and how to search for one by name.
- [Scoring sequences](scoring.md) — the full set of options: limiting to specific proteins, heatmap styling, cumulative plots across many sequences.
- [CLIP-based scoring](clip.md) — score against real binding evidence instead of a PWM.
- [Python API](python-api.md) — call scanRBP from your own Python code.
