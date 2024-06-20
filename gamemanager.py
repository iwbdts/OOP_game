from gameobjects import ControllableObject, DestroyableObject, GameObject, PlayerPlane, PlayerBullet, EnemyBullet, \
    EnemyPlane
from spritemanager import SpriteManager


class GameState:
    def __init__(self):
        self.game_objects = []
        self.game_started = False
        self.game_over = False
        self.game_won = False
        self.screen_height = 60
        self.screen_width = 80
        self.time = 0
        self.enemies = 20

    def add_object(self, object):
        self.game_objects.append(object)

    def are_colliding(self, obj1, obj2):
        x1, y1, height1, width1 = obj1.pos_x, obj1.pos_y, obj1.height, obj1.width
        x2, y2, height2, width2 = obj2.pos_x, obj2.pos_y, obj2.height, obj2.width

        if obj1 == obj2:
            return False

        # Calculate the boundaries of both objects
        left1, right1, top1, bottom1 = x1, x1 + width1, y1 - height1, y1
        left2, right2, top2, bottom2 = x2, x2 + width2, y2 - height2, y2

        # Check if the rectangles overlap
        if right1 >= left2 and left1 <= right2 and bottom1 >= top2 and top1 <= bottom2:
            return True

        return False

    def colliding_objects(self, object):
        res = []
        for obj in self.game_objects:
            if self.are_colliding(object, obj):
                res.append(obj)

        return res

    def update_positions(self):
        self.time += 1
        for obj in self.game_objects:
            colliding = []
            if isinstance(obj, PlayerPlane):
                if obj.player_down:
                    self.game_over = True
                if obj.can_shoot():
                    self.add_object(PlayerBullet(obj.pos_x + obj.width // 2 - 2, obj.pos_y + 5))

            if isinstance(obj, EnemyPlane):
                if obj.can_shoot() and obj.pos_x < self.screen_width and obj.pos_y < self.screen_height:
                    self.add_object(EnemyBullet(obj.pos_x + obj.width // 2 -1, obj.pos_y - 7))
                if obj.pos_y < 10:
                    obj.destroy_self()
                    self.enemies -= 1

            if isinstance(obj, DestroyableObject):
                if obj.destroyed and obj.vanished:
                    self.game_objects.remove(obj)
                if obj.destroyed:
                    obj.vanish_self()
                    if isinstance(obj, EnemyPlane):
                        self.enemies -= 1

            if isinstance(obj, GameObject):
                if isinstance(obj, ControllableObject):
                    obj.next_move()
                    next_x, next_y = obj.next_pos_x, obj.next_pos_y
                    if obj.pos_x != obj.next_pos_x or obj.pos_y != obj.next_pos_y:
                        if next_x >= 0 and next_x + obj.width < self.screen_width:
                            obj.pos_x, obj.pos_y = next_x, next_y

                elif isinstance(obj, PlayerBullet):
                    if obj.pos_y >= self.screen_height + obj.height:
                        obj.destroy_self()
                    colliding = self.colliding_objects(obj)
                    if len(colliding) == 0:
                        obj.pos_y += 1

                else:
                    colliding = self.colliding_objects(obj)
                    if len(colliding) == 0:
                        obj.pos_y -= 1



            if isinstance(obj, DestroyableObject):
                for col_obj in colliding:
                    obj.on_collision_with(col_obj)

            if not any(isinstance(obj, EnemyPlane) for obj in self.game_objects):
                self.game_won = True
