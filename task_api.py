from flask import Flask, request, jsonify # type: ignore

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    
    if 'name' not in data or 'status' not in data:
        return jsonify({'error': 'Görev adi ve durumu gerekli'}), 400

    task_id = len(tasks) + 1 
    task = {
        'id': task_id,
        'name': data['name'],
        'description': data.get('description', ''),  
        'status': data['status']
    }
    
    tasks.append(task)
    
    return jsonify(task), 201 

@app.route('/tasks', methods=['GET'])
def list_tasks():
    status = request.args.get('status')  

    if status:
        filtered_tasks = [task for task in tasks if task['status'] == status]
        return jsonify(filtered_tasks)
    
    return jsonify(tasks)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if task is None:
        return jsonify({'error': 'Görev bulunamadi'}), 404

    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if task is None:
        return jsonify({'error': 'Görev bulunamadi'}), 404

    data = request.get_json()

    task['name'] = data.get('name', task['name'])
    task['description'] = data.get('description', task['description'])
    task['status'] = data.get('status', task['status'])
    
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    
    return jsonify({'message': 'Görev başariyla silindi'}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)