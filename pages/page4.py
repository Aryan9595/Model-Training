import streamlit as st
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Title of the page
st.title("Page 4: Model Testing and Performance Metrics")

# Explanation of what this page does
st.write("""
    This page displays the performance metrics of the model on the test dataset.
    We'll show metrics like accuracy, precision, recall, and F1 score.
    We’ll also visualize the confusion matrix to see how well the model is classifying different classes.
""")

# Example true and predicted values for testing
# You should replace this with your actual model's true and predicted labels
y_true = np.array([0, 1, 0, 1, 1, 0])  # Example true labels
y_pred = np.array([0, 1, 1, 1, 0, 0])  # Example model predictions

# Ensure that y_true and y_pred are of the same length
if len(y_true) != len(y_pred):
    st.error("The length of true labels (y_true) and predicted labels (y_pred) must be the same.")
else:
    # Display classification report
    st.subheader("Classification Report")
    st.text(classification_report(y_true, y_pred))

    # Generate confusion matrix
    cm = confusion_matrix(y_true, y_pred)

    # Check if cm has valid dimensions
    if cm.shape[0] == 2 and cm.shape[1] == 2:
        # Plot confusion matrix
        fig, ax = plt.subplots()
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Class 0', 'Class 1'], yticklabels=['Class 0', 'Class 1'])
        ax.set_xlabel('Predicted')
        ax.set_ylabel('True')
        ax.set_title('Confusion Matrix')
        st.pyplot(fig)
    else:
        st.error("The confusion matrix is not a 2x2 matrix. Check the dimensions of your data.")

