# Put your solution here.
import networkx as nx
import random

def solve(client):
    client.end()
    client.start()

    mst=nx.minimum_spanning_tree(client.G)
    pathLength = {}
    for vertex in mst.nodes:
        currLen = nx.shortest_path_length(mst,client.h,vertex)
        pathLength[vertex] = currLen
    all_students = list(range(1, client.students + 1))
    non_home = list(range(1, client.home)) + list(range(client.home + 1, client.v + 1))
    
    
    ScoutResults = {}

	# Setting initial scout results to false for all vertices
    # Scout all students, making it true to scout results if greater than 0.5
    for vertex in non_home:
    	trueNum = 0
    	report = client.scout(vertex, all_students)
    	for i in report.values():
    		if i:
    			trueNum += 1
    	if trueNum/len(report) >= 0.4:
    		ScoutResults[vertex] = True
    	else:
    		ScoutResults[vertex] = False

    # remote the bot that the majority of the students scout TRUE.
    for vertex in non_home:
        if ScoutResults[vertex]:
            remoteBot(client, client.graph, vertex, pathLength)

    print(client.l)
    print(client.bot_locations)
    print(client.h)

    while i in range(100):
        furBot = findFurthestBot(client, mst, pathLength)
        if furBot == None:
            break
        remoteBot(client, mst, furBot, pathLength)

    client.end()

# return if the total number of known bots is equal to the total bots.
def knownBotsEqualToTotal(client):
	return len(client.bot_locations()) == client.l

# find the bot which has the largest distance to home vertex h.
def findFurthestBot(client, mst, pathLength):
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
def remoteBot(client, mst, bot, pathLength):
    neighbors = mst.neighbors(bot)
    minLen = float('inf')
    minNeighbor = None
    for neighbor in neighbors:
        if minLen > pathLength[neighbor]:
            minLen = pathLength[neighbor]
            minNeighbor = neighbor
    client.remote(bot, minNeighbor)


		



	








	






