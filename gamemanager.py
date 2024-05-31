from gameobjects import PlayerPlane

class GameState:
    def __init__(self):
        self.game_objects = []
        self.game_started = False
        self.game_finished = False
        self.time = 0

    def add_object(self, obj):
        self.game_objects.append(obj)

    def slide_window(self):
        self.time += 1
        for obj in self.game_objects:
            if isinstance(obj, PlayerPlane):
                pass
            else:
                obj.y_pos -= 1

