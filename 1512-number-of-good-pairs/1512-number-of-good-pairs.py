class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        left = 0
        ans = 0
        while left < len(nums) - 1:
            for right in range(left+1,len(nums)):
                if nums[left] == nums[right]:
                    ans += 1
            left += 1
        return ans
        