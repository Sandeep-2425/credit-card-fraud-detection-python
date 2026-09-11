import numpy as np
from flask import Flask, request, render_template
import pickle


app = Flask(__name__)

model = pickle.load(open('models/model.pkl', 'rb'))
amount_scaler = pickle.load(open('models/amount.pkl', 'rb'))
time_scaler = pickle.load(open('models/time.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    feature_names = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'Amount']
    form_features = [float(request.form[name]) for name in feature_names]
    
    time_val = np.array(form_features[0]).reshape(-1, 1)
    amount_val = np.array(form_features[6]).reshape(-1, 1)

    scaled_time = time_scaler.transform(time_val)
    scaled_amount = amount_scaler.transform(amount_val)
    

    final_features = [
        scaled_time[0][0],
        form_features[1],  
        form_features[2],  
        form_features[3],  
        form_features[4],  
        form_features[5],  
        scaled_amount[0][0]
    ]
    
    final_features_array = [np.array(final_features)]

    prediction = model.predict(final_features_array)
    prediction_proba = model.predict_proba(final_features_array)

    if prediction[0] == 1:
        result_text = f"Warning: This transaction is likely FRAUDULENT ({prediction_proba[0][1]*100:.2f}% confidence)."
    else:
        result_text = f"This transaction is likely LEGITIMATE ({prediction_proba[0][0]*100:.2f}% confidence)."

    return render_template('index.html', prediction_text=result_text)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
    