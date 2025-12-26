# Indexes of Subarray Sum

**Difficulty:** Medium
**Problem Link:** [View on GeeksforGeeks](https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1?page=1&sortBy=submissions)
**Date Solved:** 2025-12-26
**Language:** cpp

## Tags
No tags

---

## Problem Statement

Problem statement not available

---

## Examples

Input: arr[] = [1, 2, 3, 7, 5], target = 12
Output: [2, 4]
Explanation: The sum of elements from 2nd to 4th position is 12.

Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 15
Output: [1, 5]
Explanation: The sum of elements from 1st to 5th position is 15.

Input: arr[] = [5, 3, 4], target = 2
Output: [-1]
Explanation: There is no subarray with sum 2.

---

## Solution

```cpp
class Solution:
    def subarraySum(self, arr, target):
        left = 0
        curr_sum = 0

        for right in range(len(arr)):
            curr_sum += arr[right]

            while curr_sum > target and left <= right:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                # return 1-based indices
                return [left + 1, right + 1]

        return [-1]
```

---

*Last Updated: 2025-12-26*
*Synced by GFGHub*
