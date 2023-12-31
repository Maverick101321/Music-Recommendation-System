import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime
from sklearn.metrics.pairwise import cosine_similarity
from secondcode import music_df

print(music_df)
data = music_df

#Function to calculate the weighted popularity score based on the relesed date of a music
def weighted_popularity_calc(release_date):
    release_date = datetime.strptime(release_date, '%Y-%m-%d')
    #calculating the current date and time
    current_date = datetime.now()
    #calculating the time since the release of the music/track
    time_span = current_date - release_date
    #calculating weight
    weight = 1/(time_span+1)
    return weight

#Normalizing the music features by MinMacScale
scaler = MinMaxScaler()
music_features = music_df[['Danceability', 'Energy', 'Key', 
                           'Loudness', 'Mode', 'Speechiness', 'Acousticness',
                           'Instrumentalness', 'Liveness', 'Valence', 'Tempo']].values
music_features_scaler = scaler.fit_transform(music_features)

#Making a function to get content based recommendations based on music audio features
def content_based_recommendations(input_song_name, num_recommendations = 5):
    if input_song_name not in music_df['Track Name'].values():
        print(f"The song {input_song_name} is not present in the track for analysis")
        return
    #getting the index of the input song in the music_df dataframe
    #input_index = np.where((music_df['Track Name'] == input_song_name))[0]
    input_song_index = music_df[music_df['Track Name'] == input_song_name].index[0]
    #calculating the similarity scores based on the music features
    similarity_scores = cosine_similarity([music_features_scaler[input_song_index]], music_features_scaler)
    #extracting the most similar songs based off the similarity scores
    similar_songs_indices = similarity_scores.argsort()[0][::-1][1, num_recommendations+1]
    #extracting the name, artist and other details of the similar songs 
    content_based_recommendations = music_df.iloc[similar_songs_indices][['Track Name', 'Artists', 'Album Name', 'Release Date', 'Popularity']]
    return content_based_recommendations

#A function to get recommendations using the weighted popularity and combing it with the content based recommendations
#We do this so as to get the recommendations in the form of the latest released songs or tracks 

def hybrid_recommednations(input_song_name, num_recommendations = 5, alpha = 0.5):
    if input_song_name not in music_df['Track Name'].values():
        print(f"the song {input_song_name} is not present in the track for analysis")
        return
    #get the content based recommendation for the imput song
    content_based_rec = content_based_recommendations(input_song_name, num_recommendations)
    #getting the popularity of the input song
    popularity_score = music_df.loc[music_df['Track Name'] == input_song_name, 'Popularity'].values[0]
    weighted_popularity_score = popularity_score * calculated_weighted_popularity(music_df[music_df['Track Name'] == input_song_name, 'Release Date'].values[0])
    #Combining the content based and the popularity based recommendations based on weighted popularity
    hybrid_recommednations = content_based_recommendations
    hybrid_recommednations = hybrid_recommednations.append({
        'Track Name': input_song_name,
        'Artist': music_df.loc[music_df['Track Name'] == input_song_name, 'Artist'].values[0],
        'Album Name': music_df.loc[music_df["Track Name"] == input_song_name, 'Album Name'].values[0],
        'Release Date': music_df.loc[music_df['Track Name'] == input_song_name, 'Release Date'].values[0],
        'Popularity': weighted_popularity_score 
    }, ignore_index = True)
    #Sorting the hybrid recommendation according to the most popular first
    hybrid_recommednations = hybrid_recommednations.sort_values(by='Popularity', ascending=False)
    #Removing the input song from the recommendations
    hybrid_recommednations = hybrid_recommednations[hybrid_recommednations['Track Name'] != input_song_name]
    return hybrid_recommednations

