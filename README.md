
# New York Collisions and Crashes Analysis  

## Overview  
This project aims to analyze and predict traffic collisions and crashes in New York City using machine learning models. The goal is to identify patterns and contributing factors to improve road safety. The project includes a web application that allows users to input data and receive predictions about pedestrian injuries and weekend incidents.  

## Project Structure  
```
├── models/                       # Contains the machine learning models and encoders as pickle files  
├── pedestriansec/                # Contains the Python virtual environment  
├── static/                       # Stores static files like CSS and images  
├── templates/                    # Contains HTML templates for the web application  
├── app.py                        # The main Flask application script  
├── requirements.txt              # Required dependencies  
└── README.md                     # Project documentation  
```

## Prerequisites  
To run this project, ensure you have the following installed on your machine:  
- Python 3  
- Flask  
- pip  

## Setting Up the Environment  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/yourusername/new-york-collisions-analysis.git && cd new-york-collisions-analysis  
   ```

2. Create a virtual environment:  
   ```bash  
   # For macOS/Linux  
   python3 -m venv pedestriansec && source pedestriansec/bin/activate  
   
   # For Windows  
   pedestriansec\Scripts\activate  
   ```

3. Install the required packages:  
   ```bash  
   pip install -r requirements.txt  
   ```

## Running the Application  
Start the Flask application:  
```bash  
python app.py  
```
Access the web application by opening your browser and navigating to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).  

## Using the Application  
The application provides a web interface for analyzing and predicting New York collisions and crashes. You can access different forms and visualizations from the main page.

### Pedestrian Safety Analysis  
- **Route**: `/pedestrian`  
- **Form Fields**:  
  - Borough  
  - Number of Cyclist Injured  
  - Number of Motorist Injured  
  - Contributing Factor Vehicle 1  
  - Vehicle Type Code 1  
  - Weekend  
- **Prediction Result**: Displays the likelihood of a pedestrian injury based on the input data.

### Weekend Incident Analysis  
- **Route**: `/weekend`  
- **Form Fields**:  
  - Borough  
  - Number of Pedestrians Killed  
  - Number of Cyclists Injured  
  - Number of Motorists Injured  
  - Contributing Factor Vehicle 1  
  - Vehicle Type Code 1  
  - Number of Persons Killed  
  - Number of Pedestrians Injured  
- **Prediction Result**: Displays the likelihood of an incident occurring over the weekend based on the input data.

## Models and Encoders  
The application uses several pre-trained models and encoders:  
- `model.pkl`: The main prediction model for pedestrian safety  
- `model_weekend.pkl`: The model for predicting weekend incidents  
- `BOROUGH_encoder.pkl`: Encoder for the borough feature  
- `CONTRIBUTINGFACTORVEHICLE1_encoder.pkl`: Encoder for vehicle contributing factors  
- `ONSTREETNAME_encoder.pkl`: Encoder for street names  
- `VEHICLETYPECODE1_encoder.pkl`: Encoder for vehicle types  

## Visualizations  
The visualizations section provides graphical insights into the data, including:  
- Distribution of incidents across boroughs  
- Contributing factors to incidents  
- Trends over time  
- Comparisons of incidents between different times of the week  

## Extending the Project  
The current model can be extended by incorporating more granular temporal data, weather conditions, and traffic flow patterns. Implementing real-time data feeds and deploying the model into a mobile application are also potential future enhancements.  

## References  
- [StatQuest with Josh Starmer (YouTube Video): "Random Forests Part 1 Building, Using and Evaluating"](https://www.youtube.com/watch?v=J4v2vS6n7tI)  
- [StatQuest with Josh Starmer (YouTube Video): "Naive Bayes, Clearly Explained!!!"](https://www.youtube.com/watch?v=O2D3x8oV2uM)  
- [DataCamp: "Supervised Learning with scikit-learn"](https://www.datacamp.com/courses/supervised-learning-with-scikit-learn)  
- [StatQuest with Josh Starmer (YouTube Video): "Decision Trees"](https://www.youtube.com/watch?v=7VeUPuFGJ8I)  

## Report  
For a detailed report on the project, please visit [Report Link](./Report.pdf).  
