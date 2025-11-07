# SMS Spam Detection

SMS Spam Detection is a Python-based Machine Learning project that classifies SMS messages as **Spam** or **Ham (Not Spam)** using **TF-IDF vectorization** and a **Naive Bayes classifier**.  
It provides a simple web interface built with **Streamlit** for real-time message classification.

---

## Features
- End-to-end text classification pipeline  
- TF-IDF vectorization for feature extraction  
- Multinomial Naive Bayes model for spam detection  
- Streamlit web app for live predictions  
- Clean and reproducible Jupyter notebook for training and evaluation  

---

## Installation

### Requirements
- Python 3.8 or higher  
- Pip (Python package manager)  

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/JatinPurushwani/Spam-Detection.git
   cd spam-detection

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   # or
   source venv/bin/activate   # macOS/Linux

3. Install depenedencies:
   ```bash
   pip install -r requirements.txt

---

## Usage

1. Run Jupyter Notebook (for training and analysis)
   ```bash
   jupyter notebook
Open the notebook notebooks/Spam_Detection.ipynb to view the code, visualizations, and model training workflow.

2. Run Streamlit Web App
   ```bash
   streamlit run app.py
This will launch a local web interface in your browser where you can enter any SMS message and get instant predictions:
>     Spam → if the message is classified as spam.
>     Ham → if the message is safe / non-spam

Example:
- Input:  "Congratulations! You have won a $1000 gift card!"
- Output:  Spam
