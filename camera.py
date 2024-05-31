class Camera:
    def __init__(self, gamestate, height, width):
        self.game_state = gamestate
        self.height = height
        self.width = width
        self.view = [[" " for _ in range(width)] for _ in range(height)]

    def view(self):
        objs = self.game_state.game_objects
        # h
        # ^
        # |
        # |
        # |---------->
        # 0          w
        for obj in objs:
            if obj.y_pos- len(obj.sprite) < self.height:
                pass