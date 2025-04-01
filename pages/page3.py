import streamlit as st

def display():
    st.title("Live Predictions")
    st.write("This is the live prediction page where you can make predictions using the trained model.")
    
    # Add user input here for making live predictions
    user_input = st.text_input("Enter your input data:")
    
    if st.button('Predict'):
        st.write(f"Making prediction for the input: {user_input}")
        # Here you would use your trained model to make a prediction
        st.write("Prediction result: 0.85 (dummy value)")  # Replace with actual prediction logic
