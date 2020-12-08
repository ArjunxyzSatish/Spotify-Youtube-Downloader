#!/usr/bin/python3

import os
import youtube_dl
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.oauth2 as oauth2
from youtube_search import YoutubeSearch
import json
import webbrowser

## YouTube downloader options
ydl_opts = {
    'format': 'bestaudio/best',
     'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        },
            {'key': 'FFmpegMetadata'},
        ],
}

'''
# you'll need this to download songs on spotify
CLIENT_ID = config.SPOTIFY_CLIENT_ID
CLIENT_SECRET = config.SPOTIFY_CLIENT_SECRET
'''

songs = [] # list of songs from spotify playlist
urls = []  # yt links of all the songs from the urls array

# Authorizes and gets the track names from the playlist
def downloadFromPlaylist(Playlist, CID, secret):

### for auth
    credentials = oauth2.SpotifyClientCredentials(
            client_id=CID,
            client_secret=secret)

    token = credentials.get_access_token()
    spotify = spotipy.Spotify(auth=token)

### looks for spotify playlist

    PID = Playlist.rsplit('/', 1)[1]
    items = spotify.playlist_tracks(PID)

### gets the artist name and song name from playlist and adds them to the array 'songs'
    for item in items['items']:
        for artist in item['track']['album']['artists']:
            artistName = artist['name']
        songName = item['track']['name']
        ### added 'lyrics' at the end so it's easier to find the song on yt later
        searchQuery = songName + ' ' + artistName + ' lyrics'
        songs.append(searchQuery)

def UrlFinder(song):
    print('Looking for song: ', song, 'on YouTube')
    results = YoutubeSearch(song, max_results=1).to_json()
    data = json.loads(results)
    for v in data['videos']:
        videoID = v['id']
        baseUrl = 'https://www.youtube.com/watch?v='
        videoURL = baseUrl + videoID
        urls.append(videoURL)


### function that downloads songs from the 'songs' array using the urls in the urls array with youtube-dl
def download_song(song_url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(song_url, download=True)


def downloadFromLinks(urlList):
   for url in urls:
        download_song(url)


print('''
        ##############################################################
        ##################  SPOTIFY DOWNLOADER  ######################
       ---------------------------------------------------------------
          This program lets you download songs from spotify for free
       ---------------------------------------------------------------
        ##################  SPOTIFY DOWNLOADER  ######################
        ##############################################################
Menu:
1. Download songs from a Spotify playlist.
2. Download songs from a YouTube playlist.
3. Download songs from a list of songs.
4. Download a single song.
5. Help
      ''')

choice = input("Enter your choice: ")

if choice == '1':

    if "SPOTIFY_CLIENT_ID" and "SPOTIFY_CLIENT_SECRET" in os.environ:
        print('Found SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET! :D')
        client_ID = os.environ['SPOTIFY_CLIENT_ID']
        client_Secret = os.environ['SPOTIFY_CLIENT_SECRET']
        playlistLink = input("Enter the playlist link: ")
        downloadFromPlaylist(playlistLink, client_ID, client_Secret)
        for song in songs:
            UrlFinder(song)
        downloadFromLinks(urls)

    else:
        print('To download songs from a Spotify playlist, you need your Spotify Client_ID and CLIENT_SECRET.')
        ch = input("Do you have them with you? (y/n): ")
        if ch == 'y' or ch == 'Y' or ch == 'yes':
                client_ID = input("Enter your client ID: ")
                client_Secret = input("Enter your client Secret: ")
                print('''
Note:
Next time, remember to add these as environment variables on your OS so you don't have to enter them each time you want to download a playlist from Spotify. You can find instructions on how to do this on my website or on my Github both of which can be accessed from the 'Help' menu in the main menu :)
                    ''')

                playlistLink = input("Enter the playlist link: ")
                downloadFromPlaylist(playlistLink, client_ID, client_Secret)
                for song in songs:
                    UrlFinder(song)
                downloadFromLinks(urls)

        elif ch == 'n' or ch == 'N' or ch == 'no':
            print('''
You can find the instructions on how to get your Spotify Client_ID and Secret on my website or on my Github. Check it out by selecting the 'Help' option from the menu. It's not at all complicated and won't take more than 10 minutes. :) ''')


elif choice == '2':
    ytPlaylistLink = input("Enter the link of the youtube playlist: ")
    download_song(ytPlaylistLink)

elif choice == '3':
    userlist = input('Enter the name of the file (with the extension): ')
    with open(userlist, 'r') as file:
        listOfSongs = file.readlines()
        for song in listOfSongs:
            UrlFinder(song)
        downloadFromLinks(urls)

elif choice == '4':
    songName = input("Enter the name of the song: ")
    UrlFinder(songName)
    downloadFromLinks(urls)

elif choice == '5':

    spotify = 'http://theothersyde.herokuapp.com'
    github = 'https://github.com/ArjunxyzSatish/SaveThatSong'
    youtube = ''

    print('''
    1. How to get Client ID and Secret from Spotify
    2. Author's Website
    3. Video Tutorial (YouTube)
    ''')


    ch = input("Enter your choice: ")

    if ch == '1':
        webbrowser.open(spotify)
    elif ch == '2':
        webbrowser.open(github)
    elif ch == '3':
        webbrowser.open(youtube)
