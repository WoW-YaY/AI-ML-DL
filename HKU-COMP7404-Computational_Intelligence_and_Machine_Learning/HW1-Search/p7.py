import sys, parse, grader, p6

def better_board(problem):
    #Your p7 code here
    atk_board = []
    atk_board_str_list = p6.number_of_attacks(problem).split('\n')
    # transform string to list
    for rows in atk_board_str_list:
        atk_board.append(list(map(int,rows.split())))

    current_atk = p6.atk_cnt(problem)
    better_atk = current_atk
    pos_i,pos_j = -1,-1
    for i in range(len(atk_board)):
        for j in range(len(atk_board[0])):
            if atk_board[i][j] < better_atk:
                better_atk = atk_board[i][j]
                pos_i,pos_j = i,j

    if pos_i >= 0 and pos_j >= 0: # detect if the position is detected
        for k in range(len(problem)):
            if problem[k][pos_j] == 'q':
                problem[pos_i][pos_j], problem[k][pos_j] = problem[k][pos_j], problem[pos_i][pos_j]

    # generate the answer format
    s = []
    for i in range(len(problem)):
        for j in range(len(problem[0])):
            problem[i][j] = str(problem[i][j])
    for i in range(len(problem)):
        temp = ' '.join(problem[i])
        s.append(temp)
    s = '\n'.join(s)
    solution = s
    return solution

if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 7
    grader.grade(problem_id, test_case_id, better_board, parse.read_8queens_search_problem)