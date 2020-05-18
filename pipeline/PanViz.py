from globalVariables import *
import sys
import re
import numpy


from processXMFA import processXMFA
nodeOrders, nodeLengths, chrmEndNodes, chrmEndCNodes = processXMFA()
print "finish processXMFA"

from getConsensus import getConsensus
consensus = getConsensus(nodeOrders)
print "finish consensus"


from getBED import getBED
getBED(consensus, nodeOrders, nodeLengths, chrmEndNodes, chrmEndCNodes)

from plot import plot
plot()