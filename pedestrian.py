import config

class Pedestrian:
    json_pos_key = "position"
    json_vel_key = "velocity"

    json_weight_key = "weight"
    json_radius_key = "radius"
    json_desire_rate_key = "desire_rate"
    json_turn_time_key = "turn_time"
    json_A_key = "A"
    json_B_key = "B"

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
        if Pedestrian.json_desire_rate_key in json_ped:
            self.desire_rate = json_ped[Pedestrian.json_desire_rate_key]
        else:
            self.desire_rate = config.default_desire_rate
        if Pedestrian.json_turn_time_key in json_ped:
            self.turn_time = json_ped[Pedestrian.json_turn_time_key]
        else:
            self.turn_time = config.default_turn_time
        if Pedestrian.json_A_key in json_ped:
            self.A = json_ped[Pedestrian.json_A_key]
        else:
            self.A = config.default_A
        if Pedestrian.json_B_key in json_ped:
            self.B = json_ped[Pedestrian.json_B_key]
        else:
            self.B = config.default_B

    def __str__(self):
        s = "pos: " + str(self.pos) + "\n"
        s = s + "vel: " + str(self.vel) + "\n"
        s = s + "weight: " + str(self.weight) + "\n"
        s = s + "radius: " + str(self.radius) + "\n"
        s = s + "desire_rate: " + str(self.desire_rate) + "\n"
        s = s + "turn_time: " + str(self.turn_time) + "\n"
        s = s + "A: " + str(self.A) + "\n"
        s = s + "B: " + str(self.B) + "\n"
        return s

    def toJson(self):
        json_ped = {}
        json_ped[Pedestrian.json_pos_key] = self.pos
        json_ped[Pedestrian.json_vel_key] = self.vel
        json_ped[Pedestrian.json_weight_key] = self.weight
        json_ped[Pedestrian.json_radius_key] = self.radius
        json_ped[Pedestrian.json_desire_rate_key] = self.desire_rate
        json_ped[Pedestrian.json_turn_time_key] = self.turn_time
        json_ped[Pedestrian.json_A_key] = self.A
        json_ped[Pedestrian.json_B_key] = self.B
        return json_ped