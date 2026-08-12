# 8. Build a HuffmanCoder class with build_tree(frequencies: Dict[str, int]) -> Node and
# generate_codes() -> Dict[str, str] methods accepting character frequencies and returning
# binary encoding mappings.

from dataclasses import dataclass
from typing import Dict, Optional
import heapq


@dataclass
class Node:
    char: Optional[str]
    frequency: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class HuffmanCoder:
    def __init__(self):
        self.root = None
        self.codes = {}

    def build_tree(self, frequencies: Dict[str, int]) -> Node:
        heap = []
        counter = 0

        # Create leaf nodes
        for char, freq in frequencies.items():
            node = Node(char, freq)
            heapq.heappush(heap, (freq, counter, node))
            counter += 1

        # Build Huffman tree
        while len(heap) > 1:
            freq1, _, left = heapq.heappop(heap)
            freq2, _, right = heapq.heappop(heap)

            merged = Node(
                None,
                freq1 + freq2,
                left,
                right
            )

            heapq.heappush(heap, (merged.frequency, counter, merged))
            counter += 1

        self.root = heap[0][2]
        return self.root

    def generate_codes(self) -> Dict[str, str]:
        self.codes = {}

        def generate(node, code):
            if node is None:
                return

            # Leaf node
            if node.char is not None:
                self.codes[node.char] = code
                return

            generate(node.left, code + "0")
            generate(node.right, code + "1")

        generate(self.root, "")

        return self.codes


# ---------------- EXAMPLE ----------------

frequencies = {
    'a': 5,
    'b': 9,
    'c': 12,
    'd': 13,
    'e': 16,
    'f': 45
}

coder = HuffmanCoder()

coder.build_tree(frequencies)

codes = coder.generate_codes()

print("Huffman Codes:")

for char, code in codes.items():
    print(char, ":", code)