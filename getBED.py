from globalVariables import *

from collections import Counter

gap = 0

def getBED(consensus, nodeOrders, nodeLengths, chrmEndNodes, chrmEndCNodes):
	#### get consensus end Cnodes
	consensusEndCNodes = list()
	for i in range(numOfChrms):
		candidateCNodes = list()
		for j in range(numOfGenomes):
			candidateCNodes.append(chrmEndCNodes[j][i])
		occurences = Counter(candidateCNodes)
		consensusEndCNodes.append(occurences.most_common(1)[0][0])

	#### insert dummyHead into consensus/nodeOrder
	consensusWhead = ["dummyHead"] # consensusWhead = dummy, chr1, dummy, chr2... dummy, contigs
	for Cnode in consensus:
		consensusWhead.append(Cnode)
		if Cnode in consensusEndCNodes:
			consensusWhead.append("dummyHead")
	consensusWhead.append("dummyTail")

	AllCnodes = list()
	nodeOrdersWhead = list()
	for i in range(numOfGenomes):
		nodeOrder = nodeOrders[i]
		Cnodes = list()
		chrmEndNode = chrmEndNodes[i]
		nodeOrderWhead = ["dummyHead"]
		for node in nodeOrder:
			nodeOrderWhead.append(node)
			if node.startswith("C"):
				Cnodes.append(node)
			if node in chrmEndNode:
				nodeOrderWhead.append("dummyHead")
				Cnodes.append("dummyHead")
		Cnodes.append("dummyTail")
		nodeOrderWhead.append("dummyTail")
		AllCnodes.append(Cnodes)
		nodeOrdersWhead.append(nodeOrderWhead)

	#### initalize interval from consensus input
	intervals = dict() ## intervals[interval] = max length within this interval
	for i in range(len(consensusWhead)):
		currNode = consensusWhead[i]
		if currNode.startswith("C"):
			interval = (consensusWhead[i-1], consensusWhead[i])
			intervals[interval] = 0

	#### update intervals
	for i in range(numOfGenomes):
		nodeOrder = nodeOrdersWhead[i]
		chrmEndNode = chrmEndNodes[i]
		prevNode = "dummyHead"
		lengthsBetweenInterval = 0
		for node in nodeOrder:
			if node.startswith("C"):
				interval = (prevNode, node)
				if interval in intervals and lengthsBetweenInterval > intervals[interval]:
					intervals[interval] = lengthsBetweenInterval
				lengthsBetweenInterval = 0
				prevNode = node
			elif node.startswith("dummy"):
				lengthsBetweenInterval = 0
				prevNode = node
			else:
				lengthsBetweenInterval += nodeLengths[node][i] + gap


	#### output consensus BED
	prevC = dict()
	neighborCsNoDirection = dict()
	neighborCsWDirection = dict()
	Cstarts = dict()

	startPos = 1
	chrmCount = 0

	prev = "dummyHead"

	OUTconsensus = open(outBEDConsensus, "w")
	#print >>OUTconsensus, "track itemRgb=On useScore=1"
	for i in range(len(consensusWhead)):
		currNode = consensusWhead[i]
		if currNode.startswith("C"):
			startPos += intervals[(prev, currNode)]
			endPos = startPos + max(nodeLengths[currNode])
			if chrmCount <= numOfChrms:
				chrmName = "chr"+str(chrmCount)
			else:
				chrmName = "contigs"
			#print >>OUTconsensus, chrmName, startPos, endPos, currNode,". .", startPos, endPos, colorConsensus
			print(chrmName, startPos, endPos, currNode, ". +", startPos, endPos,  colorConsensus, file=OUTconsensus)
			Cstarts[currNode] = (chrmCount, startPos)
			prevC[currNode] = prev
			neighborCsNoDirection[currNode] = set([prev, consensusWhead[i+1]])
			neighborCsWDirection[currNode] = [prev, consensusWhead[i+1]]
			startPos = endPos + 1
		else:
			chrmCount += 1
			startPos = 1
		prev = currNode


	#### output all BEDs
	for i in range(numOfGenomes):
		outFile = open(inputGenomes[i].split("/")[-1]+".bed", "w")
		nodeOrderWhead = nodeOrdersWhead[i]
		startPos = 1
		chrmCount = 0
		for j in range(len(nodeOrderWhead)):
			currNode = nodeOrderWhead[j]
			if chrmCount <= numOfChrms:
				chrmName = "chr"+str(chrmCount)
			else:
				chrmName = "contigs"

			if currNode.startswith("C"):
				if BEDaligned and chrmCount == Cstarts[currNode][0] and startPos < Cstarts[currNode][1]:
					startPos = Cstarts[currNode][1]
				endPos = startPos + nodeLengths[currNode][i]
				Cindex = AllCnodes[i].index(currNode)
				if neighborCsWDirection[currNode] == [AllCnodes[i][Cindex-1], AllCnodes[i][Cindex+1]]: ## same prev and next
					#print >>outFile, chrmName, startPos, endPos, currNode, 1, ".", startPos, endPos, colorC
                                        print(chrmName, startPos, endPos, currNode, 1, "+", startPos, endPos, colorC, file=outFile)
				elif neighborCsNoDirection[currNode] == set([AllCnodes[i][Cindex-1], AllCnodes[i][Cindex+1]]): ## rev
					#print >>outFile, chrmName, startPos, endPos, currNode, 1, ".", startPos, endPos, colorCrev
                                        print(chrmName, startPos, endPos, currNode, 1, "-", startPos, endPos, colorCrev, file=outFile)
				else: ## translocation
					#print >>outFile, chrmName, startPos, endPos, currNode, 1, ".", startPos, endPos, colorCtransloc
                                        print(chrmName, startPos, endPos, currNode, 1, "+", startPos, endPos, colorCtrans, file=outFile)
				startPos = endPos + 1

			elif currNode.startswith("D"):
				endPos = startPos + nodeLengths[currNode][i]
				#print >>outFile, chrmName, startPos, endPos, currNode, 1, ".", startPos, endPos, colorP
				print(chrmName, startPos, endPos, currNode, 1, "+", startPos, endPos, colorP, file=outFile)
				startPos = endPos + 1
			elif currNode.startswith("U"):
				endPos = startPos + nodeLengths[currNode][i]
				#print >>outFile, chrmName , startPos, endPos, currNode, 1000, ".", startPos, endPos, colorU
				print(chrmName, startPos, endPos, currNode, 1, "+", startPos, endPos, colorU, file=outFile)
				startPos = endPos + 1
			else: ## dummyHead/Tail
				chrmCount += 1
				startPos = 1


