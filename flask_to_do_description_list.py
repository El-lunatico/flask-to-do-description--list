from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def init_sqlite_db():
    conn = sqlite3.connect("database.db")
    conn.execute('CREATE TABLE IF NOT EXISTS task(id INTEGER PRIMARY KEY, title TEXT, description TEXT)')
    conn.close()
init_sqlite_db()

@app.route('/')
def text_list():
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("SELECT id, title, description FROM task ORDER BY id DESC")
        tasks = cur.fetchall()
    return render_template('text_list.html', tasks=tasks)

@app.route('/', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get('userInput')
    description = data.get('userInput2')

    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("INSERT INTO task (title, description) VALUES (?, ?)", (task, description))
        con.commit()

    return jsonify(success=True)

@app.route('/get_task/<int:task_id>')
def get_task(task_id):
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("SELECT title, description FROM task WHERE id = ?", (task_id,))
        task = cur.fetchone()

    if task:
        return jsonify({'task': task[0], 'description': task[1]})
    else:
        return jsonify({'error': 'Task not found'}), 404

@app.route('/edit_task', methods=['POST'])
def edit_task():
    data = request.get_json()
    task_id = int(data.get('index'))
    task = data.get('task')
    description = data.get('description')

    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("UPDATE task SET title = ?, description = ? WHERE id = ?", (task, description, task_id))
        con.commit()

    return jsonify({'success': True})

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("DELETE FROM task WHERE id = ?", (task_id,))
        con.commit()

    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 ,debug=True)
