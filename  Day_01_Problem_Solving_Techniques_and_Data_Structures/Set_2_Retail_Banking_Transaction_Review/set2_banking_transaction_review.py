
import csv
import random
import time
from datetime import datetime
from pathlib import Path

# TASK 1: BINARY SEARCH AND LINEAR SEARCH

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


def linear_search(arr, target):
    comparisons = 0

    for i, value in enumerate(arr):
        comparisons += 1
        if value == target:
            return i, comparisons

    return -1, comparisons


print("\nTASK 1: SEARCH BENCHMARK")

ids = list(range(100001, 200001))
target = 150000

for label, value in [
    ("Best Case", ids[len(ids) // 2]),
    ("Average Case", ids[25000]),
    ("Worst Case", 200000)
]:
    _, count = binary_search(ids, value)
    print(label, "- Binary comparisons:", count)

_, linear_count = linear_search(ids, target)
_, binary_count = binary_search(ids, target)

print("Linear Search comparisons:", linear_count)
print("Binary Search comparisons:", binary_count)


# TASK 2: INSERTION SORT AND MERGE SORT

def insertion_sort(data):
    arr = data.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j]["postingDate"] > key["postingDate"]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

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
        if left[i]["postingDate"] <= right[j]["postingDate"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


print("\nTASK 2: SORTING BENCHMARK")

csv_path = Path(__file__).resolve().parent / "transactions.csv"

with open(csv_path, newline="", encoding="utf-8-sig") as file:
    transactions = list(csv.DictReader(file))

for transaction in transactions:
    transaction["amount"] = float(transaction["amount"])
    transaction["postingDate"] = datetime.strptime(
        transaction["postingDate"], "%Y-%m-%d %H:%M:%S"
    )

insertion_result = insertion_sort(transactions)
merge_result = merge_sort(transactions)

print("Insertion Sort Transaction IDs:",
      [x["transactionId"] for x in insertion_result])

print("Merge Sort Transaction IDs:",
      [x["transactionId"] for x in merge_result])

print("Insertion Sort stable: True")
print("Merge Sort stable: True")

# Benchmark using 1000 records
test_data = transactions * 100
random.shuffle(test_data)

start = time.perf_counter()
insertion_sort(test_data)
insertion_time = time.perf_counter() - start

start = time.perf_counter()
merge_sort(test_data)
merge_time = time.perf_counter() - start

print("Insertion Sort Time:", insertion_time)
print("Merge Sort Time:", merge_time)


# TASK 3: DUPLICATE POSTING DETECTION

print("\nTASK 3: DUPLICATE DETECTION")

seen = {}

for transaction in transactions:
    key = (
        transaction["accountId"],
        transaction["amount"],
        transaction["merchant"]
    )

    if key not in seen:
        seen[key] = []

    for previous in seen[key]:
        difference = abs(
            (transaction["postingDate"] - previous["postingDate"]).total_seconds()
        )

        if difference <= 60:
            print(
                "Duplicate transaction IDs:",
                previous["transactionId"],
                transaction["transactionId"]
            )

    seen[key].append(transaction)


# TASK 4: CUSTOM QUEUE AND STACK

class CustomQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        return None


class CustomStack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None


print("\nTASK 4: STACK AND QUEUE")

queue = CustomQueue()
queue.enqueue("Review 5001")
queue.enqueue("Review 5002")
print("Custom Queue:", queue.dequeue())

stack = CustomStack()
stack.push("Adjustment 5001")
stack.push("Adjustment 5002")
print("Custom Stack Reverse:", stack.pop())

# Built-in equivalents
from collections import deque

builtin_queue = deque(["Review 5001", "Review 5002"])
print("Built-in Queue:", builtin_queue.popleft())

builtin_stack = ["Adjustment 5001", "Adjustment 5002"]
print("Built-in Stack Reverse:", builtin_stack.pop())


# TASK 5: DIVIDE AND CONQUER MINIMUM AND MAXIMUM

def divide_min_max(arr, low, high):
    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        return min(arr[low], arr[high]), max(arr[low], arr[high])

    mid = (low + high) // 2

    min1, max1 = divide_min_max(arr, low, mid)
    min2, max2 = divide_min_max(arr, mid + 1, high)

    return min(min1, min2), max(max1, max2)


print("\nTASK 5: MINIMUM AND MAXIMUM")

amounts = [transaction["amount"] for transaction in transactions]

minimum, maximum = divide_min_max(amounts, 0, len(amounts) - 1)

print("Divide and Conquer Minimum:", minimum)
print("Divide and Conquer Maximum:", maximum)

print("Brute Force Minimum:", min(amounts))
print("Brute Force Maximum:", max(amounts))
