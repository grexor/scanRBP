# Motif database & search

scanRBP ships with a database of RNA-binding protein PWMs, built from two sources:

- **[mCross](https://www.sciencedirect.com/science/article/pii/S1097276519300929?via%3Dihub)** — Feng H, Bao S, et al., *Modeling RNA-Binding Protein Specificity In Vivo by Precisely Registering Protein-RNA Crosslink Sites*, Molecular Cell, 2019. Motifs derived from eCLIP crosslink sites.
- **[CISBP-RNA](https://www.nature.com/articles/nature12311)** — Ray D, Kazan H, Cook KB, Weirauch MT, Najafabadi HS, et al., *A compendium of RNA-binding motifs for decoding gene regulation*, Nature, 2013.

## Entry naming

Each database entry has a `scan_id` of the form `<PROTEIN>.<CELL_LINE_OR_TISSUE>.<cluster>`, for example `HLTF.K562.01` or `DDX3X.HepG2.01` — the same protein can appear multiple times if it was profiled in more than one cell line or has more than one binding cluster.

## Searching the database

Use the `search` command to find which entries match a protein name, alias, or description:

```bash
scanRBP search TARDBP
```
```text
[scanRBP] Found proteins in the scanRBP database:
scan_id           protein  tissue  description                                source
TARDBP.K562.00    TARDBP   K562    TAR DNA binding protein                   mCross
TARDBP.HepG2.00   TARDBP   HepG2   TAR DNA binding protein                   mCross
```

The search matches against the `scan_id`, protein name and description (case-insensitive substring match), so a search for an alias or partial name still finds the right entries. The `-protein` scoring option (see [Scoring sequences](scoring.md#limiting-to-specific-proteins)) uses this same matching, so it's worth searching first to see exactly which `scan_id`s a name will resolve to.

## Where the database lives

On first use, scanRBP downloads the database (mCross + CISBP-RNA PWMs, ~6 MB) to `~/scanRBP_data`. Configuration is stored in `~/.scanRBP` (created automatically), with a single setting:

```text
data_folder="~/scanRBP_data"
```

To move the data folder, run:

```bash
scanRBP config /path/to/data_folder
```

This updates `~/.scanRBP` and re-downloads the database there on next use if it isn't already present.

## Other resources (not yet integrated)

Datasets under consideration for future additions to the database, kept here for reference:

**Additional PWM datasets**

- [RCRUNCH](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-023-02913-0) — motif compendium, with a [data file](https://static-content.springer.com/esm/art%3A10.1186%2Fs13059-023-02913-0/MediaObjects/13059_2023_2913_MOESM6_ESM.txt) of candidate PWMs.

**CLIP datasets** (for use with [CLIP-based scoring](clip.md) rather than the PWM database)

- [ENCODE eCLIP experiments](https://www.encodeproject.org/metadata/?status=released&internal_tags=ENCORE&assay_title=eCLIP&biosample_ontology.term_name=K562&biosample_ontology.term_name=HepG2&type=Experiment&files.analyses.status=released&files.preferred_default=true) — released eCLIP experiments in K562/HepG2.

**Gene annotation**

- [NCBI gene metadata](https://www.ncbi.nlm.nih.gov/gene/?term=human[organism]) (names, aliases) — the source used to build the `aliases`/`description` fields in the scanRBP database.
