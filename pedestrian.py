import config

class Pedestrian:
    json_pos_key = "position"
    json_vel_key = "velocity"
    json_weight_key = "weight"
    json_radius_key = "radius"

    def __init__(self, json_ped):
        self.pos = json_ped[Pedestrian.json_pos_key]
        self.vel = json_ped[Pedestrian.json_vel_key]
        if Pedestrian.json_weight_key in json_ped:
            self.weight = json_ped[Pedestrian.json_weight_key]
        else:
            self.weight = config.default_weight
        if Pedestrian.json_radius_key in json_ped:
            self.radius = json_ped[Pedestrian.json_radius_key]
        else:
            self.radius = config.default_radius

    def __str__(self):
        s = "pos: " + str(self.pos) + "\n"
        s = s + "vel: " + str(self.vel) + "\n"
        s = s + "weight: " + str(self.weight) + "\n"
        s = s + "radius: " + str(self.radius) + "\n"
        return s

    def toJson(self):
        json_ped = {}
        json_ped[Pedestrian.json_pos_key] = self.pos
        json_ped[Pedestrian.json_vel_key] = self.vel
        json_ped[Pedestrian.json_weight_key] = self.weight
        json_ped[Pedestrian.json_radius_key] = self.radius
        return json_ped