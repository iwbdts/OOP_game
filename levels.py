from gameobjects import PlayerPlane, EnemyPlane
from gamemanager import GameState
import random


def level1():
    game = GameState()
    player = PlayerPlane(30, 10, "player_plane1.txt")
    game.add_object(player)
    enemy_planes = [
        ([10, 25, 35, 50][random.randint(0, 3)], 50 + 20 * i) for i in range(20)
    ]
    for x, y in enemy_planes:
        game.add_object(EnemyPlane(x, y, "enemy_plane1.txt"))

    return game, player
