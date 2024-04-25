# XO
 A fun and exciting console based game to make your computer less boring.

 XO is a simple 2 player game of X's and O's using a 3x3 grid. 
 
## How to
 1. Each player takes a turn. 
 2. During each turn, the player marks a point using an X or an O. 
 3. A game is over once all 9 tiles have been marked or a player has won the round.
 4. A round is won when a player marks 3 tiles in any direction linearly;
     i. If a player completes 3 tiles left to right on any row as shown below:
    ```
         1   2   3
       *-----------*
     1 | X | X | X |
       *-----------*
     2 | O |   | O |
       *-----------*
     3 |   | O |   |
       *-----------*
    ```
     ii. If a player completes 3 tiles top to bottom on any column as shown below:
    ```
         1   2   3
       *-----------*
     1 | X | O |   |
       *-----------*
     2 | X | O | O |
       *-----------*
     3 | X |   |   |
       *-----------*
    ```
     iii. If a player completes 3 tiles diagonally as shown below:
    ```
         1   2   3
       *-----------*
     1 | X | O |   |
       *-----------*
     2 | O | X | O |
       *-----------*
     3 |   |   | X |
       *-----------*
    ```