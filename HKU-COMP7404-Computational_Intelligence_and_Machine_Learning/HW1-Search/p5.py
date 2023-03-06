import sys, parse, grader
from heapq import heappush, heappop

def astar_search(problem):
    #Your p5 code here
    stateSpaceGraph = problem['graph']
    startState = problem['startState']
    goalState = problem['goalState']
    h = problem['h']
    frontier = []
    heappush(frontier, (h[startState[0]], startState)) # use the heuristic information
    exploredSet = []  # use list to contain the order
    solutionPath = None
    while frontier:
        node = heappop(frontier)  # use priority queue, for each node: (<distance>, [start, ..., goal])
        if node[1][-1] in goalState:
            solutionPath = node[1]
            break
        if node[1][-1] not in exploredSet:
            exploredSet.append(node[1][-1])
            if node[1][-1] in stateSpaceGraph.keys():
                for child in stateSpaceGraph[node[1][-1]]:
                    heappush(frontier, (node[0] + child[0] - h[node[1][-1]] + h[child[1]], node[1] + [child[1]]))

    # generate the answer format
    symbol = ' '
    solution = symbol.join(exploredSet) + '\n' + symbol.join(solutionPath)
    return solution

if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 5
    grader.grade(problem_id, test_case_id, astar_search, parse.read_graph_search_problem)