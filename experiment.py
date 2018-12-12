from path_solver import PathSolver
from mylog import log
import config
import math
import numpy as np
# Note: Using numpy for internal vector calculating.


def calLength(pos):
    return math.sqrt(pos[0]*pos[0] + pos[1]*pos[1])

def calDistance(from_pos, to_pos):
    return calLength((to_pos[0]-from_pos[0], to_pos[1]-from_pos[1]))

def calUnitVector(from_pos, to_pos):
    x = from_pos[0] - to_pos[0]
    y = from_pos[1] - to_pos[1]
    length = calLength((x,y))
    return (x/length, y/length)

def calOrthogonalVector(ori_vec):
    return (-ori_vec[1], ori_vec[0])

class Experiment:
    def __init__(self, map_info, start_time=0):
        self.map = map_info
        self.time = start_time
        self.path_solver = PathSolver(self.map, self.map.getTargetArea())

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

        log.debug("Desire forces: " + str(desire_list))

        # cal force comes from wall
        wall_list = []
        for ped in ped_list:
            ped_vel = np.array(ped.vel)
            wall_area = self.map.getWallArea()
            wall_joint = np.array((0, 0))
            for wall in wall_area:
                dist = calDistance(wall, ped.pos)/self.map.scale
                rad_diff = ped.radius - dist
                unit_vec = calUnitVector(ped.pos, wall)
                orth_vec = calOrthogonalVector(unit_vec)

                # cal social force
                wall_joint = wall_joint + self.calSocial(unit_vec, rad_diff, ped.A, ped.B)

                # cal physical force
                if rad_diff > 0:
                    # touched
                    wall_joint = wall_joint + self.calPhysical(unit_vec, orth_vec, rad_diff, ped_vel)
            wall_list.append(wall_joint)

        log.debug("Wall froces: " + str(wall_list))

        # cal force comes from other pedestrians
        others_list = []
        for ped_i in ped_list:
            ped_vel_i = np.array(ped_i.vel)
            others_joint = np.array((0,0))
            for ped_j in ped_list:
                if ped_i == ped_j:
                    continue
                ped_vel_j = np.array(ped_j.vel)
                dist = calDistance(ped_j.pos, ped_i.pos)
                rad_diff = ped_i.radius + ped_j.radius - dist
                unit_vec = calUnitVector(ped_i.pos, ped_j.pos)
                orth_vec = calOrthogonalVector(unit_vec)

                # cal social force
                others_joint = others_joint + self.calSocial(unit_vec, rad_diff, ped_i.A, ped_i.B)

                # cal physical force
                if rad_diff > 0:
                    others_joint = others_joint + self.calPhysical(unit_vec, orth_vec, rad_diff, ped_vel_j, ped_vel_i)
            others_list.append(others_joint)

        log.debug("Others forces: " + str(others_list))

        # cal joint force
        joint_list = []
        for desire, wall, others in zip(desire_list, wall_list, others_list):
            joint = np.array((0, 0))
            joint = joint + desire
            joint = joint + wall
            joint = joint + others
            joint_list.append(joint)
        
        # cal new position(using old velocity)
        for ped in ped_list:
            pos = np.array(ped.pos)
            vel = np.array(ped.vel)
            pos = pos + vel* self.map.scale*time_tick
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
        if ped.pos in self.map.getTargetArea():
            return res # has reached, so no desire

        path = self.path_solver.solve(ped.pos)
        if path == None:
            raise Exception("Pedstrain \n" + str(ped) + "\tcannot find any path to the target area.")
        if len(path) < 2: # has reach the target
            return np.array((0, 0))

        e = calUnitVector(ped.pos, path[1])
        e = - np.array(e)
        res = ped.desire_rate * e
        vel = np.array(ped.vel)
        res = res - vel
        res = res / ped.turn_time
        res = res * ped.weight
        return res

    def calPhysical(self, unit_vec, orth_vec, rad_diff, vel_j, vel_i = np.array((0,0))):
        support_force = np.array(unit_vec)
        support_force = config.k * rad_diff * support_force

        friction_force = np.array(orth_vec)
        friction_force = np.dot((vel_j - vel_i), friction_force) * friction_force
        friction_force = config.fric_arg * rad_diff * friction_force

        return support_force - friction_force

    def calSocial(self, unit_vec, rad_diff, A, B):
        social_force = np.array(unit_vec)
        social_force = A * social_force
        social_force = math.exp(rad_diff/B) * social_force
        return social_force