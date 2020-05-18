# PanViz: Reference-agnostic Visualization of Pan-genomes
The pan-genome of a species is the union of the genes and non-coding sequences present in all individuals (cultivar, accessions,or strains) within that species. Due to the complex structural variations that can be observed whencomparing multiple individuals of the same species, an effective and intuitive visualization of a pan-genome is challenging. 

PanViz is reference-agnostic visualization of pan-genomes. It is a novel representation method based on the notion of consensus ordering that enables an intuitive, effective and interactive visualization of a pan-genome. The utility of such representation is visulizaed on  a web-based pan-genome browser that can present complex structural genomic variations.

##Using PanViz
### Installation
PanViz requires the following python packages installed:
-   [alignment](https://pypi.org/project/alignment/)

-   [Biopython](https://biopython.org)

-   [NumPy](https://numpy.org)

-   [matplotlib](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.html)

-   [recollecion](https://pypi.org/project/recollection/)


	#Install from github and install all dependencies listed above
	git clone https://github.com/qihualiang/PanViz.git

### Usage
[ProgressiveMauve](http://darlinglab.org/mauve/user-guide/progressivemauve.html) is run to generate multiple sequence alignments for all the genomes within the pan-genomes. 

Edit `globalVariables.py` to indicate:
-    Output of ProgressiveMauve
-    Genome sequences in pan-genomes
-    Number of chromosomes/contigs to be considered

Run PanViz pipeline as:
	python PanViz.py


![panviz\[fig1\]](docs/figs/flowchart.jpg)
