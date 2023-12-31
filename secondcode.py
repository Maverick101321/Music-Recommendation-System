import pandas as pd
import spotipy 
from spotipy.oauth2 import SpotifyOAuth

def get_trending_playlist_data(playlist_id, access_token):
    sp = spotipy.Spotify(auth=access_token)
    playlist_tracks = sp.playlist_tracks(playlist_id, fields='items(track(id, name, artists, album(id, name)))')
    music_data = []
    # Get the playlist details to find out how many tracks are in it
    for track_info in playlist_tracks['items']:
        track = track_info['track']
        track_name = track['name']
        artists = ', '.join([artist['name'] for artist in track['artists']])
        album_name = track['album']['name']
        album_id = track['album']['id']
        track_id = track['id']

        #Getting audio features of the track
        audio_features = sp.audio_features(track_id)[0] if track_id != 'Not Available' else None

        #Getting release date of the album
        try:
            album_info = sp.album[album_id] if album_id != 'Not Available' else None
            release_date = sp.album_info[release_date] if album_info != 'Not Available' else None
        except:
            release_date = None

        #Getting the popularity of the track
        try:
            track_info = sp.track[track_id] if track_id != 'Not Available' else None
            popularity = track_info[popularity] if track_info != 'Not Available' else None
        except:
            popularity = None
        
        #Creating a dictionary named track_data
        track_data = {
            'Track Name' : track_name,
            'Artists' : artists,
            'Album Name': album_name,
            'Album ID': album_id,
            'Track ID': track_id,
            'Release Date' : release_date,
            'Popularity' : popularity,
            'Duration(ms)': audio_features['duration_ms'] if audio_features else None,
            'Explicit': track_info.get('explicit', None),
            'External URLs': track_info.get('external_urls', {}).get('spotify', None),
            'Danceability': audio_features['danceability'] if audio_features else None,
            'Energy': audio_features['energy'] if audio_features else None,
            'Key': audio_features['key'] if audio_features else None,
            'Loudness': audio_features['loudness'] if audio_features else None,
            'Mode': audio_features['mode'] if audio_features else None,
            'Speechiness': audio_features['speechiness'] if audio_features else None,
            'Acousticness': audio_features['acousticness'] if audio_features else None,
            'Instrumentalness': audio_features['instrumentalness'] if audio_features else None,
            'Liveness': audio_features['liveness'] if audio_features else None,
            'Valence': audio_features['valence'] if audio_features else None,
            'Tempo': audio_features['tempo'] if audio_features else None,
        }

        music_data.append(track_data)

    df = pd.DataFrame(music_data)
    return df

playlist_id = '37i9dQZF1DX76Wlfdnj7AP'
#playlist_id = int(input("Enter your playlist id - "))
access_token = 'BQD_f6geaEmFTP-mx4jJ6h66z7QC1-L-ZJSXXcgqxrRDs4J4Bc_95P7LREX8AE4x5UAzfA-m41Se4OfqWlMbqsk6swe_Cq54wC7325HTkd5qcRvKhh4'
music_df = get_trending_playlist_data(playlist_id, access_token)
print(music_df)
print(music_df.isnull().sum())
