from collections import defaultdict

plots = {}
plotlist = []
lines = open("test.py").readlines()
maxx = len(lines[0].strip()) - 1
maxy = len(lines) - 1
plot_id = 0

def getc(x,y):
    if x < 0 or y < 0 or x > maxx or y > maxy: return " "
    return lines[y][x]

class Plot(object):
    def __init__(self, c, plot_id):
        self.c = c
        self.area = 0
        self.peri = 0
        self.corners = 0
        self.plot_id = plot_id
    def price1(self):
        return self.area * self.peri
    def price2(self):
        return self.area * self.corners
    def __str__(self):
        return "Plot_" + self.c + " " + str(self.area) + " " + str(self.peri)

def get_surround(x,y):
    l = []
    l.append((x-1, y))
    l.append((x, y-1))
    l.append((x+1, y))
    l.append((x, y+1))
    return l

merges = defaultdict(set)

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "\n": continue
        s_plots = []
        perimeter = 0
        for s_x, s_y in get_surround(x, y):
            if (s_x, s_y) in plots and plots[(s_x, s_y)].c == c:
                s_plots.append(plots[(s_x, s_y)])
            if getc(s_x, s_y) != c:
                perimeter += 1
        
        # Outer corners
        corners = 0
        if perimeter == 4: corners = 4
        if perimeter == 3: corners = 2
        if perimeter == 2:
            same1 = c == getc(x-1, y) == getc(x+1, y)
            same2 = c == getc(x, y-1) == getc(x, y+1)
            if not same1 and not same2:
                corners = 1
        
        # Inner corners
        if getc(x+1, y+1) != c and getc(x+1, y) == c and getc(x, y+1) == c:
            corners += 1
        if getc(x-1, y-1) != c and getc(x-1, y) == c and getc(x, y-1) == c:
            corners += 1
        if getc(x+1, y-1) != c and getc(x+1, y) == c and getc(x, y-1) == c:
            corners += 1
        if getc(x-1, y+1) != c and getc(x-1, y) == c and getc(x, y+1) == c:
            corners += 1
            
        if s_plots:
            plot = s_plots[0]
            if len(s_plots) > 1:
                for p in s_plots[1:]:
                    if p.plot_id != plot.plot_id:
                        merges[min(plot.plot_id, p.plot_id)].add(max(plot.plot_id, p.plot_id))
        else:
            plot = Plot(c, plot_id)
            plot_id += 1
            plotlist.append(plot)
        plot.area += 1
        plot.peri += perimeter
        plot.corners += corners
        plots[(x,y)] = plot

# This is awful.
needs_more_merge = True
while needs_more_merge:
    needs_more_merge = False
    for x in list(merges):
        for y in list(merges[x]):
            for j in merges[y]:
                if not max(x,j) in merges[min(x,j)]: 
                    needs_more_merge = True
                    merges[min(x,j)].add(max(x,j))
            for x2 in list(merges):
                if x != x2:
                    for y2 in list(merges[x2]):
                        if y == y2:
                            if not max(x, x2) in merges[min(x, x2)]:
                                needs_more_merge = True
                                merges[min(x, x2)].add(max(x, x2))

for x in merges:
    for y in merges[x]:
        plotlist[x].area = plotlist[x].area + plotlist[y].area
        plotlist[y].area = 0 
        plotlist[x].peri = plotlist[x].peri + plotlist[y].peri
        plotlist[y].peri = 0
        plotlist[x].corners = plotlist[x].corners + plotlist[y].corners
        plotlist[y].corners = 0

print (sum([x.price1() for x in plotlist]))
print (sum([x.price2() for x in plotlist]))
