# message = "Hello, my name' s abderrahmane I am 26 years old and I work as an software developper and work in my PHD in physics"
# freq_hash = {}
# for char in message:
#     # freq_hash[char] = freq_hash.get(char, 1)
#     # freq_hash[char] += 1

#     freq_hash[char] = freq_hash.setdefault(char, 0)
#     freq_hash[char] += 1
# print(freq_hash)


# pharmacy_prices = {
#     "panadol": 32,
#     "cold free": 25,
#     "omega 3": 45,
#     "fuciden": 37
# }

# user_input = input("Enter the item to search for: ").strip().lower()

# item_price = pharmacy_prices.get(user_input, "Not Available")
# print(item_price)
# If you want to add another item with new way

# pharmacy_prices["panadol extra"] = pharmacy_prices.get("panadol extra", 42)

# print(pharmacy_prices)


import heapq


class HeapNode:
    def __init__(self, data, frep):
        self.data = data
        self.freq = frep
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class Huffman:
    def __init__(self, message):
        self.internal_node = chr(0)
        self.codes = {}
        freq_hash = {}
        for char in message:
            freq_hash[char] = freq_hash.get(char, 0) + 1

        self.min_heap = []

        for char, freq in freq_hash.items():
            new_node = HeapNode(char, freq)
            heapq.heappush(self.min_heap, (new_node.freq, new_node))

        while len(self.min_heap) > 1:
            left_freq, left_node = heapq.heappop(self.min_heap)
            right_freq, right_node = heapq.heappop(self.min_heap)
            new_freq = left_freq + right_freq
            new_node = HeapNode(self.internal_node, new_freq)
            new_node.left = left_node
            new_node.right = right_node
            heapq.heappush(self.min_heap, (new_node.freq, new_node))
        self.generate_codes(self.min_heap[0][1], "")

    def generate_codes(self, node, code):
        if node is None:
            return
        if node.data != self.internal_node:
            self.codes[node.data] = code

        self.generate_codes(node.left, code + "0")
        self.generate_codes(node.right, code + "1")

    def get_codes(self):
        return self.codes


msg = "The output from Huffman's algorithm can be viewed as a variable length code table for encoding a source symbol. The algorithm derives this table from the estimated probability or frequency of occurrence for each possible value of the source symbol. as in other entropy encoding methods, more common symbols are generally represented using fewer bits than less common symbols. Huffman's method can be efficiently implemented, finding a code in time linear to the number of input weights if these weights are sorted. However, although optimal among methods encoding symbols separately, Huffman coding is not always optimal among all compression methods it is replaced with arithmetic coding or asymmetric numeral systems if better compression ratio is required."

huff = Huffman(msg)
codes = huff.get_codes()
for char, freq in codes.items():
    print(char, freq)
