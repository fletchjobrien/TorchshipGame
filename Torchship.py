import random

###############CLASSES##################

#tile- terrain, occupant
class Tile:
 def __init__(self, terrain, occupant):
  self.terrain = terrain
  self.occupant = occupant

#ship- health, speed, damage, range
class Ship:
 def __init__(self, type):
  #ship types for determining stats
  good_types = ["Scout", "Destroyer", "Cruiser"]
  evil_types = ["Wasp", "Sparrow", "Eagle"]

  #random gen names for ships
  good_names = ["Virginia", "Washington", "Venus", "Alexandria", "Rome", "California", "Valleyforge"]
  evil_names = ["Wolf", "Mantis", "Roach", "Fly", "Beetle", "Vulture", "Wombat", "Devil", "Monster"]

  #ship builder- don't like above. why repeat information inside every ship
  self.type = type
  if type in good_types:
   self.name = random.choice(good_names)
  else:
   self.name = random.choice(evil_names)
  self.hp = 12
  self.speed = 6
  self.damage = 4
  self.range = 6
  self.has_moved = 0
  self.has_attacked = 0


##################VARIABLES##################

map_size = 12
fleet_size = 2

selected_ship = Ship("Scout")
ship_coord = [0,0]
ship_index = (ship_coord[1]*map_size)+ship_coord[0]

selected_tile = Tile("none","none")
tile_coord = [0,0]
tile_index = (tile_coord[1]*map_size)+tile_coord[0]

##################FUNCTIONS##################

#sets indexes to what they would be in the array
def set_indices():
 global ship_index
 global tile_index
 ship_index = (ship_coord[1]*map_size)+ship_coord[0]
 tile_index = (tile_coord[1]*map_size)+tile_coord[0]

def gen_planets(tile_map):
 count = map_size/2
 while count > 0:
  for i in range(map_size*map_size):
   if i%map_size < map_size/2 and random.random() < 0.1 and count > 0:
    tile_map[i].terrain = "planet"
    count = count - 1
 print(f"Placed {map_size/2} planets.")

def gen_good_ships(count):
 ships = []
 for i in range(count):
  rand = random.random()
  if rand < 0.6:
   ships.append(Ship("Scout"))
  elif 0.6 <= rand < 0.9:
   ships.append(Ship("Destroyer"))
  else:
   ships.append(Ship("Cruiser"))
 print(f"Generated {count} good ships.")
 return ships

def gen_evil_ships(count):
 ships = []
 for i in range(count):
  rand = random.random()
  if rand < 0.6:
   ships.append(Ship("Wasp"))
  elif 0.6 <= rand < 0.9:
   ships.append(Ship("Sparrow"))
  else:
   ships.append(Ship("Eagle"))
 print(f"Generated {count} bad ships.")
 return ships

#function- generate map. make array of tiles of size*size. spawn friendly planets on the left, friendly ships on the left
#spawn enemy ships on the right
def gen_map(ships):
 #generate tile
 tile_map = []
 for i in range(map_size*map_size):
  tile_map.append(Tile("none","none"))
 print(f"Generated {map_size*map_size} tiles.")
 #generate planets
 gen_planets(tile_map)

 #generate player ships
 for ship in ships:
  print_map(tile_map)
  x, y = map(int, input("Place ship " + ship.name + " of type " + ship.type + " (X Y): ").split())
  if tile_map[(map_size*y)+x].occupant == "none" and x%map_size < map_size/2:
   tile_map[(map_size*y)+x].occupant = ship
   print(f"Placed ship at {x} {y}.")

 #generate enemy ships
 evil_ships = gen_evil_ships(fleet_size)
 for ship in evil_ships:
  print_map(tile_map)
  x, y = map(int, input("Place ship " + ship.name + " of type " + ship.type + " (X Y): ").split())
  if tile_map[(map_size*y)+x].occupant == "none" and x%map_size >= map_size/2:
   tile_map[(map_size*y)+x].occupant = ship
   print(f"Placed ship at {x} {y}.")
 return tile_map

#function select ship
def select_ship(tile_map):
 global selected_ship
 global ship_coord
 x, y = map(int, input("Select ship (X Y): ").split())
 if tile_map[(y*map_size)+x].occupant != "none":
  selected_ship = tile_map[(y*map_size)+x].occupant
  ship_coord = [x, y]
  set_indices()
  print(f"Selected ship {selected_ship.name} at {x} {y}.")

#function select tile
def select_tile(tile_map):
 global selected_tile
 global tile_coord
 x, y = map(int, input("Select tile (X Y): ").split())
 selected_tile = tile_map[(y*map_size)+x]
 tile_coord = [x, y]
 set_indices()
 print(f"Selected tile at {x} {y}.")

#function move ship
def move_ship(tile_map):
 global selected_ship
 global ship_coord
 tile_map[(tile_coord[1]*map_size)+tile_coord[0]].occupant = selected_ship
 print(f"Moved ship to {tile_coord[0]} {tile_coord[1]}.")
 tile_map[(ship_coord[1]*map_size)+ship_coord[0]].occupant = "none"
 print(f"Moving ship from {ship_coord[0]} {ship_coord[1]}.")
 ship_coord[0] = tile_coord[0]
 ship_coord[1] = tile_coord[1]
 selected_ship.has_moved = 1
 set_indices()

#function attack ship or planet
def attack_ship(tile_map):
 global selected_ship
 tile_map[(tile_coord[1]*map_size)+tile_coord[0]].occupant.hp -= selected_ship.damage
 selected_ship.has_attacked = 1
 print(f"Attacking {tile_map[(tile_coord[1]*map_size)+tile_coord[0]].occupant.name} for {selected_ship.damage}.")

def print_map(tile_map):
 row = ""
 for i in tile_map:
  if i.occupant != "none":
   row += " S "
  elif i.terrain == "planet":
   row += " P "
  else:
   row += " E "

  if len(row) >= map_size*3:
   print(row)
   row = ""

##################GAME LOOP##################

#game loop- while game is not over
good_fleet = gen_good_ships(fleet_size)
game_map = gen_map(good_fleet)
game_over = 0
turn = 0
while game_over == 0:
 while turn == 0:
  #player can select a ship
  print_map(game_map)
  select_ship(game_map)
  #player can move each ship one time
  select_tile(game_map)
  move_ship(game_map)
  #player can attack with each ship once
  print_map(game_map)
  select_tile(game_map)
  attack_ship(game_map)
  #player can hit end turn
  if input("Type e to end turn? ") == "e":
   turn = 1

  #enemy
  while turn == 1:
   #enemy moves their ships each once toward player planets/ships
   print_map(game_map)
   select_ship(game_map)
   select_tile(game_map)
   move_ship(game_map)
   #enemy attacks once with each ship a nearby player planet/ship
   print_map(game_map)
   select_tile(game_map)
   attack_ship(game_map)
   if input("Type e to end turn? ") == "e":
    turn = 0

  #spawn new enemies
  #reset all hasmoved/hasattacked to 0
  #game ends when all enemy ships or player ships/planets are dead
