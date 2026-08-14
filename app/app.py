from flask import Flask, jsonify
import os
import socket
from datetime import datetime

app = Flask(__name__)

VERSION = os.environ.get('APP_VERSION', '1.0.0')
ENV     = os.environ.get('APP_ENV', 'dev')

@app.route('/')
def home():
    return jsonify({
        "message"  : "Hello from EKS + ArgoCD!",
        "version"  : VERSION,
        "env"      : ENV,
        "pod"      : socket.gethostname(),
        "timestamp": datetime.now().isoformat()
    })

@app.route('/health')
def health():
    return jsonify({
        "status" : "healthy",
        "version": VERSION
    }), 200

@app.route('/ready')
def ready():
    return jsonify({"status": "ready"}), 200

@app.route('/tasks')
def tasks():
    return jsonify([
        {"id": 1, "title": "Learn ArgoCD", "done": True},
        {"id": 2, "title": "Deploy to EKS", "done": True},
        {"id": 3, "title": "Setup GitOps",  "done": False}
    ])

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=ENV == 'dev'
    )