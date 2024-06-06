import random
from spritemanager import SpriteManager
PRESSED_KEYS = {}

def on_press(key):
    try:
        PRESSED_KEYS[key.char] = True
    except AttributeError:
        PRESSED_KEYS[key] = True

def on_release(key):
    try:
        PRESSED_KEYS[key.char] = False
    except AttributeError:
        PRESSED_KEYS[key] = False




class GameObject:
    def __init__(self, x, y, sprite):
        self.name = ""
        self.pos_x = x
        self.pos_y = y
        self.sprite = SpriteManager().get(sprite)
        self.height = len(self.sprite)
        self.width = len(self.sprite[0])
        self.movable = True


class DestroyableObject(GameObject):
    def __init__(self, hp, x, y, sprite):
        GameObject.__init__(self, x, y, sprite)
        self.hp = hp
        self.destroyed = False
        self.vanished = False

    def on_collision_with(self, obj):
        if isinstance(obj, DestroyableObject):
            obj.hp, self.hp = obj.hp - self.hp, self.hp - obj.hp
            if obj.hp <= 0:
                obj.hp = 0
                obj.destroy_self()
            if self.hp <= 0:
                self.hp = 0
                self.destroy_self()
            with open("output.txt", "a") as f:
                print("Hp after collision ", self.name, self.hp, obj.name, obj.hp )

    def destroy_self(self):
        self.destroyed = True
        self.sprite = SpriteManager().get("explosion.txt")

    def vanish_self(self):
        self.vanished = True
        self.sprite = ""

    def receive_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.destroy_self()


class ControllableObject:
    def __init__(self, x, y, controls):
        self.pos_x = x
        self.pos_y = y
        self.controls = controls
        self.next_pos_x = x
        self.next_pos_y = y

    def next_move(self):
        if self.controls[2] in PRESSED_KEYS and PRESSED_KEYS[self.controls[2]]:
            self.next_pos_x = self.pos_x - 3
        if self.controls[3] in PRESSED_KEYS and PRESSED_KEYS[self.controls[3]]:
            self.next_pos_x = self.pos_x + 3


class Plane(DestroyableObject):

    def __init__(self, hp, x, y, sprite):
        DestroyableObject.__init__(self, hp, x, y, sprite)
        self.player_down = False

    def shoot(self):
        pass

    def destroy_self(self):
        self.player_down = True
        super().destroy_self( )


class PlayerPlane(Plane, ControllableObject):
    def __init__(self, x, y, sprite, controls = "wsad"):
        Plane.__init__(self, 30, x, y, sprite)
        ControllableObject.__init__(self, x, y, controls)
        self.name = "player_plane"


class EnemyPlane(Plane):
    def __init__(self, x, y, sprite):
        Plane.__init__(self, random.randint(5, 15), x, y, sprite)
        self.name = "enemy_plane"

class Bullet(DestroyableObject):
    def __init__(self, hp, x, y, sprite):
        DestroyableObject.__init__(self, hp, x, y, sprite)
        self.name = "bullet"