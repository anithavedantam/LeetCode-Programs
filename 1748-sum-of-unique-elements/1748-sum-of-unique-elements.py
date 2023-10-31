class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        #seen = {}
        #total_sum = 0
        #for num in nums:
        #    if num not in seen:
        #        seen[num] = 1
        #    else:
        #        seen[num] += 1
        #for num in seen:
        #    if seen[num] == 1:
        #        total_sum += num
        #return total_sum
        total_sum = 0
        for num in nums:
            if nums.count(num) == 1:
                total_sum += num
        return total_sum
                
                