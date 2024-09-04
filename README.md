# Turtle Cross Game

## Short Description

A fun and challenging Turtle Cross game where you guide a turtle across the road while avoiding oncoming cars. Each successful crossing advances the level, increasing the game's difficulty. Inspired by Angela Yu's Udemy course.

## Full Description

The Turtle Cross Game is a Python-based arcade-style game where the player controls a turtle trying to cross a road filled with moving cars. The objective is to safely navigate the turtle from the bottom to the top of the screen without getting hit by a car. As the turtle successfully crosses the road, the game progresses to the next level, making the cars move faster and increasing the difficulty.

**Features:**
- **Player Movement:** The player controls the turtle using the "Up" arrow key to move forward.
- **Car Generation:** Cars are randomly generated on the road, moving horizontally across the screen.
- **Collision Detection:** If the turtle collides with a car, the game ends, and a "Game Over" message is displayed.
- **Level Progression:** Each time the turtle crosses the road successfully, the game advances to the next level, increasing the speed of the cars.
- **Scoreboard:** A scoreboard keeps track of the current level, adding a competitive element to the game.

**Note**: This project was inspired by Angela Yu's course on Udemy.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- The Turtle graphics module (usually included with Python installations).

### How to Play

1. Clone or download the repository to your local machine.
2. Run the script using Python:

   ```bash
   python turtle_cross_game.py
   ```

3. Use the "Up" arrow key to move the turtle forward across the road.
4. Avoid getting hit by the cars as they move across the screen.
5. Reach the top of the screen to advance to the next level, which increases the difficulty.
6. The game ends if the turtle collides with a car, displaying a "Game Over" message.

### Customization

You can customize the game by:
- **Changing Car Speed:** Modify the car speed settings in the `CarManager` class to adjust difficulty.
- **Adding Levels:** Increase the complexity by adding more levels with additional challenges or obstacles.
- **Changing Visuals:** Customize the appearance of the turtle, cars, or background by editing the Turtle shapes and colors.
