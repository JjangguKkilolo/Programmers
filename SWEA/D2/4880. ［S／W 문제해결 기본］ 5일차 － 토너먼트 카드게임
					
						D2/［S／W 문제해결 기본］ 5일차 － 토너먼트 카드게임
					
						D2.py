def winner(a,b):
    if A[a] == A[b]:
        return a
    if (A[a] == 1 and A[b] ==3) or (A[a] == 2 and A[b] == 1) or (A[a] == 3 and A[b] == 2):
        return a
    else:
        return b
    
def tournament(start, end):
    if start == end:
        return start

    mid = (start + end) //2
    left = tournament(start, mid)
    right = tournament(mid+1, end)

    return winner(left, right)





T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    A = [0] + list(map(int, input().split()))

    ans = tournament(1, N)

    print(f"#{test_case} {ans}")
