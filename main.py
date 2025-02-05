from spoti import get_liked_songs, authenticate_spotify
from ytmusic import add_liked_ytmusic, authenticate_ytmusic

def main():
    print("Iniciando a transferência de músicas do Spotify para o Youtube Music...")

    # Autentica no Spotify e obtém suas músicas curtidas.
    print("\nPasso 1: Obtendo músicas curtidas do Spotify...")
    sp = authenticate_spotify()
    get_liked_songs(sp)

    # Autentica no Youtube Music e cria/adiciona as músicas a playlist.
    print("\nPasso 2: Criando playlist no YouTube Music e adicionando as músicas...")
    ytmusic = authenticate_ytmusic()
    add_liked_ytmusic(ytmusic)

    print("\nProcesso concluído com sucesso!")

if __name__ == "__main__":
    main()