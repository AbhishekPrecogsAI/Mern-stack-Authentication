"""
vuln_examples.py
Intentionally vulnerable Python code for security testing
"""

import os
import sqlite3
import pickle
import requests
import hashlib
from flask import Flask, request

app = Flask(__name__)

# 1️⃣ HARDCODED SECRET
API_KEY = "sk_test_1234567890abcdef"


# 2️⃣ COMMAND INJECTION
def list_files(user_path):
    os.system("ls " + user_path)


# 3️⃣ SQL INJECTION
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()


# 4️⃣ INSECURE DESERIALIZATION (RCE)
def load_session(data):
    return pickle.loads(data)


# 5️⃣ PATH TRAVERSAL
def read_file(filename):
    with open("uploads/" + filename, "r") as f:
        return f.read()


# 6️⃣ SSRF
def fetch_url(url):
    return requests.get(url).text


# 7️⃣ UNSAFE EVAL
def calculate(expression):
    return eval(expression)


# 8️⃣ WEAK PASSWORD HASHING
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


# 9️⃣ FLASK DEBUG MODE + USER INPUT EXECUTION
@app.route("/debug")
def debug():
    cmd = request.args.get("cmd")
    return os.popen(cmd).read()


# 🔟 OVERLY BROAD EXCEPTION (ERROR HIDING)
def divide(a, b):
    try:
        return a / b
    except:
        return None


if __name__ == "__main__":
    # 11️⃣ DEBUG MODE ENABLED
    app.run(host="0.0.0.0", port=5000, debug=True)
