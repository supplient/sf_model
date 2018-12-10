from mymap import Map
import bfs_path
from a_star import AStarSolver
from mylog import log

class PathSolver:
    def __init__(self, map_info, to_area):
        self.map = map_info
        self.a_star_solver = AStarSolver(map_info, to_area)

    def solve(self, from_pos):
        '''@param
            from_pos: a tuple (x, y) representing the path's start pos.
            to_area: a list of tuples (x, y) representing the path's possible end pos.
        @return
            If the path is found, return the path as a list of tuples (x,y).
            Otherwise, return None
        '''

        #result = bfs_path.bfs(from_pos[0],from_pos[1], self.to_area, self.map)
        result = self.a_star_solver.solve(from_pos)
        log.debug("Path: " + str(result))
        return result
