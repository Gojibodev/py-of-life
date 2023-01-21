
# Game of Life

The Game of Life is a cellular automaton invented by mathematician John Horton Conway in 1970. It simulates the evolution of a population of cells on a two-dimensional grid, according to a set of simple rules.

![screenshot_01](/src/screenshot_1.png)
## Rules
The basic rules of the Game of Life are as follows:

-   Each cell in the grid can be in one of two states: alive or dead.
-   The state of a cell in the next generation is determined by the number of live neighbors it has in the current generation.
-   If a live cell has fewer than two live neighbors, it dies of underpopulation.
-   If a live cell has two or three live neighbors, it lives on to the next generation.
-   If a live cell has more than three live neighbors, it dies of overpopulation.
-   If a dead cell has exactly three live neighbors, it becomes alive through reproduction.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need to have python 3 installed on your machine in order to run this project.

### Installing

Clone the repository to your local machine:

Copy code

`git clone https://github.com/Gojimandev/py-of-life.git` 

Navigate to the project directory:

Copy code

`cd game-of-life` 

### Running

To run the project, simply execute the main script:

Copy code

`python gameoflife.py` 

This will generate a random board and run the simulation.

## Built With

-   [Python](https://www.python.org/) - The programming language used

## Author

-   **Gojibo** - [Gojimandev](https://github.com/Gojimandev)

## Acknowledgments
- [Nico](https://github.com/NicoLeiner "https://github.com/NicoLeiner") For pointing out errors in the code

## Notes
This project is a simple implementation of Game of life where it randomly generates a board, applies the rules of the Game of life to each cell of the board and updates them. The board is displayed in the console, with Unicode characters for squares. Please note that this project is built for demonstration purposes and can be further improved and customized as needed.

### Todo:
- A graphical user interface (GUI)
- Different shapes of the grid (e.g. triangular, hexagonal, etc)
