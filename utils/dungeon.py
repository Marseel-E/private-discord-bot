__all__ = ('Dungeon', 'Path', 'Wall', 'Door', 'Enemy', 'Entity', 'Tile')

from random import randint, choice, choices
from typing import Optional, List
from dataclasses import dataclass
from pprint import pprint
from time import sleep


@dataclass
class Entity:
	icon: str
	type: str
	hidden: bool

class Player(Entity):
	def __init__(self, _id: int) -> None:
		self.id = _id
		super().__init__(icon="🦊", type="player", hidden=False)

class Enemy(Entity):
	def __init__(self, name: str, icon: str, hidden: bool = False) -> None:
		self.name = name
		self.icon = icon
		self.hidden = hidden
		super().__init__(icon=self.icon, type="enemy", hidden=self.hidden)


@dataclass
class Tile:
	icon: str
	type: str
	hidden: bool

class Path(Tile):
	def __init__(self, hidden: bool = False) -> None:
		self.hidden = hidden
		super().__init__(icon="🟨", type="path", hidden=self.hidden)

class Door(Tile):
	def __init__(self, _type: str, hidden: bool = False) -> None:
		self.type = _type
		self.hidden = hidden
		super().__init__(icon="🚪", type="door", hidden=self.hidden)

class Wall(Tile):
	def __init__(self) -> None:
		super().__init__(icon="⬛", type="door", hidden=False)


