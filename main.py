from flask import Flask, request, json, render_template, jsonify, Response
import pickle
app = Flask(__name__)

app.config["SERVER_HOST"] = "0.0.0.0"
app.config["SERVER_PORT"] = 5000


@app.route('/', methods=['GET'])
def index():
    """render index template (homepage)"""
    return render_template("index.html")


@app.route('/', methods=['POST'])
def predict():
    dt_model_file = 'model_DT.sav'
    dt_model = pickle.load(open(dt_model_file, 'rb'))
    dt_result = dt_model.predict([[float(request.json["latitude"]), float(request.json["longitude"]),
                                   float(request.json["elevation"]), float(request.json["wind"]),
                                   float(request.json["precipitation"]), float(request.json["maxTemprature"])]])
    # dt_result = dt_model.predict([[41.3,-122.3,1077.5,0.67,0,60]])
    print(dt_result)

    ann_model_file = 'model_ANN.sav'
    ann_model = pickle.load(open(ann_model_file, 'rb'))
    ann_result = ann_model.predict([[float(request.json["latitude"]), float(request.json["longitude"]),
                                   float(request.json["elevation"]), float(request.json["wind"]),
                                   float(request.json["precipitation"]), float(request.json["maxTemprature"])]])
    print(ann_result)

    rf_model_file = 'model_RF.sav'
    rf_model = pickle.load(open(rf_model_file, 'rb'))
    rf_result = rf_model.predict([[float(request.json["latitude"]), float(request.json["longitude"]),
                                   float(request.json["elevation"]), float(request.json["wind"]),
                                   float(request.json["precipitation"]), float(request.json["maxTemprature"])]])
    print(rf_result)

    data = {'dt_result': dt_result[0], 'ann_result': ann_result[0],
            'rf_result': rf_result[0]}

    return jsonify(data)

    # return Response(headers=[("Content-Type", "json/application")],
    #                     response=json.dumps(data),
    #                     status=200)


if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(debug=True,
            host=app.config["SERVER_HOST"],
            port=app.config["SERVER_PORT"])