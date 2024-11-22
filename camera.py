import colorama
from spritemanager import SpriteManager

CURSOR_UP = "\033[A"
CLEAR_SCREEN = "\033[2J\033[H"


class Camera:
    def __init__(self, gamestate):
        self.game_over = False
        self.game_state = gamestate
        self.height = gamestate.screen_height
        self.width = gamestate.screen_width
        self.viewport = [[" " for _ in range(self.width)] for _ in range(self.height)]
        self.BACKGROUND_COLOR = colorama.Back.BLUE
        self.game_over_sprite = SpriteManager().get("game_over_text.txt")
        self.start_game_sprite = SpriteManager().get("start_game_text.txt")
        self.game_won_sprite = SpriteManager().get("you_won_text.txt")
        self.start_game_screen = self.load_start_game_screen()
        self.update_view()
        self.game_over_screen = self.load_game_over_screen()
        self.game_won_screen = self.load_game_won_screen()

    def clear(self):
        self.viewport = [[" " for _ in range(self.width)] for _ in range(self.height)]

    def load_game_over_screen(self):
        game_over_screen = [
            [" " for _ in range(self.width)] for _ in range(self.height)
        ]
        sprite_width, sprite_height = len(self.game_over_sprite[0]), len(
            self.game_over_sprite
        )
        i = self.width // 2 - sprite_width // 2
        j = self.height // 2 - sprite_height // 2
        if sprite_width % 2 == 1:
            i -= 1
        if sprite_height % 2 == 1:
            j -= 1
        for k in range(sprite_width):
            for l in range(sprite_height):
                if 0 <= i + k < self.width and 0 <= j + l < self.height:
                    game_over_screen[j + l][i + k] = self.game_over_sprite[l][k]
        return game_over_screen

    def load_start_game_screen(self):
        start_game_screen = [
            [" " for _ in range(self.width)] for _ in range(self.height)
        ]
        sprite_width, sprite_height = len(self.start_game_sprite[0]), len(
            self.start_game_sprite
        )
        i = self.width // 2 - sprite_width // 2
        j = self.height // 2 - sprite_height // 2
        if sprite_width % 2 == 1:
            i -= 1
        if sprite_height % 2 == 1:
            j -= 1
        for k in range(sprite_width):
            for l in range(sprite_height):
                if 0 <= i + k < self.width and 0 <= j + l < self.height:
                    start_game_screen[j + l][i + k] = self.start_game_sprite[l][k]
        return start_game_screen

    def load_game_won_screen(self):
        game_won_screen = [[" " for _ in range(self.width)] for _ in range(self.height)]
        sprite_width, sprite_height = len(self.game_won_sprite[0]), len(
            self.game_won_sprite
        )
        i = self.width // 2 - sprite_width // 2
        j = self.height // 2 - sprite_height // 2
        if sprite_width % 2 == 1:
            i -= 1
        if sprite_height % 2 == 1:
            j -= 1
        for k in range(sprite_width):
            for l in range(sprite_height):
                if 0 <= i + k < self.width and 0 <= j + l < self.height:
                    game_won_screen[j + l][i + k] = self.game_won_sprite[l][k]
        return game_won_screen

    def update_view(self):
        self.clear()

        if not self.game_state.game_started:
            self.viewport = self.start_game_screen

        elif self.game_state.game_over:
            self.viewport = self.game_over_screen

        elif self.game_state.game_won:
            self.viewport = self.game_won_screen

        else:
            self.game_state.update_positions()
            objs = self.game_state.game_objects
            for obj in objs:
                y = obj.pos_y
                x = obj.pos_x
                sprite = obj.sprite

                for line in sprite:
                    y -= 1
                    for i in range(len(line)):
                        if (
                            x + i < self.width
                            and self.height - y >= 1
                            and self.height - y <= 59
                        ):
                            if i == 0:
                                self.viewport[self.height - y - 1][x + i] = " "
                            self.viewport[self.height - y][x + i] = line[i]

    def display_view(self):
        ROW_START = self.BACKGROUND_COLOR
        ROW_END = colorama.Style.RESET_ALL
        self.update_view()
        view = CURSOR_UP * (2 * self.height)
        for line in self.viewport:
            view += "".join(line) + "\n"
        print(ROW_START + view + ROW_END, end="")
