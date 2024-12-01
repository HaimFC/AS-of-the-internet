
# Assignment - Autonomous Systems and Tier Analysis

### General Information
- **Description**: This assignment involves analyzing Autonomous Systems (AS) relationships, identifying Tier 1 AS networks, and categorizing AS into tiers based on their connections and roles.

---

## Task Details

### Questions
1. **Tier 1 Identification**:
   - Identify AS numbers and their associated company names that belong to Tier 1.
2. **Tier 1 Graph Visualization**:
   - Construct a graph showing connections between Tier 1 AS (nodes and edges).
3. **Tier Analysis**:
   - Identify the number of tiers in the network and the number of AS in each tier.

---

## Code Implementation

### Script: `ASofTheInternet.py`
#### Summary of Tasks
1. **Data Parsing**:
   - Parse AS relationships from a file to determine providers, customers, and peers.
2. **Tier 1 Identification**:
   - Identify Tier 1 AS based on connectivity and non-customer status.
   - Filter Tier 1 AS based on a threshold of 150+ customers.
3. **Graph Construction**:
   - Create a graph of Tier 1 AS using NetworkX.
   - Nodes represent AS, and edges represent peer connections.
4. **Graph Visualization**:
   - Draw the graph using Matplotlib with labeled nodes and edges.
5. **Tier Count**:
   - Categorize all AS into tiers based on relationships and count AS in each tier.


---

## Expected Output
1. **Tier 1 AS List**:
   - AS numbers and names of Tier 1 AS.
2. **Graph Visualization**:
   - Graph showing connections among Tier 1 AS.
3. **Tier Analysis**:
   - Number of tiers identified and the number of AS in each tier.

---

## Notes
- Ensure the file `names.txt` is in the same directory as the script to map AS numbers to company names.
- The relationships file (`20210901.as-rel.txt`) should also be included for accurate parsing.
