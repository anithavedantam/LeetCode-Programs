class Solution {
private:  
    void bfs (int row, int col, vector<vector<char>>& grid, vector<vector<bool>>& visited) {
        
        int num_rows  = grid.size();
        int num_cols = grid[0].size();
        queue<pair<int, int>> q;
        q.push({row, col});
        
        vector<pair<int,int>> directions = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        
        visited[row][col] = true;
        
        while (!q.empty()) {
            int r = q.front().first;
            int c = q.front().second;
            q.pop();
            for(auto dir:directions) {
                int new_r = r + dir.first;
                int new_c = c + dir.second;
                
                if (new_r >=0 && new_r < num_rows && 
                    new_c >= 0 && new_c < num_cols && 
                    grid[new_r][new_c] == '1' && 
                    !visited[new_r][new_c]) {
                    q.push({new_r, new_c});
                    visited[new_r][new_c] = true;
                    
                }
            }
        }
    }
public:
    int numIslands(vector<vector<char>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int islands = 0;
        
        if (rows == 0){
            return 0;
        }
        
                
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));
            
        
        for (int r=0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1' && !visited[r][c]) {
                    islands ++;
                    bfs(r,c, grid, visited);
                    
                }
            }
        }
        return islands;
    }
};