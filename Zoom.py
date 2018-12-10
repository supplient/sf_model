import mymap


def zoom(map, zoom):
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



if __name__ == "__main__":
    myMap = mymap.Map("data/basic_map.txt")
    zoom(myMap, 2)
