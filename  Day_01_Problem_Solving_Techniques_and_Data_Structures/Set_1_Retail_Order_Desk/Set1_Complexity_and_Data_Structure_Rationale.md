# Set 1 – Complexity and Data Structure Rationale

## 1. Searching Algorithms

| Algorithm | Best Case | Average Case | Worst Case |
|---|---|---|---|
| Linear Search | O(1) | O(n) | O(n) |
| Binary Search | O(1) | O(log n) | O(log n) |

Binary Search is more efficient for sorted data because it repeatedly divides the search space into half.

## 2. Sorting Algorithms

| Algorithm | Time Complexity | Space Complexity |
|---|---|---|
| Selection Sort | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n) |
| Python Built-in Sort | O(n log n) average | O(n) |

Merge Sort performed significantly better than Selection Sort for 10,000 records.

## 3. Duplicate Detection

A hash-based structure stores previously encountered order details.

- Average time complexity: O(n)
- Worst-case time complexity: O(n²)
- Space complexity: O(n)

It efficiently identifies duplicate orders using customer ID, amount and transaction minute.

## 4. Stack and Queue

| Data Structure | Principle | Main Operation | Complexity |
|---|---|---|---|
| Stack | LIFO | Push / Pop | O(1) |
| Queue | FIFO | Enqueue / Dequeue | O(1) |

Stack is suitable for undo operations, while Queue is suitable for order dispatch.

## 5. Greedy and Dynamic Programming

Greedy chooses the largest available denomination at each step. It does not always produce the optimal result.

Dynamic Programming evaluates smaller subproblems and finds the minimum number of coins.

For amount 6 with denominations [1, 3, 4]:
- Greedy: 3 coins
- Dynamic Programming: 2 coins

## Conclusion

The tasks demonstrate how selecting appropriate algorithms and data structures improves performance, reduces processing time and produces reliable results in retail order management.