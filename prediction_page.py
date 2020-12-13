import streamlit as st
from pickle import dump,load
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
def text_preprocess(pre_text):
    letter_only = re.sub("[^a-zA-A]"," ",pre_text)

    letter_only = letter_only.lower()
    words = letter_only.split()

    words = [w for w in words if not w in stopwords.words("english")]

    token = [word_tokenize(word) for word in words]
    token = [''.join(ele) for ele in token]
    clean_text = []
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in token]
    clean_text.append(" ".join(words))
    return (clean_text[0])

def predict(text):
    vectorizer = load(open('pickle/disaster_countvectorizer.pkl', 'rb'))

    classifier = load(open('pickle/disaster_decision_model.pkl', 'rb'))

    clean_text = text_preprocess(text)

    clean_text_vec = vectorizer.transform([clean_text])

    text_input = clean_text_vec.toarray()

    prediction = classifier.predict(text_input)

    return prediction

def main():
    st.title('Identifying Tweets About Real Disasters')

    text = st.text_input('Enter your Message')
    prediction = predict(text)
    # button =
    if st.button('Predict'):
        st.subheader("Prediction:")
        if (prediction == 1):
            # st.image("data/ham.jpg", use_column_width=True)
            st.write("This is a Real Disaster Tweet")
        else:
            # st.image("data/spam.jpg", use_column_width=True)
            st.write("This is Not a Disaster Tweet")

# A man gets stuck in a flash flood triggered by heavy rainfall in Belagavi district.

if(__name__ == '__main__'):
    main()