## File Structure

The file structure of the project is as follows:

```
├── algorithms/
│   ├── fcfs.py
│   ├── sjf.py
│   ├── priority.py
│   ├── rr.py
│   └── priority_rr.py
├── models/
│   └── process.py
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── templates/
│   └── index.html
├── main.py
└── README.md
```

- **algorithms/**: Contains Python modules for different scheduling algorithms.
- **models/**: Contains the Process class definition.
- **static/**: Contains static files such as CSS and JavaScript.
- **templates/**: Contains HTML templates for the user interface.
- **main.py**: Flask server script.
- **README.md**: Instructions for using the application (this file).

## Usage

1. **Running the Server**:
   - Open a terminal.
   - Navigate to the project directory.
   - Run the Flask server by executing the following command:
     ```bash
     python main.py
     ```

2. **Accessing the Application**:
   - Open a web browser.
   - Enter the following URL in the address bar:
     ```
     http://127.0.0.1:5000
     ```

3. **Importing Processes from CSV**:
   - Click on the "Import from CSV" button to import processes from a CSV file.
   - If the CSV file contains a priority column, the algorithm dropdown menu will switch to the priority-based options.

4. **Generating Random Processes**:
   - Enter the desired number of processes, arrival time range, burst time range, and priority range (if applicable).
   - Click on the "Generate Random Processes" button to generate random processes.

5. **Manually Inputting Processes**:
   - Enter process details (ID, arrival time, burst time, and priority if applicable) in the input fields.
   - Click on the "Add Process" button to add the process to the table.

6. **Clearing the Process Table**:
   - Click on the "Clear Table" button to clear all processes from the table.

7. **Calculating Scheduling Results**:
   - Select a scheduling algorithm from the dropdown menu.
   - Click on the "Calculate" button to compute scheduling results.
   - Scheduling results, including turnaround time, waiting time, and completion time, will be displayed in the table.

8. **Exporting Scheduler Results to CSV**:
   - After computing scheduling results, click on the "Export to CSV" button to export the results to a CSV file.

---
