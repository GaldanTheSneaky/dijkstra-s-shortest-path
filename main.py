from collections import defaultdict

class Node_Distance :

    def __init__(self, name, dist):
        self.name = name
        self.dist = dist

class Graph :

    def __init__(self, node_count):
        self.adjlist = defaultdict(list)
        self.node_count = node_count
        self.parent_node = []
        for i in range(self.node_count):
            self.parent_node.append(-1)

    def Add_Into_Adjlist(self, src, node_dist):
        self.adjlist[src].append(node_dist)

    def Dijkstras_Shortest_Path(self, source):
        distance = []
        for i in range(self.node_count):
            distance.append(99999999)
        distance[source] = 0

        dict_node_length = {source: 0}

        while dict_node_length :
            current_source_node = min(dict_node_length, key=lambda k: dict_node_length[k])
            del dict_node_length[current_source_node]

            for node_dist in self.adjlist[current_source_node]:
                adjnode = node_dist.name
                length_to_adjnode = node_dist.dist

                if distance[adjnode] > distance[current_source_node] + length_to_adjnode:
                    distance[adjnode] = distance[current_source_node] + length_to_adjnode
                    dict_node_length[adjnode] = distance[adjnode]
                    self.parent_node[adjnode] = current_source_node

        for i in range(self.node_count):
            print("Source Node ("+str(source)+")  -> Destination Node(" + str(i) + ")  : " + str(distance[i]))
            path = []
            path_node = self.parent_node[i]
            while path_node != -1:
                path.append(path_node)
                path_node = self.parent_node[path_node]
            path.reverse()
            print(path)


with open('input.txt') as input_file:
    size = [int(x) for x in next(input_file).split()]
    graph = Graph(size[0])
    for line in input_file:
        source, dest, dist = [int(x) for x in line.split()]
        graph.Add_Into_Adjlist(source, Node_Distance(dest, dist))

print("Enter source node:\n")
source_node = int(input())
graph.Dijkstras_Shortest_Path(source_node)



