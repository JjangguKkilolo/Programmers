T = int(input())
for test_case in range(1, T+1):
    E, N = map(int,input().split())

    tree = [[] for _ in range(E+2)]

    node = list(map(int, input().split()))

    it = iter(node)

    for a, b in zip(it,it):
        tree[a].append(b)



    def dfs(node):
        cnt = 1

        for next_node in tree[node]:
            cnt +=dfs(next_node)

        return cnt

    answer = dfs(N)

    print(f"#{test_case} {answer}")
