# Set 3 – Complexity and Data Structure Rationale

## 1. Searching Algorithms

| Algorithm | Best Case | Average Case | Worst Case |
|---|---|---|---|
| Linear Search | O(1) | O(n) | O(n) |
| Binary Search | O(1) | O(log n) | O(log n) |

Binary Search works efficiently on sorted patient IDs.

## 2. Sorting Algorithms

| Algorithm | Best Case | Average Case | Worst Case |
|---|---|---|---|
| Selection Sort | O(n²) | O(n²) | O(n²) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |

Selection Sort repeatedly selects the smallest element. Quick Sort partitions appointments around a pivot.

## 3. Double-Booking Detection

A hash-based set stores patient ID and appointment time combinations.

- Average time complexity: O(n)
- Space complexity: O(n)

This avoids repeatedly scanning the complete appointment list.

## 4. Stack and Queue

| Data Structure | Principle | Application |
|---|---|---|
| Queue | FIFO | Walk-in token line |
| Stack | LIFO | Recent patients viewed |

Both structures support efficient insertion and removal operations.

## 5. Appointment Scheduling

Dynamic Programming calculates the maximum number of non-overlapping appointments.

- Time complexity: O(n²) in the implemented approach.
- Space complexity: O(n).

The greedy method selects appointments by earliest finishing time and is used for comparison.

## Conclusion
The selected algorithms and data structures support efficient patient searching, appointment sorting, double-booking detection and doctor scheduling.