from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Create SQLite database
conn = sqlite3.connect('registration.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')
conn.commit()
conn.close()

@app.route('/')
def registration_form():
    return render_template('registration_form.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']

    # Insert data into the database
    conn = sqlite3.connect('registration.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()

    return redirect(url_for('display_records'))

@app.route('/records')
def display_records():
    # Fetch all records from the database
    conn = sqlite3.connect('registration.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    records = cursor.fetchall()
    conn.close()

    return render_template('records.html', records=records)

if __name__ == '__main__':
    app.run(debug=True)
