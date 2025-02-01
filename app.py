from flask import Flask, request, render_template, send_from_directory
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
model_path = 'models/model.pkl'
weekend_model_path = 'models/model_weekend.pkl'
encoders_path = 'models/'


with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

with open(weekend_model_path, 'rb') as model_file1:
    weekend_model = pickle.load(model_file1)

# Load the encoders
encoders = {}
categorical_columns = ['BOROUGH', 'CONTRIBUTING FACTOR VEHICLE 1', 'VEHICLE TYPE CODE 1']
for col in categorical_columns:
    with open(f'{encoders_path}{col}_encoder.pkl', 'rb') as encoder_file:
        encoders[col] = pickle.load(encoder_file)

# Load the encoders
encoders1 = {}
categorical_columns1 = ['BOROUGH', 'CONTRIBUTING FACTOR VEHICLE 1', 'VEHICLE TYPE CODE 1']
for col in categorical_columns1:
    with open(f'{encoders_path}{col}_encoder.pkl', 'rb') as encoder_file1:
        encoders1[col] = pickle.load(encoder_file1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pedestrian')
def pedestrian():
    
    return render_template('pedestrian.html')

@app.route('/weekend')
def weekend():
    
    return render_template('weekend.html')


@app.route('/predict_pedestrian', methods=['POST'])
def predict_pedestrian():
   
    input_data = {col: request.form.get(col) for col in categorical_columns}
    cyclist_injured = request.form.get('cyclistInjured')
    motorist_injured = request.form.get('motoristInjured')
    weekend = request.form.get('weekend')
    encoded_data = []
    for col, value in input_data.items():
        if col in encoders:
            try:
                encoded_value = encoders[col].transform([value])
                encoded_data.extend(encoded_value)
            except ValueError:
        
                encoded_data.extend(encoders[col].transform(['Other'])) 
        else:
            encoded_data.append(value)

    
    encoded_data.append(int(cyclist_injured))
    encoded_data.append(int(motorist_injured))
    encoded_data.append(int(weekend))
    encoded_array = np.array(encoded_data).reshape(1, -1)
    print("Encoded data for prediction:", encoded_array)

    try:
        prediction = model.predict(encoded_array)
        print("Prediction:", prediction)
    except Exception as e:
        print(f"Error during prediction: {e}")
        return render_template('pedestrian.html', error="An error occurred during prediction.")

    return render_template('pedestrian.html', prediction=prediction[0])


@app.route('/predict_weekend', methods=['POST'])
def predict_weekend():
    input_data = {col: request.form.get(col) for col in categorical_columns}
    persons_killed = request.form.get('PERSONS_KILLED')
    pedestrians_killed = request.form.get('PEDESTRIANS_KILLED')
    pedestrians_injured = request.form.get('PEDESTRIANS_INJURED') 
    motorist_injured = request.form.get('MOTORIST_INJURED') 
    cyclist_injured = request.form.get('CYCLIST_INJURED') 

    encoded_data = []
    for col, value in input_data.items():
        if col in encoders1:
            try:
                encoded_value = encoders1[col].transform([value])
                encoded_data.extend(encoded_value)
            except ValueError:
        
                encoded_data.extend(encoders1[col].transform(['Other'])) 
        else:
            encoded_data.append(value)

    encoded_data.append(int(persons_killed))
    encoded_data.append(int(pedestrians_killed))
    encoded_data.append(int(pedestrians_injured))
    encoded_data.append(int(motorist_injured))
    encoded_data.append(int(cyclist_injured))

    encoded_array = np.array(encoded_data).reshape(1, -1)
    print("Encoded data for prediction:", encoded_array)
    try:
        prediction = weekend_model.predict(encoded_array)
        print("Prediction:", prediction)
    except Exception as e:
        print(f"Error during prediction: {e}")
        return render_template('weekend.html', error="An error occurred during prediction.")

    return render_template('weekend.html', prediction=prediction[0])




@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(encoders_path, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
