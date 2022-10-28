from matplotlib.font_manager import json_dump
import config
import pandas as pd
import numpy as np
import json
import pickle
import warnings
warnings.filterwarnings("ignore")

class BengluruHousePrice():

    def __init__(self,total_sqft, bath, balcony, BHK, location):

        self.total_sqft = total_sqft
        self.bath = bath
        self.balcony = balcony
        self.BHK = BHK
        self.location = "location_" + location

    def load_model(self):

        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)

        #print(self.model)

        with open(config.PROJECT_DATA_PATH, "r") as f:
            self.project_data = json.load(f)


    def get_house_price(self):
        self.load_model()

        location_index = self.project_data["columns"].index(self.location)

        len_array = len(self.project_data["columns"])

        user_array = np.zeros(len_array)

        user_array[0] = self.total_sqft
        user_array[1] = self.bath
        user_array[2] = self.balcony
        user_array[3] = self.BHK
        user_array[location_index] = 1

        #print("user array --> ", user_array) 

        predicted_price = self.model.predict([user_array])[0]

        print("Predicted price of your Dream House -- > Rs.", np.around(predicted_price, decimals= 2),"Lakhs only.")

        return np.around(predicted_price, decimals= 2)


if __name__ == "__main__":
    total_sqft = 2000
    bath = 3
    balcony = 3
    BHK = 4 
    location = "9th Phase JP Nagar"

    class_obj = BengluruHousePrice(total_sqft, bath, balcony, BHK, location)
    class_obj.get_house_price()


