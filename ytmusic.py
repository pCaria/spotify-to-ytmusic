from ytmusicapi import YTMusic
from ytmusicapi.auth.oauth import OAuthCredentials
import json
import time
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente.
load_dotenv()

DATA_FILE = "liked_songs.json"

# Carrega a lista de músicas do JSON.
def load_spotify_songs():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Erro ao carregar o JSON. Verifique se o arquivo existe.")
        return []

# Autenticação no YT Music.
def authenticate_ytmusic():
    return YTMusic('oauth.json', oauth_credentials = OAuthCredentials(
        client_id = os.getenv('YT_CLIENT_ID'),
        client_secret= os.getenv('YT_CLIENT_SECRET')
        ))


# Função checa se a playlist já foi criada pra evitar duplicidade.
def check_playlist_exists(ytmusic, title):
    playlists = ytmusic.get_library_playlists()
    for playlist in playlists:
        if playlist['title'] == title:
            print(f"Playlist '{title}' já existe.")
            return playlist
    return None

# Cria a playlist caso ela não exista.
def create_playlist(ytmusic, title, description):
    try:
        playlist_id = ytmusic.create_playlist(title, description, privacy_status="UNLISTED")
        print(f"Playlist criada com sucesso: {title}")
        return playlist_id
    except Exception as e:
        print(f"Erro ao criar a playlist: {e}")
        return None
    
# Função para adicionar músicas a uma playlist
def add_songs_to_playlist(ytmusic, playlist_Id, yt_song_id):
    try:
        ytmusic.add_playlist_items(playlist_Id, [yt_song_id], duplicates=False)
        print(f"Músicas adicionadas à playlist com ID {playlist_Id} com sucesso!")
    except Exception as e:
        print(f"Erro ao adicionar músicas à playlist: {e}")
    
def add_liked_ytmusic(ytmusic):

    spotify_songs = load_spotify_songs()[::-1]

    if not spotify_songs:
        print("Nenhuma música encontrada no JSON.")
        return

    playlist_title = "Músicas Curtidas Spotify"
    playlist_desc = "Músicas curtidas do Spotify transferidas para o Youtube Music"
    playlist = check_playlist_exists(playlist_title)

    if not playlist:
        playlist = create_playlist(playlist_title, playlist_desc)

    if playlist:
        playlist_Id = playlist

        liked_songs_yt = ytmusic.get_playlist(playlist_Id)
        liked_titles_yt = {song["title"] + song["artists"][0]["name"] for song in liked_songs_yt["tracks"]}

        for song in spotify_songs:
            search_query = f"{song['name']} {song['artist']}"

            search_results = ytmusic.search(search_query, filter="songs")

            if search_results:
                yt_song = search_results[0]
                yt_song_id = yt_song["videoId"]
                yt_song_title = yt_song["title"]
                yt_song_artist = yt_song["artists"][0]["name"]

                song_key = yt_song_title + yt_song_artist

                if song_key not in liked_titles_yt:
                    add_songs_to_playlist(playlist_Id, yt_song_id)
                    print(f"👍 Adicionada: {yt_song_title} - {yt_song_artist}")
                    time.sleep(0.2)
                else:
                    print(f"🔁 Já curtida: {yt_song_title} - {yt_song_artist}")

            else:
                print(f"❌ Não encontrada: {search_query}")