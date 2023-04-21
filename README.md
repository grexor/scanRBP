# What is scanRBP?

scanRBP loads RNA-protein binding motif PWM and computes the log-odds scores for all the loaded RBPs across a given genomic sequence + draws a heatmap of the scores.

The scores can be described as follows:

```
Here we can see positive values for symbols more frequent in the motif than in the background and negative for symbols more frequent in the background. 0.0 means that it's equally likely to see a symbol in the background and in the motif.
```

```
Using the background distribution and PWM with pseudo-counts added, it's easy to compute the log-odds ratios, telling us what are the log odds of a particular symbol to be coming from a motif against the background.
```

For more information, see the [biopython docs](http://biopython.org/DIST/docs/tutorial/Tutorial.html).

# Example run

scanRBP quick start:

```
Usage for single sequence: scanRBP sequence output [options]
     * one sequence provided on the command line, generates output.png/pdf + output.tab

Usage for processing FASTA file: scanRBP filename.fasta [options]
     * one heatmap/matrix will be generated per sequence
     * output name of the files will be sequence ids provided in the fasta file

Options:
     -annotate               Annotate each heatmap cell with the number
     -xlabels                Display sequence (x-labels), default False
     -only_protein TARDBP    Only analyze binding for the specific protein / search by name
     -all_protein TARDBP     Additionally to one motif per protein (for all proteins), also include all motifs (PWMs) for this specific protein (search by name)
                             (note that one protein can have several PWMs)
     -figsize "(10,20)"      Change matplotlib/seaborn figure size for the heatmap, example width=10, height=20
     -heatmap title          Make heatmap (png+pdf) with title
     -output_folder folder   Store all results to the output folder (default: current folder)
     -nonzero                All negative vector values are set to 0, not enabled by default
```

Example runs:

```
# taking a random sequence, will produce binding scores and a heatmap
# output: example1_PWM.tab # file with log-odds vectors for all proteins for the given command line sequence
# output: example1.png/pdf # heatmap image with clustering of protein binding vectors
./scanRBP AAAGCGGCGACTTATTATATCCCCATATATTATATCTTCTTCTCTTATATATAAACCAGAGATAGATGTGTGTGGTGG example1 -heatmap example1

# instead of taking one single sequence, the input can be a fasta file with multiple sequences
./scanRBP data.fasta
```

# Motif PWM database

Using the mCross database of 112 RBPs from the paper:

Feng H, Bao S et al.<br>
[Modeling RNA-Binding Protein Specificity In Vivo by Precisely Registering Protein-RNA Crosslink Sites](https://www.sciencedirect.com/science/article/pii/S1097276519300929?via%3Dihub)<br>
Molecular Cell, 2019<br>

To download the PWMs:

```
wget http://zhanglab.c2b2.columbia.edu/data/mCross/eCLIP_mCross_PWM.tgz --no-check-certificate
tar xfz eCLIP_mCross_PWM.tgz
```

# Additional PWM dataset

https://genomebiology.biomedcentral.com/articles/10.1186/s13059-023-02913-0
https://static-content.springer.com/esm/art%3A10.1186%2Fs13059-023-02913-0/MediaObjects/13059_2023_2913_MOESM6_ESM.txt

# CLIP dataset

Any bedGraph CLIP peak called file for a specific genome.