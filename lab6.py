import heapq
import math
from collections import Counter


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


def compute_huffman_avg_length(freq, tree, length):
    huffman_avg_length = 0
    for pair in tree[1:]:
        huffman_avg_length += (len(pair[1]) * (freq[pair[0]] / length))
    return huffman_avg_length


def entropy(freq, length):
    H = 0
    P = [fre / length for _, fre in freq.items()]
    for x in P:
        H += -(x * math.log2(x))
    return H


message = "aaabbbbbccccccddddee"
freq = calculate_frequency(message)
heap = build_heap(freq)
tree = build_tree(heap)
# tree=[20, ['D', '0'], ['B', '01'], ['E', '100'], ['A', '101'], ['C', '11']] not optimal
huffman_avg_length = compute_huffman_avg_length(freq, tree, len(message))
H = entropy(freq, len(message))
print("Huffman : %.2f bits" % huffman_avg_length)
print('Entropy : %.2f bits' % H)
if huffman_avg_length >= H:
    print("Huffman code is optimal")
else:
    print("Code is not optimal")
