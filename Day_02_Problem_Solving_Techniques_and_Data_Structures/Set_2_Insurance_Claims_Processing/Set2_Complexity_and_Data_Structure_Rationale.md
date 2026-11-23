# Set 2 – Complexity and Data Structure Rationale

| Task | Algorithm / Data Structure | Time Complexity | Reason |
|---|---|---|---|
| Claim ID operations | Binary Search Tree | Average O(log n), worst O(n) | Supports insertion, searching and traversal |
| Duplicate detection | Hash Map | Average O(n), worst O(n²) | Identifies duplicate claims using normalized keys |
| Collision handling | Hashing | Average O(1), worst O(n) | Handles multiple keys sharing a bucket |
| Shortest approval path | BFS | O(V + E) | Finds shortest path in an unweighted graph |
| Cycle detection | DFS | O(V + E) | Detects cycles in a directed graph |
| Longest consecutive run | Linear Scan | O(n) | Tracks consecutive values above the threshold |
| Merge regional lists | Two Pointers | O(n + m) | Merges two sorted lists in one pass |

## Algorithm Decisions

- **BST:** Stores claim IDs and supports searching and traversal.
- **Hash Map:** Identifies duplicate claims using normalized keys.
- **BFS:** Finds the shortest path between approval stages.
- **DFS:** Detects loops in the approval graph.
- **Linear Scan:** Finds the longest consecutive sequence above the threshold.
- **Two Pointers:** Merges sorted regional lists efficiently.

## Notes

- BST performance depends on tree height.
- Hashing has average constant-time lookup, but collisions can increase lookup time.
- Graph traversal takes O(V + E), where V is vertices and E is edges.
- Merging two sorted lists takes O(n + m) time.
