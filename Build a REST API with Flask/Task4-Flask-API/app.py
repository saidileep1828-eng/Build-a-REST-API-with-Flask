from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
users = {
    1: {"name": "John", "age": 22},
    2: {"name": "Alice", "age": 25}
}

# Home Route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to User Management API"})

# GET All Users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET Single User
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id])
    return jsonify({"error": "User not found"}), 404

# POST Create User
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    if not data or 'name' not in data or 'age' not in data:
        return jsonify({"error": "Invalid input. 'name' and 'age' are required."}), 400

    new_id = max(users.keys()) + 1 if users else 1
    users[new_id] = {
        "name": data["name"],
        "age": data["age"]
    }
    return jsonify({
        "message": "User added successfully",
        "user": users[new_id]
    }), 201

# PUT Update User
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    if not data or 'name' not in data or 'age' not in data:
        return jsonify({"error": "Invalid input. 'name' and 'age' are required."}), 400

    users[user_id] = {
        "name": data["name"],
        "age": data["age"]
    }
    return jsonify({
        "message": "User updated successfully",
        "user": users[user_id]
    })

# DELETE User
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    deleted_user = users.pop(user_id)
    return jsonify({
        "message": "User deleted successfully",
        "user": deleted_user
    })

if __name__ == '__main__':
    app.run(debug=True)
