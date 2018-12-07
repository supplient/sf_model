from path_solver import PathSolver

class Experiment:
    def __init__(self, map_info, start_time=0):
        self.map = map_info
        self.time = start_time
        self.path_solver = PathSolver(self.map)

    def tick(self, ped_list, time_tick):
        desire_list = []
        for ped in ped_list:
            desire_list.append(self.calDesire(ped))

    def calDesire(self, ped):
        res = None
        path = self.path_solver.solve(ped.pos, self.map.getTargetArea())
        if not path:
            raise Exception("Pedstrain \n" + str(ped) + "\tcannot find any path to the target area.")
        # TODO 
        return res