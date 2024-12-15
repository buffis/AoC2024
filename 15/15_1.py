f = open("input.txt").readlines()
moves = []
walls = []
boxes = []
posx, posy = 0, 0
maxx, maxy = len(f[0].strip()) - 2, 0
for y, line in enumerate(f):
    line = line.strip()
    if line.startswith("#"):
        for x, c in enumerate(line):
            if c == "#":
                walls.append((x, y))
            elif c == "O":
                boxes.append((x, y))
            elif c == "@":
                posx, posy = x, y 
        pass
    elif line:
        for c in line:
            moves.append(c)
    else:
        maxy = y - 2

# Return True if moved.
def move_box(x, y, deltax, deltay):
    if (x, y) in boxes:
        if move_box(x+deltax, y+deltay, deltax, deltay):
            boxes.remove((x,y))
            boxes.append((x+deltax, y+deltay))
            return True
        else:
            return False
    elif (x,y) in walls:
        return False
    return True

def move():
    global posx, posy
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
        if not move_box(newx, newy, deltax, deltay):
            return
    posx, posy = newx, newy

def out():
    for y in range(0, maxy+2):
        for x in range(0, maxx+2):
            c = "."
            if (x,y) in walls:
                c = "#"
            if (x,y) in boxes:
                c = "O"
            if posx == x and posy == y:
                c = "@"
            print(c, end="")
        print("")

while moves:
    move()
out()

print (sum([b[0] + b[1] * 100 for b in boxes]))
    