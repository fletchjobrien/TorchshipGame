# Ship object
from Pilot import Pilot
from Engine import Engine
from Weapon import Weapon

class Ship:
 def __init__(self, pilot, team, hp, shield, weapons, engine, effect):
  self.pilot = pilot
  self.team = team
  self.hp = hp
  self.shield = shield
  self.weapons = []
  for wep in weapons:
   if wep == "Test":
    self.weapons.append(Weapon("Test",0,20,20,0,0.9))
  if engine == "Small Jump":
   self.engine = Engine("Small Jump", 3)
  else:
   self.engine = Engine("Small Line", 4)
  self.effect = effect

