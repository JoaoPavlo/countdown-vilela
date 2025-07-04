from flask import Flask, render_template
from datetime import datetime, timedelta
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Calculate the target date (30 days from now)
    target_date = datetime.now() + timedelta(days=30)
    return render_template('index.html', target_date=target_date.isoformat())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port) 