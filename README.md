# Spotify Music Recommendations Project

## Introduction
#### This repository hosts a Python script developed by a college student to harness the power of the Spotify API. The script goes beyond simple playlist retrieval; it analyzes trending playlists and provides comprehensive music recommendations based on both content features and popularity scores. 
#### The project is intended to showcase the student's programming skills and understanding of data manipulation, API integration, and recommendation algorithms. The code is structured into distinct parts, each serving a specific function.

## Overview
### Prerequisites
#### Before diving into the code, it's crucial to ensure that your local environment is set up correctly. The script relies on several Python packages, including requests, base64, pandas, numpy, scikit-learn, and datetime. Make sure these packages are installed using pip install <package-name>.
### Setup
#### To run the script, you'll need to obtain Spotify API credentials. This involves creating a Spotify Developer account, generating a new application, and replacing placeholder values in the script with your unique Client ID and Client Secret.

## Understanding The Code
### First Part - Initializing Spotify API Credentials
#### In this section, the script sets up the groundwork for interacting with the Spotify API. It initializes the Spotify API credentials, comprised of the Client ID and Client Secret. The script then base64 encodes these credentials, constructs the necessary headers, and sends a request to Spotify to obtain an access token.

### Second Part - Retrieving Playlist Data
#### The second part focuses on interacting with Spotify's Spotipy library to fetch playlist details. It imports the required libraries and defines a function to retrieve information about tracks within a specified playlist. The retrieved data is organized into a Pandas DataFrame for further analysis.

### Third Part - Calculating Weighted Popularity and Normalizing Features
#### This section introduces additional functionalities. It imports necessary libraries, defines functions to calculate weighted popularity scores, and normalizes music features using MinMaxScaler. The script also incorporates cosine similarity to compute the likeness between tracks based on audio features.

### Final Part - Hybrid Recommendations
#### The final part combines the earlier components to provide a holistic music recommendation system. It imports the previously defined functions and demonstrates how to use them. An example showcases obtaining hybrid recommendations based on both content features and popularity scores for a specified input song.

## Running the Script
### To run the script:

#### 1. Ensure Python and the required packages are installed.
#### 2. Set up Spotify API credentials.
#### 3. Replace placeholder values in the script with your credentials.
#### 4. Execute the code in sequence: First Part, Second Part, Third Part, and Final Part.
#### 5. Upon completion, you'll have access to Spotify access tokens, trending playlist data, and personalized music recommendations. Feel free to explore and customize the code based on your preferences and additional functionalities. This project serves as a testament to the student's programming capabilities and creativity in leveraging APIs for real-world applications.
