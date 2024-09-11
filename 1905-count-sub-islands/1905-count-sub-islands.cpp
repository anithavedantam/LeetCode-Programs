class Solution {
private:
    bool dfs(int r, int c, vector<vector<bool>>& visited, 
            vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
        int rows = grid1.size();
        int cols = grid1[0].size();
        
        if (r < 0 || r == rows || c < 0 || c == cols ||
            grid2[r][c] == 0 || visited[r][c]) {
            return true;
        }
        
        bool res = true;
        
        if (!grid1[r][c]) {
            res = false;
        }
        
        visited[r][c] = true;
        res = dfs(r+1, c, visited, grid1, grid2) && res;
        res = dfs(r-1, c, visited, grid1, grid2) && res;
        res = dfs(r, c+1, visited, grid1, grid2) && res;
        res = dfs(r, c-1, visited, grid1, grid2) && res;
        
        return res;
    }
public:
    int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
        int rows = grid1.size();
        int cols = grid1[0].size();
        int count = 0;
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));
        
        for (int r = 0; r < rows; r++){
            for (int c = 0; c < cols; c++) {
                if (grid2[r][c] && !visited[r][c] &&
                    dfs(r, c, visited, grid1, grid2)) {
                    count += 1;
                }
            }
        }
        return count;
    }
};