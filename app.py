from flask import Flask, render_template, jsonify
import json
import webbrowser
import threading
import time
import os
import sys

app = Flask(__name__)
app.secret_key = 'disney_clone_secret_key_2024'

# Dados dos filmes Disney e Marvel (simulando uma base de dados)
DISNEY_MOVIES = [
    {
        'id': 1,
        'title': 'Frozen II',
        'year': 2019,
        'genre': 'Animação, Aventura, Comédia',
        'duration': '103 min',
        'rating': 7.0,
        'description': 'Elsa, Anna, Kristoff e Olaf se aventuram nas florestas encantadas para descobrir a origem dos poderes de Elsa.',
        'poster': 'https://m.media-amazon.com/images/M/MV5BMjA0YjYyZGMtN2U0Ni00YmJhLWJkZWQtYzUxYWM5ZjcyNTVlXkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_.jpg',
        'trailer': 'https://www.youtube.com/embed/Zi4LMpSDccc',
        'featured': True,
        'studio': 'Disney'
    },
    {
        'id': 2,
        'title': 'Avengers: Endgame',
        'year': 2019,
        'genre': 'Ação, Aventura, Drama',
        'duration': '181 min',
        'rating': 8.4,
        'description': 'Após os eventos devastadores de Vingadores: Guerra Infinita, os heróis restantes se unem para reverter as ações de Thanos.',
        'poster': 'https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_.jpg',
        'trailer': 'https://www.youtube.com/embed/TcMBFSGVi1c',
        'featured': True,
        'studio': 'Marvel'
    },
    {
        'id': 3,
        'title': 'Spider-Man: No Way Home',
        'year': 2021,
        'genre': 'Ação, Aventura, Ficção Científica',
        'duration': '148 min',
        'rating': 8.2,
        'description': 'Peter Parker busca a ajuda do Doutor Estranho para fazer com que o mundo esqueça que ele é o Homem-Aranha.',
        'poster': 'https://m.media-amazon.com/images/M/MV5BZWMyYzFjYTYtNTRjYi00OGExLWE2YzgtOGRmYjAxZTU3NzBiXkEyXkFqcGdeQXVyMzQ0MzA0NTM@._V1_.jpg',
        'trailer': 'https://www.youtube.com/embed/JfVOs4VSpmA',
        'featured': True,
        'studio': 'Marvel'
    },
    {
        'id': 4,
        'title': 'Encanto',
        'year': 2021,
        'genre': 'Animação, Comédia, Drama',
        'duration': '102 min',
        'rating': 7.2,
        'description': 'Mirabel é uma garota de uma família extraordinária que vive em uma casa mágica nas montanhas da Colômbia.',
        'poster': 'https://m.media-amazon.com/images/M/MV5BNjE5NzA4ZDctOTJkZi00NzM0LTkwOTYtMDI4MmNkMzIxODhkXkEyXkFqcGdeQXVyNjY1MTg4Mzc@._V1_.jpg',
        'trailer': 'https://www.youtube.com/embed/CaimKeDcudo',
        'featured': True,
        'studio': 'Disney'
    },
    {
        'id': 5,
        'title': 'Doctor Strange in the Multiverse of Madness',
        'year': 2022,
        'genre': 'Ação, Aventura, Horror',
        'duration': '126 min',
        'rating': 6.9,
        'description': 'O Doutor Estranho explora o perigoso e inexplorado multiverso com a ajuda de aliados novos e outros já conhecidos.',
        'poster': 'https://m.media-amazon.com/images/M/MV5BNWM0ZGJlMzMtZmYwMi00NzI3LTgzMzMtNjMzNjliNDRmZmFlXkEyXkFqcGdeQXVyMTM1MTE1NDMx@._V1_.jpg',
        'trailer': 'https://www.youtube.com/embed/aWzlQ2N6qqg',
        'featured': False,
        'studio': 'Marvel'
    },
    {
        'id': 6,
        'title': 'Black Panther: Wakanda Forever',
        'year': 2022,
        'genre': 'Ação, Aventura, Drama',
        'duration': '161 min',
        'rating': 6.7,
        'description': 'A rainha Ramonda, Shuri, M\'Baku, Okoye e as Dora Milaje lutam para proteger Wakanda após a morte do rei T\'Challa.',
        'poster': 'https://m.media-amazon.com/images/M/MV5BNTM4NjIxNmEtYWE5NS00NDczLTkyNWQtYThhNmQyZGQzMjM0XkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_.jpg',
        'trailer': 'https://www.youtube.com/embed/_Z3QKkl1WyM',
        'featured': True,
        'studio': 'Marvel'
    },
    {
        'id': 7,
        'title': 'Moana',
        'year': 2016,
        'genre': 'Animação, Aventura, Comédia',
        'duration': '107 min',
        'rating': 7.6,
        'description': 'Uma jovem navegadora polinésia embarca numa jornada épica para salvar sua ilha natal.',
        'poster': 'https://m.media-amazon.com/images/M/MV5BMjI4MzU5NTExNF5BMl5BanBnXkFtZTgwNzY1MTEwMDI@._V1_.jpg',
        'trailer': 'https://www.youtube.com/embed/LKFuXETZUsI',
        'featured': False,
        'studio': 'Disney'
    },
    {
        'id': 8,
        'title': 'Thor: Love and Thunder',
        'year': 2022,
        'genre': 'Ação, Aventura, Comédia',
        'duration': '119 min',
        'rating': 6.2,
        'description': 'Thor embarca numa jornada diferente de tudo que já enfrentou - uma busca pela paz interior.',
        'poster': 'https://m.media-amazon.com/images/M/MV5BYmMxZWRiMTgtZjM0Ny00NDQxLWIxYWQtZDI2NWE1OWI5Nzc5XkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg',
        'trailer': 'https://www.youtube.com/embed/Go8nTmfrQd8',
        'featured': False,
        'studio': 'Marvel'
    },
    {
        'id': 9,
        'title': 'Toy Story 4',
        'year': 2019,
        'genre': 'Animação, Aventura, Comédia',
        'duration': '100 min',
        'rating': 7.7,
        'description': 'Woody e Buzz em uma nova aventura com Bonnie e um novo brinquedo chamado Forky.',
        'poster': 'https://m.media-amazon.com/images/M/MV5BMTYzMDM4NzkxOV5BMl5BanBnXkFtZTgwNzM1Mzg2NzM@._V1_.jpg',
        'trailer': 'https://www.youtube.com/embed/wmiIUN-7qhE',
        'featured': True,
        'studio': 'Disney'
    },
    {
        'id': 10,
        'title': 'Guardians of the Galaxy Vol. 3',
        'year': 2023,
        'genre': 'Ação, Aventura, Comédia',
        'duration': '150 min',
        'rating': 7.9,
        'description': 'Peter Quill ainda está se recuperando da perda de Gamora e deve reunir sua equipe para defender o universo.',
        'poster': 'https://m.media-amazon.com/images/M/MV5BMDgxOTdjMzYtZGQxMS00ZTAzLWI4Y2UtMTQzN2VlYjYyZWRiXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg',
        'trailer': 'https://www.youtube.com/embed/u3V5KDHRQvk',
        'featured': False,
        'studio': 'Marvel'
    },
    {
        'id': 11,
        'title': 'Luca',
        'year': 2021,
        'genre': 'Animação, Aventura, Comédia',
        'duration': '95 min',
        'rating': 7.4,
        'description': 'Um garoto monstro marinho vive um verão inesquecível em uma cidade costeira italiana.',
        'poster': 'https://m.media-amazon.com/images/M/MV5BZTQyNTU0MDktYTFkYi00ZjNhLWE2ODctMzBkM2U1ZTk3YTMzXkEyXkFqcGdeQXVyNTI4MzE4MDU@._V1_.jpg',
        'trailer': 'https://www.youtube.com/embed/mYfJxlgR2jw',
        'featured': False,
        'studio': 'Disney'
    },
    {
        'id': 12,
        'title': 'The Marvels',
        'year': 2023,
        'genre': 'Ação, Aventura, Ficção Científica',
        'duration': '105 min',
        'rating': 5.5,
        'description': 'Carol Danvers, Kamala Khan e Monica Rambeau trocam de lugar toda vez que usam seus poderes.',
        'poster': 'https://m.media-amazon.com/images/M/MV5BM2U2YWU5NWMtOGI2Ni00MGE0LWFkZjQtOGY1ZDY4NzFlNzBhXkEyXkFqcGdeQXVyMTUzMTg2ODkz@._V1_.jpg',
        'trailer': 'https://www.youtube.com/embed/wS_qbDztgVY',
        'featured': False,
        'studio': 'Marvel'
    },
    {
        'id': 13,
        'title': 'Coco',
        'year': 2017,
        'genre': 'Animação, Aventura, Drama',
        'duration': '105 min',
        'rating': 8.4,
        'description': 'Miguel sonha em se tornar músico, mas sua família odeia música. Durante o Dia dos Mortos, ele entra no mundo dos mortos.',
        'poster': 'https://m.media-amazon.com/images/M/MV5BYjQ5NjM0Y2YtNjZkNC00ZDhkLWJjMWItN2QyNzFkMDE3ZjAxXkEyXkFqcGdeQXVyODIxMzk5NjA@._V1_.jpg',
        'trailer': 'https://www.youtube.com/embed/Ga6RYejo6Hk',
        'featured': True,
        'studio': 'Disney'
    },
    {
        'id': 14,
        'title': 'Ant-Man and the Wasp: Quantumania',
        'year': 2023,
        'genre': 'Ação, Aventura, Comédia',
        'duration': '124 min',
        'rating': 6.0,
        'description': 'Scott Lang e Hope Van Dyne se aventuram no Reino Quântico, onde conhecem criaturas estranhas.',
        'poster': 'https://m.media-amazon.com/images/M/MV5BODZhNzlmOGItMWUyYS00Y2Q5LWFlNzMtM2I2NDFkM2ZkYmE1XkEyXkFqcGdeQXVyMTU5OTA4NTIz@._V1_.jpg',
        'trailer': 'https://www.youtube.com/embed/ZlNFpri-Y40',
        'featured': False,
        'studio': 'Marvel'
    },
    {
        'id': 15,
        'title': 'Soul',
        'year': 2020,
        'genre': 'Animação, Aventura, Comédia',
        'duration': '100 min',
        'rating': 8.0,
        'description': 'Joe Gardner, um músico de jazz, embarca numa jornada para descobrir o verdadeiro significado da vida.',
        'poster': 'https://m.media-amazon.com/images/M/MV5BZGE1MDg5M2MtNTkyZS00MTY5LTg1YzUtZTlhZmM1Y2EwNmFmXkEyXkFqcGdeQXVyNjY1MTg4Mzc@._V1_.jpg',
        'trailer': 'https://www.youtube.com/embed/xOsLIiBStEs',
        'featured': True,
        'studio': 'Disney'
    },
    {
        'id': 16,
        'title': 'Captain Marvel',
        'year': 2019,
        'genre': 'Ação, Aventura, Ficção Científica',
        'duration': '123 min',
        'rating': 6.8,
        'description': 'Carol Danvers se torna uma das heroínas mais poderosas do universo quando a Terra fica presa em uma guerra galáctica.',
        'poster': 'https://m.media-amazon.com/images/M/MV5BMTE0YWFmOTMtYTU2ZS00ZTIxLWE3OTEtYTNiYzBkOGM5MTllXkEyXkFqcGdeQXVyODMzMzQ4OTI@._V1_.jpg',
        'trailer': 'https://www.youtube.com/embed/Z1BCujX3pw8',
        'featured': False,
        'studio': 'Marvel'
    }
]

