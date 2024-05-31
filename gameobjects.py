
class GameObject:
    def __init__(self, x, y, sprite):
        self.pos_x = x
        self.pos_y = y
        self.height = len(sprite)
        self.width = len(sprite[0])
        self.sprite = sprite

class DestroyableObject(GameObject):
    def __init__(self, hp, x, y, sprite):
        super().__init__(x, y, sprite)
        self.hp = hp

    def receive_damage(self, damage):
        self.hp -= damage

    def destroy_self(self):
        if self.hp <= 0:
            pass


class Weapon():
    def __init__(self, x, y, d, coff, visible):
        self.damage = d
        self.shot_cooloff = coff
        self.x_pos = x
        self.y_pos = y
        self.visible = visible

    def shoot_weapon(self):
        if self.shot_cooloff <= 0:
            bullet = Bullet(self.x_pos, self.y_pos, self.damage)


class InitWeapon(Weapon):
    def __init__(self, x, y, visible):
        super().__init__(self, x, y, 1, 3, visible)


class FasterWeapon(Weapon):
    def __init__(self, x, y, visible):
        super().__init__(self, x, y, 1, 2, visible)


class StrongerWeapon(Weapon):
    def __init__(self, x, y, visible):
        super().__init__(self, x, y, 2, 4, visible)


class Bullet(DestroyableObject):
    def __init__(self, x, y, damage):
        self.damage = damage
        super().__init__(5, x, y)

    def on_collision(self, game_obj):
        game_obj.receive_damage(self.damage)


class Plane():
    def __init__(self):
        pass

class PlayerPlane(Plane):
    def __init__(self):
        pass


class EnemyPlane(Plane):
    def __init__(self):
        pass
