from spritemanager import SpriteManager

class Camera:
    def __init__(self, gamestate, height, width):
        self.game_state = gamestate
        self.height = height
        self.width = width
        self.viewport = [[" " for _ in range(width)] for _ in range(height)]
        self.update_view()

    def update_view(self):
        objs = self.game_state.game_objects
        for obj in objs:
            y = obj.pos_y
            x = obj.pos_x
            sprite = SpriteManager().get(obj.sprite)
            if y - len(sprite) < self.height:
                for line in sprite:
                    y -=1
                    for i in range(len(line)):
                        if x + i < self.width:
                            self.viewport[self.height-y][x+i] = line[i]

    def display_view(self):
        for i in range(len(self.viewport)):
            line = self.viewport[i]
            print(i, end="")
            for j in range(len(line)):
                print(line[j], end="")
            print()

# h
# ^
# |
# |
# |---------->
# 0          w