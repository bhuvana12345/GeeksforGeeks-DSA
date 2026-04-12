# Rotate Array by One

**Difficulty:** Basic
**Problem Link:** [View on GeeksforGeeks](https://www.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1?page=1&category=Arrays&difficulty=Basic&sortBy=submissions)
**Date Solved:** 2026-04-12
**Language:** cpp

## Tags
`Arrays`, `implementation`, `C Program Cyclically Rotate Array One`

## Problem Statement

Given an array arr, rotate the array by one position in clockwise direction.
Examples:
Input: arr[] = [1, 2, 3, 4, 5]
Output: [5, 1, 2, 3, 4]Explanation: If we rotate arr by one position in clockwise 5 come to the front and remaining those are shifted to the end.
Input: arr[] = [9, 8, 7, 6, 4, 2, 1, 3]
Output: [3, 9, 8, 7, 6, 4, 2, 1]Explanation: After rotating clock-wise 3 comes in first position.
Constraints:1<=arr.size()<=1050<=arr[i]<=105

## Solution

```cpp
class Solution:
    def rotate(self, arr):
        if not arr:
            return arr
        
        last = arr[-1]
        
        for i in range(len(arr) - 1, 0, -1):
            arr[i] = arr[i - 1]
        
        arr[0] = last
        return arr
```

---
*Synced automatically by GFGHub Chrome Extension*