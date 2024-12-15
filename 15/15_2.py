f = open("input.txt").readlines()
moves, walls, boxes = [], [], {}
posx, posy = 0, 0
maxx, maxy = 2*len(f[0].strip()), 0
for y, line in enumerate(f):
    line = line.strip()
    if line.startswith("#"):
        for x, c in enumerate(line):
            if c == "#":
                walls.append((2*x, y))
                walls.append((2*x + 1, y))
            elif c == "O":
                boxes[(2*x, y)] = '['
                boxes[(2*x+1, y)] = ']'
            elif c == "@":
                posx, posy = 2*x, y 
        pass
    elif line:
        for c in line:
            moves.append(c)
    else:
        maxy = y

def move_box(x, y, deltax, deltay):
    if (x, y) in boxes:
        if deltax != 0:
            if move_box(x+deltax, y+deltay, deltax, deltay):
                boxes[(x+deltax, y+deltay)] = boxes[(x,y)]
                del boxes[(x,y)]
                return True
            else:
                return False
        else:
            if boxes[(x,y)] == "[":
                can_move = True
                can_move &= move_box(x+deltax, y+deltay, deltax, deltay)
                can_move &= move_box(x+1+deltax, y+deltay, deltax, deltay)
                if can_move:
                    del boxes[(x,y)]
                    del boxes[(x+1,y)]
                    boxes[(x+deltax, y+deltay)] = "["
                    boxes[(x+1+deltax, y+deltay)] = "]"
            else:
                can_move = True
                can_move &= move_box(x+deltax, y+deltay, deltax, deltay)
                can_move &= move_box(x-1+deltax, y+deltay, deltax, deltay)
                if can_move:
                    del boxes[(x,y)]
                    del boxes[(x-1,y)]
                    boxes[(x-1+deltax, y+deltay)] = "["
                    boxes[(x+deltax, y+deltay)] = "]"
            return can_move
    elif (x,y) in walls:
        return False
    return True

def move():
    global posx, posy, boxes
    move = moves.pop(0)
    newx, newy = (posx, posy)
    deltax, deltay = 0, 0
    match(move):
        case "^": deltay -= 1 
        case "v": deltay += 1 
        case ">": deltax += 1 
        case "<": deltax -= 1
    newx, newy = posx + deltax, posy + deltay
    if (newx, newy) in walls:
        return
    elif (newx, newy) in boxes:
        if deltax != 0:
            if not move_box(newx, newy, deltax, deltay):
                return
        else:
            boxes2 = boxes.copy() # hacky 
            if not move_box(newx, newy, deltax, deltay):
                boxes = boxes2
                return
    posx, posy = newx, newy

def out():
    for y in range(0, maxy):
        for x in range(0, maxx):
            c = "."
            if (x,y) in walls: c = "#"
            if (x,y) in boxes: c = boxes[(x,y)]
            if posx == x and posy == y: c = "@"
            print(c, end="")
        print("")

while moves:
    move()
    #out()

print (sum([b[0] + b[1] * 100 for b in boxes if boxes[b] == "["]))
