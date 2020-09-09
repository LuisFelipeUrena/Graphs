# from projects.graph import Graph

# Note: This Queue class is sub-optimal. Why?
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        import warnings
        if vertex_id in self.vertices:
            return warnings.warn('vertex already in the graph')


        self.vertices[vertex_id] = set()
        

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        import warnings
        if v1 not in self.vertices and v2 not in self.vertices:
           return warnings.warn('v1 not in self.vertices, please add')
        else:
            self.vertices[v1].add(v2)


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        to_visit = Queue()
        visited = set()
        to_visit.enqueue(starting_vertex)
       
        while to_visit.size() > 0:
            v = to_visit.dequeue()
           
            if v not in visited:
                print(v)
                visited.add(v)
            
                for n in self.get_neighbors(v):
                    to_visit.enqueue(n)   

        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        to_visit = Stack()
        visited = set()
        to_visit.push(starting_vertex)
        while to_visit.size() > 0:
            v = to_visit.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for n in self.get_neighbors(v):
                    to_visit.push(n)

    
    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # keep track of the ones we already visited
        visited = set()
        # define a inner function to apply the recursion
        def _inner(vertex):
            # if the vertex we pass into the inner function is already in the cache
            # just return
            if vertex in visited:
                return
            #otherwise add it to the cache 
            else:
                visited.add(vertex)
            # print the vertex
            print(vertex)
            # recurse on each neighbor
            for neighbors in self.get_neighbors(vertex):
                _inner(neighbors)
        # call the inner recursion on the starting vertex
        _inner(starting_vertex)        


       

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # keep track of the visited paths
        visited = set()
        # keep a queue of the path
        path_q = Queue()
        # add the starting point to the queue
        # wrap the starting vertex in a list
        path_q.enqueue([starting_vertex])
        while path_q.size() > 0:
            # while the queue has elements on it...
            # get the path that was dequeued
            path = path_q.dequeue()
            # get the last element of that path
            last_vertex = path[-1]
            # check if the last element is in the list 
            # if not just continue
            if last_vertex in visited:
                continue
            # otherwise add the last vertex to the visited cache
            # since we were already there
            else:
                visited.add(last_vertex)
            # then loop thru each of the neighbors of the last vertex 
            for i in self.get_neighbors(last_vertex):
                # get the path that is on the queue and make a copy...
                next_path = path.copy()
                # and append each neighbor to it
                next_path.append(i)    

                # if we find that one of the neighbors is the one we
                # were looking for return it
                if i == destination_vertex:
                    return next_path
                # other wise enqueue the next math    
                path_q.enqueue(next_path)    

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = {}
        to_search = Stack()
        to_search.push((starting_vertex,None))
        while to_search.size() > 0:
            (vertex, prev) = to_search.pop()
            if vertex not in visited:
                visited[vertex] = prev
                if vertex == destination_vertex:
                    step = vertex
                    path = []
                    while step is not None:
                        path.append(step)
                        step = visited[step]
                    return path[::-1]
            for edge in self.vertices[vertex]:
                if edge not in visited:
                    to_search.push((edge,vertex))



def earliest_ancestor(ancestors, starting_node):
    # append each childs parent into the graph
    children_parents = Graph()
    for i in ancestors:
        parent = i[0]
        child = i[1]
        if child in children_parents.vertices:
            children_parents.add_edge(child,parent)
        else:    
            children_parents.add_vertex(child)
            children_parents.add_edge(child,parent)
    #first we have to see if the node has any children or not
    # if it does not it means that it has no early ancestor so just return 1
    if starting_node not in children_parents.vertices:
        return print(-1)
    # otherwise we take the minimum value out of the get_neighbors
    # and apply get neighbors until we reach a point where the minimum value is the earlies ancestor
    min_numeric = min(children_parents.get_neighbors(starting_node))
    while min_numeric in children_parents.vertices:

            
        min_numeric = min(children_parents.get_neighbors(min_numeric))
    
    return print(int(min_numeric))

        
        
                 



if __name__ == "__main__":
    x = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    for i in range(1,12):
        earliest_ancestor(x,i)


