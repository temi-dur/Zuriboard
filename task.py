from flask import Flask, request, jsonify
import datetime
import pytz
import json, time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_info():
    info = {
        'slack_name': "Temitope",
        'current_day': time.time(),
        'track': "backend",
        'github_url_file': "https://github.com/temi-dur/yourrepository/blob/main/task.py",
        'github_url_source': "https://github.com/temi-dur/Zuriboard",
        'status': "status"
    }
    json_dump = json.dumps(info)

    return json_dump

if __name__ == '__main__':
    app.run(port=5000, debug=True)