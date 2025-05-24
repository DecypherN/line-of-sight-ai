# line-of-sight-ai
2D stealth game simulation using terminal/console display

#  EnemyAI_Game - Terminal Stealth Game

A simple but clever Python-based 2D stealth game, where the player has to survive while being hunted by enemies with patrol patterns, hearing, and line-of-sight vision. All in just a few Python files.

##  How It Works

- You move the player using WASD keys.
- You can drop a "bait" using the `B` key to distract enemies.
- Enemies patrol horizontally, but if they **see** you (no walls blocking line of sight) or **hear** you (within 2-tile radius), they’ll go into alert or chase mode.
- The game renders everything in your terminal.
- Each turn progresses after your input, giving time to strategize.

##  AI Features

- **Patrolling**: Moves back and forth along a set row.
- **Line of Sight**: Can see the player in a straight line (no walls blocking).
- **Hearing**: Can detect player or bait sounds within 2 tiles.
- **Chasing**: Once seen or heard, enemies pursue until they reach the last known position.

##  Files

- `main.py`: Starts the game loop and manages turns.
- `src/enemy.py`: EnemyAI class handling all behavior.
- `src/player.py`: Handles player position and controls.
- `src/map.py`: Sets up the grid and handles printing to terminal.

##  Setup

Requires Python 3. No external libraries needed.

```bash
git clone https://github.com/yourusername/EnemyAI_Game.git
cd EnemyAI_Game
python main.py
