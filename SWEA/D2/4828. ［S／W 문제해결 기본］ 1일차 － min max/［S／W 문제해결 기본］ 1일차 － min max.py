T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    result = A[-1] - A[0]

    print(f'#{test_case} {result}')
