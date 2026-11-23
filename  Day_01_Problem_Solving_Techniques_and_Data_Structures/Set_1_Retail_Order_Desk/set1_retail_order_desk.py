
import csv
import random
import time
from datetime import datetime
from collections import deque


# TASK 1: LINEAR SEARCH AND BINARY SEARCH

def linear_search(data, target):
    comparisons = 0
    for item in data:
        comparisons += 1
        if item["orderId"] == target:
            return item, comparisons
    return None, comparisons


def binary_search(data, target):
    left, right = 0, len(data) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if data[mid]["orderId"] == target:
            return data[mid], comparisons
        elif data[mid]["orderId"] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None, comparisons


# TASK 2: SELECTION SORT AND MERGE SORT

def selection_sort(data):
    arr = data.copy()

    for i in range(len(arr)):
        best = i
        for j in range(i + 1, len(arr)):
            if arr[j]["amount"] > arr[best]["amount"]:
                best = j
        arr[i], arr[best] = arr[best], arr[i]

    return arr


def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]["amount"] >= right[j]["amount"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result + left[i:] + right[j:]


def selection_trace(data):
    arr = data.copy()
    print("\nSelection Sort - First Three Passes")

    for i in range(min(3, len(arr))):
        best = i
        for j in range(i + 1, len(arr)):
            if arr[j]["amount"] > arr[best]["amount"]:
                best = j
        arr[i], arr[best] = arr[best], arr[i]
        print("Pass", i + 1, [x["amount"] for x in arr])


def merge_trace(data):
    arr = data.copy()
    print("\nMerge Sort - First Three Merge Passes")

    width = 1
    pass_no = 1

    while width < len(arr) and pass_no <= 3:
        merged = []

        for start in range(0, len(arr), 2 * width):
            left = arr[start:start + width]
            right = arr[start + width:start + 2 * width]

            i = j = 0
            part = []

            while i < len(left) and j < len(right):
                if left[i]["amount"] >= right[j]["amount"]:
                    part.append(left[i])
                    i += 1
                else:
                    part.append(right[j])
                    j += 1

            merged.extend(part + left[i:] + right[j:])

        arr = merged
        print("Pass", pass_no, [x["amount"] for x in arr])
        width *= 2
        pass_no += 1


# TASK 3: HASH-BASED DUPLICATE DETECTION

def find_duplicates(orders):
    seen = {}
    duplicates = []

    for order in orders:
        dt = datetime.strptime(
            order["createdAt"], "%Y-%m-%d %H:%M:%S"
        )
        minute = dt.strftime("%Y-%m-%d %H:%M")

        key = (
            order["customerId"],
            float(order["amount"]),
            minute
        )

        if key in seen:
            duplicates.append((seen[key], order))
        else:
            seen[key] = order

    return duplicates


# TASK 4: CUSTOM STACK AND QUEUE

class CustomStack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop() if self.items else None


class CustomQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.pop(0) if self.items else None


# TASK 5: GREEDY AND DYNAMIC PROGRAMMING

def greedy_change(amount, denominations):
    result = []

    for coin in sorted(denominations, reverse=True):
        while amount >= coin:
            amount -= coin
            result.append(coin)

    return result if amount == 0 else None


def dp_change(amount, denominations):
    dp = [float("inf")] * (amount + 1)
    choice = [0] * (amount + 1)
    dp[0] = 0

    for value in range(1, amount + 1):
        for coin in denominations:
            if coin <= value and dp[value - coin] + 1 < dp[value]:
                dp[value] = dp[value - coin] + 1
                choice[value] = coin

    if dp[amount] == float("inf"):
        return None

    result = []
    while amount > 0:
        coin = choice[amount]
        result.append(coin)
        amount -= coin

    return result


# MAIN PROGRAM

with open("orders.csv", newline="") as file:
    orders = list(csv.DictReader(file))

for order in orders:
    order["orderId"] = int(order["orderId"])
    order["amount"] = float(order["amount"])


print("\nTASK 1: SEARCH BENCHMARK")

records = [
    {"orderId": i, "amount": random.randint(100, 10000)}
    for i in range(1, 50001)
]

target = 50000
sorted_records = sorted(records, key=lambda x: x["orderId"])

start = time.perf_counter()
linear_result, linear_comparisons = linear_search(records, target)
linear_time = time.perf_counter() - start

start = time.perf_counter()
binary_result, binary_comparisons = binary_search(sorted_records, target)
binary_time = time.perf_counter() - start

print("Records:", len(records))
print("Target:", target)
print("Linear comparisons:", linear_comparisons)
print("Binary comparisons:", binary_comparisons)
print("Linear time:", linear_time)
print("Binary time:", binary_time)


print("\nTASK 2: SORTING BENCHMARK")

sample = [
    {"orderId": i, "amount": random.randint(100, 10000)}
    for i in range(10000)
]

small_sample = sample[:8]
selection_trace(small_sample)
merge_trace(small_sample)

start = time.perf_counter()
selection_result = selection_sort(sample)
selection_time = time.perf_counter() - start

start = time.perf_counter()
merge_result = merge_sort(sample)
merge_time = time.perf_counter() - start

start = time.perf_counter()
builtin_result = sorted(
    sample, key=lambda x: x["amount"], reverse=True
)
builtin_time = time.perf_counter() - start

print("\nSorting 10,000 records")
print("Selection Sort:", selection_time)
print("Merge Sort:", merge_time)
print("Built-in Sort:", builtin_time)

expected = [x["amount"] for x in builtin_result]

print("Selection correctly sorted:",
      [x["amount"] for x in selection_result] == expected)

print("Merge correctly sorted:",
      [x["amount"] for x in merge_result] == expected)


print("\nTASK 3: DUPLICATE DETECTION")

duplicates = find_duplicates(orders)

for first, second in duplicates:
    print("Duplicate order IDs:",
          first["orderId"], second["orderId"])


print("\nTASK 4: STACK AND QUEUE")

custom_stack = CustomStack()
custom_stack.push("Edit 1001")
custom_stack.push("Edit 1002")
print("Custom Stack Undo:", custom_stack.pop())

builtin_stack = []
builtin_stack.append("Edit 1001")
builtin_stack.append("Edit 1002")
print("Built-in Stack Undo:", builtin_stack.pop())

custom_queue = CustomQueue()
custom_queue.enqueue("Order 1001")
custom_queue.enqueue("Order 1002")
print("Custom Queue Dispatch:", custom_queue.dequeue())

builtin_queue = deque()
builtin_queue.append("Order 1001")
builtin_queue.append("Order 1002")
print("Built-in Queue Dispatch:", builtin_queue.popleft())


print("\nTASK 5: GREEDY VS DYNAMIC PROGRAMMING")

amount = 6
denominations = [1, 3, 4]

greedy_result = greedy_change(amount, denominations)
dp_result = dp_change(amount, denominations)

print("Refund amount:", amount)
print("Denominations:", denominations)
print("Greedy solution:", greedy_result)
print("Greedy notes/coins:", len(greedy_result))
print("DP solution:", dp_result)
print("DP notes/coins:", len(dp_result))
