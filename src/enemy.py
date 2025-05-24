class EnemyAI:
    def __init__(self, start_pos):
        self.pos = start_pos
        self.state = "patrolling"
        self.memory_pos = None
        self.patrol_dir = 1

    def can_hear(self, player_pos, bait, radius=2):
        targets = [player_pos]
        if bait:
            targets.append(bait)
        for target in targets:
            if abs(self.pos[0] - target[0]) + abs(self.pos[1] - target[1]) <= radius:
                return target
        return None

    def can_see(self, player_pos, grid):
        if self.pos[0] == player_pos[0]:
            step = 1 if player_pos[1] > self.pos[1] else -1
            for y in range(self.pos[1] + step, player_pos[1], step):
                if grid[self.pos[0]][y] == "#":
                    return False
            return True
        elif self.pos[1] == player_pos[1]:
            step = 1 if player_pos[0] > self.pos[0] else -1
            for x in range(self.pos[0] + step, player_pos[0], step):
                if grid[x][self.pos[1]] == "#":
                    return False
            return True
        return False

    def move_towards(self, target):
        if self.pos[0] < target[0]:
            self.pos[0] += 1
        elif self.pos[0] > target[0]:
            self.pos[0] -= 1
        elif self.pos[1] < target[1]:
            self.pos[1] += 1
        elif self.pos[1] > target[1]:
            self.pos[1] -= 1

    def patrol(self):
        next_y = self.pos[1] + self.patrol_dir
        if next_y < 0 or next_y >= 8:
            self.patrol_dir *= -1
        self.pos[1] += self.patrol_dir

    def update(self, player, game_map, bait):
        sees = self.can_see(player.pos, game_map.grid)
        heard = self.can_hear(player.pos, bait)

        if sees:
            self.state = "chasing"
            self.memory_pos = player.pos[:]
        elif heard and self.state != "chasing":
            self.state = "alert"
            self.memory_pos = heard[:]
        elif self.state == "alert" and self.pos == self.memory_pos:
            self.state = "patrolling"
            self.memory_pos = None

        if self.state == "patrolling":
            self.patrol()
        elif self.state in ["alert", "chasing"] and self.memory_pos:
            self.move_towards(self.memory_pos)
