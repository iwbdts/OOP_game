from gameobjects import PlayerPlane, EnemyPlane
from gamemanager import GameState


def level1():
    game = GameState()
    player = PlayerPlane(30,10, "player_plane1.txt")
    game.add_object(player)

    enemy_planes = [(10, 60), (10, 120), (50, 80)]
    for x, y in enemy_planes:
        game.add_object(EnemyPlane(x, y, "enemy_plane1.txt"))

    # asteroids = [(90, 140)]
    # for x, y in asteroids:
    #     game.add_object(Asteroid(x, y, "asteroid1.txt"))

    return game, player
