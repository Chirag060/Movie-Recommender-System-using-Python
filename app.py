import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(
            movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie_title):
    # Find the index of the movie from the DataFrame
    index = movies_list[movies_list['title'] == movie_title].index[0]

    # Get the similarity scores for that movie
    movie_new = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_new:
        movie_id = movies_list.iloc[i[0]].movie_id
        # Append the title of each recommended movie
        recommended_movies.append(movies_list.iloc[movie_id].title)
        #fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))


    return recommended_movies


# Load your data
movies_list = pickle.load(open('movie_list.pkl', 'rb'))
movies_list_new = movies_list['title'].values

# Load the similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit App
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Choose a movie:",
    movies_list_new,
)

if st.button("Recommend"):
    recommendations, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")

    with col4:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")

    with col5:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")

    for j in recommendations:
        st.write(j)
