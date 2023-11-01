class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        prefix_arr = [0]
        for i in range(0,len(nums)):
            prefix_arr.append(nums[i] + prefix_arr[-1])
        count = collections.Counter()
        for val in prefix_arr:
            ans += count[val]
            count[val + goal] += 1
        return ans