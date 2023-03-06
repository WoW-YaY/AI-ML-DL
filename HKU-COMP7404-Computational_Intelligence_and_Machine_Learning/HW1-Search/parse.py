import os, sys
def read_graph_search_problem(file_path):
    #Your p1 code here
    f = open(file_path,'r')
    problem = {}
    problem['h'] = {}
    problem['graph'] = {}
    problem['startState'] = f.readline().strip('\n').split()[1:] # the first line is start_state
    problem['goalState'] = f.readline().strip('\n').split()[1:]  # the second line is goal_states
    lines = f.readlines()
    for line in lines:
        s = line.strip('\n').split()
        if len(s) == 2:
            problem['h'][s[0]] = float(s[1])
        if len(s) == 3:
            if s[0] not in problem['graph'].keys():
                problem['graph'][s[0]] = []
            problem['graph'][s[0]].append((float(s[2]),s[1]))
    f.close()
    return problem

def read_8queens_search_problem(file_path):
    #Your p6 code here
    f = open(file_path, 'r')
    problem = []
    lines = f.readlines()
    for line in lines:
        problem.append(line.strip('\n').split())
    f.close()
    return problem

if __name__ == "__main__":
    if len(sys.argv) == 3:
        problem_id, test_case_id = sys.argv[1], sys.argv[2]
        if int(problem_id) <= 5:
            problem = read_graph_search_problem(os.path.join('test_cases','p'+problem_id, test_case_id+'.prob'))
        else:
            problem = read_8queens_search_problem(os.path.join('test_cases','p'+problem_id, test_case_id+'.prob'))
        print(problem)
    else:
        print('Error: I need exactly 2 arguments!')