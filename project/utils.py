import pickle
import json
import config
import numpy as np

class ClaimStatus():
    def __init__(self,age_of_car,age_of_policyholder,area_cluster,population_density, make,segment,model,fuel_type,engine_type,rear_brakes_type,transmission_type,gear_box,steering_type):
        self.age_of_car = age_of_car
        self.age_of_policyholder = age_of_policyholder
        self.area_cluster = area_cluster
        self.population_density = population_density
        self.make = make
        self.segment = segment
        self.model = model
        self.fuel_type = fuel_type
        self.engine_type = engine_type
        self.rear_brakes_type = rear_brakes_type
        self.transmission_type = transmission_type
        self.gear_box = gear_box
        self.steering_type = steering_type
    def load_models(self):
        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data = json.load(f)
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.dt_model = pickle.load(f)
    def get_prediction(self):
        self.load_models()
        test_array = np.zeros(len(self.json_data["columns"]))
        test_array[0] = self.age_of_car
        test_array[1] = self.age_of_policyholder
        test_array[2] = self.json_data['area_cluster'][self.area_cluster]
        test_array[3] = self.population_density
        test_array[4] = self.make
        test_array[5] = self.json_data['segment'][self.segment]
        test_array[6] = self.json_data['model'][self.model]
        test_array[7] = self.json_data['fuel_type'][self.fuel_type]
        test_array[8] = self.json_data['engine_type'][self.engine_type]
        test_array[9] = self.json_data['rear_brakes_type'][self.rear_brakes_type]
        test_array[10] = self.json_data['transmission_type'][self.transmission_type]
        test_array[11] = self.gear_box
        test_array[12] = self.json_data['steering_type'][self.steering_type]
        
        prediction = self.dt_model.predict([test_array])
        return prediction
