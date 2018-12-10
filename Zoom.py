import mymap


def Zoom(map, zoom):
    mark_target = "o"
    mark_wall = "#"
    mark_empty = " "
    mark_hor_bound = "-"
    mark_ver_bound = "|"

    def isWall(node):
        if (node == mark_wall or node == mark_target):
            return True
        else:
            return False

    new_width = map.width() * zoom
    new_length = map.length() * zoom
    new_map = [[" "] * new_width for i in range(new_length)]
    for x in range(map.length()):
        for y in range(map.width()):
            for i in range(zoom):
                for t in range(zoom):
                    new_map[x * zoom + i][y * zoom + t] = map.map_data[x][y]
    return new_map


class largeMap:
    def __init__(self, length, width,path):
        self.output_file = open(path,"w")
        self.length = length
        self.width = width
        self.new_map = [[" "] * self.width for i in range(self.length)]

    # sign 为o/#/|/_这样的符号 只能画直线
    def draw(self, start, end, sign):
        if start[0] == end[0]:
            for i in range(start[1], end[1]+1):
                self.new_map[start[0]][i] = sign
        else:
            if start[1] == end[1]:
                for i in range(start[0], end[0]+1):
                    self.new_map[i][start[1]] = sign
            else:
                return None

    def output(self):
        line = list()
        for i in range(self.length):
            for t in range(self.width):
                line.append(self.new_map[i][t])
            if i != self.length-1:
                line.append("\n")

        self.output_file.write("".join(line))


if __name__ == "__main__":
    myMap = mymap.Map("data/basic_map.txt")
    Zoom(myMap, 2)

    largemap = largeMap(1000,1000,"data/largeMap")
    largemap.draw((0,0),(0,999),"o")
    largemap.draw((1,0),(999,0),"#")
    largemap.draw((1,999), (999, 999), "#")
    largemap.draw((999, 0), (999, 999), "#")
    largemap.draw((1, 0), (1, 300), "#")
    largemap.draw((1, 700), (1, 999), "#")
    largemap.output()
