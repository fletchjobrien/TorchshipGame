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
  self.weapons = weapons
  self.engine = engine
  self.effect = effect
