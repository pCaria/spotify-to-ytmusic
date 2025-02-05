Transferindo suas músicas curtidas do Spotify para o YouTube Music
Este projeto permite que você transfira suas músicas curtidas no Spotify para uma playlist no YouTube Music de forma automática. Para isso, você precisará configurar algumas chaves de API e instalar algumas dependências. Siga os passos abaixo para rodar o código em sua máquina.

Passo 1: Instalar o Python
    Baixe e instale o Python:

    Acesse o site oficial do Python: https://www.python.org/downloads/.

    Faça o download da versão mais recente do Python (3.9 ou superior).

    Durante a instalação, marque a opção "Add Python to PATH" e clique em "Install Now".

    Verifique a instalação:

    Abra o terminal (ou Prompt de Comando no Windows) e digite:

        python --version

    Se a instalação foi bem-sucedida, a versão do Python será exibida.

Passo 2: Clonar o repositório
    Instale o Git (caso ainda não tenha):

    Baixe o Git em: https://git-scm.com/downloads.
    Siga as instruções de instalação.

    Clone o repositório:

    Abra o terminal e execute o seguinte comando:

        git clone https://github.com/seu-usuario/nome-do-repositorio.git

    Substitua seu-usuario e nome-do-repositorio pelo seu nome de usuário do GitHub e o nome do repositório.

    Navegue até a pasta do projeto:

    No terminal, acesse a pasta do projeto:

        cd nome-do-repositorio

Passo 3: Instalar as dependências
    Instale as bibliotecas necessárias:

    No terminal, execute o seguinte comando para instalar as dependências:

        pip install -r requirements.txt

    Isso instalará automaticamente as bibliotecas spotipy, ytmusicapi e python-dotenv.

Passo 4: Configurar as chaves de API
    1. Obter as credenciais do Spotify
        Acesse o Spotify for Developers.

        Faça login com sua conta do Spotify.

        Clique em "Create an App".

        Preencha o formulário com um nome e uma descrição para o aplicativo.

        Após criar o aplicativo, anote:

        Client ID

        Client Secret

        Defina o Redirect URI como http://localhost:8888.

    2. Obter as credenciais do YouTube Music
        Acesse o Google Cloud Console.

        Crie um novo projeto ou selecione um existente.

        No menu lateral, vá para "APIs e Serviços" > "Credenciais".

        Clique em "Criar Credenciais" e selecione "OAuth client ID".

        Escolha o tipo de aplicativo como "Desktop".

        Anote:

        Client ID

        Client Secret

    3. Configurar o arquivo .env
        Na pasta do projeto, crie um arquivo .env.

        Abra o arquivo .env no VSCode ou em qualquer editor de texto e adicione as seguintes linhas:

        SPOTIFY_CLIENT_ID=seu_client_id_do_spotify
        SPOTIFY_CLIENT_SECRET=seu_client_secret_do_spotify
        SPOTIFY_REDIRECT_URI=http://localhost:8888
        YT_CLIENT_ID=seu_client_id_do_youtube
        YT_CLIENT_SECRET=seu_client_secret_do_youtube

        Substitua os valores pelos que você obteve nas etapas anteriores.

Passo 5: Autenticar no YouTube Music
    Execute o seguinte comando no terminal:

        python -m ytmusicapi oauth

    Siga as instruções para autenticar sua conta do YouTube Music.

    Após a autenticação, um arquivo chamado oauth.json será gerado na pasta do projeto. Não compartilhe esse arquivo!

Passo 6: Executar o código
    No terminal, execute:
    ```bash
        python main.py

    Isso salvará suas músicas curtidas em um arquivo chamado liked_songs.json.


Passo 7: Verificar a playlist
    Acesse o YouTube Music em: https://music.youtube.com.

    Verifique se a playlist "Músicas Curtidas Spotify" foi criada e contém suas músicas.

Dúvidas e Problemas Comuns:
    1- Erro de autenticação:

        Certifique-se de que as credenciais no arquivo .env estão corretas.

        Verifique se o arquivo oauth.json foi gerado corretamente.

    2- Músicas não encontradas:

        Algumas músicas podem não ser encontradas no YouTube Music devido a diferenças nos catálogos.

    3- Problemas com dependências:

        Certifique-se de que todas as dependências foram instaladas corretamente com pip install -r requirements.txt.

Contribuições
    Se você quiser contribuir para o projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request no repositório do GitHub.

Licença
    Este projeto é licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.