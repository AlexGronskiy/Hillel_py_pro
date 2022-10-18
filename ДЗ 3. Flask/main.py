from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/music_list/', methods=['get'])
def all_tracks():
    with sqlite3.connect('music_lib.sqlite3') as connection:
        cursor = connection.cursor()
        music = cursor.execute(
            "SELECT music.id, music.name, author.name, genre.name FROM music JOIN author ON music.author_id = "
            "author.id JOIN genre ON music.genre_id = genre.id")
        context = {'musics': music.fetchall()}
        return render_template("music_list.html", **context)


@app.route('/add_music/', methods=['get', 'post'])
def add_tracks():

    context = {'genres': [], 'authors': []}
    with sqlite3.connect('music_lib.sqlite3') as connection:
        cursor = connection.cursor()
        genres = cursor.execute("SELECT id, name FROM genre")
        context['genres'] = genres.fetchall()
        authors = cursor.execute("SELECT id, name FROM author")
        context['authors'] = authors.fetchall()

    if request.method == 'POST':

        with sqlite3.connect('music_lib.sqlite3') as connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO music(name, author_id, genre_id) VALUES ("
                f"'{request.form['name']}',"
                f" '{request.form['author']}',"
                f" '{request.form['genre']}')"
            )
            connection.commit()

    return render_template('add_music.html', **context)


@app.route('/del_music/', methods=['get', 'post'])
def del_music():
    context = {}
    with sqlite3.connect('music_lib.sqlite3') as connection:
        cursor = connection.cursor()
        music = cursor.execute(
            "SELECT music.name, author.name, genre.name FROM music JOIN author ON music.author_id = "
            "author.id JOIN genre ON music.genre_id = genre.id")
        context = {'musics': music.fetchall()}
    if request.method == 'POST':
        with sqlite3.connect('music_lib.sqlite3') as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"DELETE FROM music WHERE name='{request.form['name']}'"
            )
            connection.commit()
    return render_template('del_music.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
