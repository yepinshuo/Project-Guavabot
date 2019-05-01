# Put your solution here.
import networkx as nx
import random

def solve(client):
    client.end()
    client.start()

    # cant_scout    : a list of sets, each set representing the
    #                 vertices that student i may not scout.
    # bot_count     : a list storing the number of bots at vertex i.
    # bot_locations : a list of vertex indices, one for each
    #                 known bot. Generated from bot_count.

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
    	if trueNum/len(report) >= 0.5:
    		ScoutResults[vertex] = True
    	else:
    		ScoutResults[vertex] = False
    
#    for vertex in non_home:
#   	if ScoutResults[vertex]:
#    		num = clinet.remote(vertex, )

    for vertex in non_home:
    	if ScoutResults[vertex]:
   			for u, v in list(client.graph.edges()):
   				if u == vertex:
   					num = client.remote(u, v)
   					break;


#    for _ in range(100):
#        u, v = random.choice(list(client.G.edges()))
#        client.remote(u, v)
	

    client.end()

# return the total number of known bots that
def knownBotsEqualToTotal(client):
	return len(client.bot_locations()) == client.l


def findFurthestBot(client):
	mst=nx.minimum_spanning_tree(client.G)
	pathLength = {}
	# unique vertex indices of all bot 
	bot_loc = set(client.bot_locations)
	max_Len = 0
	max_bot = None
	for vertex in mst.nodes:
		currLen = nx.shortest_path_length(mst,client.h,vertex)
		pathLength[vertex] = currLen
		if vertex in bot_loc & currLen > max_Len:
			max_Len = currLen
			max_bot = vertex
	return max_bot







	






