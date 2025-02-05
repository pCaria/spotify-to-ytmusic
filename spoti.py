import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from dotenv import load_dotenv
import os

load_dotenv()

# Configurações de autenticação
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

# Inicializa a autenticação
def authenticate_spotify():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope="user-library-read"
    ))

DATA_FILE = "liked_songs.json"

# Carrega as músicas salvas no arquivo JSON.
def load_existing_songs():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                data = file.read().strip()
                return json.loads(data) if data else []
        except json.JSONDecodeError:
            print("Erro ao carregar JSON.")
            return[]
        return []

# Salva a lista de músicas no arquivo JSON.
def save_songs(songs):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(songs, file, indent=4, ensure_ascii=False)


# Função para obter músicas curtidas
def get_liked_songs(sp):
    existing_songs = load_existing_songs()
    # conjunto para facilitar verificação de duplicatas. cria uma key para as músicas já no JSON.
    existing_titles = {song["name"] + song["artist"] for song in existing_songs}

    all_songs = []
    results = sp.current_user_saved_tracks(limit=50)

    while results:
        for item in results['items']:
            track = item['track']
            song_info = {
                "name": track['name'],
                "artist": track['artists'][0]['name'],
                "album": track['album']['name']
            }
            # Cria uma key para as músicas que estão passando pelo loop do results.
            song_key = song_info["name"] + song_info["artist"]

            # Compara a key das músicas analisadas pelo loop com a key das musicas já no JSON.
            if song_key not in existing_titles:
                all_songs.append(song_info)
        
        # Pega a próxima página de músicas.
        results = sp.next(results) if results['next'] else None

    if all_songs:
        print(f"{len(all_songs)} novas músicas encontradas e adicionadas.")
        existing_songs.extend(all_songs)
        save_songs(existing_songs)
    else:
        print("Nenhuma nova música foi encontrada.")
    