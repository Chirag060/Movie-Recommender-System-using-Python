# Movie Recommender System

## Introduction

This project is a movie recommender system that suggests movies based on their similarity to a given movie. The system leverages Natural Language Processing (NLP) techniques and machine learning algorithms to identify and recommend movies with similar content, cast, genres, and keywords. This is achieved by analyzing the metadata of movies and calculating the cosine similarity between them.

## Dataset

The dataset used in this project is derived from the TMDB (The Movie Database) 5000 movie dataset. The data includes various features such as `movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, and `crew`. These features are used to create a comprehensive profile for each movie, which is then used to calculate similarities between movies.

## Preprocessing and Feature Engineering

To build an effective recommendation system, the following preprocessing steps were performed:

- **Merging Datasets**: The movie metadata and credits datasets were merged on the title field to create a unified dataset containing all relevant information.

- **Feature Selection**: Only the most relevant features (`movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, `crew`) were retained to reduce noise and enhance the quality of the recommendations.

- **Handling Missing Data**: Null values were identified and removed from the dataset to ensure the accuracy of the model.

- **Textual Data Processing**:
  - **Genres, Keywords, Cast, and Crew**: These features were extracted and converted into lists of relevant terms. For instance, the genres column was parsed to extract genres such as "Action", "Drama", etc.
  - **Overview**: The movie overview (a brief description) was tokenized and converted into a list of words.
  - **Removing Spaces**: Spaces within the words were removed to treat phrases like "science fiction" as a single term rather than two separate terms.
  - **Stemming**: Words were stemmed to their root form to normalize the data and improve the matching process.
  - **Tag Creation**: A new `tags` feature was created by concatenating all the textual information (overview, genres, keywords, cast, crew) into a single string for each movie. This consolidated feature was used to calculate similarity.

## Model and Similarity Calculation

- **Vectorization**: The consolidated `tags` feature was vectorized using the `CountVectorizer`, which converts the text into a matrix of token counts. This approach helps in transforming the textual data into a format suitable for similarity calculations.

- **Cosine Similarity**: The similarity between movies was calculated using cosine similarity, which measures the cosine of the angle between two vectors in a multi-dimensional space. A smaller angle indicates higher similarity. The output is a similarity matrix where each entry `[i, j]` represents the similarity between movie `i` and movie `j`.

## Recommendations

To recommend movies, the system identifies the most similar movies based on the cosine similarity scores. Given a movie title, the system retrieves its index and sorts the similarity scores in descending order to recommend the top 5 most similar movies.

## Web App Development

The web application for the recommender system was developed using **Streamlit**, a popular framework for creating interactive web apps in Python. The Streamlit app provides a user-friendly interface that allows users to interact with the movie recommender system easily.

### Key Features of the Streamlit App

- **Interactive User Input**: 
  - Users can input the title of a movie into a text field. This input is used to query the recommender system to find and process the movie's data.
  - The app includes a search box where users can type in the name of the movie they are interested in.

- **Real-Time Recommendations**:
  - Once a movie title is entered, the app quickly retrieves and processes the data to generate recommendations.
  - The app displays the top 5 movies that are most similar to the entered movie based on the similarity scores.

- **User-Friendly Display**:
  - Recommendations are shown in a clean and organized format, including the movie titles and relevant details such as genre or overview.
  - The interface is designed to be intuitive, with clear prompts and an aesthetically pleasing layout.

### Implementation Details

- **Streamlit Integration**: 
  - The Streamlit application code is located in `app/app.py`. This script sets up the Streamlit server, handles user interactions, and displays the recommendation results.
  - It utilizes Streamlit's interactive components like text input fields and buttons to make the app engaging and easy to use.

- **Connection with Recommendation System**:
  - The app integrates with the recommendation engine, which is implemented in the `src/` directory. The app sends user input to the recommendation system, processes the data, and retrieves the results.
  - The recommendation system logic is invoked to fetch similar movies based on the user's input, and the results are passed back to the Streamlit app for display.

- **Deployment**:
  - The app is designed to be deployed on a local server for development purposes. However, it can also be deployed to a cloud platform or a web hosting service for broader accessibility.

## Conclusions

This movie recommender system effectively demonstrates how metadata and textual analysis can be used to find similarities between movies and provide meaningful recommendations. By focusing on key features such as genres, keywords, and cast, the system is able to capture the essence of a movie and suggest others with similar characteristics.

## Future Work

Several enhancements can be made to improve the accuracy and relevance of the recommendations:

- **Incorporating User Ratings**: Integrating user ratings and preferences could personalize recommendations, making them more relevant to individual users.

- **Advanced NLP Techniques**: Using more sophisticated NLP techniques like TF-IDF or word embeddings could improve the quality of text processing and similarity calculations.

- **Hybrid Recommendation Systems**: Combining content-based filtering (as implemented in this project) with collaborative filtering could yield more robust recommendations by considering both movie metadata and user behavior.

- **Real-Time Data Updates**: Implementing a system that continuously updates with new movie data and user interactions could keep the recommendations up-to-date and more relevant.

- **Exploring Other Similarity Metrics**: Experimenting with other similarity metrics, such as Pearson correlation, could provide insights into different aspects of movie similarity.

