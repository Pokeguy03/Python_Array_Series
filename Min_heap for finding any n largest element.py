#For all n terms
import heapq

def kth_largest(arr, k):
    if len(arr) < k:
        return -1

    heap = []

    for num in arr:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]
