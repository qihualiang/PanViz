from globalVariables import *
import sys
import re
import numpy


from processXMFA import processXMFA
nodeOrders, nodeLengths, chrmEndNodes, chrmEndCNodes = processXMFA()

from getConsensus import getConsensus
consensus = getConsensus(nodeOrders)

from getBED import getBED
getBED(consensus, nodeOrders, nodeLengths, chrmEndNodes, chrmEndCNodes)

from plot import plot
plot()
