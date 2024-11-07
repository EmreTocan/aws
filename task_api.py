from flask import Flask, request, jsonify

app = Flask(__name__)

# Görevleri saklayacak basit bir liste (Veritabanı yerine kullanılacak)
tasks = []

# Görev ekleme (POST /tasks)
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    
    # Görev için gerekli alanların varlığı kontrol ediliyor
    if 'name' not in data or 'status' not in data:
        return jsonify({'error': 'Görev adı ve durumu gerekli'}), 400

    task_id = len(tasks) + 1  # Her yeni görev için benzersiz bir id
    task = {
        'id': task_id,
        'name': data['name'],
        'description': data.get('description', ''),  # Açıklama opsiyonel
        'status': data['status']
    }
    
    tasks.append(task)
    
    return jsonify(task), 201  # Başarıyla eklenmiş görevi döndürür

# Görev listeleme (GET /tasks)
@app.route('/tasks', methods=['GET'])
def list_tasks():
    status = request.args.get('status')  # Filtreleme için 'status' parametresi

    if status:
        filtered_tasks = [task for task in tasks if task['status'] == status]
        return jsonify(filtered_tasks)
    
    return jsonify(tasks)

# Belirli bir görevi alma (GET /tasks/<id>)
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if task is None:
        return jsonify({'error': 'Görev bulunamadı'}), 404

    return jsonify(task)

# Görev güncelleme (PUT /tasks/<id>)
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if task is None:
        return jsonify({'error': 'Görev bulunamadı'}), 404

    data = request.get_json()

    task['name'] = data.get('name', task['name'])
    task['description'] = data.get('description', task['description'])
    task['status'] = data.get('status', task['status'])
    
    return jsonify(task)

# Görev silme (DELETE /tasks/<id>)
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    
    return jsonify({'message': 'Görev başarıyla silindi'}), 200

# Uygulama çalıştırma
if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)