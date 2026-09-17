# Python API

scanRBP's scoring logic is available directly from Python, for embedding into other tools — this is how the [expressRNA](https://www.expressrna.org) scanRBP analysis calls it under the hood.

## Scoring a sequence

```python
import scanRBP
df = scanRBP.scan("AAAGCGGCGACTTATTATATCCCCATATATTATATCTTCTTCTCTTATATATAAACCAGAGATAGATGTGTGTGGTGG")
```

`scan(seq)` returns a `pandas.DataFrame` indexed by `scan_id` (one row per RBP in the database), with one column per position in `seq` — the same log-odds score matrix the command line writes to `.tab.gz`.

!!! note
    `scan()` always floors negative scores to 0 (equivalent to the CLI's `-nonzero` flag) — unlike the plain CLI invocation, which keeps negative scores by default. Keep this in mind if you're comparing Python API output against a CLI run made without `-nonzero`.

```python
df.loc["TARDBP.K562.00"]       # score vector for one RBP across the sequence
df.sum(axis=1).sort_values()   # total binding score per RBP, ranked
```

## Inspecting the database

```python
import scanRBP

# scan_id -> {protein, tissue, source, cluster, pwm_path, aliases, description, ...}
scanRBP.database.proteins["TARDBP.K562.00"]

# scan_id -> biopython PSSM (log-odds matrix) used by scan()
scanRBP.pwm.pssm["TARDBP.K562.00"]
```

Both `scanRBP.database.proteins` and `scanRBP.pwm.pssm` are populated once, automatically, when you `import scanRBP` (triggering the same PWM database download described in [Motif database & search](motifs.md#where-the-database-lives) if it isn't present yet) — there's no separate init call needed.

## Configuration

```python
import scanRBP
scanRBP.config.data_folder   # currently configured data folder (default ~/scanRBP_data)
scanRBP.config.init("/path/to/data_folder")  # change it, same as `scanRBP config /path` on the CLI
```
