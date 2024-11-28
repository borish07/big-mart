from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open('xg_final.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Dummy predict function (replace with your actual prediction logic)
def predict_sales(features):
    # This is a dummy prediction, replace with your actual model
    return np.random.randint(1000, 5000)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Get features from form
        item_weight = float(request.form['item_weight'])
        item_fat_content = request.form['item_fat_content']
        item_visibility = float(request.form['item_visibility'])
        item_type = request.form['item_type']
        item_mrp = float(request.form['item_mrp'])
        outlet_size = request.form['outlet_size']
        outlet_location_type = request.form['outlet_location_type']
        outlet_type = request.form['outlet_type']

        # Prepare features (you might need to preprocess these based on your model)
        features = [item_weight, item_fat_content, item_visibility, item_type, item_mrp, outlet_size, outlet_location_type, outlet_type]

        # Make prediction
        prediction = predict_sales(features)

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)