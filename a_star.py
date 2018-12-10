from mymap import Map

def calH(pos, to_area):
    if pos in to_area:
        return 0
    min_h = abs(to_area[0][0]-pos[0]) + abs(to_area[0][1]-pos[1])
    for to_pos in to_area:
        h = abs(to_pos[0]-pos[0]) + abs(to_pos[1]-pos[1])
        if h < min_h:
            min_h = h
    return min_h

class AStarSolver:
    def __init__(self, map_info, to_area):
        self.map = map_info
        self.H_tab = []
        self.G_tab = []
        self.F_tab = []
        self.father_tab = []

        # init h
        for y in range(map_info.length()):
            H_line = []
            for x in range(map_info.width()):
                if map_info.isWall(x, y):
                    H_line.append(-1)
                elif map_info.isTarget(x, y):
                    H_line.append(0)
                else:
                    H_line.append(calH((x, y), to_area))
            self.H_tab.append(H_line)

        # fill father, G, F
        for y in range(map_info.length()):
            father_line = []
            G_line = []
            F_line = []
            for x in range(map_info.width()):
                father_line.append(None)
                G_line.append(None)
                F_line.append(None)
            self.father_tab.append(father_line)
            self.G_tab.append(G_line)
            self.F_tab.append(F_line)

    def calAround(self, pos):
        res = []
        if pos[0] > 0:
            if pos[1] > 0:
                res.append((pos[0]-1, pos[1]-1)) # left-up
            res.append((pos[0]-1, pos[1])) # left
            if pos[1] < self.map.length()-1:
                res.append((pos[0]-1, pos[1]+1)) # left-down
        if pos[0] < self.map.width()-1:
            if pos[1] > 0:
                res.append((pos[0]+1, pos[1]-1)) # right-up
            res.append((pos[0]+1, pos[1])) # right
            if pos[1] < self.map.length()-1:
                res.append((pos[0]+1, pos[1]+1)) # right-down
        return res

    def solve(self, from_pos):
        open_list = [from_pos]
        close_list = []

        self.G_tab[from_pos[0]][from_pos[1]] = 0
        while len(open_list) > 0:
            pos = open_list.pop()
            close_list.append(pos)

            around_list = self.calAround(pos)
            # TODO
