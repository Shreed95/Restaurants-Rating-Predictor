import pickle
from flask import Flask, request, jsonify, render_template

application = Flask(__name__)
app = application

# Load models and encoders
model = pickle.load(open("models/model.pkl", "rb"))
label_enc1 = pickle.load(open("models/label_enc1.pkl", "rb"))  # online_order, book_table
label_enc2 = pickle.load(open("models/label_enc2.pkl", "rb"))  # rest_type
label_enc3 = pickle.load(open("models/label_enc3.pkl", "rb"))  # cuisine
label_enc4 = pickle.load(open("models/label_enc4.pkl", "rb"))  # type

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predictdata", methods=["POST", "GET"])
def predict_datapoint():
    if request.method == "POST":
        try:
            # Get input values
            online_order = request.form.get('online_order', None)
            book_table = request.form.get('book_table', None)
            votes = request.form.get('votes', 0)
            rest_type = request.form.get('rest_type', None)
            cost = request.form.get('cost', 0.0)
            type = request.form.get('type', None)
            cuisine = request.form.get('cuisine', None)

            # Ensure proper transformation of inputs
            online_order = label_enc1.transform([online_order])[0] if online_order else 0
            book_table = label_enc1.transform([book_table])[0] if book_table else 0
            rest_type = label_enc2.transform([rest_type])[0] if rest_type else 0
            type = label_enc4.transform([type])[0] if type else 0
            cuisine = label_enc3.transform([cuisine])[0] if cuisine else 0
            votes = int(votes)
            cost = float(cost)

            # Create input array
            X_test = [[online_order, book_table, votes, rest_type, cost, type, cuisine]]
            print(X_test)

            # Model prediction
            result = model.predict(X_test)

            return render_template('home.html', result=result[0])
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
