T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    answer = 10e9
    
    def dfs(row, total):
        global answer

        if total >= answer:
            return

        if row == N:
            answer = min(answer, total)
            return

        for col in range(N):
            if not visited[col]:
                visited[col] = True

                dfs(row+1, total+ A[row][col])

                visited[col] = False


    dfs(0,0)

    print(f'#{test_case} {answer}')
    
