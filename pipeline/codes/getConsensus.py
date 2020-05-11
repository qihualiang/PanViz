import sys
from globalVariables import *
from linkNodes import linkNodes
from merge import merge

def getConsensus(nodeOrders):
    sys.setrecursionlimit(len(nodeOrders[0]))

    unlink = dict()  ## unlink[node] = [ (left, right), (left, right), ... ] list of tuples
    allNodes = set()

    CnodeOrders = []
    for nodeOrder in nodeOrders:
        CnodeOrder = ["dummyHead"] ## Cnodes only in the list with dummyHead/Tail
        for i in range(len(nodeOrder)):
            if nodeOrder[i].startswith("C"):
                CnodeOrder.append(nodeOrder[i])
        CnodeOrder.append("dummyTail")
        CnodeOrders.append(CnodeOrder[1:-1])
        for i in range(1, len(CnodeOrder)-1): ## instead of range(2, len(CnodeOrder)-2) Aug 21
            node = CnodeOrder[i]
            neighbors = [CnodeOrder[i-1],CnodeOrder[i+1]]
            unlink[node] = unlink[node]+neighbors if node in unlink else neighbors


    linked = linkNodes(unlink)
    consensus = merge(CnodeOrders, linked)

    return consensus



