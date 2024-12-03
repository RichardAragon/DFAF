from flask import Flask, request, jsonify, render_template
import numpy as np

# Initialize Flask application
app = Flask(__name__)

# D-FAF Function
def d_faf(x, a=1.0, n_iterations=10):
    y = x
    for _ in range(n_iterations):
        y = x * np.sin(a * y)
    return y

# P-FAF Function
def p_faf(x, a=1.0, n_iterations=10, noise_level=0.1):
    y = x
    for _ in range(n_iterations):
        noise = np.random.normal(0, noise_level, size=np.shape(x))
        y = x * np.sin(a * y) + noise
    return y

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# API for D-FAF
@app.route('/api/dfaf', methods=['POST'])
def api_dfaf():
    data = request.json
    x = np.array(data['x'])
    a = data.get('a', 1.0)
    n_iterations = data.get('n_iterations', 10)
    result = d_faf(x, a, n_iterations).tolist()
    return jsonify({'result': result})

# API for P-FAF
@app.route('/api/pfaf', methods=['POST'])
def api_pfaf():
    data = request.json
    x = np.array(data['x'])
    a = data.get('a', 1.0)
    n_iterations = data.get('n_iterations', 10)
    noise_level = data.get('noise_level', 0.1)
    result = p_faf(x, a, n_iterations, noise_level).tolist()
    return jsonify({'result': result})

# Start the application
if __name__ == '__main__':
    app.run(debug=True)
