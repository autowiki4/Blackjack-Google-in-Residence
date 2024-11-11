# Blackjack Game Project

This repository contains a Python-based Blackjack game, developed as part of the Google in Residence program. The project simulates a full Blackjack game that allows multiple players to compete against a dealer, with additional features for scorekeeping across multiple rounds.

# Project Overview

**Files**

**blackjack.py**: This file runs the main Blackjack game. It manages user interactions, displays player turns, and determines winners for each round.
**blackjack_helper.py**: A collection of helper functions to support the main game, capturing repeated code and key game functions. This file contains reusable functions for dealing cards, calculating hand totals, and other essential operations.

# Game Features

The game follows the instructions provided in three parts:

**1. Multiplayer Mode**

**Setup:** Prompts the player with "Welcome to Blackjack! How many players?" and collects each player’s name.

**Gameplay:** Each player plays a hand of Blackjack individually against the dealer, with their turn header displayed as "{player_name}'S TURN".

**Dealer Simulation:** After all players complete their turns, the dealer plays. The results are compared individually with each player, displaying either "{player_name} wins!", "{player_name} loses!", or "{player_name} pushes."

**2. Multiple Rounds & Scorekeeping**

**Score Initialization**: Each player starts with a score of 3.

**Score Updates:**

Winning a hand increases a player’s score by 1.

Losing a hand decreases their score by 1.

Pushing keeps the score unchanged.

**Prompt for Next Round:** After each round, players are prompted, "Do you want to play another hand (y/n)?" If "y", scores carry over to the next round; if "n", the game ends.

# Getting Started

To run the game:

Ensure blackjack.py and blackjack_helper.py are in the same directory.

Execute blackjack.py in your Python environment.


Requirements
Python 3.x
Packages: No external packages are required. The game uses Python’s standard libraries.

# Future Improvements

**Possible enhancements include:**

Adding AI opponents with adjustable difficulty.

Integrating advanced scoring metrics or achievements.

Building a graphical user interface for a more interactive experience.
