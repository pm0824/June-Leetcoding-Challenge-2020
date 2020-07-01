'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" 
cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 
Example:
Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
 
Note:
All inputs are consist of lowercase letters a-z.
The values of words are distinct.
Hint #1  
You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
Hint #2  
If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.
'''

#Solution:

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.result = []
        t = {}
        for word in words:
            self.insert(word,t)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.solve(board,t,i,j)
        return self.result
    def solve(self,board,d,i,j,s=""):
        if i<0 or j<0 or i>=len(board) or j>=(len(board[0])):
            return
        l = board[i][j]
        if l in d:
            d = d[l]
            s+=l
            if "#" in d and d['#']:
                self.result.append(s)
                d['#'] = 0
            board[i][j] = '*'
            if i+1<len(board) and board[i+1][j] in d :
                self.solve(board,d,i+1,j,s)
            if j+1 < len(board[0]) and board[i][j+1] in d:
                self.solve(board,d,i,j+1,s)
            if i-1>=0 and board[i-1][j] in d :
                self.solve(board,d,i-1,j,s)
            if j-1>=0 and board[i][j-1] in d :
                self.solve(board,d,i,j-1,s)
            board[i][j] = l
    def insert(self, word,t):
        current = t
        for i in word:
            if i not in current:
                current[i] = {}
            current =current[i]
        current['#']=1





