from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('scraped_data.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/groups')
def show_groups():
    conn = get_db_connection()
    groups = conn.execute('SELECT * FROM groups').fetchall()
    conn.close()
    return render_template('table.html', title='Groups', rows=groups, columns=['Associated_groups', 'Name', 'Description'])

@app.route('/softwares')
def show_softwares():
    conn = get_db_connection()
    softwares = conn.execute('SELECT * FROM softwares').fetchall()
    conn.close()
    return render_template('table.html', title='Softwares', rows=softwares, columns=['Associated_softwares', 'Name', 'Description', 'Type'])

@app.route('/techniques')
def show_techniques():
    conn = get_db_connection()
    techniques = conn.execute('SELECT * FROM techniques').fetchall()
    conn.close()
    return render_template('table.html', title='Techniques', rows=techniques, columns=['Name', 'Description', 'Type'])

if __name__ == '__main__':
    app.run(debug=True)