from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (replace this with your actual data or database interactions)
tasks = [
    {
        'id': 1,
        'title': 'Task 1',
        'done': False
    },
    {
        'id': 2,
        'title': 'Task 2',
        'done': False
    }
]

# Route to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Route to get a specific task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify({'task': task})
    return jsonify({'error': 'Task not found'}), 404

# Route to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        return jsonify({'error': 'Task title is required'}), 400

    new_task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'done': False
    }
    tasks.append(new_task)
    return jsonify({'task': new_task}), 201

# Route to update a task by ID
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    if 'title' in request.json:
        task['title'] = request.json['title']
    if 'done' in request.json:
        task['done'] = request.json['done']

    return jsonify({'task': task})

# Route to delete a task by ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'result': 'Task deleted'})

if __name__ == '__main__':
    app.run(debug=True)
