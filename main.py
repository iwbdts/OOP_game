import random
from camera import Camera
from pynput import keyboard

if __name__ == "__main__":
    arrows = [keyboard.Key.up, keyboard.Key.down, keyboard.Key.left, keyboard.Key.right]
    camera = Camera(600, 800)

    print("START")
