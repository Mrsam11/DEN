# Heart Disease Prediction

This project implements a heart disease prediction model using machine learning techniques, specifically a Random Forest Classifier. The model predicts the presence of heart disease based on various health-related features. A user-friendly web application is built using Streamlit, allowing users to input their data and receive predictions.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Contributing](#contributing)
- [License](#license)

## Features

- Input fields for various health metrics.
- Prediction of heart disease presence (Yes/No).
- Display of prediction probabilities for both outcomes.
- User-friendly interface powered by Streamlit.

## Technologies Used

- Python
- scikit-learn (for machine learning)
- Streamlit (for web interface)
- Pandas (for data manipulation)
- NumPy (for numerical operations)
- Joblib (for model serialization)

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Mrsam11/DEN/tree/09c4ef0ce4b3565c2cf7c318e34c8f82c575ea2e/Heart%20Disease
   cd heart-disease-prediction

2. Install the required packages:
   ```bash
   pip install -r requirements.txt

4. Usage:
   To run the Streamlit application, use the following command:
   ```bash
   py -m streamlit run app.py

This will open a new tab in your web browser where you can input the relevant health metrics to get predictions.

# Model Training
The model is trained using historical data containing various health features and corresponding outcomes for heart disease. 

The training process involves:
  1. Data preprocessing and feature selection.
  2. Splitting the dataset into training and testing sets.
  3. Training the Random Forest Classifier.
  4. Saving the trained model using Joblib.
# Contributing
Contributions are welcome! If you have suggestions for improvements or want to add features, please create a new issue or submit a pull request.
