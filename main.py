from board import easyboard, fullboard

class Sudoku:
  def __init__(self, boardText=None):
    self.board = []
    if boardText is not None:
      self.parse(boardText)
    else:
      self.parse(".........\n.........\n.........\n.........\n.........\n.........\n.........\n.........\n.........")

  def __repr__(self):
    out_string = ""
    for row in self.board:
      for cell in row:
        if cell is None:
          out_string += "."
        if cell in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
          out_string += str(cell)
      out_string += '\n'
          
    return out_string

  def parse(self, board):
    def process_char(c):
      try:
        if int(c) in {1,2,3,4,5,6,7,8,9}:
          return int(c)
        else:
          return None
      except:
        return None

    board = board.split('\n')

    self.board = []
    for line in board:
      self.board.append(([process_char(c) for c in line]))

  def poss(self, y, x):
    possnums = {1,2,3,4,5,6,7,8,9}
  
    #remove those of the row
    row = set(self.board[y])
    
    #remove the column
    colm = set()
    for d in range(9):
      colm.add(self.board[d][x])
      
    #remove the box
    topleft_row = (y//3)*3
    topleft_colm= (x//3)*3

    row1 = set(self.board[topleft_row][topleft_colm:topleft_colm+3])
    row2 = set(self.board[topleft_row+1][topleft_colm:topleft_colm+3])
    row3 = set(self.board[topleft_row+2][topleft_colm:topleft_colm+3])

    possnums = possnums.difference(row, colm, row1, row2, row3)
    if len(possnums) == 0:
      possnums.add(None)

    return possnums

  def check_solve(self):
    for i in range(9):
      for j in range(9):
        if self.board[i][j] == None:
         return False
    return True

  def solve(self):
#  while not self.check_solve(): #new sentace
    changes = False
    for j in range(9):
      for i in range(9):
        if self.board[j][i] == None:
          a = self.poss(j,i)
          if len(a) == 1:
            self.board[j][i] = a.pop() #check if works
            changes = True
    if not changes:
      return self.board
      

def main():
  board = Sudoku(fullboard)
  board2 = Sudoku(easyboard)
  board2.solve()
  board.solve()
  print(board2)


main()