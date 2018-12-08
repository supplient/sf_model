from path_solver import PathSolver
import math
import numpy as np
# Note: Using numpy for internal vector calculating.


def calLength(pos):
    return math.sqrt(pos[0]*pos[0] + pos[1]*pos[1])

def calUnitVector(from_pos, to_pos):
    x = to_pos[0] - from_pos[0]
    y = to_pos[1] - from_pos[1]
    length = calLength((x,y))
    return (x/length, y/length)

class Experiment:
    def __init__(self, map_info, start_time=0):
        self.map = map_info
        self.time = start_time
        self.path_solver = PathSolver(self.map)

    def tick(self, ped_list, time_tick):
        '''[IN]
            ped_list: a list of current pedestrians
            time_tick: how much time to pass
        [EFFECT]
            Update ped_list to the time after tick_tick passed.
        '''
        # cal desire force
        desire_list = []
        for ped in ped_list:
            desire_list.append(self.calDesire(ped))

        # TODO cal other forces

        # cal joint force
        joint_list = []
        for desire in desire_list:
            joint = np.array((0, 0))
            joint = joint + desire
            joint_list.append(joint)
        
        # cal new position(using old velocity)
        for ped in ped_list:
            pos = np.array(ped.pos)
            vel = np.array(ped.vel)
            pos = pos + vel*time_tick
            ped.pos = (int(pos[0]), int(pos[1]))

        # cal new velocity
        for ped, joint in zip(ped_list, joint_list):
            vel = np.array(ped.vel)
            vel = vel + joint*time_tick
            ped.vel = (float(vel[0]), float(vel[1]))

        # update experiment's time
        self.time = self.time + time_tick


    def calDesire(self, ped):
        res = np.array((0, 0))

        path = self.path_solver.solve(ped.pos, self.map.getTargetArea())
        if not path:
            raise Exception("Pedstrain \n" + str(ped) + "\tcannot find any path to the target area.")
        if len(path) < 2: # has reach the target
            return np.array((0, 0))

        e = calUnitVector(ped.pos, path[1])
        e = np.array(e)
        res = ped.desire_rate * e
        vel = np.array(ped.vel)
        res = res - vel
        res = res / ped.turn_time
        res = res * ped.weight
        return res