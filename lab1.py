import heapq
from collections import defaultdict, Counter


def calculate_frequency(my_text):
    my_text = my_text.upper().replace(' ', '')
    frequency = dict(Counter(my_text))
    return frequency


def build_heap(freq):
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapq.heapify(heap)
    return heap


def build_tree(heap):
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return heap[0]


freq = calculate_frequency("aaabbbbbccccccddddee")
heap = build_heap(freq)
tree = build_tree(heap)
for pair in tree[1:]:
    print(pair[0], '->', pair[1])
