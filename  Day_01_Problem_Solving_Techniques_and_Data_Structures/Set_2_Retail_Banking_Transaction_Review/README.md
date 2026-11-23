# Set 2 – Retail Banking Transaction Review

## Project Overview
This project demonstrates searching, sorting, duplicate transaction detection, queue and stack operations, and divide-and-conquer techniques in a banking transaction review system.

## Tasks Implemented

### Task 1: Search Benchmark
- Created a sorted list of 100,000 transaction IDs.
- Implemented Binary Search and Linear Search.
- Counted comparisons for best, average and worst cases.
- Compared the searching approaches.

### Task 2: Statement Sorting
Implemented:
- Insertion Sort – O(n²)
- Merge Sort – O(n log n)

Both algorithms sort transactions by posting date.

**Stability:** A stable sorting algorithm preserves the original relative order of records with equal timestamps. This is important when multiple transactions share the same posting time.

### Task 3: Duplicate Posting Detection
Used a hash-based dictionary to identify transactions having:
- The same account ID.
- The same transaction amount.
- The same merchant.
- Posting times within 60 seconds.

### Task 4: Stack and Queue
Implemented custom data structures and built-in equivalents.

- Queue: Models the manual-review backlog using FIFO.
- Stack: Models reversing the most recent adjustment using LIFO.

### Task 5: Divide and Conquer
Implemented divide-and-conquer to find the minimum and maximum transaction amounts.

Compared the results with a brute-force scan.

## Conclusion
The project demonstrates how searching, sorting and data structures can support efficient banking transaction reviews, duplicate detection and transaction analysis.