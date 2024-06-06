from gameobjects import ControllableObject, GameObject


class GameState:
    def __init__(self):
        self.game_objects = []
        self.game_started = False
        self.game_finished = False
        self.screen_height = 60
        self.screen_width = 80
        self.time = 0

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
        with open("output.txt", "a") as f:
            print("CALLED IS_COLLIDING FOR", object.name, file=f)
            for obj in self.game_objects:
                if self.are_colliding(object, obj):
                    res.append(obj)
                else:
                    print("NO COLLISION BETWEEN ",
                          object.name, "(", object.pos_x, ", ", object.pos_y, ") ", object.height, object.width,
                          " and ",
                          obj.name, "(", obj.pos_x, ", ", object.pos_y, ")", obj.height, obj.width, file=f)

            print(object.name, res, file=f)

        return res

    def update_positions(self):
        self.time += 1
        for obj in self.game_objects:

            if isinstance(obj, GameObject):
                if isinstance(obj, ControllableObject):
                    obj.next_move()
                    next_x, next_y = obj.next_pos_x, obj.next_pos_y
                    if obj.pos_x != obj.next_pos_x or obj.pos_y != obj.next_pos_y:
                        if next_x >= 0 and next_x + obj.width < self.screen_width:
                            obj.pos_x, obj.pos_y = next_x, next_y

                else:
                    if len(self.colliding_objects(obj)) == 0:
                        with open("output.txt", "a") as f:
                            print("NO COLLISION!!!", file=f)
                        if obj.movable:
                            obj.pos_y -= 1
                    