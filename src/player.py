class Player:
    def __init__(self):
        self.pos = [2, 5]

    def move(self, direction, grid):
        x, y = self.pos
        if direction == "W" and x > 0 and grid[x-1][y] != "#":
            self.pos[0] -= 1
        elif direction == "S" and x < len(grid)-1 and grid[x+1][y] != "#":
            self.pos[0] += 1
        elif direction == "A" and y > 0 and grid[x][y-1] != "#":
            self.pos[1] -= 1
        elif direction == "D" and y < len(grid[0])-1 and grid[x][y+1] != "#":
            self.pos[1] += 1
