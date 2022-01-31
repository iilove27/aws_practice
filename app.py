from flask import Flask, request
import json

app = Flask(__name__)
seed = 0
@app.route('/', methods=['GET', 'POST'])
def index():
    global seed 
    if request.method == 'POST':
        num = json.loads(request.data)
        seed = num
        return f'SEED VALUE UPDATED TO {seed}.'
    
    if request.method == 'GET':
        return f'{seed}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)