@app.route('/')
def index():
    """Página inicial com filmes em destaque"""
    featured_movies = [movie for movie in DISNEY_MOVIES if movie.get('featured', False)]
    return render_template('index.html', featured_movies=featured_movies)

@app.route('/movies')
def movies():
    """Página com todos os filmes"""
    return render_template('movies.html', movies=DISNEY_MOVIES)

@app.route('/disney')
def disney_movies():
    """Página só com filmes Disney"""
    disney_films = [movie for movie in DISNEY_MOVIES if movie.get('studio') == 'Disney']
    return render_template('movies.html', movies=disney_films, studio='Disney')

@app.route('/marvel')
def marvel_movies():
    """Página só com filmes Marvel"""
    marvel_films = [movie for movie in DISNEY_MOVIES if movie.get('studio') == 'Marvel']
    return render_template('movies.html', movies=marvel_films, studio='Marvel')

@app.route('/movie/<int:movie_id>')
def movie_detail(movie_id):
    """Detalhes de um filme específico"""
    movie = next((m for m in DISNEY_MOVIES if m['id'] == movie_id), None)
    if not movie:
        return "Filme não encontrado", 404
    return render_template('movie_detail.html', movie=movie)

@app.route('/api/movies')
def api_movies():
    """API endpoint para obter lista de filmes"""
    return jsonify(DISNEY_MOVIES)

@app.route('/api/movie/<int:movie_id>')
def api_movie(movie_id):
    """API endpoint para obter detalhes de um filme"""
    movie = next((m for m in DISNEY_MOVIES if m['id'] == movie_id), None)
    if not movie:
        return jsonify({'error': 'Filme não encontrado'}), 404
    return jsonify(movie)

@app.route('/about')
def about():
    """Página sobre o projeto"""
    return render_template('about.html')

def open_browser():
    """Abre o navegador após 1.5 segundos"""
    time.sleep(1.5)
    webbrowser.open('http://127.0.0.1:5000')

if __name__ == '__main__':
    # Só abre o navegador se for a execução principal (não o reloader)
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        threading.Thread(target=open_browser, daemon=True).start()
        print("🎬 Iniciando Disney Clone...")
        print("🌐 Abrindo no navegador em http://127.0.0.1:5000")
        print("🏰 Bem-vindo ao mundo mágico da Disney!")
        print("📱 Para parar, pressione Ctrl+C")
    
    app.run(debug=True, host='127.0.0.1', port=5000)