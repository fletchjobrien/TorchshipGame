# Gameplayer obj
from Gamestate import Gamestate
from Ship import Ship
from Map import Map
import random



class Gameplayer:
 def __init__(self, turnnum, turntype, gamestate):
  self.turnnum = turnnum
  self.turntype= turntype
  self.gamestate = gamestate
  self.playerfleet = []
  self.aifleet = []
  self.gameend = 0
  self.selectedship = Ship("Test","Test",12,12,["Test","Test"],"Test","Test")
  self.selectedshipspace = [12,12]

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
     index = (12*y)+x
     selectedspace = gamestate.map.map[(12*y)+x]
     if (selectedspace.occupier == "Empty"):
      print(f"No ship in selected coords {x} {y}")
      print(f"Checking map at index {index}, finding that terrain is " + selectedspace.terrain)
     elif (selectedspace.occupier.team == "Player"):
      print("Ship selected")
      self.selectedshipspace[0] = x
      self.selectedshipspace[1] = y
      self.selectedship = selectedspace.occupier
    #move
    if choice == "m":
     #check if ship has already moved this turn
     if (self.selectedship.hasmoved == 1):
      print("Ship has already moved this turn.")
     else:
      user_input = input("Select Coords to Move to(X Y): ")
      x, y = map(int, user_input.split())
      #check if on the map and in range for ship's engine and chosen space not occupied
      if (x < 12 and x >=0 and y < 12 and y >=0):
       if (abs(x-self.selectedshipspace[0])+abs(y-self.selectedshipspace[1])<=self.selectedship.engine.distance):
        if (gamestate.map.map[(12*y)+x].occupier == "Empty"):
         gamestate.map.map[(12*y)+x].occupier = self.selectedship
         print(f"{12*self.selectedshipspace[1]} plus {self.selectedshipspace[0]}")
         gamestate.map.map[(12*self.selectedshipspace[1])+self.selectedshipspace[0]].occupier = "Empty"
         self.selectedshipspace[0] = x
         self.selectedshipspace[1] = y
         self.selectedship.hasmoved = 1
        else:
         print("Space occupied by another ship.")
       else:
        print("Out of range for ship's engine.")
      else:
       print("Out of bounds for map.")
    #attack
    if choice == "a":
     #check if ship has already attacked this turn
     if (self.selectedship.hasattacked == 1):
      print("Ship has already attacked this turn.")
     else:
      for i in range(len(self.selectedship.weapons)):
       print(f"{i} - " + self.selectedship.weapons[i].name)
      user_input = input("Select Weapon: ")
      choice = int(user_input)
      if choice < len(self.selectedship.weapons):
       user_input = input("Select Coords to Attack(X Y): ")
       x, y = map(int, user_input.split())
       if (abs(x-self.selectedshipspace[0])+abs(y-self.selectedshipspace[1])<=self.selectedship.weapons[choice].range):
        print(f"Space in range of weapon, firing! Chance to hit: {self.selectedship.weapons[choice].accuracy*100}%")
        bonus = 0;
        self.selectedship.hasattacked = 1
        if (abs(x-self.selectedshipspace[0])+abs(y-self.selectedshipspace[1])<=self.selectedship.weapons[choice].range/2):
         bonus = self.selectedship.weapons[choice].accuracy/2;
         print(f"Space is in close range, accuracy bonus! Chance to hit: {self.selectedship.weapons[choice].accuracy+bonus}")
        if (random.random() < self.selectedship.weapons[choice].accuracy + bonus):
         #check if aoe attack
         if (self.selectedship.weapons[choice].aoe > 0):
          aoe = self.selectedship.weapons[choice].aoe
          aoe_squared = aoe*aoe
          for dx in range(-aoe, aoe + 1):
           for dy in range(-aoe, aoe + 1):
            if dx*dx + dy*dy <= aoe_squared:
             nx, ny = x + dx, y + dy
             if 0 <= nx < 12 and 0 <= ny < 12:
              if gamestate.map.map[(12*ny)+nx].occupier != "Empty":
               gamestate.map.map[(12*ny)+nx].occupier.hp -= self.selectedship.weapons[choice].dmg
               print(f"Successful hit! Your ship hp: {self.selectedship.hp} His ship hp: {gamestate.map.map[(12*y)+x].occupier.hp}")
         else:
          gamestate.map.map[(12*y)+x].occupier.hp -= self.selectedship.weapons[choice].dmg
          print(f"Successful hit! Your ship hp: {self.selectedship.hp} His ship hp: {gamestate.map.map[(12*y)+x].occupier.hp}")
        else:
         print("Missed! Damn!")
       else:
        print("Not in range.")
    #enemyturn
    if choice == "e":
     self.turntype = "Enemy Turn"
    if choice == "r":
     self.turntype = "Menu"
   #gameendscreen
   elif self.turntype == "Enemy Turn":
    closestplayership = [100, 100]
    #loop through map and at each ship with team Enemy
    for i in gamestate.map.map:
     if i.occupier != "Empty":
      print("Found space with ship")
      if i.occupier.team == "Enemy":
       print(f"Found enemy ship at {i.coordinate[0]}, {i.coordinate[1]}")
       selectedenemyship = i.occupier
       selectedenemyshipspace = i.coordinate
       # loop through map and find closest player ship
       for z in gamestate.map.map:
        if z.occupier != "Empty" and z.occupier.team == "Player":
         print("Found player ship.")
         print(f"Checking if {abs(z.coordinate[0]-selectedenemyshipspace[0])} < {abs(closestplayership[0]-selectedenemyshipspace[0])}")
         if abs(z.coordinate[0]-selectedenemyshipspace[0]) < abs(closestplayership[0]-selectedenemyshipspace[0]):
          print(f"Checking if {abs(z.coordinate[1]-selectedenemyshipspace[1])} < {abs(closestplayership[1]-selectedenemyshipspace[1])}")
          if abs(z.coordinate[1]-selectedenemyshipspace[1]) < abs(closestplayership[1]-selectedenemyshipspace[1]):
           closestplayership = z.coordinate
           print(f"Closest player ship set to {z.coordinate[0]}, {z.coordinate[1]}")
       # move toward closest player ship
       spacetomove = selectedenemyshipspace.copy()
       print(f"Moving ship at {selectedenemyshipspace[0]}, {selectedenemyshipspace[1]} toward ship at {closestplayership[0]}, {closestplayership[1]}")
       for q in range(selectedenemyship.engine.distance):
        if closestplayership[0] > spacetomove[0]:
         spacetomove[0]+=1
        elif closestplayership[1] > spacetomove[1]:
         spacetomove[1]+=1
        elif closestplayership[0] < spacetomove[0]:
         spacetomove[0]-=1
        elif closestplayership[1] < spacetomove[1]:
         spacetomove[1]-=1
       gamestate.map.map[(12*spacetomove[1])+spacetomove[0]].occupier = selectedenemyship
       gamestate.map.map[(12*selectedenemyshipspace[1])+selectedenemyshipspace[0]].occupier = "Empty"
     # attack closest player ship
     #set to player turn
     self.turntype = "Player Turn"
   elif self.turntype == "End Game":
    print("Game over. Goodbye.")
    self.gameend = 1

playerfleet = [Ship("Test","Player",12,12,["Small Gun","Test"],"Small Jump","Test"), Ship("Test","Player",12,12,["Nuclear Missile","Test"],"Small Line","Test"), Ship("Test","Player",12,12,["Small Gun","Test"],"Small Jump","Test")]
aifleet = [Ship("Simple","Enemy",12,12,["Test","Test"],"Small Jump","Test"), Ship("Simple","Enemy",12,12,["Test","Test"],"Small Jump","Test")]
game = Gameplayer(0, "Menu", Gamestate("Random", playerfleet, aifleet, "TestAI"))

#game.gamestate.printMap()

