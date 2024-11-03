from flask import Flask, jsonify, redirect, url_for
import psycopg2

app = Flask(__name__)

def get_db_connection():

    with open('/run/secrets/db_password', 'r') as file:
        password = file.read().strip()

    conn = psycopg2.connect(
        host="db",
        database="db_emre",
        user="emre",
        password=password
    )


    cur = conn.cursor()

    cur.execute('SELECT nom FROM message LIMIT 1;')
    name = cur.fetchone()

    cur.close()
    conn.close()

    return name

@app.route('/')
def index():
    return redirect(url_for('hello'))
    

@app.route('/hello')
def hello():

    conn = get_db_connection()
    

    if conn is None:
        return jsonify({"message": "No data found"}), 404
    else:
        return jsonify({"message": conn})
        

if __name__ == '__main__':
    app.run()
