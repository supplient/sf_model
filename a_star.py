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

def isTen(pos_i, pos_j):
    x_diff = abs(pos_i[0] - pos_j[0])
    y_diff = abs(pos_i[1] - pos_j[1])
    return x_diff + y_diff == 1

def isCross(pos_i, pos_j):
    x_diff = abs(pos_i[0] - pos_j[0])
    y_diff = abs(pos_i[1] - pos_j[1])
    return x_diff == 1 and y_diff == 1

def calG(from_pos, to_pos):
    if isTen(from_pos, to_pos):
        return AStarSolver.ten_cost
    elif isCross(from_pos, to_pos):
        return AStarSolver.cross_cost
    else:
        raise Exception("Cannot calculate G between " + str(from_pos) + " and " + str(to_pos))

class AStarSolver:
    ten_cost = 10 # + 直着走
    cross_cost = 14 # x 斜着走

    def __init__(self, map_info, to_area):
        self.map = map_info
        self.to_area = to_area

        self.H_tab = []
        self.G_tab = []
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
            for x in range(map_info.width()):
                father_line.append(None)
                G_line.append(None)
            self.father_tab.append(father_line)
            self.G_tab.append(G_line)

    def calF(self, pos):
        return self.H_tab[pos[0]][pos[1]] + self.G_tab[pos[0]][pos[1]]

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
        if pos[1] > 0:
            res.append((pos[0], pos[1]-1)) # up
        if pos[1] < self.map.length()-1:
            res.append((pos[0], pos[1]+1)) # down
        return res

    def solve(self, from_pos):
        open_list = [from_pos]
        close_list = []
        self.G_tab[from_pos[0]][from_pos[1]] = 0

        not_found = True
        end_pos = None
        while not_found and len(open_list) > 0:
            min_F = self.calF(open_list[0])
            min_index = 0
            for i in range(len(open_list)):
                if self.calF(open_list[i]) < min_F:
                    min_F = self.calF(open_list[i])
                    min_index = i
            pos = open_list[min_index]
            del open_list[min_index]
                
            close_list.append(pos)

            around_list = self.calAround(pos)
            for neigh in around_list:
                if neigh in close_list:
                    continue
                if self.map.isWall(neigh):
                    continue
                    
                neigh_G = self.G_tab[pos[0]][pos[1]] + calG(pos, neigh)
                if neigh in open_list:
                    if neigh_G >= self.G_tab[neigh[0]][neigh[1]]:
                        # if not better, do nothing
                        continue
                    # better route
                    self.G_tab[neigh[0]][neigh[1]] = neigh_G
                    self.father_tab[neigh[0]][neigh[1]] = pos
                else:
                    open_list.append(neigh)
                    self.G_tab[neigh[0]][neigh[1]] = neigh_G
                    self.father_tab[neigh[0]][neigh[1]] = pos

                    if neigh in self.to_area:
                        not_found = False
                        end_pos = neigh
                        break
            # for neigh in around_list:
        # while not_found:

        if not_found:
            return None

        route = [end_pos]
        now_pos = end_pos
        while now_pos != from_pos:
            now_pos = self.father_tab[now_pos[0]][now_pos[1]]
            route.append(now_pos)
        route.reverse()
        return route


if __name__ == "__main__":
    map_info = Map("data/basic_map.txt")
    solver = AStarSolver(map_info, map_info.getTargetArea())
    
    one = (3, 1)
    one_res = solver.solve(one)
    print(one, ": ", one_res)