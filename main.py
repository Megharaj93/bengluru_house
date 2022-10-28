
from flask import Flask, render_template, request
import config
from utils import BengluruHousePrice
#from distutils.command.config import config

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/prediction_price", methods= ["POST", "GET"])
def get_predicted_price():

    if request.method == "GET":
        total_sqft = float(request.args.get("total_sqft"))
        bath = float(request.args.get("bath"))
        balcony = float(request.args.get("balcony"))
        BHK = float(request.args.get("BHK"))
        location = request.args.get("location")

        class_obj = BengluruHousePrice(total_sqft, bath, balcony, BHK, location)
        price = class_obj.get_house_price()

        return render_template("index.html", prediction = price)

    else:
        total_sqft = float(request.form.get("total_sqft"))
        bath = float(request.form.get("bath"))
        balcony = float(request.form.get("balcony"))
        BHK = float(request.form.get("BHK"))
        location = request.form.get("location")

        class_obj = BengluruHousePrice(total_sqft, bath, balcony, BHK, location)
        price = class_obj.get_house_price()

        return render_template("index.html", prediction = price)


if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= config.PORT_NUMBER, debug= True)


