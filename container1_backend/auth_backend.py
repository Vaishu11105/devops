from flask import Flask, request, jsonify
from flask_cors import CORS
from mydb import Database
import requests

app = Flask(__name__)
CORS(app)
db = Database()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"status": "error", "message": "Missing fields"}), 400

    if db.validate_credentials(email, password):
        try:
            r = requests.post("http://container2_backend:5000/start_gui")  # Corrected
            r.raise_for_status()
        except Exception as e:
            return jsonify({"status": "error", "message": f"Login OK but failed to start GUI: {str(e)}"}), 500

        return jsonify({"status": "success", "message": "Login successful and GUI launched!"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid credentials"}), 401
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')

    if not email or not password or not confirm_password:
        return jsonify({"status": "error", "message": "Missing fields"}), 400

    if password != confirm_password:
        return jsonify({"status": "error", "message": "Passwords do not match"}), 400

    result = db.add_data(email, password)
    if result:
        return jsonify({"status": "success", "message": "Registration successful!"}), 201
    else:
        return jsonify({"status": "error", "message": "User already exists"}), 409

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
