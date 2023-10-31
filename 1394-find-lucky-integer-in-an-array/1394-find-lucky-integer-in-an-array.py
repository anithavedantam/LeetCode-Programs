class Solution:
    def findLucky(self, arr: List[int]) -> int:
        max_num = -1
        for num in arr:
            if arr.count(num) == num:
                max_num = max(num, max_num)
        return max_num
        