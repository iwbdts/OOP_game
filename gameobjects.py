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

    def destroy_self(self):
        pass

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

    def shoot(self):
        pass


class PlayerPlane(Plane, ControllableObject):
    def __init__(self, x, y, sprite, controls = "wsad"):
        Plane.__init__(self, 20, x, y, sprite)
        ControllableObject.__init__(self, x, y, controls)
        self.name = "player_plane"


class EnemyPlane(Plane):
    def __init__(self, x, y, sprite):
        Plane.__init__(self, random.randint(5, 15), x, y, sprite)
        self.name = "enemy_plane"
