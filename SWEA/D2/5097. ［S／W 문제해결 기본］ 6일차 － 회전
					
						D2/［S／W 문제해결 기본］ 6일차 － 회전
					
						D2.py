from collections import deque
T = int(input())
for test_case in range(1,T+1):
    N, M = map(int, input().split())
    
    q = deque(map(int, input().split()))
    
    
    q.rotate(-M)
    print(f'#{test_case} {q[0]}')
