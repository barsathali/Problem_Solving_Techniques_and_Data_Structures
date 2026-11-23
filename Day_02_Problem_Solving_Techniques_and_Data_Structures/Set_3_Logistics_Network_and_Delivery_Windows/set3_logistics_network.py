import csv
from collections import deque


# 1. Binary Search Tree for hub codes
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right

    def search(self, value):
        current = self.root
        while current:
            if current.value == value:
                return True
            current = current.left if value < current.value else current.right
        return False

    def height(self, node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)


# 2. Hash Map for duplicate parcel scans
def detect_duplicate_scans(parcels):
    seen = set()
    duplicates = []

    for parcel in parcels:
        key = (parcel["trackingNumber"], parcel["hubCode"])

        if key in seen:
            duplicates.append(key)
        else:
            seen.add(key)

    return duplicates


# 3. Graph algorithms
def bfs_shortest_path(graph, start, target):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        node, path = queue.popleft()

        if node == target:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None


def dfs_reachable(graph, start):
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            order.append(node)

            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return order


# 4. Sliding window: highest average for 4 consecutive hours
def highest_four_hour_average(values):
    if len(values) < 4:
        return None

    window_sum = sum(values[:4])
    best_sum = window_sum
    best_start = 0

    for i in range(4, len(values)):
        window_sum += values[i] - values[i - 4]

        if window_sum > best_sum:
            best_sum = window_sum
            best_start = i - 3

    return best_start, best_sum / 4


# 5. Two pointers: palindrome check
def is_palindrome(value):
    cleaned = "".join(char.lower() for char in value if char.isalnum())

    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True


def main():
    print("DAY 2 - SET 3: LOGISTICS NETWORK AND DELIVERY WINDOWS")

    # Task 1: BST
    print("\n1. HUB CODE BINARY SEARCH TREE")

    with open("hubs.csv", newline="") as file:
        hubs = list(csv.DictReader(file))

    codes = [hub["hubCode"] for hub in hubs]

    tree = BST()
    for code in codes:
        tree.insert(code)

    print("Inorder traversal:")
    tree.inorder(tree.root)
    print("\nSearch H05:", tree.search("H05"))
    print("Tree height for CSV insertion order:", tree.height(tree.root))

    sorted_tree = BST()
    for code in sorted(codes):
        sorted_tree.insert(code)

    print("Tree height for sorted insertion:", sorted_tree.height(sorted_tree.root))
    print("Sorted insertion can produce a skewed tree.")

    # Task 2: Duplicate scans
    print("\n2. DUPLICATE PARCEL SCANS")

    with open("parcels.csv", newline="") as file:
        parcels = list(csv.DictReader(file))

    duplicates = detect_duplicate_scans(parcels)
    print("Duplicate tracking number and hub combinations:", duplicates)

    # Task 3: Logistics graph
    print("\n3. LOGISTICS NETWORK GRAPH")

    graph = {
        "H01": ["H02", "H08"],
        "H02": ["H01", "H03", "H04"],
        "H03": ["H02", "H05"],
        "H04": ["H02", "H05", "H06"],
        "H05": ["H03", "H04", "H09"],
        "H06": ["H04", "H07"],
        "H07": ["H06", "H10"],
        "H08": ["H01", "H09"],
        "H09": ["H05", "H08", "H10"],
        "H10": ["H07", "H09"]
    }

    print("Adjacency list:")
    for hub, neighbors in graph.items():
        print(hub, "->", neighbors)

    print("Fewest-hop route H01 to H07:",
          bfs_shortest_path(graph, "H01", "H07"))

    print("Hubs reachable from central depot H01:",
          dfs_reachable(graph, "H01"))

    # Task 4: Four-hour sliding window
    print("\n4. BUSIEST FOUR-HOUR DELIVERY WINDOW")

    with open("hourly_parcels.csv", newline="") as file:
        hourly_data = list(csv.DictReader(file))

    counts = [int(row["parcelCount"]) for row in hourly_data]
    result = highest_four_hour_average(counts)

    if result:
        start, average = result
        print("Starting hour:", hourly_data[start]["hour"])
        print("Ending hour:", hourly_data[start + 3]["hour"])
        print("Highest four-hour average:", average)

    # Task 5: Two-pointer palindrome
    print("\n5. HUB CODE PALINDROME CHECK")

    test_code = "H01-10H"
    print("Hub code sequence:", test_code)
    print("Is palindrome:", is_palindrome(test_code))

    print("Additional test:", is_palindrome("AB-12-21-BA"))
    print("Non-palindrome test:", is_palindrome("H01-H02"))


if __name__ == "__main__":
    main()
