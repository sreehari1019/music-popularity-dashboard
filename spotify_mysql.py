import re
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

# Set up Spotify API credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='6cd9d19380e641bea39a622a31fe2026',  # Replace with your Client ID
    client_secret='bf953334d433495dad488e6547f6bcf7'  # Replace with your Client Secret
))

# MySQL Database Connection
db_config = {
    'host': 'localhost',           
    'user': '*****',       
    'password': '*******',   
    'database': 'spotify'       
}

 
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()


track_url = "https://open.spotify.com/track/3n3Ppam7vgaVa1iaRUc9Lp"


track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)


track = sp.track(track_id)


track_data = {
    'Track Name': track['name'],
    'Artist': track['artists'][0]['name'],
    'Album': track['album']['name'],
    'Popularity': track['popularity'],
    'Duration (minutes)': track['duration_ms'] / 60000
}


insert_query = """
INSERT INTO spotify_tracks (track_name, artist, album, popularity, duration_minutes)
VALUES (%s, %s, %s, %s, %s)
"""
cursor.execute(insert_query, (
    track_data['Track Name'],
    track_data['Artist'],
    track_data['Album'],
    track_data['Popularity'],
    track_data['Duration (minutes)']
))
connection.commit()

print(f"Track '{track_data['Track Name']}' by {track_data['Artist']} inserted into the database.")


cursor.close()
connection.close()


