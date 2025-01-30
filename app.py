# import nltk
# nltk.download('punkt')
# nltk.download('punkt_tab')
# nltk.download('stopwords')

# import streamlit as st
# import pickle
# import string
# from nltk.corpus import stopwords
# from nltk.stem.porter import PorterStemmer

# ps=PorterStemmer()

# def transform_text(text):
#     text=text.lower()
#     text=nltk.word_tokenize(text)

#     y=[]
#     for i in text:
#         if i.isalnum():
#             y.append(i)

#     text=y[:]
#     y.clear()

#     for i in text:
#         y.append (ps.stem(i))

#     return " ". join (y)
# tk = pickle.load(open("vectorizer.pkl", 'rb'))
# model = pickle.load(open("model.pkl", 'rb'))

# st.title ("SMS Spam Detection Model")

# input_sms = st.text_input ("Enter the SMS")

# if st.button('Predict') :
#     # 1. preprocess
#     transformed_sms = transform_text (input_sms)
#     # 2. vectorize
#     vector_input=tk.transform([transformed_sms])
#     # 3.predict
#     result=model.predict(vector_input)[0]
#     # 4.Display
#     if result==1:
#         st.header('Spam')
#     else:
#         st.header(' Not Spam')






# "C:\Program Files\Python312\python.exe" -m streamlit run app.py      

import streamlit as st
import pickle

model = pickle.load(open("model.pkl", 'rb'))
cv = pickle.load(open("vectorizer.pkl", 'rb'))

def main() :
    st.title("Email Spam Classification Application")
    st. write("This is a Machine Learning application to classify emails as spam or ham. ")
    st. subheader("Classification")
    user_input=st. text_area("Enter an email to classify" , height=150)
    if st. button( "Classify") :
        if user_input:
            data=[user_input]
            print (data)
            vec=cv. transform(data) . toarray()
            result=model.predict(vec)
            if result[0] == 0:
                st. success ("This is Not A Spam Email")
            else:
                st.error ("This is A Spam Email")
    else:
        st.write("Please enter an email to classify.")
main()