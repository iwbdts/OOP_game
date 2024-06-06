import time
import threading
from camera import Camera
from levels import level1
from gameobjects import PRESSED_KEYS, on_press, on_release
from pynput import keyboard

if __name__ == "__main__":
    game, player = level1()
    camera = Camera(game)

    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener_thread = threading.Thread(target=listener.start)
    listener_thread.start()

    while not game.game_finished:
        camera.display_view()
        # print(PRESSED_KEYS)
        time.sleep(0.1)


    listener_thread.join()