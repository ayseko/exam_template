class Item:
    """Representerar saker man kan plocka upp."""

    def __init__(self, name, value=20, symbol="?", item_type="fruit"):
        self.name = name
        self.value = value
        self.symbol = symbol
        self.item_type = item_type

    def __str__(self):
        return self.symbol


pickups = [
    Item("carrot"),
    Item("apple"),
    Item("strawberry"),
    Item("cherry"),
    Item("watermelon"),
    Item("radish"),
    Item("cucumber"),
    Item("meatball"),
    Item("spade", value=0, symbol="S", item_type="tool"),
    Item("key", value=0, symbol="K", item_type="key"),
    Item("chest", value=0, symbol="C", item_type="chest")
]


def randomize(grid):
    for item in pickups:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen
