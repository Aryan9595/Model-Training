import streamlit as st
from pages import page1, page2, page3, page4

PAGES = {
    "Model Training": page1,
    "Explainability": page2,
    "Live Predictions": page3,
    "SHAP Values": page4,
}

def app():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))  # Sidebar navigation
    page = PAGES[selection]  # Get the selected page
    page.display()  # Display the selected page

if __name__ == "__main__":
    app()
