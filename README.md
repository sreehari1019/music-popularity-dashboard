Music Popularity Dashboard 🎵

A project to analyze and visualize Spotify track data, exploring trends in track popularity, duration, and artist statistics. This dashboard provides insights into music trends using SQL and data visualization.

Features

✅ View most popular tracks

✅ Categorize tracks by popularity: Very Popular, Popular, Less Popular

✅ Filter tracks by duration (e.g., greater than 4 minutes)

✅ Compute average popularity and other statistics

✅ Easy-to-read visualizations and tables



Technologies Used
Database: MySQL
Data Analysis: SQL queries
Visualization: Optional Python libraries like Matplotlib/Seaborn or dashboards
Version Control: Git & GitHub


Installation

1. Clone the repository:

git clone https://github.com/<your-username>/music-popularity-dashboard.git


2. Import the spotify_tracks dataset into MySQL.

3. Run SQL queries to analyze the data.

4. (Optional) Connect with Python for visualizations.



Usage

Analyze top tracks by popularity:
SELECT track_name, artist, popularity
FROM spotify_tracks
ORDER BY popularity DESC
LIMIT 10;


Find tracks longer than 4 minutes:
SELECT track_name, artist, duration_ms
FROM spotify_tracks
WHERE duration_ms > 240000;


Categorize tracks by popularity range:
SELECT CASE 
         WHEN popularity >= 80 THEN 'Very Popular'
         WHEN popularity >= 50 THEN 'Popular'
         ELSE 'Less Popular'
       END AS popularity_range,
       COUNT(*) AS track_count
FROM spotify_tracks
GROUP BY popularity_range;

License
This project is licensed under the MIT License.
