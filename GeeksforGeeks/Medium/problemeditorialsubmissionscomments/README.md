# ProblemEditorialSubmissionsComments

**Difficulty:** Medium
**Problem Link:** [View on GeeksforGeeks](https://www.geeksforgeeks.org/problems/implement-queue-using-array/1?page=1&category=Arrays&difficulty=Basic&sortBy=submissions)
**Date Solved:** 2026-04-11
**Language:** py

## Tags
`Amazon`, `Goldman Sachs`, `Arrays`, `Queue`, `Data Structures`, `Array Implementation Of Queue Simple`

## Problem Statement

Implement a Queue using an Array, where the size of the array, n is given. The Queue must support the following operations:
(i) enqueue(x): Insert an element x at the rear of the queue.(ii) dequeue(): Remove the element from the front of the queue.(iii) getFront(): Return front element if not empty, else -1.(iv) getRear(): Return rear element if not empty, else -1.(v) isEmpty(): Return true if the queue is empty else return false.(vi) isFull(): Return true if the queue is full else return false.
There will be a sequence of queries queries[][]. The queries are represented in numeric form:

1 x : Call enqueue(x)
2: Call dequeue()
3: Call getFront()
4: Call getRear()
5: Call isEmpty()
6: Call isFull()

You just have to implement the functions enqueue, dequeue, getFront, getRear, isEmpty and isFull and the driver code will handle the output.
Examples:
Input: n = 3, q = 7, queries[][] = [[1, 5], [1, 3], [1, 4], [3], [2], [5], [4]]
Output: [5, false, 4]
Explanation: Queries on queue are as follows:enqueue(5): Insert 5 at the rear of the queue.enqueue(3): Insert 3 at the rear of the queue.enqueue(4): Insert 4 at the rear of the queue.getFront(): Return the front element i.e 5.dequeue(): Remove the front element 5 from the queue.isEmpty(): Return false as the queue is not empty.getRear(): Return the rear element i.e 4.
Input: n = 2, q = 4, queries[][] = [[4], [1, 3], [1, 7], [6]]
Output: [-1, true]
Explanation: Queries on queue are as follows:getRear(): As the queue is empty return -1.enqueue(3): Insert 3 at the rear of the queue.enqueue(7): Insert 7 at the rear of the queue.isFull(): Return true as the queue is full i.e containing 2 elements.
Constraints:1 ≤ n ≤ 1031 ≤ number of query ≤ 1030 ≤ x ≤ 105

## Solution

```py
class myQueue:
    def __init__(self, n):
        self.size = n
        self.queue = []
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def isFull(self):
        return len(self.queue) == self.size
    
    def enqueue(self, x):
        if not self.isFull():
            self.queue.append(x)
    
    def dequeue(self):
        if not self.isEmpty():
            self.queue.pop(0)
    
    def getFront(self):
        if self.isEmpty():
            return -1
        return self.queue[0]
    
    def getRear(self):
        if self.isEmpty():
            return -1
        return self.queue[-1]
```

---
*Synced automatically by GFGHub Chrome Extension*