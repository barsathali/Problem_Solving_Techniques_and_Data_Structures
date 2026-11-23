# Set 2 – Insurance Claims Processing

## Overview
This project demonstrates tree structures, hashing, graph algorithms, sliding-window techniques, and two-pointer merging for insurance claim processing.

## Tasks Implemented

1. **Binary Search Tree**
   - Inserted claim IDs.
   - Implemented search.
   - Displayed inorder, preorder, and postorder traversals.
   - Demonstrated that inorder traversal produces sorted IDs.

2. **Hashing**
   - Detected duplicate and near-duplicate claims.
   - Normalized policy numbers by ignoring letter case and spaces.
   - Demonstrated hash bucket collisions.

3. **Graph Algorithms**
   - Represented claim approval stages using a directed graph.
   - Used BFS to find the shortest path.
   - Used DFS to detect cycles.

4. **Sliding Window**
   - Identified the longest consecutive run of days with more than 100 claims.

5. **Two Pointers**
   - Merged two sorted regional claim lists without sorting the combined result.

## Files
- `claims.csv` – Sample insurance claims.
- `regional_claims.csv` – Regional claim records.
- `set2_insurance_claims.py` – Main Python implementation.

## Execution
```bash
python3 set2_insurance_claims.py
