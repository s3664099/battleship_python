# Battleship - Python3

This is a game that I developed from one of the text books that I had from university, namely *The Design and 
Analysis Algorithms*. It was a shame that I never got a chance to practice more of those questions, but I'm doing now,
even though I'm still stuck in brute force algorithms (which is why Battleships is one of the games that they
suggested). Anyway, this is the python version of the game (and I do plan on writing a Java and C++ version of it as
well).

## Executing the Game

A *shebang* has been included in the file, but you run it by typing either *python3 battleship.py* or by making
*battleship.py* executable and then typing *./battleship.py*. This has been designed to run on Linux, and I haven't
tested it out on windows (and don't intend to do so, but others are willing to do it if they wish.) To make the file
executable the following command is required:

*chmod +x battleship.py*

## Playing the Game

You start off by selection 0,1, or 2 players. 0 players will have the computer play against itself, one player you play
against the computer, and two players will do the obvious (though it is on a single computer, therefore you will need to
look away when the other player is playing).

The first thing is you set your ships. The ships need to be at least one space apart (for some reason ships can't be
placed on the bottom line). You select whether they are across or down, and then select the co-ordinates. If the ship
can't be placed there, then you are given a list of co-ordinates where the ship can be placed.

Once the ships have been placed, the game begins. You select co-ordinates where you are going to fire, and the opponent
does the same. You cannot shot the same place twice (as is the case with the board game). You are notified of when you
hit a ship, and the ship you hit. If you sink the ship you are notified, and if you are the first to sink all of the
ships then you win.

## Issues
It looks like you can't place a ship on the bottom line (number 9) of the grid.

I had a look at the instructions, and you are supposed to keep on shooting if you hit a ship. This will need to be
added. (Fixed so far)

## Algorithms

There are two algorithms that are of note in the game, which I will outline below. The first is where the computer
places the ships, and the second is where the computer makes the shot.

**Place Ships**

**Select Shot**