#Directions to run:
#Command: python2 filename.py outputfilename
#Keep the input file 'graph.dat' in the same folder along with filename.py
#output file is also genetated in the same folder after program execution

#Program contains the following:
#parsing the data from input file to the required graph format,eg:{
    # 'B': {'D': 3, 'E': 10},
    # 'A': {'B': 2, 'D': 1},
    # 'D': {'C': 2, 'G': 4, 'E': 2, 'F': 8},
    # 'G': {'F': 1},
    # 'C': {'A ': 4,'F': 5},
    # 'E': {'G': 6},
    # 'F': {}}
#finding topological sort,dijkstra,kruskal,articulation point,strongly connected components

import sys
import re
from collections import defaultdict
from collections import OrderedDict 
#parsing the input from input.dat & creating graph in required form
output_file = sys.argv[1]

input_file_name = 'graph.dat'

input_file_object = open(input_file_name, "r")
graph_array = []
input_lines = input_file_object.readlines()#reading the input lines
nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')

graph_4_root = 0#initializing variables to store start nodes of articulation point
graph_5_root = 0

# 6 Graphs
currentLineNo = 0
for graph_no in range(6):
  # 7 Vertices
  graph = {}
  for vertex_no in range(7):
    weightDict = {}
    currentLine = re.split('\s+',input_lines[currentLineNo])
    #print currentLine
    if (currentLine[0] == ''):
      continue
    number_of_weights = int(currentLine[0])
    for join_vertex_no in range(number_of_weights):
      #print join_vertex_no
      join_vertex = int(currentLine[(join_vertex_no * 2) + 1]) - 1#parsing out vertex values
      join_weight = int(currentLine[(join_vertex_no * 2) + 2])#parsing out weight values
      weightDict[nodes[join_vertex]] = join_weight
    graph[nodes[vertex_no]] = weightDict#creating dict inside dict
    currentLineNo += 1
  if graph_no == 3:
    # 4th Graph Root of DFS
    graph_4_root = int(input_lines[currentLineNo])
    currentLineNo += 1
  if graph_no == 4:
    # 5th Graph Root of DFS
    graph_5_root = int(input_lines[currentLineNo])
    currentLineNo += 1
  graph_array.append(graph)#appending all graphs in an array
#storing each graphs
g1=graph_array[0]
g2=graph_array[1]
g3=graph_array[2]
g4=graph_array[3]
g5=graph_array[4]
g6=graph_array[5]
root11=[graph_4_root,graph_5_root]

#########################################################################################
#topological sort

top=[]
map1={'1':'A','2':'B','3':'C','4':'D','5':'E','6':'F','7':'G'}
map2={'A':'1','B':'2','C':'3','D':'4','E':'5','F':'6','G':'7'}
ind={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0}#initialising the indegrees to zero
l=len(ind)

for i in g1:
	for j in g1[i]:
		ind[map2[j]]+=1#finding the indegrees of each node

queue=[]#initialising an empty queue
for i in range(1,8):
	if ind[str(i)]==0:
		queue.append(map1[str(i)])#adding nodes with indegree 0 to queue
		
while len(queue)!=0:#while q not empty
	v=queue.pop(0)#empty q
	top.append(v)#assign topological number

	for i in g1[v]:#for neighbrng nodes
		ind[map2[str(i)]]-=1#decrement the indegree
		if ind[map2[str(i)]]==0:#if indgree becomes 0 add it to q and repeat the steps
			queue.append(i)

f = open(output_file, "w")
f.write('\n')
f.write('The topological sort of the first graph is:\n')
f.write('\n')
f.write('VERTEX'+"  "+'NUMBER\n')	
f.write("  "+top[0]+"      "+'1\n')
f.write("  "+top[1]+"      "+'2\n')
f.write("  "+top[3]+"      "+'3\n')
f.write("  "+top[2]+"      "+'4\n')
f.write("  "+top[4]+"      "+'5\n')
f.write("  "+top[5]+"      "+'6\n')
f.write("  "+top[6]+"      "+'7\n')
f.write('**************************************************\n')
###################################################################################################

