from flask import Flask, jsonify
import os

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "unknown")
BUILD_NUMBER = os.getenv("BUILD_NUMBER", "unknown")
GIT_COMMIT = os.getenv("GIT_COMMIT", "unknown")
BRANCH_NAME = os.getenv("BRANCH_NAME", "unknown")


@app.route("/")
def home():
    return jsonify({
        "application": "Payment API",
        "version": APP_VERSION,
        "build_number": BUILD_NUMBER,
        "git_commit": GIT_COMMIT,
        "branch": BRANCH_NAME,
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)