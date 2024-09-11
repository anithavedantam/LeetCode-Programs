#include <algorithm> // For std::min

class Solution {
private:
    int dfs(int r, int c, vector<vector<bool>>& visited, vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        
        if (r < 0 || r == rows || c < 0 || c == cols) {
            return 0;
        }
        
        if (grid[r][c] == 1 || visited[r][c]) {
            return 1;
        }
        visited[r][c] = true;
        
        return min(min(dfs(r+1, c, visited, grid),
                   dfs(r-1, c, visited, grid)),
                   min(dfs(r, c+1, visited, grid),
                   dfs(r, c-1, visited, grid)));
    }

public:
    int closedIsland(vector<vector<int>>& grid) {
        int res = 0;
        int rows = grid.size();
        int cols = grid[0].size();
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));
        
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (!grid[r][c] && !visited[r][c]) {
                    res += dfs(r, c, visited, grid);
                }
            }
        }
        return res;
        
    }
};