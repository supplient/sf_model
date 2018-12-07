class Map:
    mark_target = "o"
    mark_wall = "#"
    mark_empty = " "
    mark_hor_bound = "-"
    mark_ver_bound = "|"

    def __init__(self, filename):
        self.src_file = filename

        # load map
        with open(filename, "rt") as fd:
            self.map_data = fd.readlines()

        # remove line change
        for i in range(0, len(self.map_data)):
            self.map_data[i] = self.map_data[i].replace("\n", "")

        # map size check
        if len(self.map_data) < 1:
            raise Exception("Map: map_data is empty")
        width = len(self.map_data[0])
        for line in self.map_data:
            if len(line) < 1:
                raise Exception("Map: one line is empty")
            if width != len(line):
                raise Exception("Map: lines' lengths are not equal: " + str(width) + " and " + str(len(line)))

    def __str__(self):
        hor_bound = "".join([Map.mark_hor_bound for i in range(0, self.width() + 2)])
        s = hor_bound + "\n"
        for line in self.map_data:
            s = s + Map.mark_ver_bound + line + Map.mark_ver_bound + "\n"
        s = s + hor_bound + "\n"
        return s

    def width(self):
        return len(self.map_data[0])

    def length(self):
        return len(self.map_data)

    def isWall(self, x, y=None):
        '''@param
            x: If y is given, this means pos's x. Otherwise this means the pos(x, y) itself.
            y: Optional. If given, this means pos's y.
        '''
        if not (y is None):
            return self.map_data[x][y] == Map.mark_wall
        else:
            return self.map_data[x[0]][x[1]] == Map.mark_wall

    def isEmpty(self, x, y=None):
        if not (y is None):
            return self.map_data[x][y] == Map.mark_empty
        else:
            return self.map_data[x[0]][x[1]] == Map.mark_empty

    def isTarget(self, x, y=None):
        if not (y is None):
            return self.map_data[x][y] == Map.mark_target
        else:
            return self.map_data[x[0]][x[1]] == Map.mark_target
