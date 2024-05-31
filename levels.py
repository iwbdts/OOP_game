from gameobjects import PlayerPlane, EnemyPlane, Asteroid
from gamemanager import GameState


def level1():
    game = GameState()
    player = PlayerPlane(30,30, "player_plane1.txt")
    game.add_object(player)

    enemy_planes = [(50, 100), (60, 120)]
    for x, y in enemy_planes:
        game.add_object(EnemyPlane(x, y, "enemy_plane1.txt"))

    # asteroids = [(90, 140)]
    # for x, y in asteroids:
    #     game.add_object(Asteroid(x, y, "asteroid1.txt"))

    return game, player
