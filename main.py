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

    while True:
        if "s" in PRESSED_KEYS and PRESSED_KEYS["s"]:
            game.game_started = True

        if "r" in PRESSED_KEYS and PRESSED_KEYS["r"]:
            game, player = level1()
            camera = Camera(game)

        if "q" in PRESSED_KEYS and PRESSED_KEYS["q"]:
            break
        camera.display_view()
        time.sleep(0.1)

    listener_thread.join()
