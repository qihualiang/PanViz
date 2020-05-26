# PanViz: Reference-agnostic Visualization of Pan-genomes
The pan-genome of a species is the union of the genes and non-coding sequences present in all individuals (cultivar, accessions,or strains) within that species. Due to the complex structural variations that can be observed whencomparing multiple individuals of the same species, an effective and intuitive visualization of a pan-genome is challenging. 

PanViz is reference-agnostic visualization of pan-genomes. It is a novel representation method based on the notion of consensus ordering that enables an intuitive, effective and interactive visualization of a pan-genome. The utility of such representation is visulizaed on  a web-based pan-genome browser that can present complex structural genomic variations.

## Using PanViz

### Installation
PanViz requires the following python packages installed:
-   [alignment](https://pypi.org/project/alignment/)

-   [Biopython](https://biopython.org)

-   [NumPy](https://numpy.org)

-   [matplotlib](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.html)

-   [recollecion](https://pypi.org/project/recollection/)


```
#Install from github and install all dependencies listed above
git clone https://github.com/qihualiang/PanViz.git
```

### Workflow

The input to PanViz is a set of n individual genomes for the same species, or a set of genomes from very closely-related species. To obtain the best results, input genomes must have a similar level of contiguity. 

First, PanViz carries out a genome-wide multiple sequence alignment on all the inputs using [progressiveMauve](http://darlinglab.org/mauve/user-guide/progressivemauve.html). The output of progressiveMauve is used to convert genome sequences into block orderings consisted of C/D/U blocks. C-block (core) corresponds to an alignment that contains all n individuals; D-block (dispensable) corresponds to an alignment which contains at least two individuals and at most n−1. U-block (unique), is a block that belongs exclusively to one individual genome. After the conversion of each genome into blocks, PanViz computes the consensus ordering for the C-blocks, which will constitute the “back-bone” of the pan-genome. 

![panviz\[fig1\]](docs/figs/flowchart.jpg)

There are three different output formats of PanViz:
  (i) dotplot comparing n genome orderings with consensus ordering
  (ii) [PanViz Genome Viewer](http://panviz.cs.ucr.edu) for blocks with acutal coordinates
  (iii) PanViz Genome Viewer for blocks with gapped coordinates aligned with consensus


### Usage
[ProgressiveMauve](http://darlinglab.org/mauve/user-guide/progressivemauve.html) is used to generate multiple sequence alignments for all the genomes within the pan-genomes. 

Edit `globalVariables.py` to indicate:
-    `XMFAFile` Output file of ProgressiveMauve (.xmfa)
-    `inputGenomes` Genome sequence files in pan-genomes 
-    `numOfChrms` Number of chromosomes/contigs to be considered
-    `alnScoreThr` Threshold for alignment scores to determine potential misjoins
-    `BEDaligned` Whether to align core blocks in accession with corresponding core blocks in consensus
-    `color` Colors used for different blocks in PanViz Genome Viewer [optional]

Run PanViz pipeline as:
```
python PanViz.py
```


Example:
To run PanViz on Arabidopsis pan-genomes with 4Mb sequences on chromosome three for three different accessions, move the globalVariables file:
```
mv sample/globalVariables.py .
```
Then run PanViz pipeline as:
```
python PanViz.py
```
This will generate a dotplot comparing core blocks of each accessions to consensus ordering. 
![panviz\[fig2\]](docs/figs/arabidopsisDotplot.png =30x30)

This will also generate three unaligned BED files for the input genomes to be viewed in PanViz Genome Viewer. All blocks are at their acutal coordinates along each genome.
![panviz\[fig3\]](docs/figs/arabidopsisPanVizUnaligned.png)

If BED files are set to be aligned by `BEDaligned`, C-blocks will be gapped and aligned to their corresponding ordinates on consensus ordering. 
![panviz\[fig4\]](docs/figs/arabidopsisPanVizAligned.png)






