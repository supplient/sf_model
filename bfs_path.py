import mymap

map = mymap.Map("data/basic_map.txt");
width = map.width()
length = map.length()
unsearched = list()
searched = list()
node_distance = [[-1]*width for i in range(length)]


def search_by_node(x, y):
    if x > 0 and (not map.isWall(x-1,y)):
        if node_distance[x][y]+1<node_distance[x-1][y] or node_distance[x-1][y]==-1:
            node_distance[x - 1][y] = node_distance[x][y]+1
        if (x-1,y) not in searched:
            unsearched.append((x-1,y))
    if x<length-1 and(not map.isWall(x+1,y)):
        if node_distance[x][y]+1<node_distance[x+1][y]or node_distance[x+1][y]==-1:
            node_distance[x + 1][y] = node_distance[x][y]+1
        if (x + 1, y) not in searched:
            unsearched.append((x+1,y))
    if y >0 and (not map.isWall(x,y-1)):
        if node_distance[x][y]+1<node_distance[x][y-1] or node_distance[x][y-1]==-1:
            node_distance[x][y-1] = node_distance[x][y]+1
        if (x, y-1) not in searched:
            unsearched.append((x,y-1))
    if y<width-1 and(not map.isWall(x,y+1)):
        if node_distance[x][y] + 1 < node_distance[x][y+1]or node_distance[x][y+1]==-1:
            node_distance[x][y+1] = node_distance[x][y] + 1
        if (x, y+1) not in searched:
            unsearched.append((x,y+1))
        
def getTarget():
    targets = list()
    min_distance = -1
    for x_axis in range(length):
        for y_axis in range(width):
            if map.isTarget(x_axis, y_axis) and node_distance[x_axis][y_axis] != -1:
                if min_distance == -1 or node_distance[x_axis][y_axis] <= min_distance:
                    if node_distance[x_axis][y_axis] == min_distance:
                        targets.append((x_axis, y_axis))
                    else:
                        targets = list()
                        targets.append((x_axis, y_axis))
                    min_distance = node_distance[x_axis][y_axis]

    for target in targets:
        print(target, node_distance[target[0]][target[1]])
    return targets


def bfs(x_start,y_start):
    if x_start<0 or x_start>=length:
        print("wrong x_start")
        return
    if y_start<0 or y_start>=width:
        print("wrong y_start")
        return
    if not map.isEmpty(x_start,y_start):
        print("wrong position")
        return
    search_by_node(x_start,y_start)
    searched.append((x_start,y_start))
    while len(unsearched)!=0:
        node = unsearched.pop(0)
        searched.append(node)
        search_by_node(node[0],node[1])
    targets = getTarget()






if __name__ =="__main__":
    bfs(3,3)





