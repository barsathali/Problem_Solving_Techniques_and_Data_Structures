# Set 2 – Complexity and Data Structure Rationale

## 1. Searching Algorithms

| Algorithm | Best Case | Average Case | Worst Case |
|---|---|---|---|
| Linear Search | O(1) | O(n) | O(n) |
| Binary Search | O(1) | O(log n) | O(log n) |

Binary Search is suitable for sorted transaction IDs because it repeatedly halves the search range.

## 2. Sorting Algorithms

| Algorithm | Time Complexity | Space Complexity |
|---|---|---|
| Insertion Sort | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n) |

Both algorithms are stable in the implemented versions. Stability preserves the original order of transactions sharing the same timestamp.

## 3. Duplicate Detection

A hash-based dictionary groups transactions by account ID, amount and merchant.

- Average time complexity: O(n + d), where d represents comparisons among matching groups.
- Space complexity: O(n).

The timestamp difference is checked to identify duplicate postings within 60 seconds.

## 4. Stack and Queue

| Data Structure | Principle | Application |
|---|---|---|
| Queue | FIFO | Manual-review backlog |
| Stack | LIFO | Reverse last adjustment |

The custom implementations demonstrate the underlying operations. Built-in equivalents provide convenient implementations.

## 5. Divide and Conquer

The transaction amount list is divided into smaller parts. Each part returns its minimum and maximum, which are combined to obtain the final result.

| Method | Time Complexity | Space Complexity |
|---|---|---|
| Divide and Conquer | O(n) | O(log n) recursion stack |
| Brute-force scan | O(n) | O(1) |

## Conclusion

The selected algorithms and data structures provide suitable solutions for transaction searching, chronological sorting, duplicate detection, review processing and amount analysis.