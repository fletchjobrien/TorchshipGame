#map class
import random
from Space import Space
from Ship import Ship

rows, cols = 12, 12

def generateSpace(coords):
 random_float = random.random()
 if (random_float <= 0.1):
  terrain = "Asteroid"
 elif (random_float > 0.1 and random_float <= 0.15):
  terrain = "Planet"
 elif (random_float > 0.15 and random_float <= 0.18):
  terrain = "Black Hole"
 else:
  terrain = "Empty"

 random_float = random.random()
 if (random_float <= 0.05):
  structure = "Starport"
 elif (random_float > 0.05 and random_float <= 0.1):
  structure = "Starbase"
 elif (terrain == "Planet" and random_float > 0.1 and random_float <= 0.6):
  structure = "City"
 else:
  structure = "Empty"

 coordinate = coords

 occupier = "Empty"

 return Space(terrain, structure, coordinate, occupier)

def generateShips(map, playerfleet, aifleet):


class Map:
 #add ship array argument so gameplayer and tell what ships to add
 def __init__(self):
  # create array of spaces
  self.map = []
  for c in range(cols):
   for r in range(rows):
    coords = [c, r]
    self.map.append(generateSpace(coords))
