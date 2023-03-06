import sys, parse, grader, copy

def atk_cnt(board):
    cnt = 0
    for i in range(len(board[0])): # for each column
        for j in range(len(board)): # for each row
            if board[j][i] == 'q':
                for k in range(i+1,len(board[0])): # for the columns in the right side
                    for l in range(len(board)):
                        if board[l][k] == 'q':
                            # detects if two Qs are attackable
                            if j == l or i == k or abs(j-l) == abs(i-k):
                                cnt += 1
    return cnt

def number_of_attacks(problem):
    #Your p6 code here
    atk_board = [[0 for i in range(8)] for j in range(8)]
    for i in range(len(problem[0])): # for each column
        temp = copy.deepcopy(problem)
        for j in range(len(problem)): # for each row
            for k in range(len(problem)):
                temp[k][i] = '.'
            temp[j][i] = 'q'
            atk_board[j][i] = atk_cnt(temp)

    # generate the answer format
    s = []
    for i in range(len(atk_board)):
        for j in range(len(atk_board[0])):
            atk_board[i][j] = str(atk_board[i][j]).rjust(2) # right alignment
    for i in range(len(atk_board)):
        temp = ' '.join(atk_board[i])
        s.append(temp)
    s = '\n'.join(s)
    solution = s
    return solution

if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 6
    grader.grade(problem_id, test_case_id, number_of_attacks, parse.read_8queens_search_problem)