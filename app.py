from flask import Flask, request, jsonify

app = Flask(__name__)
servers = []

@app.route('/')
def home():
    return "Hello!"

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    servers.append(data)
    return "Registered", 200

@app.route('/unregister', methods=['POST'])
def unregister():
    data = request.json
    servers.remove(data)
    return "Registered", 200

@app.route('/server_list', methods=['GET'])
def server_list():
    return jsonify(servers), 200

@app.route('/clear', methods=['POST'])
def clear_list():
    servers.clear()
    return "List cleared", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)