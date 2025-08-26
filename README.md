# 🃏 Python Blackjack Game

This project is a simple terminal-based simulation of the classic Blackjack game, built with Python.
Both the player and the computer are dealt random cards, scores are calculated, and whoever gets closest to 21 without going over wins. Perfect for beginners looking to learn Python in a fun way!

## 🎮 Features

    Random card distribution for player and computer

    Dynamic Ace (11) adjustment to 1 if score exceeds 21

    Option for the player to draw or pass

    Computer draws cards until reaching a score of 17 or more

    Game outcome: win, lose, or draw

    ASCII art intro screen via the shape module

# 📦 File Structure

  blackjack/
  
│

├── blackjack.py       # Main game file

└── shape.py           # ASCII art module



# 📋 Game Rules

    Each player starts with 2 cards.

    Cards range from 2–10, with face cards (J, Q, K) worth 10, and Ace worth 11 or 1.

    The player can choose to draw more cards.

    The computer draws until its score reaches at least 17.

    If a player exceeds 21, they lose.

    The highest score under or equal to 21 wins.

## Installation

Make sure Python is installed on your system. Then, open your terminal and run:

```bash
git clone https://github.com/Siddikaslan/Calculator.git
cd BlackJack
python main.py
```
