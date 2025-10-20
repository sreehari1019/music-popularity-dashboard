from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import re


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='6cd9d19380e641bea39a622a31fe2026',  
    client_secret='bf953334d433495dad488e6547f6bcf7'  
))


track_url = "https://open.spotify.com/track/3n3Ppam7vgaVa1iaRUc9Lp"

track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)


track = sp.track(track_id)
print(track)

track_data = {
    'Track Name': track['name'],
    'Artist': track['artists'][0]['name'],
    'Album': track['album']['name'],
    'Popularity': track['popularity'],
    'Duration (minutes)': track['duration_ms'] / 60000
}


print(f"\nTrack Name: {track_data['Track Name']}")
print(f"Artist: {track_data['Artist']}")
print(f"Album: {track_data['Album']}")
print(f"Popularity: {track_data['Popularity']}")
print(f"Duration: {track_data['Duration (minutes)']:.2f} minutes")

df = pd.DataFrame([track_data])
print("\nTrack Data as DataFrame:")
print(df)


df.to_csv('spotify_track_data.csv', index=False)

features = ['Popularity', 'Duration (minutes)']
values = [track_data['Popularity'], track_data['Duration (minutes)']]

plt.figure(figsize=(8, 5))
plt.bar(features, values, color='skyblue', edgecolor='black')
plt.title(f"Track Metadata for '{track_data['Track Name']}'")
plt.ylabel('Value')
plt.show()