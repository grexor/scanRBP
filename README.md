<picture><img src="media/scanRBP_logo.png" height="30"/></picture>
### What is scanRBP?

scanRBP loads RNA-protein binding motif PWM and computes the log-odds scores for all the loaded RBPs across a given genomic sequence + draws a heatmap of the scores.

The scores can be described as follows ([biopython docs](http://biopython.org/DIST/docs/tutorial/Tutorial.html)):

> Here we can see positive values for symbols more frequent in the motif than in the background and negative for symbols more frequent in the background. 0.0 means that it's equally likely to see a symbol in the background and in the motif.

> Using the background distribution and PWM with pseudo-counts added, it's easy to compute the log-odds ratios, telling us what are the log odds of a particular symbol to be coming from a motif against the background.

For more information, see the [biopython docs](http://biopython.org/DIST/docs/tutorial/Tutorial.html).

### Installation <a name="initial_setup"></a>

The easiest way to install scanRBP is to simply run:

`$ pip install scanRBP`

### Quick Start

Super quick example:

```
# taking a random sequence, will produce binding scores and a heatmap
# output: example1_PWM.tab # file with log-odds vectors for all proteins for the given command line sequence
# output: example1.png/pdf # heatmap image with clustering of protein binding vectors
./scanRBP AAAGCGGCGACTTATTATATCCCCATATATTATATCTTCTTCTCTTATATATAAACCAGAGATAGATGTGTGTGGTGG example1 -heatmap example1

# instead of taking one single sequence, the input can be a fasta file with multiple sequences
./scanRBP data.fasta
```

### Documentation

* [PDF reference manual](https://github.com/grexor/scanRBP/raw/main/docs/scanRBP_docs.pdf)
* [Google docs](https://docs.google.com/document/d/1ejfayohzaKnLZfdyfINtEBLm4IacJBHxfC5eqSa1QLc/edit?usp=sharing) of the above PDF (comment if you like)

### Change log

**v0.2**: June 2024
* new: loading of BED files with peaks from *CLIP experiments, example from [Encode Project](https://www.encodeproject.org)
* integrated PWMs from [CIS-BP](https://cisbp.ccbr.utoronto.ca) and [mCrossBase](https://zhanglab.c2b2.columbia.edu/mCrossBase)

**v0.1.7**: November 2023
* added mCross and CISBP-RNA motifs