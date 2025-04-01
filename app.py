import streamlit as st

# Sidebar for navigation
st.sidebar.title("Model Explainer App")
page = st.sidebar.radio("Choose a page", ["Page 1", "Page 2", "Page 3", "Page 4"])

# Page rendering based on the selected option
if page == "Page 1":
    import pages.page1
elif page == "Page 2":
    import pages.page2
elif page == "Page 3":
    import pages.page3
elif page == "Page 4":
    import pages.page4
