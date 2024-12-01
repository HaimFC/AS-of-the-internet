import collections
import re
from operator import itemgetter
import numpy as np
import scipy as sp
from itertools import groupby
import matplotlib.pyplot as plt
import networkx as nx


providers = []
costumers = []
peers = []

providers_set = {}
costumers_set = {}
peers_Set = {}

numOfCostumers = []

Tier1 = []
Tier1_Final = []

edgesOfGraphBI = []
edgesOfGraphBN = []
nodesOfGraphBN = {}
namesDict = {}

# Get the data we need from the txt file.
# We extract who are providers and who are  customers (As costumer-provder policy)
# We extract all peers AS policy
with open("20210901.as-rel.txt") as bgpAsFile:
    lines = bgpAsFile.readlines()
    for line in lines:
        if "|-1" in line:
            tempSplit = line.split("|")
            providers.append(tempSplit[0])
            costumers.append(tempSplit[1])
        elif "|0" in line:
            tempSplit = line.split("|")
            peers.append([tempSplit[0], tempSplit[1]])
bgpAsFile.close()
# Remove duplicates by making it as group/set
providers_set = providers
costumers_set = costumers
providers_set = set(providers_set)
costumers_set = set(costumers_set)
# Get the providers that they are not costumers
provAndCost = providers_set & costumers_set
Tier1 = providers_set - provAndCost
# Count for each provider how many he costumers he provide
for provider in Tier1:
    numOfCostumers.append([provider, providers.count(provider)])

# Takes only providers who serve a lot of costumers(Nodes)
for provider in numOfCostumers:
    if int(provider[1]) >= 150:
        Tier1_Final.append(provider[0])


# Create names dictionary
with open("names.txt", encoding="utf8") as namesOfAS:
    namesLines = namesOfAS.readlines()
    for namesLine in namesLines:
        namesSplit = namesLine.split(' ', 1)
        namesDict[namesSplit[0].replace("AS", "")] = namesSplit[1].replace("\n", "")
namesOfAS.close()

# Get only names we know from the txt files(Nodes by name)
for provider in Tier1_Final:
    try:
        nodesOfGraphBN[provider] = provider + " : " + namesDict[provider]
    except KeyError:
        Tier1_Final.remove(provider)
        pass

# Checks if there is peer connection between Tier1 members(Edges)
for peer in peers:
    if peer[0] in Tier1_Final:
        if peer[1] in Tier1_Final:
            edgesOfGraphBI.append(peer)

# Print Tier1 As
for key in nodesOfGraphBN:
    print(key + ":" + nodesOfGraphBN[key])

# Draw Graph
graphOfTier1 = nx.Graph()
graphOfTier1.add_nodes_from(nodesOfGraphBN)
graphOfTier1.add_edges_from(edgesOfGraphBI)
pos = nx.spring_layout(graphOfTier1, k=1, iterations=20)
nx.draw(graphOfTier1, pos, labels=nodesOfGraphBN, with_labels=True, node_size=750, node_color='blue',
        edge_color='purple')
plt.show()
