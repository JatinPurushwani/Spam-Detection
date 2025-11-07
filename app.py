import streamlit as st
import joblib

# Load the trained pipeline
pipeline = joblib.load('models/spam_pipeline.pkl')

# Streamlit App UI
st.set_page_config(page_title="SMS Spam Detection", page_icon="📩", layout="centered")
st.title("SMS Spam Detection App")
st.write("Enter an SMS message below to classify it as **Spam** or **Ham (Not Spam)**.")

# Text input
message = st.text_area("Message", placeholder="Type or paste a message here...")

# Predict button
if st.button("Predict"):
    if not message.strip():
        st.warning("Please enter a message before predicting.")
    else:
        prediction = pipeline.predict([message])[0]
        if prediction == "spam":
            st.error("🚨 This message is classified as **SPAM**.")
        else:
            st.success("✅ This message is classified as **HAM (Not Spam)**.")
