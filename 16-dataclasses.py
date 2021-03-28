#https://realpython.com/python-data-classes/

from dataclasses import dataclass

@dataclass
class Card:
  rank: str
  suit: str

print(Card("Ace", "spades"))