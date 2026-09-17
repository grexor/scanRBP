# Scoring sequences

This page covers the full set of scoring and plotting options, beyond the basics in [Quick Start](quickstart.md).

## Limiting to specific proteins

By default scanRBP scores a sequence against **every** RBP in the database. To restrict to one (or a group matching a search term), use `-protein`:

```bash
scanRBP AAAGCGGCGACTT... example1 -protein TARDBP -heatmap example1
```

`-protein` is matched the same way as the [`search` command](motifs.md#searching-the-database) — a case-insensitive substring match against `scan_id`, protein name and description — so `-protein TARDBP` can resolve to more than one `scan_id` if the protein was profiled in multiple cell lines. Run `scanRBP search <term>` first if you want to see exactly which entries a given `-protein` value will include.

## Cumulative plots across many sequences

`-cumulative` changes the output shape: instead of one heatmap per sequence (proteins × positions), it produces a single heatmap for one protein across **all** sequences in a FASTA file (sequences × positions). This is useful for looking at how one RBP's predicted binding varies across many loci — e.g. all 3'-UTRs of a gene family, or all sequences flanking a set of splice sites.

```bash
scanRBP loci.fasta -cumulative -protein TARDBP -heatmap tardbp_binding
```

- Requires `-protein` to name the protein(s) to plot (there's no "all proteins, cumulative" mode).
- All sequences in the FASTA file must be the same length — scanRBP exits with an error otherwise.
- Only usable with a FASTA file input, not a single command-line sequence.

## Heatmap styling

Heatmaps are only generated when `-heatmap <title>` is given — without it, scanRBP still writes the `.tab.gz` score matrix but skips the plot.

| Option | Effect |
|---|---|
| `-heatmap title` | Generate the heatmap (PNG + PDF), with `title` used as the plot title. |
| `-annotate` | Print the numeric score inside each heatmap cell. |
| `-xlabels` | Show the sequence itself along the x-axis (off by default, since long sequences make this unreadable). |
| `-figsize "(10,20)"` | Set the matplotlib figure size (width, height in inches). |
| `-fontscale 0.2` | Scale all heatmap text (default `0.2` — the database has many proteins, so labels start small). |
| `-vlines "10,-5"` | Draw dashed vertical guide lines at the given x positions. Negative values count back from the end of the sequence (e.g. `-5` is 5 bases before the end) — handy for marking a splice site or crosslink position. |

## Other options

| Option | Effect |
|---|---|
| `-nonzero` | Clip all negative scores to 0 before scoring/plotting (off by default — negative scores, meaning "less consistent with the motif than background," are kept). |
| `-output_folder folder` | Write all output files here instead of the current directory (created if it doesn't exist). |
| `-force` | Overwrite existing output files. Without it, scanRBP skips a sequence whose `.tab.gz` output already exists — useful for resuming a large FASTA batch. |

## Output files

For an output name `example1` (or a FASTA sequence id `seq1`, prefixed `pwm_`):

```text
example1.tab.gz   # log-odds score matrix (proteins x positions), gzipped TSV
example1.png      # heatmap, if -heatmap was given
example1.pdf      # heatmap, if -heatmap was given
```

`+` and `-` characters in the output name are replaced with `plus`/`minus` (common when a FASTA id encodes a genomic strand), so filenames stay filesystem-safe.
