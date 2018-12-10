import json

from mylog import log
import config

from mymap import Map
from pedestrian import Pedestrian
from experiment import Experiment

def loadPedestrians(filename):
    json_data = None
    ped_list = []
    with open(filename, "rt") as fd:
        json_data = json.load(fd)
    for json_ped in json_data:
        ped_list.append(Pedestrian(json_ped))
    return ped_list

def isAllReachTarget(ped_list, target_area):
    for ped in ped_list:
        if not ped.pos in target_area:
            return False
    return True

def savePed(ped_list, time):
    log_msg = "Time " + str(time) + "----\n"
    for ped in ped_list:
        log_msg = log_msg + str(ped) + "\n"
    log.info(log_msg)


if __name__ == "__main__":
    map_info = Map("data/large_basic_map.txt")
    ped_list = loadPedestrians("data/three_ped.json")
    time_tick = config.default_time_tick

    tick_count = 0
    experiment = Experiment(map_info)
    while not isAllReachTarget(ped_list, map_info.getTargetArea()):
        if tick_count % 10 == 0:
            print("Tick", tick_count)
        savePed(ped_list, experiment.time)
        experiment.tick(ped_list, time_tick)
        tick_count = tick_count + 1
    savePed(ped_list, experiment.time)