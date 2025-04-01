import streamlit as st

def display():
    st.title("Model Training")
    st.write("This is the model training page where you can train a model.")
    
    # Add your model training logic here (e.g., user input for training data, model selection, etc.)
    st.write("Here you will train your machine learning model using your dataset.")
    
    # Add some dummy code for now:
    if st.button('Train Model'):
        st.write("Model training started...")

