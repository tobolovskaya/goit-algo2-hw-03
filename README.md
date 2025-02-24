# Task_1 - Maximum Flow in Logistics Network

## Overview
This project focuses on optimizing the logistics network using the **Edmonds-Karp algorithm** to determine the **maximum flow** of goods from terminals to stores through warehouses. The goal is to model and analyze the network's efficiency, identify bottlenecks, and propose optimizations.

## Problem Statement
The logistics network consists of:
- **2 terminals** that distribute goods.
- **4 warehouses** that manage supply distribution.
- **14 stores** that receive goods.
- **Directed connections with defined capacities** between these entities.

The objective is to compute the **maximum flow** in this network and analyze the results to identify the most and least efficient routes.

## Implementation Details
1. The **graph** is modeled using `networkx.DiGraph()` with **nodes representing terminals, warehouses, and stores**, and **edges representing transport routes with specific capacities**.
2. The **Edmonds-Karp algorithm** is applied to compute the **maximum flow** from the source (virtual supply node) to the sink (final demand node).
3. The computed results are **analyzed** to identify major contributors, low-capacity bottlenecks, and potential optimizations.

## Results Analysis
After processing the network flow, the following conclusions were drawn:

### **1. Which terminals provide the highest flow of goods to stores?**
- **Terminal 2** provided the highest flow of goods overall due to its higher capacity routes leading to **Warehouse 4**, which serves multiple stores.
- **Terminal 1** contributed significantly but had slightly lower overall flow due to limited capacity connections to **Warehouse 3**.

### **2. Which routes have the lowest capacity, and how does this affect the overall flow?**
- The lowest capacity routes are **Warehouse 4 → Store 13 (5 units)** and **Warehouse 4 → Store 14 (10 units)**.
- These low-capacity routes **create bottlenecks**, preventing an even distribution of goods across stores.
- Increasing the capacity of these routes would allow better balance in store deliveries.

### **3. Which stores received the least goods, and can their supply be increased by improving certain route capacities?**
- **Store 13 and Store 14** received the lowest amount of goods due to the restricted capacity of their supply routes.
- Increasing the flow capacity from **Warehouse 4 to these stores** would enhance their supply.

### **4. Are there bottlenecks that can be eliminated to improve the efficiency of the logistics network?**
- The **primary bottleneck** is in **Warehouse 4**, which serves multiple stores but has constrained capacity.
- **Suggested Improvement**: Expanding the capacity from **Terminal 2 to Warehouse 4** and from **Warehouse 4 to its dependent stores** would **enhance overall flow distribution**.

---

## Task_2: OOBTree vs Dict - Range Query Performance Comparison

### Overview
This project compares the efficiency of **OOBTree** (from `BTrees` library) and the standard **Python dict** for executing range queries over a large dataset of products. The goal is to determine which data structure provides better performance for querying product price ranges.

### Problem Statement
- The dataset is loaded from `generated_items_data.csv`, containing **ID, Name, Category, and Price**.
- The same dataset is stored in two data structures:
  1. **OOBTree**, where **ID is the key** and the product details are stored as values.
  2. **Dict**, where **ID is the key**, and the values contain the same product details.
- The performance of range queries (e.g., find all products within a given price range) is tested for both structures.

### Implementation Details
1. **Data Structures Implemented**:
   - `OOBTree`: Uses `BTrees.OOBTree` for efficient range-based lookups.
   - `Dict`: Uses a standard Python dictionary, requiring linear search for range queries.
2. **Functionality Implemented**:
   - `add_item_to_tree()` and `add_item_to_dict()` to add items to both structures.
   - `range_query_tree()` and `range_query_dict()` to execute range queries.
3. **Performance Measurement**:
   - The `timeit` library is used to measure execution time.
   - Each structure is tested with **100 range queries**, and the total execution time is recorded.

### Acceptance Criteria
1. The program correctly executes range queries and returns **accurate results** for both **OOBTree** and **dict**.
2. Data is correctly stored in each structure.
3. `OOBTree` utilizes `items()` for efficient access.
4. `Dict` performs range queries using **linear search**.
5. Execution time for 100 range queries is correctly reported.
6. **Expected Outcome**: `OOBTree` should outperform `dict` due to its sorted data structure.

### Expected Output Format
```
Total range_query time for OOBTree: X.XXXXXX seconds
Total range_query time for Dict: X.XXXXXX seconds
```

