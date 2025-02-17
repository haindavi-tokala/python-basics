from flask import Flask, jsonify, request

app = Flask(__name__)

# Example data - in a real application, this might come from a database
tasks = [
    {'id': 1, 'title': 'Do the laundry', 'done': False},
    {'id': 2, 'title': 'Buy groceries', 'done': False},
    {'id': 3, 'title': 'Finish project', 'done': True}
]

# Route to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Route to get a single task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404
    return jsonify({'task': task})

# Route to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = request.get_json()
    new_task['id'] = len(tasks) + 1  # Generate new task ID
    tasks.append(new_task)
    return jsonify({'task': new_task}), 201

# Route to update a task by ID
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404
    task_data = request.get_json()
    task.update(task_data)
    return jsonify({'task': task})

# Route to delete a task by ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404
    tasks.remove(task)
    return jsonify({'message': 'Task deleted'})

if __name__ == '__main__':
    app.run(debug=True)
