import numpy as np 
import pandas as pd 
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('CKD.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/Prediction',methods=['POST','GET'])
def prediction():
    return render_template('ckd.html')
@app.route('/Home',methods=['POST','GET'])
def my_home():
    return render_template('ckd.html')

@app.route('/predict',methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]

    features_name = ['blood_urea','blood_glucose_random','coronary_artery_disease',
    'anemia','pus_cell','red_blood_cells','diabetesmellitus','pedal_edema']

    df = pd.DataFrame(features_value, columns=features_name)

    output = model.predict(df)

    return render_template('result.html',predict_text=output)

    if output==str(1):
         return render_template('ckd.html',pred='You have CHRONIC KIDNEY DISEASE')
    else:
        return render_template('ckd.html',pred='You do not have CHRONIC KIDNEY DISEASE')

if __name__ == '__main__':
    app.run(debug=True)