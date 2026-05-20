T = int(input())
for test_case in range(1, T+1):
    P, A, B = map(int,input().split())
    
    A_num = 0
    B_num = 0

    #A
    left = 1
    right = P
    
    while True:
        A_num += 1
        mid = (left+right)//2
        if mid == A:
            break
        elif A<mid:
            right = mid
        else:
            left = mid

    #B
    left = 1
    right = P
    
    while True:
        B_num += 1
        mid = (left+right)//2
        if mid == B:
            break
        elif B<mid:
            right = mid
        else:
            left = mid

        mid = (left+right)//2


    if A_num < B_num:
        print(f'#{test_case} A')
    elif A_num > B_num:
        print(f"#{test_case} B")
    else:
        print(f'#{test_case} 0')
    
