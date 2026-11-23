import csv
import time
from collections import deque
from datetime import datetime


# 1. Binary Search Tree
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

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")


# 2. Normalize claims and detect duplicates
def normalize(value):
    return "".join(value.lower().split())


def find_duplicates(claims):
    seen = {}
    duplicates = []

    for claim in claims:
        key = (
            normalize(claim["policyNumber"]),
            claim["incidentDate"]
        )

        if key in seen:
            duplicates.append((seen[key], claim["claimId"]))
        else:
            seen[key] = claim["claimId"]

    return duplicates


# 3. Graph BFS and DFS cycle detection
def shortest_path(graph, start, target):
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


def has_cycle(graph):
    visited = set()
    active = set()

    def visit(node):
        visited.add(node)
        active.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if visit(neighbor):
                    return True
            elif neighbor in active:
                return True

        active.remove(node)
        return False

    for node in graph:
        if node not in visited and visit(node):
            return True

    return False


# 4. Sliding window: longest consecutive days above threshold
def longest_above_threshold(values, threshold):
    best_start = -1
    best_length = 0
    current_start = 0
    current_length = 0

    for i, value in enumerate(values):
        if value > threshold:
            if current_length == 0:
                current_start = i
            current_length += 1

            if current_length > best_length:
                best_length = current_length
                best_start = current_start
        else:
            current_length = 0

    return best_start, best_length


# 5. Two-pointer merge of sorted regional claim lists
def merge_sorted_lists(first, second):
    i = 0
    j = 0
    merged = []

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            merged.append(first[i])
            i += 1
        else:
            merged.append(second[j])
            j += 1

    merged.extend(first[i:])
    merged.extend(second[j:])
    return merged


def main():
    print("SET 2 - INSURANCE CLAIMS PROCESSING")

    # Task 1: BST
    print("\n1. CLAIM ID BINARY SEARCH TREE")

    with open("claims.csv", newline="") as file:
        claims = list(csv.DictReader(file))

    bst = BST()
    for claim in claims:
        bst.insert(claim["claimId"])

    print("Inorder:")
    bst.inorder(bst.root)
    print("\nPreorder:")
    bst.preorder(bst.root)
    print("\nPostorder:")
    bst.postorder(bst.root)
    print("\nSearch CL1005:", bst.search("CL1005"))
    print("Inorder traversal gives sorted claim IDs.")

    # Task 2: Duplicate detection
    print("\n\n2. DUPLICATE CLAIM DETECTION")
    duplicates = find_duplicates(claims)
    print("Duplicate or near-duplicate claims:", duplicates)

    # Demonstrate collision using a small hash table
    buckets = [[] for _ in range(5)]
    for policy in ["POL100", "POL101", "POL102"]:
        index = sum(ord(char) for char in policy) % 5
        buckets[index].append(policy)

    print("Hash buckets:", buckets)
    print("Collisions occur when different keys map to the same bucket.")

    # Task 3: Claim approval graph
    print("\n3. CLAIM APPROVAL GRAPH")

    graph = {
        "Registration": ["Assessment"],
        "Assessment": ["Surveyor"],
        "Surveyor": ["Settlement"],
        "Settlement": []
    }

    print(
        "Shortest path:",
        shortest_path(graph, "Registration", "Settlement")
    )
    print("Cycle detected:", has_cycle(graph))

    cyclic_graph = {
        "Registration": ["Assessment"],
        "Assessment": ["Surveyor"],
        "Surveyor": ["Assessment"]
    }
    print("Cycle test graph detected:", has_cycle(cyclic_graph))

    # Task 4: Daily claim counts
    print("\n4. CONSECUTIVE DAYS ABOVE 100 CLAIMS")

    daily_claims = [
        80, 110, 125, 140, 90, 115, 130, 150,
        160, 70, 105, 120, 135, 95, 80
    ]

    start, length = longest_above_threshold(daily_claims, 100)
    print("Daily claim counts:", daily_claims)

    if length:
        print("Longest run starts at day:", start + 1)
        print("Number of consecutive days:", length)
    else:
        print("No days exceeded the threshold.")

    # Task 5: Merge regional sorted claim lists
    print("\n5. MERGE REGIONAL CLAIM LISTS")

    with open("regional_claims.csv", newline="") as file:
        rows = list(csv.DictReader(file))

    north = sorted(row["claimId"] for row in rows if row["region"] == "North")
    south = sorted(row["claimId"] for row in rows if row["region"] == "South")

    print("North claims:", north)
    print("South claims:", south)
    print("Merged claims:", merge_sorted_lists(north, south))

    # Empty input and duplicate test cases
    print("\nTEST CASES")
    print("Empty BST search:", BST().search("CL9999"))
    print("Empty merge:", merge_sorted_lists([], []))
    print("Duplicate test:", find_duplicates([
        {
            "claimId": "A",
            "policyNumber": "POL100",
            "incidentDate": "2026-10-01"
        },
        {
            "claimId": "B",
            "policyNumber": " pol 100 ",
            "incidentDate": "2026-10-01"
        }
    ]))


if __name__ == "__main__":
    main()
