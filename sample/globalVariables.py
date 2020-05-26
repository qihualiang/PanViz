MauveExecutable = "/home/qliang/0.soft/Mauve/mauve_snapshot_2015-02-13/linux-x64/progressiveMauve"
inputGenomes = ["example/GCA_000001735.2_TAIR10.1_genomic.fna", "example/GCA_001651475.1_Ler_Assembly_genomic.fna", "example/GCA_900660825.1_Ath.Ler-0.MPIPZ.v1.0_genomic.fna"]

XMFAFile = "example/output.xmfa"

numOfGenomes = 3
numOfChrms = 1

BEDaligned = False  ## whether to align all C blocks
outBEDConsensus = "PGV.consensus.bed"

colorConsensus = "0,0,255"
colorC = "230,243,255"
colorCrev = "255,0,255"
colorCtransloc = "0,0,255"
colorP = "0,255,0"
colorU = "255,0,0"
