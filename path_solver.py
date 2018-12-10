from mymap import Map
import bfs_path
class PathSolver:
    def __init__(self, map_info):
        self.map = map_info

    def solve(self, from_pos, to_area):
        '''@param
            from_pos: a tuple (x, y) representing the path's start pos.
            to_area: a list of tuples (x, y) representing the path's possible end pos.
        @return
            If the path is found, return the path as a list of tuples (x,y).
            Otherwise, return None
        '''
        result = bfs_path.bfs(from_pos[0],from_pos[1],to_area, self.map)
        if result is None:
            return None
        else:
            return result[0]

if __name__ == "__main__":
    input_map = Map("data/largeMap")
    path_solver = PathSolver(input_map)
    path_solver.solve((55,55),[(0,55)])