import colorama

CURSOR_UP = "\033[A"
CLEAR_SCREEN = "\033[2J\033[H"


class Camera:
    def __init__(self, gamestate):
        self.game_state = gamestate
        self.height = gamestate.screen_height
        self.width = gamestate.screen_width
        self.viewport = [[" " for _ in range(self.width)] for _ in range(self.height)]
        self.update_view()
        self.BACKGROUND_COLOR = colorama.Back.BLUE

    def clear(self):
        self.viewport = [[" " for _ in range(self.width)] for _ in range(self.height)]

    def update_view(self):
        self.clear()
        self.game_state.update_positions()
        objs = self.game_state.game_objects
        for obj in objs:
            y = obj.pos_y
            x = obj.pos_x
            sprite = obj.sprite

            for line in sprite:
                y -= 1
                for i in range(len(line)):
                    if x + i < self.width and self.height - y >= 1 and self.height - y <= 59:
                        if i == 0:
                            self.viewport[self.height - y - 1][x + i] = " "
                        self.viewport[self.height - y][x + i] = line[i]

    def display_view(self):
        ROW_START = self.BACKGROUND_COLOR
        ROW_END = colorama.Style.RESET_ALL
        self.update_view()
        view = CURSOR_UP * (2*self.height)
        for line in self.viewport:
            view += "".join(line) + "\n"
        print(ROW_START + view + ROW_END, end="")
