class GameMap:
    def __init__(self):
        self.grid = [
            list("........"),
            list("..#....."),
            list("..#..P.."),
            list("..#....."),
            list("........"),
        ]

    def render(self, player, enemies, bait):
        display = [row[:] for row in self.grid]
        x, y = player.pos
        display[x][y] = "P"
        if bait:
            display[bait[0]][bait[1]] = "B"
        for e in enemies:
            ex, ey = e.pos
            display[ex][ey] = "E"
        for row in display:
            print("".join(row))
        for i, e in enumerate(enemies):
            print(f"Enemy {i+1} State: {e.state}")
        print("-" * 20)
