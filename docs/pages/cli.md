# Command-line reference

Every `scanRBP` invocation prints its version, config file path and data folder first. Run `scanRBP -help` for the built-in summary; this page is the fuller reference.

## Usage forms

| Form | Description |
|---|---|
| `scanRBP sequence output [options]` | Score a sequence given directly on the command line. |
| `scanRBP filename.fasta [options]` | Score every sequence in a FASTA file — one output set per sequence. |
| `scanRBP search search_term` | List database entries matching `search_term`. See [Motif database & search](motifs.md#searching-the-database). |
| `scanRBP config [folder]` | Show (no argument) or change (`folder`) the data storage folder in `~/.scanRBP`. |

## Scoring options

| Option | Description |
|---|---|
| `-protein <term>` | Restrict scoring to database entries matching `term` (same matching as `search`). Default: score against every entry. |
| `-clip peaks.bed.gz` | Score against real CLIP peak data instead of a PWM. Requires a FASTA input with genomically-encoded sequence ids. See [CLIP-based scoring](clip.md). |
| `-cumulative` | Plot one protein's binding across every sequence in a FASTA file, instead of one heatmap per sequence. Requires `-protein`. See [Cumulative plots](scoring.md#cumulative-plots-across-many-sequences). |
| `-nonzero` | Clip all negative scores to 0. Off by default. |
| `-force` | Overwrite existing output files instead of skipping already-processed sequences. |
| `-output_folder folder` | Write outputs here (default: current directory). |

## Heatmap options

| Option | Description |
|---|---|
| `-heatmap title` | Generate a heatmap (PNG + PDF) with this title. Without it, only the `.tab.gz` score matrix is written. |
| `-annotate` | Print the numeric score inside each heatmap cell. |
| `-xlabels` | Show the sequence along the x-axis. |
| `-figsize "(w,h)"` | matplotlib/seaborn figure size in inches. |
| `-fontscale n` | Heatmap text scale (default `0.2`). |
| `-vlines "x1,x2"` | Dashed vertical guide lines at these x positions (negative values count from the sequence end). |

## Other

| Option | Description |
|---|---|
| `-version` | Print the installed scanRBP version and exit. |
| `-help` | Print the built-in usage summary. |
