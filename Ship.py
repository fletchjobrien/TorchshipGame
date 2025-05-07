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
   if wep == "Small Gun":
    self.weapons.append(Weapon("Small Gun",0,20,20,0,0.6))
  if engine == "Small Jump":
   self.engine = Engine("Small Jump", 3)
  else:
   self.engine = Engine("Small Line", 4)
  self.effect = effect

