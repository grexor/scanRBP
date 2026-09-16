<picture><img src="media/scanRBP_logo.png" height="30" alt="scanRBP"/></picture>

### What is scanRBP?

scanRBP loads RNA-binding protein (RBP) motif position weight matrices (PWMs) and computes log-odds binding scores for every loaded RBP across a given nucleotide sequence, then draws a heatmap of the scores.

The scores can be described as follows ([biopython docs](http://biopython.org/DIST/docs/tutorial/Tutorial.html)):

> Here we can see positive values for symbols more frequent in the motif than in the background and negative for symbols more frequent in the background. 0.0 means that it's equally likely to see a symbol in the background and in the motif.

> Using the background distribution and PWM with pseudo-counts added, it's easy to compute the log-odds ratios, telling us what are the log odds of a particular symbol to be coming from a motif against the background.

For more information, see the [biopython docs](http://biopython.org/DIST/docs/tutorial/Tutorial.html).

### Installation <a name="initial_setup"></a>

The easiest way to install scanRBP is to simply run:

`$ pip install scanRBP`

On first use, scanRBP automatically downloads its PWM database (mCross eCLIP + CISBP-RNA, ~6 MB) to `~/scanRBP_data`. To store it somewhere else instead:

`$ scanRBP config /path/to/data_folder`

### Quick Start

Super quick example:

```
# taking a sequence given directly on the command line, will produce binding scores and a heatmap
# output: example1.tab.gz  # log-odds score matrix (proteins x positions) for the given sequence
# output: example1.png/pdf # heatmap image with hierarchical clustering of protein binding vectors
./scanRBP AAAGCGGCGACTTATTATATCCCCATATATTATATCTTCTTCTCTTATATATAAACCAGAGATAGATGTGTGTGGTGG example1 -heatmap example1

# instead of a single sequence, the input can be a FASTA file with multiple sequences
# (one heatmap/matrix is produced per sequence, named after its FASTA id)
./scanRBP data.fasta
```

### Documentation

* [PDF reference manual](https://github.com/grexor/scanRBP/raw/main/docs/scanRBP_docs.pdf)
* [Google docs](https://docs.google.com/document/d/1ejfayohzaKnLZfdyfINtEBLm4IacJBHxfC5eqSa1QLc/edit?usp=sharing) of the above PDF (comment if you like)

### Change log

**v0.3**: February 2025
* scan code speed-up using numpy

**v0.2**: June 2024
* new: score against real binding sites from CLIP-family experiments (eCLIP, iCLIP, etc.) via a BED/bedGraph peak file, as an alternative to PWM-based scoring — example dataset from the [ENCODE Project](https://www.encodeproject.org)

**v0.1.7**: November 2023
* added mCross (eCLIP-derived) and CISBP-RNA motif PWMs

### Citation

scanRBP is developed and distributed as part of the [splicekit](https://github.com/grexor/splicekit) toolkit. If you use scanRBP in your research, please cite the splicekit paper:

Rot, G., Wehling, A., Schmucki, R., Berntenis, N., Zhang, J. D., & Ebeling, M. (2024)<br>
[splicekit: an integrative toolkit for splicing analysis from short-read RNA-seq](https://academic.oup.com/bioinformaticsadvances/article/4/1/vbae121/7735317)<br>
Bioinformatics Advances, 4(1). https://doi.org/10.1093/bioadv/vbae121
