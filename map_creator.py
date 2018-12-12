from mymap import Map

class MapCreator:
    def __init__(self, length, width):
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

    def output(self, path):
        line = list()
        for i in range(self.length):
            for t in range(self.width):
                line.append(self.new_map[i][t])
            if i != self.length-1:
                line.append("\n")
        with open(path, "wt") as fd:
            fd.write("".join(line))

def createBasicLargeMap():
    size1 = 400
    size2 = 500
    half_size = int(size1/2)
    large_map = MapCreator(size1, size2)
    large_map.draw((0,0), (size1-1,0), Map.mark_target)
    large_map.draw((0,1), (size1-1,1), Map.mark_target)
    large_map.draw((0,2), (half_size-50,2), Map.mark_wall)
    large_map.draw((half_size+50,2), (size1-1,2), Map.mark_wall)
    large_map.draw((0,3), (0,size2-1), Map.mark_wall)
    large_map.draw((size1-1,3), (size1-1,size2-1), Map.mark_wall)
    large_map.draw((0,size2-1), (size1-1,size2-1), Map.mark_wall)
    large_map.output("data/large_basic_map.txt")

def createExampleMap():
    largemap = MapCreator(1000,1000)
    largemap.draw((0,0),(0,999),"o")
    largemap.draw((1,0),(999,0),"#")
    largemap.draw((1,999), (999, 999), "#")
    largemap.draw((999, 0), (999, 999), "#")
    largemap.draw((1, 0), (1, 300), "#")
    largemap.draw((1, 700), (1, 999), "#")
    largemap.output("data/largeMap")

if __name__ == "__main__":
    createBasicLargeMap()
    createExampleMap()