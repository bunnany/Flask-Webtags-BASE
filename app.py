from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABASE = "tags.db"

def create_connection(db_file):
    """
    Creates a connection to the database
    :parameter    db_file - the name of the file
    :returns      connection - a connection to the database
    """
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    return None


@app.route('/')
def render_home():
    return render_template('index.html')


@app.route('/webpages')
def render_webpage():
    query = "SELECT tag, description FROM html_tags WHERE type='HTML'"
    con = create_connection(DATABASE)
    cur = con.cursor()
    
    # Query the DATABASE
    cur.execute(query)
    tag_list = cur.fetchall()
    con.close()
    print(tag_list)
    return render_template('webpages.html', tags=tag_list)


@app.route('/styles')
def render_styles():
    query = "SELECT tag, description FROM html_tags WHERE type='CSS'"
    con = create_connection(DATABASE)
    cur = con.cursor()
    
    # Query the DATABASE
    cur.execute(query)
    tag_list = cur.fetchall()
    con.close()
    print(tag_list)
    return render_template('styles.html', tags=tag_list)

if __name__ == "__main__":
    app.run()
