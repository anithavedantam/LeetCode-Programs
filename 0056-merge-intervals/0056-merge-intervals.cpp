class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, 
                                                    const vector<int>& b) {
            return a[0] < b[0];
        });
        
        vector<vector<int>> output;
        output.push_back(intervals[0]);
        
        for (int i = 1; i < intervals.size(); i++) {
            int last_end = output.back()[1];
            int start = intervals[i][0];
            int end = intervals[i][1];
            
            if (start <= last_end) {
                output.back()[1] = max(end, last_end);
            } else {
                output.push_back({start, end});
            }
        }
        return output;
    }
};