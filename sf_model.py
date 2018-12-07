import json

from mymap import Map
from pedestrian import Pedestrian
from mylog import log

def loadPedestrians(filename):
    json_data = None
    ped_list = []
    with open(filename, "rt") as fd:
        json_data = json.load(fd)
    for json_ped in json_data:
        ped_list.append(Pedestrian(json_ped))
    return ped_list

if __name__ == "__main__":
    log.error("233")