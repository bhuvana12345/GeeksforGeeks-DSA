class Solution:
    def valueEqualToIndex(self, arr):
        result = []
        for i in range(len(arr)):
            if arr[i] == i + 1:      # i+1 converts 0-based index to 1-based
                result.append(i + 1) # append the 1-based index
        return result