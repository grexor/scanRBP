# Installation

The easiest way to install **scanRBP** is by running:

```bash
pip install scanRBP
```

!!! note
    On some systems, **pip** installs the executable scripts under `~/.local/bin`. However this folder is not in the `PATH`, which will result in `command not found` if you try to run `scanRBP` on the command line. To fix this, run `export PATH="$PATH:~/.local/bin"` (and add this to your `.profile`). Another option is to install inside a virtual environment (using `virtualenv`).

If you would instead like to **install the latest development version** from this repository:

```bash
# clone the scanRBP GitHub repository
git clone https://github.com/grexor/scanRBP.git

# build and install
./build.sh
```

## The motif database

On first use, scanRBP automatically downloads its PWM database — mCross eCLIP motifs plus CISBP-RNA motifs, about 6 MB — to `~/scanRBP_data`. Nothing to configure for a default setup; see [Motif database & search](motifs.md#where-the-database-lives) if you want to store it somewhere else.

scanRBP depends on [pybio](https://grexor.github.io/pybio/) for FASTA/bedGraph reading, and on scipy/biopython/seaborn/matplotlib for scoring and plotting — all installed automatically by `pip install scanRBP`. See [Dependencies](dependencies.md).
