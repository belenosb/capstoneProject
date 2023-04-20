from flask import Flask, render_template, request
from pubsub import pub

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    # Get user commands and publish to relevant topics
    pass

if __name__ == '__main__':
    main()