from models import queue
def search(graph, start):
    # print("TO DO: implement Breadth-First search")
    frontier = queue.Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True

    while not frontier.empty():
        current = frontier.get()
        print("Visiting %r" %(current))
        for next in graph.neighbors(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True