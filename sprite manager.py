import os

class SpriteManager():
    def __init__(self):
        self.sprite_files = os.listdir("sprites/")
        self.sprites = {}
        for name in self.sprite_files:
            self.sprites[name] = SpriteManager.load_sprite(name)

    def load_sprite(self,file_name):
        with open("sprites/" + file_name, 'r') as file:
            lines = file.readlines()
        lines = [line.rstrip('\n') for line in lines]
        max_length = max(len(line) for line in lines)
        sprite = [line.ljust(max_length) for line in lines]
        return sprite

    def get(self, name):
        return self.sprites[name]
