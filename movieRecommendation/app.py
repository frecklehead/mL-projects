import streamlit as st
st.header("Movie Recommender System")
st.write("This is a movie recommender system that uses the content-based filtering technique to recommend movies")
import pickle
movies=pickle.load(open('movies.pkl','rb'))
st.selectbox('Select Movies From the Dropdown',movies)
if st.button("Show Recommendations"):
  pass
