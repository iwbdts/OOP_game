import random


class GameObject:
    def __init__(self, x, y, sprite):
        self.pos_x = x
        self.pos_y = y
        self.height = len(sprite)
        self.width = len(sprite[0])
        self.sprite = sprite


class DestroyableObject(GameObject):
    def __init__(self, hp, x, y, sprite):
        GameObject.__init__(self,x, y, sprite)
        self.hp = hp

    def destroy_self(self):
        pass

    def receive_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.destroy_self()


class Asteroid(DestroyableObject):
    def __init__(self, x, y, sprite):
        DestroyableObject.__init__(self,5, x, y, sprite)


class Weapon():
    def __init__(self, x, y, damage, coff, visible):
        self.damage = damage
        self.shot_cooloff = coff
        self.x_pos = x
        self.y_pos = y
        self.visible = visible

    def shoot_weapon(self):
        if self.shot_cooloff <= 0:
            bullet = Bullet(self.x_pos, self.y_pos, self.damage)


class InitWeapon(Weapon):
    def __init__(self, x, y, visible):
        Weapon.__init__(self, x, y, 1, 3, visible)


class FasterWeapon(Weapon):
    def __init__(self, x, y, visible):
        Weapon.__init__(self, x, y, 1, 2, visible)


class StrongerWeapon(Weapon):
    def __init__(self, x, y, visible):
        Weapon.__init__(self, x, y, 2, 4, visible)


class Bullet(DestroyableObject):
    def __init__(self, x, y, sprite, damage):
        DestroyableObject.__init__(self,5, x, y, sprite)
        self.damage = damage

    def on_collision(self, game_obj):
        game_obj.receive_damage(self.damage)


class Plane(DestroyableObject):
    def __init__(self, hp, x, y, sprite):
        DestroyableObject.__init__(self, hp, x, y, sprite)
        self.weapon = InitWeapon(x, y, False)

    def shoot(self):
        pass


class PlayerPlane(Plane):
    def __init__(self, x, y, sprite):
        Plane.__init__(self, 20, x, y, sprite)

    # def update_x_pos(self):



class EnemyPlane(Plane):
    def __init__(self, x, y, sprite):
        Plane.__init__(self, random.randint(5, 15), x, y, sprite)
