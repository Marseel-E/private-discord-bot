__all__ = ('Dungeon', 'Path', 'Wall', 'Door', 'Entity', 'Tile')

from random import randint, choice
from typing import Optional, List
from dataclasses import dataclass
from pprint import pprint
from time import sleep


@dataclass
class Entity:
	icon: str
	type: str

class Player(Entity):
	def __init__(self, _id: int) -> None:
		self.id = _id
		super().__init__(icon="🦊", type="player")


@dataclass
class Tile:
	icon: str
	type: str

class Path(Tile):
	def __init__(self) -> None:
		super().__init__(icon="🟨", type="path")

class Door(Tile):
	def __init__(self, _type: str) -> None:
		self.type = _type
		super().__init__(icon="🚪", type="door")

class Wall(Tile):
	def __init__(self) -> None:
		super().__init__(icon="⬛", type="door")


class Dungeon:
	def __init__(self, player_id: int, rows: int = 10, columns: int = 10) -> None:
		self.player = Player(player_id)

		self.start = (0, 0)
		self.end = (0, 0)

		self.rows = rows
		self.cols = columns

		self.tiles = [[Wall() for i in range(self.cols)] for i in range(self.rows)]

		self.generate_points()
		self.generate_path()


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
				((s_x > 0) and (self.tiles[s_x-1][s_y] == Path())) or
				(self.tiles[s_x][s_y+1] == Path()) or
				((s_x < (self.rows - 1)) and (self.tiles[s_x+1][s_y] == Path()))
			) and (
				((e_x > 0) and (self.tiles[e_x-1][e_y] == Path())) or
				(self.tiles[e_x][e_y-1] == Path()) or
				((e_x < (self.rows - 1)) and (self.tiles[e_x+1][e_y] == Path()))
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

		return ([Wall() for x in range(0, self.rows-1) for y in range(0, self.cols-1) if self.tiles[x][y] == Wall()])


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

		to_disable = randint(1,4)

		empty_tiles = []

		# UP
		if (not to_disable == 1) and (x > 0) and (self.tiles[x-1][y] == Wall()):
			empty_tiles.append((x-1, y))
		# RIGHT
		if (not to_disable == 2) and (y < (self.cols - 1)) and (self.tiles[x][y+1] == Wall()):
			empty_tiles.append((x, y+1))
		# DOWN
		if (not to_disable == 3) and (x < (self.rows - 1)) and (self.tiles[x+1][y] == Wall()):
			empty_tiles.append((x+1, y))
		# LEFT
		if (not to_disable == 4) and (y > 0) and (self.tiles[x][y-1] == Wall()):
			empty_tiles.append((x, y-1))

		return empty_tiles


	def generate_points(self) -> None:
		"""Generates the start and end points"""

		x, y = randint(0, self.rows-1), 0
		self.start = (x, y)
		self.tiles[x][y] = Door("start")

		x, y = randint(0, self.rows-1), self.cols-1
		self.end = (x, y)
		self.tiles[x][y] = Door("end")

	def generate_path(self) -> None:
		"""Generates the path between the start and end points"""
		cycle = 0

		while not self.check_connection():
			cycle += 1

			if cycle > 5000:
				exit()

			if not (self.check_walls()):
				break

			for x in range(0, self.rows-1):
				for y in range(0, self.cols-1):
					if self.tiles[x][y] == Wall():
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

					self.tiles[x][y] = Path() # choice([Path(), Wall()])

		x, y = self.start
		self.tiles[x][y+1] = self.player


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

		return [[self.tiles[row][col].icon for col in range(self.cols)] for row in range(self.rows)]


if __name__ == '__main__':
	game = Dungeon()
	pprint(game.style_map())