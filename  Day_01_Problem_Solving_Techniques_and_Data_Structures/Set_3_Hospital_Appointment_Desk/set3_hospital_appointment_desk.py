
import csv
import random
import time
from functools import lru_cache


# TASK 1: LINEAR SEARCH AND BINARY SEARCH

def linear_search(records, target):
    for i, record in enumerate(records):
        if record["patientId"] == target:
            return i
    return -1


def binary_search(records, target):
    low, high = 0, len(records) - 1

    while low <= high:
        mid = (low + high) // 2
        value = records[mid]["patientId"]

        if value == target:
            return mid
        elif value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


print("\nTASK 1: SEARCH BENCHMARK")

patients = [
    {"patientId": i, "patientName": "Patient" + str(i)}
    for i in range(20001, 40001)
]

targets = random.Random(42).sample(
    range(20001, 40001), 1000
)

start = time.perf_counter()
for target in targets:
    linear_search(patients, target)
linear_time = time.perf_counter() - start

start = time.perf_counter()
for target in targets:
    binary_search(patients, target)
binary_time = time.perf_counter() - start

print("Patient Records:", len(patients))
print("Lookups:", len(targets))
print("Linear Search Time:", linear_time)
print("Binary Search Time:", binary_time)


# LOAD APPOINTMENTS

with open("appointments.csv", newline="", encoding="utf-8-sig") as file:
    appointments = list(csv.DictReader(file))

for a in appointments:
    a["urgency"] = int(a["urgency"])


# TASK 2: SELECTION SORT AND QUICK SORT

def selection_sort(data):
    arr = data.copy()
    swaps = 0

    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            key1 = (arr[j]["urgency"], arr[j]["arrivalTime"])
            key2 = (arr[minimum]["urgency"], arr[minimum]["arrivalTime"])

            if key1 < key2:
                minimum = j

        if minimum != i:
            arr[i], arr[minimum] = arr[minimum], arr[i]
            swaps += 1

    return arr, swaps


def quick_sort(data):
    arr = data.copy()
    swaps = [0]

    def sort(low, high):
        if low >= high:
            return

        pivot = (
            arr[high]["urgency"],
            arr[high]["arrivalTime"]
        )

        i = low - 1

        for j in range(low, high):
            key = (arr[j]["urgency"], arr[j]["arrivalTime"])

            if key <= pivot:
                i += 1
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps[0] += 1

        if i + 1 != high:
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            swaps[0] += 1

        pivot_index = i + 1

        sort(low, pivot_index - 1)
        sort(pivot_index + 1, high)

    sort(0, len(arr) - 1)
    return arr, swaps[0]


print("\nTASK 2: SORTING BENCHMARK")

selection_result, selection_swaps = selection_sort(appointments)
quick_result, quick_swaps = quick_sort(appointments)

print("Selection Sort Order:")
print([
    (a["patientId"], a["urgency"], a["arrivalTime"])
    for a in selection_result
])

print("Quick Sort Order:")
print([
    (a["patientId"], a["urgency"], a["arrivalTime"])
    for a in quick_result
])

print("Selection Sort Swaps:", selection_swaps)
print("Quick Sort Swaps:", quick_swaps)

start = time.perf_counter()
selection_sort(appointments)
selection_time = time.perf_counter() - start

start = time.perf_counter()
quick_sort(appointments)
quick_time = time.perf_counter() - start

print("Selection Sort Time:", selection_time)
print("Quick Sort Time:", quick_time)


# TASK 3: DOUBLE-BOOKED SLOT DETECTION

print("\nTASK 3: DOUBLE BOOKING DETECTION")

seen = set()

for a in appointments:
    key = (a["patientId"], a["startTime"], a["endTime"])

    if key in seen:
        print(
            "Double booking detected:",
            a["patientId"],
            a["startTime"],
            a["endTime"]
        )
    else:
        seen.add(key)


# TASK 4: CUSTOM QUEUE AND STACK

class CustomQueue:
    def __init__(self):
        self.items = []
        self.front = 0

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.front < len(self.items):
            value = self.items[self.front]
            self.front += 1
            return value
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
queue.enqueue("Patient 2001")
queue.enqueue("Patient 2002")
print("Custom Queue:", queue.dequeue())

stack = CustomStack()
stack.push("Patient 2001")
stack.push("Patient 2002")
print("Custom Stack:", stack.pop())


# TASK 5: DYNAMIC PROGRAMMING FOR APPOINTMENT SCHEDULING

def maximum_appointments(data):
    arr = sorted(
        data,
        key=lambda a: (a["endTime"], a["startTime"])
    )

    n = len(arr)

    previous = []

    for i in range(n):
        p = -1

        for j in range(i - 1, -1, -1):
            if arr[j]["endTime"] <= arr[i]["startTime"]:
                p = j
                break

        previous.append(p)

    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        include = 1 + dp[previous[i - 1] + 1]
        exclude = dp[i - 1]
        dp[i] = max(include, exclude)

    return dp[n]


print("\nTASK 5: DYNAMIC PROGRAMMING")

print(
    "Maximum Appointments:",
    maximum_appointments(appointments)
)

# Greedy comparison: earliest finishing appointment first

def greedy_appointments(data):
    arr = sorted(data, key=lambda a: a["endTime"])
    count = 0
    last_end = ""

    for a in arr:
        if not last_end or a["startTime"] >= last_end:
            count += 1
            last_end = a["endTime"]

    return count


print("Greedy Appointments:", greedy_appointments(appointments))
