from flask import Flask, render_template, request
import numpy as np
import pickle
#import joblib
app = Flask(__name__)
filename = 'file_iris.pkl'
model = pickle.load(open(filename, 'rb'))    # load the model
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])  # The user input is processed here
def predict():
    Sepal_Length = request.form['sepal_length']
    Sepal_Width = request.form['sepal_width']
    Petak_Length = request.form['petal_length']
    Petal_Width = request.form['petal_width']
    pred = model.predict(np.array([[Sepal_Length, Sepal_Width, Petak_Length, Petal_Width ]]))
    return render_template('index.html', predictValue=str(pred))
if __name__ == '__main__':
    app.run(debug=True)
