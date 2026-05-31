class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        vector = []
        for i in matrix:
            for j in i:
                vector.append(j)
        
        left = 0
        right = len(vector)-1
        while left <= right:
            mid = (left + right) // 2
            if target > vector[mid]:
                left = mid + 1
            elif target < vector[mid]:
                right = mid - 1
            else:
                return True
        return False