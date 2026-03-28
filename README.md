# 📧 SMS Spam Detection using Machine Learning

A machine learning-based project that classifies SMS messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP) techniques.

---

```## 📂 Project Structure
├── app.py
├── model.pkl
├── vectorizer.pkl
├── new.csv
├── requirements.txt
├── sms-spams.ipynb
├── spams.ipynb
├── tempCodeRunnerFile.py
└── .ipynb_checkpoints/
```

---

## 🚀 Features

- 📩 Classifies SMS messages into Spam or Ham
- 🧠 Uses NLP for text preprocessing
- 📊 Data cleaning and visualization included
- ⚡ Pre-trained model saved using `.pkl`
- 🔍 Real-time prediction using `app.py`

---

## 🧠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- NLTK
- Scikit-learn

---

## 📊 Dataset

- Contains SMS messages labeled as:
  - `spam` → unwanted messages
  - `ham` → normal messages

- Initial dataset size: **184 rows**
- After cleaning duplicates: **172 rows**

---

## 🔄 Data Preprocessing

- Renamed columns:
  - `Label` → `Result`
  - `Message` → `Input`

- Removed duplicate rows
- Converted labels:
  - `ham → 0`
  - `spam → 1`

- Checked for:
  - Missing values ✅
  - Duplicate values ❌ (removed)

---

##🧹 Text Preprocessing (NLP)
Lowercasing text
Tokenization using NLTK
Removing stopwords

---

##🏗️ Model Building
Text converted into numerical form using vectorization
Model trained using machine learning algorithm
Saved files:
model.pkl → trained model
vectorizer.pkl → text vectorizer

---

##📌 Key Highlights
Clean and structured dataset
Effective NLP preprocessing pipeline
Lightweight and fast model
Easy to deploy and use

---

##🚀 Future Improvements
Improve accuracy with advanced models (LSTM, BERT)
Add web interface using Flask or Streamlit
Use larger dataset for better generalization
Add real-time API support

---

##📚 Learning Outcomes
Natural Language Processing fundamentals
Text preprocessing techniques
Machine learning model building
Data cleaning and visualization
Model deployment basics
