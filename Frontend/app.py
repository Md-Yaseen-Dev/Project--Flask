from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
# Or your actual connection string
client = MongoClient("mongodb://localhost:27017/")
db = client.todo_db  # Your DB name
todos = db.todo_items  # Your collection name


@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    data = request.get_json()

    item_name = data.get('itemName')
    item_desc = data.get('itemDescription')

    if not item_name or not item_desc:
        return jsonify({'error': 'Both itemName and itemDescription are required'}), 400

    # Insert into MongoDB
    todos.insert_one({
        'itemName': item_name,
        'itemDescription': item_desc
    })

    return jsonify({'message': 'Item saved successfully'}), 201