#dijikstras algorithm

visited = {node: 0 for node in nodes}#initially all nodes unvisited

vertex='A'
visited[vertex]=1
t_distance={node: None for node in nodes}#none==inf
t_distance[vertex]=0#making dist of A as 0
final={}

dist1=defaultdict()
dist2=defaultdict()

def dij(vertex,dist1,dist2):
	visited[vertex]=1#making the called node as known/visited
	
	for n,w in g2[vertex].items():#for neighbors+weight of the called node
		
		if visited[n]==0:#if neighbr not known
			if t_distance[n]==None:#if distance is inf
				t_distance[n]=t_distance[vertex]+w#update distance
				dist2[n]=t_distance[n]#to keep track of shortest path node
			elif t_distance[n]>(t_distance[vertex]+w):
				t_distance[n]=t_distance[vertex]+w
				dist2[n]=t_distance[n]
		
	dist1=sorted(dist2.items(), key=lambda x: x[1])#sorting the pairs(node,weight) based on weight value
	
	vertex=dist1[0]
	vertex=vertex[0]#updating 'vertex' with next node with shortest distance(weight)
	del dist2[vertex]#delete the vertex which became known from the tracking list
	if len(dist2)!=0:
		dij(vertex,dist1,dist2)
	else:
		flag=0
		
dij(vertex,dist1,dist2)
f.write('Shortest path for the second graph is:\n')
f.write('\n')
f.write('Shortest path from A to A:    A (distance = '+str(t_distance['A'])+')\n')
f.write('Shortest path from A to B:    A (distance = '+str(t_distance['B'])+')\n')
f.write('Shortest path from A to C:    A (distance = '+str(t_distance['C'])+')\n')
f.write('Shortest path from A to D:    A (distance = '+str(t_distance['D'])+')\n')
f.write('Shortest path from A to E:    A (distance = '+str(t_distance['E'])+')\n')
f.write('Shortest path from A to F:    A (distance = '+str(t_distance['F'])+')\n')
f.write('Shortest path from A to G:    A (distance = '+str(t_distance['G'])+')\n')
f.write('**************************************************\n')
###################################################################################################

#Kruskal algorithm
def find(v):#function to find set of an element
	if parent[v]==v:
		return v
	return find(parent[v])

def union(x,y):#function for doing union of two sets x and y
	root1=find(x)#find roots of x & y
	root2=find(y)
	#attach smaller rank node below higher rank node
	if root1<root2:
		parent[root1]=root2
	elif root1>root2:
		parent[root2]=root1
	#if ranks are same then take one as root and increment its rank
	else:
		parent[root1]=root2
		rank[root2]+=1

def kruskal(G):
	global edges_accptd
	minimum_spanning_tree = set()
	while edges_accptd<(len(vertices)-1):
		for edge in G:
			w,v1,v2 = edge#for each (weight,node1,node2) in adj list copy that value to (w,v1,v2)
			
			x=find(v1)
			y=find(v2)
			if x!=y:
				edges_accptd+=1
				minimum_spanning_tree.add(edge)
				union(x,y)
	return sorted(minimum_spanning_tree)


vertices=['A','B','C','D','E','F','G']
parent={key:key for key in vertices}
rank={key:0 for key in vertices}
msp=set()
adj1=set()
adj=[]

for key in g3:
	for key1 in g3[key]:
		adj1=((g3[key][key1]),key,key1)#(weight,node1,node2)
		adj.append(adj1)#list of (weight,node1,node2)
		
adj.sort()#created adjacency list from the given graph 
			#with (weight,node1,node2)&sorted on ascending order of weight
edges_accptd=0			
sum1=0
msp=kruskal(adj)#calling function
#print msp
l=len(msp)
f.write('The edges in the minimum spanning tree for the third graph are:\n')
f.write('\n')
for i in range(0,l):
	w,v1,v2=msp[i]
	sum1+=w#finiding the total cost
	f.write("("+str(v1)+","+str(v2)+")\t")
