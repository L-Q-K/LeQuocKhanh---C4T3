#create game:

maps = {"size_x": 5,
        "size_y": 5
}

player_pos = [
    {"x": 3, "y": 4},
    {"x": 1, "y": 1},
    {"x": 2, "y": 0}
]             

boxes_pos = [
    [{"x": 1, "y": 1}, {"x": 2, "y": 2}, {"x": 3, "y": 3}],
    [{"x": 2, "y": 2}, {"x": 3, "y": 3}, {"x": 1, "y": 3}],
    [{"x": 2, "y": 1}]
]

door_pos = [
    [{"x": 2, "y": 1}, {"x": 3, "y":2}, {"x": 4, "y":3}],
    [{"x": 3, "y": 2}, {"x": 4, "y": 3}, {"x": 0, "y": 0}],
    [{"x": 2, "y": 3}]
]

walls = [
    [{"x": 0, "y": 0}],
    [{"x": 4, "y": 2}, {"x": 2, "y": 1}],
    [{"x": 1, "y": 3}, {"x": 1, "y": 2}, {"x": 2, "y": 3}]
]

real_level = 0
undo = {}

def print_map(level):
    for y in range(maps["size_y"]):
        for x in range(maps["size_x"]):
            box_is_here = False
            for box in boxes_pos[level]:
                if x == box["x"] and y == box["y"]:
                    box_is_here = True
                    break

            door_is_here = False
            for door in door_pos[level]:
                if x == door["x"] and y == door["y"]:
                    door_is_here = True
                    break

            wall_is_here = False
            for wall in walls[level]:
                if x == wall["x"] and y == wall["y"]:
                    wall_is_here = True
                    break
                    
            player_is_here = False
            if x == player_pos[level]["x"] and y == player_pos[level]["y"]:
                player_is_here = True

            if player_is_here:
                print("P ", end="")
            elif box_is_here:
                print("B ", end="")
            elif door_is_here:
                print("D ", end="")
            elif wall_is_here:
                print("W ", end="")
            else:
                print("_ ", end="")

        print()

#gameplay

def game_play(level):
    undo_times = 0
    
    while True:
        print_map(level)

        # win_check

        win = True
        for box in boxes_pos[level]:
            if box not in door_pos[level]:
                win = False

        if win:
            if level == 2:
                print("Hết level rùi")
            else:
                game_play(level + 1)
            break

        #move player:

        move = input("Your move?: ").upper().replace(" ", "")

        dx = 0
        dy = 0

        if move == "W":
            dy = -1
        elif move == "S":
            dy = 1
        elif move == "A":
            dx = -1
        elif move == "D":
            dx = 1
        elif move == "Z":
            if undo_times == 0:
                player_pos[level] = dict(undo["player_pos"])
                if "box_pos" in undo:
                    print(boxes_pos[level][undo["box_index"]])
                    boxes_pos[level][undo["box_index"]] = dict(undo["box_pos"])
                    print(boxes_pos[level][undo["box_index"]])
                undo_times = 1
            else:
                print("Chơi kém à mà phải undo nhiều thế")
        else:
            break

        #control_check:

        if 0 <= player_pos[level]["x"] + dx < maps["size_x"]\
            and 0 <= player_pos[level]["y"]+ dy < maps["size_y"]:
            undo["player_pos"] = dict(player_pos[level])
            player_pos[level]["x"] += dx
            player_pos[level]["y"] += dy

        for wall in walls[level]:
            if  player_pos[level]["x"] == wall["x"]\
               and player_pos[level]["y"] == wall["y"]:
                player_pos[level]["x"] -= dx
                player_pos[level]["y"] -= dy

        for box in boxes_pos[level]:
            if player_pos[level]["x"] == box["x"]\
                and player_pos[level]["y"] == box["y"]:

                undo["box_pos"] = dict(boxes_pos[level][boxes_pos[level].index(box)])
                undo["box_index"] = boxes_pos[level].index(box)
                
                if  0 <= boxes_pos[level][boxes_pos[level].index(box)]["x"] + dx < maps["size_x"]\
                    and 0 <= boxes_pos[level][boxes_pos[level].index(box)]["y"] + dy < maps["size_y"]:

                    boxes_pos[level][boxes_pos[level].index(box)]["x"] += dx
                    boxes_pos[level][boxes_pos[level].index(box)]["y"] += dy
                    
                    for wall in walls[level]:
                        if boxes_pos[level][boxes_pos[level].index(box)]["x"] == wall["x"]\
                           and boxes_pos[level][boxes_pos[level].index(box)]["y"] == wall["y"]:
                            player_pos[level]["x"] -= dx
                            player_pos[level]["y"] -= dy
                            boxes_pos[level][boxes_pos[level].index(box)]["x"] -= dx
                            boxes_pos[level][boxes_pos[level].index(box)]["y"] -= dy
                            break
                    
                    new_boxes_pos = list(boxes_pos[level])
                    del new_boxes_pos[boxes_pos[level].index(box)]
                    
                    for next_box in new_boxes_pos:
                        if boxes_pos[level][boxes_pos[level].index(box)]["x"] == new_boxes_pos[new_boxes_pos.index(next_box)]["x"]\
                            and boxes_pos[level][boxes_pos[level].index(box)]["y"] == new_boxes_pos[new_boxes_pos.index(next_box)]["y"]:
                            player_pos[level]["x"] -= dx
                            player_pos[level]["y"] -= dy
                            boxes_pos[level][boxes_pos[level].index(box)]["x"] -= dx
                            boxes_pos[level][boxes_pos[level].index(box)]["y"] -= dy
                            break
                        
                else:
                    player_pos[level]["x"] -= dx
                    player_pos[level]["y"] -= dy

        
game_play(real_level)

