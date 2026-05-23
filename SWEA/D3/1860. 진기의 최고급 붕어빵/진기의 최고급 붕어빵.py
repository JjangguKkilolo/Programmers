T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()

    #붕어빵
    B = []

    for i in range(0, A[-1]+1):
        B.append((i//M)*K)


    for i in A:
        for j in range(i, len(B)):
            B[j] -= 1


    result = True

    for i in B:
        if i < 0:
            result = False
            break

    if result:
        print(f'#{test_case} Possible')
    else:
        print(f"#{test_case} Impossible")
