from flask import Flask, render_template, jsonify, request
import config
from project.utils import ClaimStatus

app = Flask(__name__)
@app.route("/")
def api_testing():
    return "successfully created"

@app.route("/is_claim",methods = ["GET"])
def claim_prediction():
    data = request.form
    age_of_car = eval(data["age_of_car"])
    age_of_policyholder = eval(data["age_of_policyholder"])
    area_cluster = data["area_cluster"]
    population_density = eval(data["population_density"])
    make = eval(data["make"])
    segment = data["segment"]
    model = data["model"]
    fuel_type = data["fuel_type"]
    engine_type = data["engine_type"]
    rear_brakes_type = data["rear_brakes_type"]
    transmission_type = data["transmission_type"]
    gear_box = int(data["gear_box"])
    steering_type = data["steering_type"]
    d1 = {0:"NO",1:"Yes"}

    claims = ClaimStatus(age_of_car,age_of_policyholder,area_cluster,population_density, make,segment,model,fuel_type,engine_type,rear_brakes_type,transmission_type,gear_box,steering_type)
    status = claims.get_prediction()
    return jsonify({"Result": f"will costomer calaim the insurance:: {d1[status[0]]}"})

if __name__ == "__main__":
    app.run()