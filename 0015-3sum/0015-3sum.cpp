class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        
        for(int i = 0; i < nums.size(); i++) {
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            
            int l = i + 1;
            int r = nums.size()-1;
            
            while (l < r) {
                int three_sum = nums[i] + nums[l] + nums[r];
                
                if (three_sum > 0) {
                    r -= 1;
                }
                else if (three_sum < 0) {
                    l += 1;
                }
                else {
                    res.push_back({nums[i], nums[l], nums[r]});
                    l += 1;
                    while (nums[l] == nums[l-1] and l < r) {
                        l += 1;
                    }
                }
            }
        }
        return res;
    }
};