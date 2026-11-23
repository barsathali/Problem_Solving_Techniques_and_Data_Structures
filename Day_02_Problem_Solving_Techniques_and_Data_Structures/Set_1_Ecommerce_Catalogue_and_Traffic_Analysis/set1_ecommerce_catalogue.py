import csv
import time
from collections import deque

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


# 2. Hash Table with Chaining
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key, value):
        index = hash(key) % self.size
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = hash(key) % self.size
        for stored_key, value in self.table[index]:
            if stored_key == key:
                return value
        return None


# 3. Graph: BFS, DFS and cycle detection
def graph_bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def graph_dfs(graph, node, visited, order):
    visited.add(node)
    order.append(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            graph_dfs(graph, neighbor, visited, order)


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


def deployment_order(graph):
    indegree = {node: 0 for node in graph}

    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = deque(node for node in graph if indegree[node] == 0)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == len(graph) else None


# 4. Sliding Window: Busiest continuous 3-hour period
def busiest_window(values):
    window_sum = sum(values[:3])
    best_sum = window_sum
    best_start = 0

    for i in range(3, len(values)):
        window_sum += values[i] - values[i - 3]
        if window_sum > best_sum:
            best_sum = window_sum
            best_start = i - 2

    return best_start, best_sum


# 5. Two Pointers: Find pairs equal to target
def find_pairs(values, target):
    left = 0
    right = len(values) - 1
    pairs = []

    while left < right:
        total = values[left] + values[right]

        if total == target:
            pairs.append((values[left], values[right]))
            left += 1
            right -= 1
        elif total < target:
            left += 1
        else:
            right -= 1

    return pairs


def main():
    print("SET 1 - E-COMMERCE CATALOGUE AND TRAFFIC ANALYSIS")

    # Task 1: BST
    print("\n1. PRODUCT CATEGORY BST")
    bst = BST()

    with open("products.csv", newline="") as file:
        categories = list(csv.DictReader(file))

    for row in categories:
        bst.insert(row["categoryName"])

    print("Inorder:")
    bst.inorder(bst.root)
    print("\nPreorder:")
    bst.preorder(bst.root)
    print("\nPostorder:")
    bst.postorder(bst.root)
    print("\nSearch Electronics:", bst.search("Electronics"))

    # Task 2: Hashing and dictionary comparison
    print("\n\n2. SKU HASHING")

    custom_hash = HashTable(10)
    custom_hash.insert("SKU100", "Laptop")
    custom_hash.insert("SKU200", "Phone")

    print("SKU100 lookup:", custom_hash.search("SKU100"))

    collision_found = False
    for i in range(1000):
        for j in range(i + 1, 1000):
            if hash(f"SKU{i}") % 10 == hash(f"SKU{j}") % 10:
                print("Collision demonstrated:", f"SKU{i}", f"SKU{j}")
                collision_found = True
                break
        if collision_found:
            break

    sku_dict = {f"SKU{i:06d}": f"Product{i}" for i in range(100000)}
    start = time.perf_counter()
    result = sku_dict.get("SKU099999")
    dict_time = time.perf_counter() - start

    print("Built-in dictionary result:", result)
    print("100,000 SKU dictionary lookup time:", dict_time)

    # Task 3: Deployment dependency graph
    print("\n3. MICROSERVICE DEPENDENCY GRAPH")

    graph = {
        "authentication": ["cart"],
        "pricing": ["cart"],
        "inventory": ["cart", "shipping"],
        "cart": ["payment"],
        "payment": ["shipping"],
        "shipping": []
    }

    print("BFS traversal:", graph_bfs(graph, "authentication"))

    dfs_order = []
    graph_dfs(graph, "authentication", set(), dfs_order)
    print("DFS traversal:", dfs_order)

    order = deployment_order(graph)
    print("Valid deployment order:", order)
    print("Circular dependency detected:", has_cycle(graph))

    cyclic_graph = {
        "serviceA": ["serviceB"],
        "serviceB": ["serviceC"],
        "serviceC": ["serviceA"]
    }
    print("Test circular graph:", has_cycle(cyclic_graph))

    # Task 4: Sliding window
    print("\n4. BUSIEST 3-HOUR WINDOW")

    with open("traffic.csv", newline="") as file:
        traffic = list(csv.DictReader(file))

    requests = [int(row["requestsPerMinute"]) for row in traffic]
    start_index, total = busiest_window(requests)

    print("Starting hour:", traffic[start_index]["hour"])
    print("Ending hour:", traffic[start_index + 2]["hour"])
    print("Total requests per minute across the window:", total)

    # Task 5: Two pointers
    print("\n5. GIFT CARD ORDER PAIRS")

    with open("orders.csv", newline="") as file:
        orders = [int(row["orderValue"]) for row in csv.DictReader(file)]

    target = 1000
    print("Gift card target:", target)
    print("Matching pairs:", find_pairs(orders, target))


if __name__ == "__main__":
    main()