class Dungeon:
	def __init__(self, player_id: int, rows: int = 10, columns: int = 10, enemies: List[Enemy] = []) -> None:
		self.player = Player(player_id)
		self.enemies = enemies

		self.start = (0, 0)
		self.end = (0, 0)

		self.rows = rows
		self.cols = columns

		self.tiles = [[Wall() for i in range(self.cols)] for i in range(self.rows)]

		self.generate_points()
		self.generate_path()
		self.generate_enemies()


	def is_path(self, x: int, y: int) -> bool:
		"""Checks if the coordinates corospond to a Path tile

		Parameters:
		-----------
			'x' <int> - The row of the tile.
			'y' <int> - The column of the tile.
		
		Returns:
		--------
			True <bool> - It is a path.
			False <bool> - It is not a path.
		"""
		return (self.tiles[x][y].type == "path")

	def is_wall(self, x: int, y: int) -> bool:
		"""Checks if the coordinates corospond to a Wall tile

		Parameters:
		-----------
			'x' <int> - The row of the tile.
			'y' <int> - The column of the tile.
		
		Returns:
		--------
			True <bool> - It is a wall.
			False <bool> - It is not a wall.
		"""
		return (self.tiles[x][y].type == "wall")

	def is_door(self, x: int, y: int) -> bool:
		"""Checks if the coordinates corospond to a Door tile

		Parameters:
		-----------
			'x' <int> - The row of the tile.
			'y' <int> - The column of the tile.
		
		Returns:
		--------
			True <bool> - It is a door.
			False <bool> - It is not a door.
		"""
		return (self.tiles[x][y].type == "door")

	def is_player(self, x: int, y: int) -> bool:
		"""Checks if the coordinates corospond to a Player

		Parameters:
		-----------
			'x' <int> - The row of the tile.
			'y' <int> - The column of the tile.
		
		Returns:
		--------
			True <bool> - It is a player.
			False <bool> - It is not a player.
		"""
		return (self.tiles[x][y].type == "player")

	def is_enemy(self, x: int, y: int) -> bool:
		"""Checks if the coordinates corospond to an Enemy

		Parameters:
		-----------
			'x' <int> - The row of the tile.
			'y' <int> - The column of the tile.
		
		Returns:
		--------
			True <bool> - It is an enemy.
			False <bool> - It is not an enemy.
		"""

		return (self.tiles[x][y].type == "enemy")


	def check_connection(self) -> bool:
		"""Checks the connection between the start and end points

		Returns:
		-------
			True <bool> - The two points are connected.
			False <bool> - The two points are not connected.
		"""
		
		s_x = self.start[0]
		s_y = self.start[1]

		e_x = self.end[0]
		e_y = self.end[1]
		
		# Start point (UP, RIGHT, DOWN)
		# End point (UP, LEFT, DOWN)

		if (
			(
				((s_x > 0) and (self.is_path(s_x-1, s_y))) or
				(self.is_path(s_x, s_y+1)) or
				((s_x < (self.rows - 1)) and (self.is_path(s_x+1, s_y)))
			) and (
				((e_x > 0) and (self.is_path(e_x-1, e_y))) or
				(self.is_path(e_x, e_y-1)) or
				((e_x < (self.rows - 1)) and (self.is_path(e_x+1, e_y)))
			)
		): return True

		return False

	def check_walls(self) -> bool:
		"""Checks if there are walls tiles still

		Returns:
		--------
			True <bool> - There are wall tiles.
			False <bool> - There aren't wall tiles.
		"""

		return ([Wall() for x in range(0, self.rows-1) for y in range(0, self.cols-1) if self.is_wall(x, y)])

	def check_enemies(self) -> bool:
		"""Checks if there are enemies still

		Returns:
		--------
			True <bool> - There are enemies.
			False <bool> - There aren't enemies.
		"""

		return ([self.tiles[x][y] for x in range(0, self.rows-1) for y in range(0, self.cols-1) if self.is_enemy(x,y)])


	def get_empty_tiles(self, x: int, y: int) -> Optional[List[tuple]]:
		"""Fetches the empty/wall tiles around a point.

		Parameters:
		-----------
			x <int> - The row of the point.
			y <int> - The column of the point.

		Returns:
		--------
			[(x, y), ...] <list> - A list of all the empty points coordinates. (can be empty)
		"""

		to_disable = randint(1,3)

		empty_tiles = []

		# UP
		if (not to_disable == 1) and (x > 0) and (self.is_wall(x-1, y)):
			empty_tiles.append((x-1, y))
		# RIGHT
		if (y < (self.cols - 1)) and (self.is_wall(x, y+1)):
			empty_tiles.append((x, y+1))
		# DOWN
		if (not to_disable == 2) and (x < (self.rows - 1)) and (self.is_wall(x+1, y)):
			empty_tiles.append((x+1, y))
		# LEFT
		if (not to_disable == 3) and (y > 0) and (self.is_wall(x, y-1)):
			empty_tiles.append((x, y-1))

		return empty_tiles


	def generate_points(self) -> None:
		"""Generates the start and end points"""

		x, y = randint(0, self.rows-1), 0
		self.start = (x, y)
		self.tiles[x][y] = Door("start")

		x, y = randint(0, self.rows-1), self.cols-1
		self.end = (x, y)
		self.tiles[x][y] = Door("end", hidden=True)

	def generate_path(self) -> None:
		"""Generates the path between the start and end points"""
		cycle = 0

		while not self.check_connection():
			cycle += 1

			if cycle > 1000:
				self.tiles = [[Wall() for i in range(self.cols)] for i in range(self.rows)]
				self.generate_points()
				self.generate_path()
				self.generate_enemies()

			if not (self.check_walls()):
				break

			for x in range(0, self.rows-1):
				for y in range(0, self.cols-1):
					if self.is_wall(x, y):
						continue

					empty_tiles = self.get_empty_tiles(x, y)

					if not (empty_tiles):
						continue

					x, y = choice(empty_tiles)

					if ((x, y) == self.start) or ((x, y) == self.end):
						continue

					if (
						x not in [i for i in range(self.rows)] or
						y not in [i for i in range(self.cols)]
					): continue

					self.tiles[x][y] = Path()

		x, y = self.start
		self.tiles[x][y+1] = self.player

	def generate_enemies(self) -> None:
		"""Places enemies on the map randomly"""
		skip = True

		for x in range(self.rows):
			if not (self.enemies):
				break

			if (skip):
				skip = False
				continue

			for y in range(self.cols):
				if y >= 3:
					if self.tiles[x][y].type == "path":
						# UP-LEFT, UP, UP-RIGHT, DOWN-LEFT, DOWN, DOWN-RIGHT, LEFT, RIGHT
						if (
							(
								(
									(x > 0) and (y > 0)
								) and (self.is_enemy(x-1, y-1))
							) or
							((x > 0) and (self.is_enemy(x-1, y))) or 
							(
								(
									(x > 0) and (y < (self.cols-1))
								) and (self.is_enemy(x-1, y+1))
							) or
							(
								(
									(x < (self.rows-1)) and (y > 0)
								) and (self.is_enemy(x+1, y-1))
							) or
							((x < (self.rows-1)) and (self.is_enemy(x+1, y))) or 
							(
								(
									(x < (self.rows-1)) and (y < (self.cols-1))
								) and (self.is_enemy(x+1, y+1))
							) or
							((y > 0) and (self.is_enemy(x, y-1))) or 
							((y < (self.cols-1)) and (self.is_enemy(x, y+1)))
						): continue

						enemy = choice(self.enemies)

						self.tiles[x][y] = choice([enemy, Path(hidden=True)])

						if self.is_enemy(x, y):
							self.enemies.remove(enemy)
							skip = True
							break

		if len(self.enemies) > 3:
			self.generate_enemies()


	def style_map(self) -> List[List[str]]:
		"""Makes the map more readable

		Returns:
		--------
			List[List[str]] <list> - A 2D array with strings instead of objects.
		"""

							# new_map = []
							
							# for row in range(self.rows):
							# 	new_row = []

							# 	for col in range(self.cols):
							# 		new_row.append(self.tiles[row][col].icon)

							# 	new_map.append(new_row)

		new_map = self.tiles.copy()
		for x in range(self.rows):
			for y in range(self.cols):
				new_map[x][y] = self.tiles[x][y].icon if not self.tiles[x][y].hidden else Wall().icon

		return new_map


	@classmethod
	def generate_enemies_list(self, amount: int) -> List[Enemy]:
		"""Generates a list of enemies for the given amount

		Parameters:
		-----------
			'amount' <int> - The amount of enemies to generate.

		Returns:
		--------
			List[Enemy] <list> - The list of generates enemies.
		"""
		enemies_list = [
			{"Ghost": '👻'},
			{"Alien": '👽'},
			{"Glitch": '👾'},
			{"Spider": '🕷'},
			{"Fence": '🤺'},
			{"Bat": '🦇'},
			{"Rat": '🐀'},
			{"Snake": '🐍'},
			{"Robot": '🤖'},
			{"Clown": '🤡'}
		]

		return [Enemy(name=name, icon=icon, hidden=True) for enemy in [choice(enemies_list) for i in range(amount)] for name, icon in enemy.items()]


if __name__ == '__main__':
	game = Dungeon(player_id=0, enemies=Dungeon.generate_enemies_list(3))
	pprint(game.style_map())