# Set 3 – Logistics Network and Delivery Windows

## Overview
This project demonstrates Binary Search Trees, Hash Maps, Graph Algorithms, Sliding Window, and Two-Pointer techniques in a logistics network.

## Tasks Implemented

1. **Binary Search Tree**
   - Inserted and searched 10 hub codes.
   - Displayed inorder traversal.
   - Calculated tree height for the CSV insertion order and sorted insertion order.
   - Demonstrated how sorted insertion can create a skewed BST.

2. **Hash Map**
   - Detected parcels scanned more than once at the same hub.
   - Used tracking number and hub code as the duplicate detection key.

3. **Graph Algorithms**
   - Represented 10 hubs and their direct routes using an adjacency list.
   - Used BFS to find the fewest-hop route.
   - Used DFS to list hubs reachable from the central depot.

4. **Sliding Window**
   - Found the four-hour period with the highest average parcel count.

5. **Two Pointers**
   - Checked whether a hub-code sequence is a palindrome.
   - Ignored letter case and separators.

## Files
- `hubs.csv` – Ten logistics hubs.
- `parcels.csv` – Parcel scan records.
- `hourly_parcels.csv` – Hourly parcel counts.
- `set3_logistics_network.py` – Main Python implementation.

## Execution
Run:

```bash
python3 set3_logistics_network.py
eod
