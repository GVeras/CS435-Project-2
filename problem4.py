from problem3 import *

class DirectedGraph(Graph):
    def addDirectedEdge(self, first: Node, second: Node) -> None:
        firstNeighbors=[node.val for node in self.nodes[first.val].neighbors]
        secondNeighbors=[node.val for node in self.nodes[second.val].neighbors]
        if second.val not in firstNeighbors and first.val not in secondNeighbors and not self.isCycle(second,first):
        #if not self.isCycle(second,first):
            self.nodes[first.val].neighbors.append(second)

    def removeUndirectedEdge(self, first: Node, second: Node) -> None:
        firstNeighbors=[node.val for node in self.nodes[first.val].neighbors]
        if second.val in firstNeighbors:
            self.nodes[first.val].neighbors.remove(second)
    
    def isCycle(self, start: Node, end: Node):
        visited=[]
        stack=[start]
        while stack:
            currNode=stack.pop()
            if currNode.val not in visited:
                if currNode.val==end.val:
                    return True
                visited.append(currNode.val)
                stack.extend(currNode.neighbors)
        return False

    
class TopSort:
    def Kahns(self, graph: DirectedGraph) -> List:
        path=[]
        visitedset()
        queue=self.getZeroDegreedNodes(graph,visited)
        visited=set(queue) #make a copy of an already made set
        while queue:
            currNode=queue.pop()
            path.add(currNode)
            if len(queue)==1:
                queue=self.getZeroDegreedNodes(graph,visited)
                visited.union(queue)
        return path
    
    def getZeroDegreedNodes(self,graph: Graph,visited: Set) -> List:
        res=set(graph.nodes.keys())-visited
        allNeighbors=[]
        for node in graph.getAllNodes():
            if node.val not in visited:
                    allNeighbors.extend(node.neighbors)    
        allNeighbors=[node.val for node in allNeighbors] 
        return res-set(allNeighbors)
    
    def mDFS(self, graph: DirectedGraph) -> List:
        path=list()
        for node in graph.getAllNodes():
            if node.val not in path:
                self.mDFSHelper(node,path)
        return path[::-1]
    
    def mDFSHelper(self, node: Node, path: List) -> List:
        path.append(node.val)
        if node.val not in path:
            neighbors=set(node.neighbors)-set(path)
            for neighbor in neighbors:
                   self.mDFSHelper(neighbor,path)

def createRandomDAGIter(n: int) -> DirectedGraph:
    randomGraph=DirectedGraph()
    for j in range(n):
        randomGraph.addNode(str(j))
    for i in range(n):
        randomNum=random.randint(0,99)
        while randomNum<65:
            secondNum=str(random.randint(0,n-1))
            if secondNum==str(i):
                continue
            randomGraph.addDirectedEdge(randomGraph.getPointer(str(i)),randomGraph.getPointer(secondNum))
            randomNum=random.randint(0,99)
    return randomGraph

rand=createRandomDAGIter(1000)
#print(rand)
search=TopSort()
#print(search.Kahns(rand))
#print(search.mDFS(rand))

