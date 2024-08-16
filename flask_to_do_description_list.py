from flask import Flask, render_template, request, jsonify, session, redirect, url_for,flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import qrcode
import socket

app = Flask(__name__)
app.secret_key = 'your_secret_key'
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(("8.8.8.8", 80))
        ip=s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'

    return ip

def init_sqlite_db():
    conn = sqlite3.connect("database.db")
    conn.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS task(
            id INTEGER PRIMARY KEY, 
            title TEXT, 
            description TEXT, 
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')
    conn.close()
init_sqlite_db()



@app.route('/')
def index():

    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            try:
                cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
                con.commit()
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                return  redirect(url_for('index'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute("SELECT id, password FROM users WHERE username = ?", (username,))
            user = cur.fetchone()

            if user and check_password_hash(user[1], password):
                session['username'] = username
                session['user_id'] = user[0]
                return redirect(url_for('text_list'))
            else:
                redirect(url_for('index'))
                error = "Your ID or password is wrong"

    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/task')
def text_list():
    if 'username' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("SELECT id, title, description FROM task WHERE user_id = ? ORDER BY id DESC", (user_id,))
        tasks = cur.fetchall()
    return render_template("text_list.html", tasks=tasks)

@app.route('/', methods=['POST'])
def add_task():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()
    task = data.get('userInput')
    description = data.get('userInput2')
    user_id = session['user_id']

    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("INSERT INTO task (title, description, user_id) VALUES (?, ?, ?)", (task, description, user_id))
        con.commit()

    return jsonify(success=True)

@app.route('/get_task/<int:task_id>')
def get_task(task_id):
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 403

    user_id = session['user_id']
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("SELECT title, description FROM task WHERE id = ? AND user_id = ?", (task_id, user_id))
        task = cur.fetchone()

    if task:
        return jsonify({'task': task[0], 'description': task[1]})
    else:
        return jsonify({'error': 'Task not found'}), 404

@app.route('/edit_task', methods=['POST'])
def edit_task():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()
    task_id = int(data.get('index'))
    task = data.get('task')
    description = data.get('description')
    user_id = session['user_id']

    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("UPDATE task SET title = ?, description = ? WHERE id = ? AND user_id = ?", 
                    (task, description, task_id, user_id))
        con.commit()

    return jsonify({'success': True})

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 403

    user_id = session['user_id']
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("DELETE FROM task WHERE id = ? AND user_id = ?", (task_id, user_id))
        con.commit()

    return jsonify({'success': True})

if __name__ == '__main__':
    IP =get_ip()
    # The data you want to encode in the QR code
    data = f"http://{IP}:5000"

# Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
        box_size=4,  # size of each box in pixels
        border=4,  # thickness of the border
        )

# Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

# Print the QR code in ASCII format
    qr.print_tty()
    app.run(host='0.0.0.0', port=5000, debug=True)
