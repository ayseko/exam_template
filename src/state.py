from src.grid import Grid
from src.player import Player
from src import pickups


class GameState:
    """Samla spelets variabler i en klass."""
    def __init__(self):
        self.player = Player(Grid.width//2, Grid.height//2)
        self.score = 10
        self.inventory = []

        self.g = Grid()
        self.g.set_player(self.player)
        self.g.make_walls()
        pickups.randomize(self.g)