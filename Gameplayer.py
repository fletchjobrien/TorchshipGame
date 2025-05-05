# Gameplayer obj
from Gamestate import Gamestate
from Ship import Ship
from Map import Map

class Gameplayer:
 def __init__(self, turnnum, turntype, gamestate):
  self.turnnum = turnnum
  self.turntype= turntype
  self.gamestate = gamestate
  self.playerfleet = []
  self.aifleet = []
  self.gameend = 0
  self.selectedship = Ship("Test","Test",12,12,["Test","Test"],"Test","Test")

  while self.gameend == 0:
   #menu
   if self.turntype == "Menu":
    user_input = input("F - Fleet Editor\nS - Start Game\nE - End Game\nEnter an option: ")
    choice = user_input
    if choice.lower() == "f":
     self.turntype = "Fleet Editor"
    if choice.lower() == "s":
     self.turntype = "Player Turn"
    if choice.lower() == "e":
     self.turntype = "End Game"
   #fleeteditor
   #playerturn
   elif self.turntype == "Player Turn":
    self.gamestate.printMap()
    user_input = input("S - Select Ship\nM - Move\nA - Attack\nE - End Turn\nR - Return to Menu\nEnter an option: ")
    choice = user_input.lower()
    if choice == "s":
     user_input = input("Select Coords of Ship(X Y): ")
     x, y = map(int, user_input.split())
    #move
    if choice == "m":
     user_input = input("Select Coords to Move to(X Y): ")
     x, y = map(int, user_input.split())
    #attack
    if choice == "a":
     for i in range(len(self.selectedship.weapons)):
      print(f"{i} - " + self.selectedship.weapons[i])
     user_input = input("Select Weapon: ")
     choice = user_input.lower()
    if choice == "e":
     self.turntype = "Enemy Turn"
    if choice == "r":
     self.turntype = "Menu"
   #enemyturn
   #gameendscreen
   elif self.turntype == "End Game":
    print("Game over. Goodbye.")
    self.gameend = 1

playerfleet = [Ship("Test","Test",12,12,["Test","Test"],"Test","Test")]
aifleet = [Ship("Test","Test",12,12,["Test","Test"],"Test","Test")]
game = Gameplayer(0, "Menu", Gamestate(Map, playerfleet, aifleet, "TestAI"))

#game.gamestate.printMap()

