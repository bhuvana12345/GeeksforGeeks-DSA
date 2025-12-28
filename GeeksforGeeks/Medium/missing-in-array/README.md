# Missing in Array

**Difficulty:** Medium
**Problem Link:** [View on GeeksforGeeks](https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1?page=1&sortBy=submissions)
**Date Solved:** 2025-12-28
**Language:** cpp

## Tags
No tags

---

## Problem Statement

Problem statement not available

---

## Examples

Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: All the numbers from 1 to 5 are present except 4.

Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
Output: 6
Explanation: All the numbers from 1 to 8 are present except 6.

Input: arr[] = [1]
Output: 2
Explanation: Only 1 is present so the missing element is 2.

---

## Solution

```cpp
class Solution:
    def missingNum(self, arr):
        n = len(arr) + 1
        xor_all = 0
        
        for i in range(1, n + 1):
            xor_all ^= i
        
        for num in arr:
            xor_all ^= num
        
        return xor_all
```

---

*Last Updated: 2025-12-28*
*Synced by GFGHub*
