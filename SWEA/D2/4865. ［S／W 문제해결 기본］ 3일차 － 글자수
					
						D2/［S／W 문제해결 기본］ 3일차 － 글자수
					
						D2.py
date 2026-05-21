T = int(input())
for test_case in range(1, T+1):
    str1 = list(input())
    str2 = list(input())

    d = {}

    for ch in str2:
        d[ch] = d.get(ch,0)+1
        

    result = 0

    for ch in str1:
        if d.get(ch,0) > result:
            result = d[ch]
    

    print(f'#{test_case} {result}')
