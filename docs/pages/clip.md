# CLIP-based scoring

Instead of scoring a sequence against a PWM, `-clip` scores it against **real binding evidence** — peaks from a CLIP-family experiment (eCLIP, iCLIP, etc.) supplied as a BED/bedGraph file:

```bash
scanRBP loci.fasta -clip peaks.bed.gz -protein MY_RBP -heatmap clip_scores
```

This is the alternative to PWM-based scanning: rather than asking "does this sequence look like this protein's known motif," it asks "did this protein actually bind here, according to this experiment." `-protein` here just labels the output row/track — it isn't used to look up a database entry, since the signal comes entirely from `peaks.bed.gz`.

## Sequence ID format

CLIP-based scoring only works with a FASTA file (not a single command-line sequence), and each FASTA sequence id must encode its genomic locus so scanRBP knows where to look up peak values:

```text
<chromosome><strand>_<start>_<stop>
```

For example, a FASTA record for chromosome 1, plus strand, from position 11012300 to 11012400:

```text
>1+_11012300_11012400
ACGTACGT...
```

The strand character (`+` or `-`) is the last character before the first underscore-delimited coordinate; everything before it is the chromosome name (chromosome names containing underscores are handled correctly, since only the last two `_`-separated fields are treated as start/stop).

## How it works

scanRBP loads the peak file once with [`pybio.data.Bedgraph`](https://grexor.github.io/pybio/bedgraph/), then for each sequence, calls `get_vector(chr, strand, start, stop)` to pull the per-position peak values for that exact locus — so `start`/`stop` in the sequence id must match real genomic coordinates in `peaks.bed.gz`'s coordinate system. `-nonzero` still applies (clip negative values to 0), and output files follow the same `.tab.gz` / `.png` / `.pdf` convention as PWM scoring — see [Output files](scoring.md#output-files).

See [Motif database & search](motifs.md#other-resources-not-yet-integrated) for a pointer to ENCODE's public eCLIP experiments if you don't have your own CLIP data.
