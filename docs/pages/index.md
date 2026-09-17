# scanRBP: RNA-protein binding toolkit

<img src="assets/scanRBP_logo.png" alt="scanRBP" style="height:60px; width:auto;">

**scanRBP** scores how strongly RNA-binding proteins (RBPs) are predicted to bind along a nucleotide sequence, using a database of pre-trained position weight matrices (PWMs), and draws the result as a heatmap.

```bash
pip install scanRBP
scanRBP AAAGCGGCGACTTATTATATCCCCATATATTATATCTTCTTCTCTTATATATAAACCAGAGATAGATGTGTGTGGTGG example1 -heatmap example1
```

!!! tip "Try it online, no installation"
    scanRBP is available directly in your browser via [expressRNA.org](https://www.expressrna.org) — go to **Analyses → New Analysis → scanRBP Analysis**.

## What it computes

For each RBP in the database, scanRBP calculates a per-position **log-odds score**: how much more (or less) likely each nucleotide is to come from that RBP's binding motif than from background sequence. Positive values mean "more consistent with the motif than background"; 0 means no preference; negative values mean "less consistent than background." See the [biopython PSSM docs](http://biopython.org/DIST/docs/tutorial/Tutorial.html) for the underlying math.

## What's included

- **PWM-based scanning** — score a sequence (or every sequence in a FASTA file) against ~100+ RBP motifs from the [mCross](https://www.sciencedirect.com/science/article/pii/S1097276519300929?via%3Dihub) and [CISBP-RNA](https://www.nature.com/articles/nature12311) databases in one command. See [Scoring sequences](scoring.md).
- **Motif search** — look up which RBP entries are in the database by name, alias or description. See [Motif database & search](motifs.md).
- **CLIP-based scoring** — score against real binding evidence (BED/bedGraph peaks from eCLIP/iCLIP experiments) instead of a PWM. See [CLIP-based scoring](clip.md).
- **Heatmap visualization** — clustered PNG/PDF heatmaps of binding scores across proteins and positions, with cumulative plots across many sequences for a single protein.
- **Python API** — call scanRBP's scoring directly from Python for embedding in other tools (this is how the [expressRNA](https://www.expressrna.org) scanRBP analysis works). See [Python API](python-api.md).

## Where to start

New to scanRBP? Read [Installation](installation.md) and then [Quick Start](quickstart.md) to get your first heatmap in under a minute. Everything else in these docs is reference material to dig into as you need it.
