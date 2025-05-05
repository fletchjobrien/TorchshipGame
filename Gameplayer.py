# Gameplayer obj
from Gamestate import Gamestate
from Ship import Ship
from Map import Map

class Gameplayer:
 def __init__(self, turnnum, turntype, gamestate):
  self.turnnum = turnnum
  self.turntype= turntype
  self.gamestate = gamestate
  #menu
  #fleeteditor
  #playerturn
  #enemyturn
  #gameendscreen

playerfleet = [Ship("Test","Test",12,12,["Test","Test"],"Test","Test")]
aifleet = [Ship("Test","Test",12,12,["Test","Test"],"Test","Test")]
game = Gameplayer(0, "Main Menu", Gamestate(Map, playerfleet, aifleet, "TestAI"))

game.gamestate.printMap(playerfleet, aifleet)
