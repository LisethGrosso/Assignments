#######################################################################################
# A5P1. 52. N-Queens II

class Solution13:
    def __init__(self,n = 0, result = 0):
        self.result = result
        self.n = n

    def totalNQueensHelp(self, row: int, queensPositions: dict):
        if self.n == row: 
            self.result = self.result + 1
        else: 
            for col in range(self.n):
                isSafe = True
                queensPositions[row] = {"row": row,"col":col}
                for queen in range(row):
                    if ((queensPositions[queen]["col"] == col) or 
                        (queensPositions[queen]["col"]-queensPositions[queen]["row"]) == (col-row) or
                        (queensPositions[queen]["row"]+queensPositions[queen]["col"]) == (col+row)):
                        isSafe = False
                        break
                if isSafe:
                    self.totalNQueensHelp( row+1, queensPositions)
                queensPositions.popitem()

    def totalNQueens(self, n: int) -> int:
        self.n = n
        self.totalNQueensHelp( 0, {})
        return self.result

#######################################################################################
# A5P2. Robot Cleaner

class Solution14(): 

    def __init__(self, iniAngle:int, position: (int,int), room = list):
        self.iniAngle = iniAngle
        self.iniCoor = position
        self.iniRow = position[0]
        self.iniCol = position[1]
        self.angle = self.iniAngle
        self.row = self.iniRow
        self.col = self.iniCol
        self.coor = position
        self.cellsCleaned = set()
        self.room = room

    def move(self):
        columnsRoom  = len(room[0])
        rowsRoom = len(room)
        if self.angle == 0:
            if self.col + 1 <  columnsRoom and self.room[self.row][self.col + 1] != 0:
                self.col = self.col +1 
                self.coor = (self.row, self.col)
                return True
            else:
                return False
        elif self.angle == 90:
            if self.row - 1 >=  0 and self.room[self.row-1][self.col] != 0:
                self.row = self.row -1 
                self.coor = (self.row, self.col)
                return True
            else:
                return False
        elif self.angle == 180:
            if self.col - 1 >= 0 and self.room[self.row][self.col - 1] != 0:
                self.col = self.col -1 
                self.coor = (self.row, self.col)
                return True
            else:
                return False
        elif self.angle == 270:
            if self.row + 1 <  rowsRoom and self.room[self.row+1][self.col] != 0:
                self.row = self.row +1 
                self.coor = (self.row, self.col)
                return True
            else:
                return False
        
        return False

    def turnLeft(self):
        self.angle = (self.angle+90)%360
        
    def turnRight(self):
        self.angle = 270  if self.angle == 0 else (self.angle-90)%360


    def clean(self):
        self.cellsCleaned.add((self.coor))

    def moveBack(self): 
        self.turnRight()
        self.turnRight()
        self.move()
        self.turnRight()
        self.turnRight()

    def dfs(self):
        if self.coor in self.cellsCleaned: 
            self.moveBack()
            return 
        self.clean()

        if self.move():
            self.dfs()
        self.turnLeft()
        
        if self.move():
            self.dfs()
        self.turnLeft()
        
        if self.move():
            self.dfs()
        self.turnLeft()

        if self.move():
            self.dfs()
        self.turnLeft()

        if (self.angle == self.iniAngle and self.coor == self.iniCoor):
            print(self.cellsCleaned)

        print("Explored all dir: "+ str(self.coor[0])+","+str(self.coor[1]))
        self.moveBack()

        
if __name__ == '__main__':

    print("N-Queens II")
    p13 = Solution13()
    print(p13.totalNQueens(4))
 
    print("Robot Cleaner")
    room = [
            [1,1,1,1,1,0,1,1],
            [1,1,1,1,1,0,1,1],
            [1,0,1,1,1,1,1,1],
            [0,0,0,1,0,0,0,0],
            [1,1,1,1,1,1,1,1]
            ]
    row = 1
    col = 2
    position = (row, col)
    p14 = Solution14(0, position, room)
    p14.dfs()
  