# Set 1 – Retail Order Desk

## Project Overview
This project implements searching, sorting, duplicate detection, stack and queue operations, and refund calculation using Greedy and Dynamic Programming techniques.

## Tasks Implemented

### Task 1: Search Benchmark
- Implemented Linear Search and Binary Search.
- Tested using 50,000 records.
- Linear Search comparisons: 50,000
- Binary Search comparisons: 16

### Task 2: Sorting Benchmark
Implemented:
- Selection Sort – O(n²)
- Merge Sort – O(n log n)
- Python Built-in Sort

Tested with 10,000 records.

| Algorithm | Execution Time |
|---|---:|
| Selection Sort | 2.89785 seconds |
| Merge Sort | 0.02502 seconds |
| Built-in Sort | 0.00127 seconds |

Both custom sorting algorithms passed validation.

### Task 3: Duplicate Detection
Used a hash-based structure to identify orders with the same customer ID and amount within the same minute.

Detected duplicate pairs:
- Order IDs 1001 and 1003
- Order IDs 1002 and 1005

### Task 4: Stack and Queue
Implemented custom and built-in versions of:
- Stack for undo operations.
- Queue for order dispatch.

Both implementations produced the expected results.

### Task 5: Greedy vs Dynamic Programming
Refund amount: 6

Denominations: [1, 3, 4]

- Greedy solution: [4, 1, 1] – 3 coins
- Dynamic Programming solution: [3, 3] – 2 coins

Dynamic Programming produced the optimal solution.

## Conclusion
All five tasks were implemented and tested successfully. The results demonstrate the differences in algorithm efficiency and the practical use of data structures in a retail order management system.