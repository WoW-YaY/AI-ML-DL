import sys, grader, parse
import collections

def dfs_search(problem):
    #Your p1 code here
    stateSpaceGraph = problem['graph']
    startState = problem['startState']
    goalState = problem['goalState']
    frontier = collections.deque([startState])
    exploredSet = []  # use list to contain the order
    solutionPath = None
    while frontier:
        node = frontier.pop()  # 'node' is a list (path)
        if node[-1] in goalState:
            solutionPath = node
            break
        if node[-1] not in exploredSet:
            exploredSet.append(node[-1])
            if node[-1] in stateSpaceGraph.keys():
                for child in stateSpaceGraph[node[-1]]:
                    frontier.append(node + [child[1]])

    # generate the answer format
    symbol = ' '
    solution = symbol.join(exploredSet) + '\n' + symbol.join(solutionPath)
    return solution

if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 1
    grader.grade(problem_id, test_case_id, dfs_search, parse.read_graph_search_problem)