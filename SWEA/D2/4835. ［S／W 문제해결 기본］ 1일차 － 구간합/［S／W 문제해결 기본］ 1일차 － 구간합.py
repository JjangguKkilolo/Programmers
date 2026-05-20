T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    a = list(map(int, input().split()))
    a_sum = [0] * (N - M +1)

    a_min = 10e8
    a_max = 0

    for i in range(N-M+1):
        for j in range(M):
            a_sum[i] += a[i+j]

    
    result = max(a_sum)-min(a_sum)
    print(f'#{test_case} {result}')
