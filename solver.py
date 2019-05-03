# Put your solution here.
import networkx as nx
import random
import operator

def solve(client):
    client.end()
    client.start()

    # initialize some useful sets and lists
    mst = nx.minimum_spanning_tree(client.G)
    pathLength = {}
    for vertex in mst.nodes:
        currLen = nx.shortest_path_length(mst, client.h, vertex) # could be mst/G
        pathLength[vertex] = currLen
    all_students = list(range(1, client.students + 1))
    non_home = list(range(1, client.home)) + list(range(client.home + 1, client.v + 1))
    

	# Setting initial scout results to false for all vertices
    # Scout all students, making it true to scout results if greater than 0.4

    ScoutResults = {}
    ScoutResults[client.h] = 0

    for vertex in non_home:
        trueNum = 0
        report = client.scout(vertex, all_students)
        for i in report.values():
            if i:
                trueNum += 1
        ScoutResults[vertex] = trueNum/len(report)

    # remote rest of the nodes if not all bots is found. 
    print(client.bot_locations)

    # Find all bot locations.
    sorted_ScoutResults = sorted(ScoutResults.items(), key=operator.itemgetter(1))
    sorted_ScoutResults.reverse()
    for vertex, prob in sorted_ScoutResults:
        print(f'Finding Bots {prob}.')
        if knownBotsEqualToTotal(client):
            break
        remoteBot(client, mst, vertex, pathLength)

#        minProbBot = findMinProb(client, mst, vertex, ScoutResults)
#        result = client.remote(vertex, minProbBot)
#        if result > 0:
#            ScoutResults[minProbBot] = 1
#            ScoutResults[vertex] = 0

    print(client.bot_locations)
    
    while True:
        print("Returning home")
        furBot = findFurthestBot(client, pathLength)
        if furBot == None:
            break
        remoteBot(client, mst, furBot, pathLength)

    client.end()

##############################################################
## Following are some useful functions that we implemented. ##
##############################################################

# return if the total number of known bots is equal to the total bots.
def knownBotsEqualToTotal(client):
	return len(client.bot_locations) == client.l

# find the bot which has the largest distance to home vertex h.
def findFurthestBot(client, pathLength):
    # unique vertex indices of all bot 
    bot_loc = set(client.bot_locations)
    max_Len = 0
    max_bot = None
    for vertex in bot_loc:
        if (pathLength[vertex] > max_Len):
            max_Len = pathLength[vertex]
            max_bot = vertex 
    return max_bot		

# remote the bot toward the direction of home vertex h.
def remoteBot(client, graph, bot, pathLength):
    neighbors = graph.neighbors(bot)
    minLen = float('inf')
    minNeighbor = None
    for neighbor in neighbors:
        if minLen > pathLength[neighbor]:
            minLen = pathLength[neighbor]
            minNeighbor = neighbor
    client.remote(bot, minNeighbor)

def remoteBotOpposite(client, graph, bot, pathLength):
    neighbors = graph.neighbors(bot)
    maxLen = 0
    maxNeighbor = None
    for neighbor in neighbors:
        if maxLen < pathLength[neighbor]:
            maxLen = pathLength[neighbor]
            maxNeighbor = neighbor
    client.remote(bot, maxNeighbor)
		
def findMinProb(client, graph, bot, ScoutResults):
    neighbors = list(graphv.neighbors(bot))
    minProbVertex = neighbors[0]
    for neighbor in neighbors:
        if ScoutResults[neighbor] < ScoutResults[minProbVertex]:
            minProbVertex = neighbor
    return minProbVertex

def remoteNearBots(client):
    homeNeighbors = list(client.graph.neighbors(client.h))
    for neighbor in homeNeighbors:
        client.remote(neighbor, client.h)

	








	






