from flask import Flask, render_template, request, jsonify
from algorithms.fcfs import fcfs
from algorithms.sjf import sjf
from algorithms.priority import priority
from algorithms.rr import round_robin
from algorithms.priority_rr import priority_round_robin
import csv

from random import randint
app = Flask(__name__)

# Dummy list to hold processes
processes = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global processes

    if request.method == 'POST':
        if request.headers['Content-Type'] == 'text/plain':
            # Clear existing processes
            processes = []

            # Parse the CSV data
            csv_data = request.data.decode('utf-8').splitlines()
            csv_reader = csv.reader(csv_data)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                pid, arrival_time, burst_time = row
                processes.append({'pid': pid, 'arrival_time': arrival_time, 'burst_time': burst_time})

            # Print received processes
            print("Received processes:", processes)

            ra = randint(1, 5)
            # Dummy response
            return jsonify({"tmp": ra})

    return render_template('index.html', algorithm='fcfs', processes=processes)

if __name__ == "__main__":
    app.run(debug=True)
