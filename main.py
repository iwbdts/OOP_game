import random
from camera import Camera
from spritemanager import SpriteManager
from levels import level1
from pynput import keyboard



if __name__ == "__main__":
    arrows = [keyboard.Key.up, keyboard.Key.down, keyboard.Key.left, keyboard.Key.right]
    game, player = level1()
    camera = Camera(game, 800, 600)
    camera.display_view()