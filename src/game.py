from src import pickups
from src.screen import print_status
from src.state import GameState


def handle_move(state, dx, dy):
    new_x = state.player.pos_x + dx
    new_y = state.player.pos_y + dy

    # KONTROLL: Väggkollision och användning av spade
    if not (0 <= new_x < state.g.width and 0 <= new_y < state.g.height):
        return
    if state.g.get(new_x, new_y) == state.g.wall:
        for item in state.inventory:
            if item.name == "spade":
                state.g.set(new_x, new_y, state.g.empty)
                print("You used a spade and broke the wall!")
                break
        else:
            return

        # MOVE
    state.player.move(dx, dy)
    state.score -= 1

    maybe_item = state.g.get(new_x, new_y)

    if isinstance(maybe_item, pickups.Item):

        if maybe_item.item_type == "tool":
            state.inventory.append(maybe_item)
            state.g.clear(new_x, new_y)
            print(f" You found a {maybe_item.name}!")

        elif maybe_item.item_type == "key":
            state.inventory.append(maybe_item)
            state.g.clear(new_x, new_y)
            print(f" You found a {maybe_item.name}!")

        elif maybe_item.item_type == "chest":
            for item in state.inventory:
                if item.item_type == "key":
                    state.inventory.remove(item)
                    state.score += 100
                    state.g.clear(new_x, new_y)
                    print("Chest opened! +100 points")
                    break
            else:
                print("Chest is locked. You need a key.")

        else:
            state.score += maybe_item.value
            state.inventory.append(maybe_item)
            state.g.clear(new_x, new_y)

    if state.score < 0:
        print("Game Over!")
        exit()


def start(state):
    command = "a"
    # Loopa tills användaren trycker Q eller X.
    while not command.casefold() in ["q", "x"]:
        print_status(state.g, state)

        command = input("Use WASD to move, Q/X to quit. ")
        command = command.casefold()[:1]

        if command == "w":
            handle_move(state, 0, -1)

        elif command == "a":
            handle_move(state, -1, 0)

        elif command == "s":
            handle_move(state, 0, 1)

        elif command == "d":
            handle_move(state, 1, 0)

        elif command == "i":
            print("Inventory:")
            if len(state.inventory) == 0:
                print("Empty")
            else:
                for item in state.inventory:
                    print(f"- {item.name} ({item.value} points)")

    # Hit kommer vi när while-loopen slutar
    print("Thank you for playing!")


# __name__ skapas av Python och sätts till "__main__" om man startar game.py
# direkt. Detta är för att undvika att start-funktionen körs om man importerar
# saker från game.py i en annan fil, till exempel vid testning.
if __name__ == "__main__":
    game_state = GameState()
    start(game_state)
