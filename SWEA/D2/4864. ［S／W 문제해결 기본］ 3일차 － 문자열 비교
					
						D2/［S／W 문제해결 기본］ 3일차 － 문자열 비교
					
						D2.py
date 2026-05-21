T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    str2 = input()

    len1 = len(str1)
    len2 = len(str2)
    result = 0

    for i in range(len2-len1+1):
        if str1  == str2[i:i+len1]:
            result = 1

    print(f'#{test_case} {result}')
        
            
