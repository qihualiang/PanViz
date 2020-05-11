MauveExecutable = "/home/qliang/0.soft/Mauve/mauve_snapshot_2015-02-13/linux-x64/progressiveMauve"
inputGenomes = ["data/GCA_900008185.2_LD2B_ii_genomic.fna", "data/GCA_900008205.2_LUY_ii_genomic.fna", "data/GCA_900008215.2_BGED_ii_genomic.fna", "data/GCA_900008225.2_AKIBA_ii_genomic.fna", "data/GCA_900008235.2_ISH3_ii_genomic.fna"]

XMFAFile = "data/output.xmfa"

numOfGenomes = len(inputGenomes)
numOfChrms = 1

BEDaligned = False  ## whether to align all C blocks
outBEDConsensus = "PGV.consensus.bed"

colorConsensus = "0,0,255"
colorC = "230,243,255"
colorCrev = "255,0,255"
colorCtransloc = "0,0,255"
colorP = "0,255,0"
colorU = "255,0,0"
