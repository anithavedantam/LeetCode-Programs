class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<char> rows[9];
        unordered_set<char> cols[9];
        unordered_set<char> squares[9];
        
        for(int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    continue;
                }
                
                if (rows[r].find(board[r][c]) != rows[r].end()) {
                    return false;
                }
                rows[r].insert(board[r][c]);
                
                if (cols[c].find(board[r][c]) != cols[c].end()) {
                    return false;
                }
                cols[c].insert(board[r][c]);
                
                if (squares[(r/3)*3 + c/3].find(board[r][c]) != squares[(r/3)*3 + c/3].end()) {
                    return false;
                }
                squares[(r/3)*3 + c/3].insert(board[r][c]);
                }
            }
        return true;
    }
};