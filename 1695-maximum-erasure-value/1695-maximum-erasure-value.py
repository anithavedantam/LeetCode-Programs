class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        ans = 0
        curr_sum = 0
        seen = set()
        for num in nums:
            while num in seen:
                curr_sum -= nums[left]
                seen.remove(nums[left])
                left += 1
            seen.add(num)
            curr_sum += num            
            ans = max(ans, curr_sum)
        return ans