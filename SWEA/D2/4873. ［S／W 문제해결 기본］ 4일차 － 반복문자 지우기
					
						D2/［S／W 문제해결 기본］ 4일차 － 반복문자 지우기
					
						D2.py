T = int(input())
for test_case in range(1,T+1):
    S = list(input())
    
    while True:
        found = False
        for i in range(len(S)-1):
            if S[i] == S[i+1]:
                S.pop(i)
                S.pop(i)
                found = True
                break
            
        if not found:
            break
        
                
    print(f'#{test_case} {len(S)}')

    