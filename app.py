from flask import Flask, request, jsonify, render_template
# import pickle5 as pickle

app = Flask(__name__)

# with open('model.pkl' , 'rb') as f:
#   sentiment_model = pickle.load(f)


@app.route("/predict", methods=['POST'])
def predict():
    json_ = request.json
    query = json_['query']
    print("Query : ",  query)
    # result = sentiment_model(query)
    # print(result)     
    # return jsonify(result)
    return jsonify({'label' : "POSITIVE", 'score' : 0.99})

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)    