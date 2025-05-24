import time
from src.enemy import EnemyAI
from src.map import GameMap
from src.player import Player

game_map = GameMap()
player = Player()
enemies = [EnemyAI([4, 0]), EnemyAI([0, 7])]
bait = None

for turn in range(30):
    print(f"Turn {turn+1}")
    user_input = input("Move (WASD) or place bait (B): ").upper()
    if user_input in ["W", "A", "S", "D"]:
        player.move(user_input, game_map.grid)
    elif user_input == "B":
        bait = player.pos[:]

    for enemy in enemies:
        enemy.update(player, game_map, bait)

    game_map.render(player, enemies, bait)
    time.sleep(0.5)