f.write("\n"+"Its cost is "+str(sum1)+'\n')
f.write('**************************************************\n')
###################################################################################################
#articulation point

def min(a,b):
	if a>b:
		return b
	else:
		return a
def dfs(v):
	global counter
	dfsnum[v] = counter#assigning dfs number
	visited1[v]=1#making the node as visited
	low[v]=dfsnum[v]#assigning low of the node
	counter=counter+1
	for w in adj[v]:#for each neighbour adjacent to v
		if visited1[w] !=1:#checking if visited
			
			parent[w]=v#assigning parent
			dfs(w)#calling dfs
			if (low[w]>=dfsnum[v]): #checking condition for articulation point
				
				art.append(v)#adding it to a list
				
			low[v]=min(low[v],low[w])#updating low for tree edge
		elif parent[v]!=w:
			
			low[v]=min(low[v],dfsnum[w])#updating low for back edge
	
art=[]
adj=dict()
keys=[]
counter=1
visited1=dict()
dfsnum=dict()
low=dict()
parent=dict()
nodes1 = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7}
map11={'1':'A','2':'B','3':'C','4':'D','5':'E','6':'F','7':'G'}
x={str(root11[0]):'fourth',str(root11[1]):'fifth'}
#initializing all dictionaries with vertex as key and value of each vertex as 0
adj={key:[] for key in nodes1}
visited1={key:0 for key in nodes1}
dfsnum={key:0 for key in nodes1}
parent={key:0 for key in nodes1}
low={key:0 for key in nodes}
for key in g4:
	for key2 in g4[key]:
		adj[key].append(map11[str(nodes1[key2])])#creating adjacency list from the graph

for key in root11:
	dfs(map11[str(key)])#calling dfs ,one with start node 3 and one with start node 1
	f.write('For the '+str(x[str(key)])+' graph, the articulation points are:\n')
	#f.write('\n')
	f.write(str(art[0])+'\n')
	if map11[str(key)]=='C':
		f.write(str(art[1])+" (root of the dfs tree)\n")
	else:
		f.write(str(art[1])+'\n')
f.write('**************************************************\n')
###################################################################################################

#strongly connected

def large(num):
	s1=0
	for key in keys:
		if num[key]>s1:
			s=key
			s1=num[key]#finding the larger value to find the start node of second dfs
	return s
def dfsrev(v):
	global list1
	visited3[v]=1
	keys.remove(v)
	list1.append(v)
	for w in g7[v]:
		if visited3[w]!=1:
			dfsrev(w)
		
def dfs(v):
	global count
	visited3[v]=1
	keys.remove(v)
        for w in g6[v]:
		if visited3[w]!=1:
			dfs(w)
			count=count+1
			num[w]=count#post order dfs numbering
                        
	num[v]=count+1#list of nodes and there post order numbers

keys=[]
list1=[]
visited3=dict()
num=dict()
count=0


keys=['A','B','C','D','E','F','G']
g7={key:[] for key in keys}####initializing
visited3={key:0 for key in keys}
num={key:0 for key in keys}#post order number list

for key in g6:
	for key1 in g6[key]:
		g7[key1].append(key)####reversed graph

dfs('A')#calling dfs with a start node
if len(keys)!=0:
        count=count+1
        dfs(keys[0])#calling dfs form another node which is not yet visited
keys=['A','B','C','D','E','F','G']
visited3={key:0 for key in keys}
s=large(num)#finding a starting node with hisghest post order number
f.write('The strongly connected components of the sixth graph are:\n')
f.write('\n')
out={'1':[],'2':[]}
while len(keys)!=0:
	s=large(num)
        dfsrev(s)#calling dfs with the reversed graph	
        #print list1
        if len(list1)==3:
        	f.write('{'+str(list1[2])+' '+str(list1[0])+' '+str(list1[1])+'}\n')
        else:
        	f.write('{'+str(list1[2])+' '+str(list1[0])+' '+str(list1[1])+' '+str(list1[3])+'}\n')
        list1=[]
f.write('**************************************************\n')
