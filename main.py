from flask import Flask, request, render_template, jsonify
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
    # Load the file for Gradient Boosting
    model1_file = 'model_GB.sav'
    model1 = pickle.load(open(model1_file, 'rb'))
    model1_result = model1.predict([[float(request.json["latitude"]), float(request.json["longitude"]),
                                   float(request.json["elevation"]), float(request.json["wind"]),
                                   float(request.json["precipitation"]), float(request.json["maxTemprature"])]])

    # Load the file for SGD
    model2_file = 'model_SGD.sav'
    model2 = pickle.load(open(model2_file, 'rb'))
    model2_result = model2.predict([[float(request.json["latitude"]), float(request.json["longitude"]),
                                   float(request.json["elevation"]), float(request.json["wind"]),
                                   float(request.json["precipitation"]), float(request.json["maxTemprature"])]])

    data = { 'result1': model1_result[0], 'result2': model2_result[0] }

    return jsonify(data)


if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(debug=True,
            host=app.config["SERVER_HOST"],
            port=app.config["SERVER_PORT"])