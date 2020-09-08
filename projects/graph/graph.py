"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

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


    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
