from gameobjects import ControllableObject, GameObject


class GameState:
    def __init__(self):
        self.game_objects = []
        self.game_started = False
        self.game_finished = False
        self.screen_height = 60
        self.screen_width = 80
        self.time = 0

    def add_object(self, obj):
        self.game_objects.append(obj)

    def update_positions(self):
        self.time += 1
        for obj in self.game_objects:

            if isinstance(obj, ControllableObject) and isinstance(obj, GameObject):
                obj.next_move()
                next_x, next_y = obj.next_pos_x, obj.next_pos_y
                if obj.pos_x != obj.next_pos_x or obj.pos_y != obj.next_pos_y:
                    if next_x >= 0 and next_x + len(obj.sprite[0]) < self.screen_width:
                        obj.pos_x, obj.pos_y = next_x, next_y

            else:
                obj.pos_y -= 1
