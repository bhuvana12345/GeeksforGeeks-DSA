# Value equal to index value

**Difficulty:** Basic
**Problem Link:** [View on GeeksforGeeks](https://www.geeksforgeeks.org/problems/value-equal-to-index-value1330/1?page=1&category=Arrays&difficulty=Basic&sortBy=submissions)
**Date Solved:** 2026-04-14
**Language:** cpp

## Tags
`Flipkart`, `Amazon`, `FactSet`, `Hike`, `Arrays`, `Searching`, `Data Structures`, `Algorithms`, `Flipkart Interview Set 3`, `Find A Fixed Point In A Given Array`

## Problem Statement

Given an array arr[]. Your task is to find the elements whose value is equal to that of its index value ( Consider 1-based indexing ).
Note: There can be more than one element in the array which have the same value as its index. You need to include every such element's index. Follows 1-based indexing of the array.
Examples:
Input: arr[] = [15, 2, 45, 4 , 7]
Output: [2, 4]
Explanation: Here, arr[2] = 2 exists here and arr[4] = 4 exists here.
Input: arr[] = [1]
Output: [1]
Explanation: Here arr[1] = 1 exists.
Constraints:1 ≤ arr.size ≤ 1051 ≤ arr[i] ≤ 106

## Solution

```cpp
class Solution:
    def valueEqualToIndex(self, arr):
        result = []
        for i in range(len(arr)):
            if arr[i] == i + 1:      # i+1 converts 0-based index to 1-based
                result.append(i + 1) # append the 1-based index
        return result
```

---
*Synced automatically by GFGHub Chrome Extension*