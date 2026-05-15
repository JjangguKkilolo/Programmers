def heappush(heap,value):
    heap.append(value)
    idx = len(heap) - 1

    while idx > 1:
        parent = idx//2

        if heap[parent]<= heap[idx]:
            break

        heap[parent], heap[idx] = heap[idx], heap[parent]
        idx = parent


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    heap = [0]
    value = list(map(int, input().split()))

    ans = 0
    
    for i in range(N):
        heappush(heap, value[i])

    idx = len(heap) - 1
    while idx > 1:
        parent = idx // 2

        ans += heap[parent]

        idx = parent
    
        
    print(f"#{test_case} {ans}")