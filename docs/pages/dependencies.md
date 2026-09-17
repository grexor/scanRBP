# Dependencies

[biopython](https://biopython.org/), [scipy](https://scipy.org/), [seaborn](https://seaborn.pydata.org/), [matplotlib](https://matplotlib.org/), [pandas](https://pandas.pydata.org/) and [pybio](https://grexor.github.io/pybio/) are required and installed automatically by `pip install scanRBP`.

scanRBP uses biopython's `Bio.motifs` for PWM parsing and log-odds scoring, pybio for FASTA and bedGraph file reading (used by [CLIP-based scoring](clip.md)), and seaborn/matplotlib for the clustered heatmap plots.
