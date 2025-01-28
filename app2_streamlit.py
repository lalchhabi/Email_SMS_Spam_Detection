import streamlit as st
import pickle as pkl
from text_preprocess import text_preprocessing

#### Load the Vectorizer and the Model.
vectorizer = pkl.load(open("vectorizer.pkl","rb"))
model = pkl.load(open("model.pkl","rb"))

### Now Create a Widget for a app
st.title("Welcome to the SMS Spam Classifier")
input_message = st.text_area("Enter the Message Here")

#### Predict the result only if I have pressed the button
if st.button("Predict"):
    #### To run the application we have three process:-

    ### 1) Text Preprocessing
    preprocess_result = text_preprocessing(input_message)

    ### 2) Text Vectorization

    vectorize_result = vectorizer.transform([preprocess_result])

    #### 3) Predict the Result

    result = model.predict(vectorize_result)[0]

    #### 4) Convert the binary digit results to the text like spam and not spam to display the result
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
