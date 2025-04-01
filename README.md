# Model Training App

This is a Streamlit-based web application that demonstrates the process of model training, explanation, and prediction using various machine learning models.

## Features:
- **Model Training**: Train a machine learning model using the Iris dataset (or another dataset of your choice).
- **Explainability**: Explain the predictions of the model using SHAP (SHapley Additive exPlanations) values.
- **Live Predictions**: Input data and get live predictions from the trained model.

## Requirements
- Python 3.x
- Streamlit
- scikit-learn
- pandas
- shap
- numpy

## Installation Instructions:
1. Clone this repository:
   ```bash
   git clone https://github.com/Aryan9595/Model-Training.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## How to Use:
- Open the web app in your browser.
- Navigate through the "Model Training", "Explainability", and "Live Predictions" sections using the sidebar.
- Train a model, view its explanations, and make live predictions based on your input.

## Contributing:
Contributions are welcome! Please fork the repo, create a new branch, and submit a pull request for any changes.
