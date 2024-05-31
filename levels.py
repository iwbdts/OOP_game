from gameobjects import GameState, PlayerPlane, EnemyPlane


def level1():
    game = GameState()
    player = PlayerPlane()
    game.add_object(player)

    enemy_planes = [(50, 100), (60, 120)]
    for enemy in enemy_planes:
        game.add_object(EnemyPlane(*enemy,"enemy_plane"))

    asteroids = [(90, 140)]
    for asteroid in asteroids:
        game.add_object(asteroid)

    return game, player