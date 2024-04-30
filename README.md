**Process Scheduling Application Report**

---

**Introduction**

The project is about a process scheduling application developed as part of the Operating Systems course at the University UM6P College of Computing. This assignment aims to provide us with a practical understanding of process scheduling algorithms by implementing a tools for analysis and experimentation. The application facilitates the study of various scheduling algorithms, including First-Come, First-Served (FCFS), Shortest Job First (SJF), Priority Scheduling (Preemptive/Non-preemptive), Round Robin (RR), and Priority-based Round Robin.

Designed to be user-friendly and informative, the application offers features such as importing processes from CSV files, generating random processes, and manually inputting processes. Through its intuitive interface and comprehensive functionality, this application serves as a valuable resource to explore and analyze different scheduling algorithms, gain insights into process management, and deepen our understanding of operating systems concepts.

---

### 2. Design Choices

#### 2.1 User Interface:
The application features a user-friendly interface built with HTML, CSS, and JavaScript. Bootstrap framework is used for responsive design and styling. The user interface includes input fields for specifying process parameters, buttons for importing, generating, and clearing processes, and a table for displaying process data and scheduling results.

#### 2.2 Functionality:
The application supports multiple functionalities, including importing processes from CSV files, generating random processes based on user-defined parameters, manually inputting processes with validation checks, clearing the process table, and analyzing scheduling results.

#### 2.3 Backend:
The backend is implemented using Flask, a lightweight Python web framework. It handles HTTP requests, processes data, and computes scheduling results using various scheduling algorithms.

#### 2.4 Scheduling Algorithms:
The application supports several scheduling algorithms, including First-Come, First-Served (FCFS), Shortest Job First (SJF), Priority Scheduling, Round Robin (RR), and Priority-based Round Robin. Each algorithm is implemented as a separate function and is invoked based on user selection.

---

### 3. Implementation Details

#### Client-Server Architecture ####

This application operates as a client-server architecture, where the client side consists of a web-based user interface and the server side performs the computation of scheduling results using various scheduling algorithms. After receiving input data from the client, such as process information and selected scheduling algorithm, the server processes the data, performs the scheduling algorithms' computations, and sends back the results to the client. The client then renders the scheduling results in a user-friendly format, providing users with insights into process scheduling performance and characteristics. This client-server model enables seamless interaction between users and the scheduling algorithms, facilitating experimentation and analysis of different scheduling strategies.

#### 3.1 Frontend:
- HTML, CSS, and JavaScript are used for building the frontend.
- JavaScript functions handle user interactions, form validations, and dynamic updates of the process table.

#### 3.2 Backend:
- Flask routes handle HTTP requests, process data, and compute scheduling results.
- Scheduling algorithms are implemented as Python functions and called based on user selections.

#### 3.3 Data Handling:
- Process data is represented using JSON format for communication between frontend and backend.
- CSV parsing is implemented to extract process data from CSV files.

#### 3.4 Data Validation:
- Input data undergoes validation checks to ensure integrity and reliability.
- Duplicate process IDs are not allowed in the list of processes.
- Priority, arrival times, and burst times must be positive integers, with burst time larger than 0, to adhere to scheduling algorithm requirements.
These implementation details ensure that the application operates efficiently and securely, providing users with a robust platform for exploring and analyzing process scheduling strategies.
---

### 4. Usage Scenarios

#### 4.1 Importing Processes from CSV:
- Users can import processes from CSV files containing columns for process ID, arrival time, burst time, and optional priority.
- The application checks for the presence of a priority column and adjusts the UI accordingly.

#### 4.2 Generating Random Processes:
- Users can specify the number of processes, arrival time range, burst time range, and priority range (if applicable) to generate random processes.
- Random processes are added to the table for analysis.

#### 4.3 Manual Input of Processes:
- Users can input processes manually via the input form.
- The application validates user input, ensuring data integrity and consistency.

#### 4.4 Analyzing Scheduling Results:
After adding processes, users can select a scheduling algorithm and click the "Calculate" button to compute scheduling results. The application displays scheduling results in the table, including turnaround time, waiting time, and completion time for each process. Additionally, the application computes the average turnaround time, average waiting time, and CPU utilization, providing users with comprehensive insights into the performance of the scheduling algorithm.

Moreover, the application also plots a Gantt chart, highlighting the details of the execution of processes, with each process displaying its start and end time. This visualization allows users to visualize the scheduling of processes over time, facilitating a better understanding of the scheduling algorithm's behavior.

Furthermore, the application provides a pie chart illustrating CPU utilization, indicating the proportion of CPU time used and unused. This visualization aids users in assessing the efficiency of the scheduling algorithm in utilizing CPU resources effectively.

#### 4.5 Exporting Scheduling Results to CSV:
Users have the option to export the scheduling results table to a CSV file for further analysis and documentation. This feature enhances the usability of the application by allowing users to save and share scheduling results with others or import them into external tools for additional processing.


These features collectively enhance the user experience by providing detailed and visual representations of scheduling results, enabling users to make informed decisions and comparisons between different scheduling algorithms.
##### 4.4.1 Example of Gantt Chart
![Gantt Chart Example](https://github.com/AminIdr/CPU-Scheduler-Simulation/blob/main/images/gantt.png?raw=true)
##### 4.4.2 Example of CPU Utilization Pie Chart
![CPU Utilization](https://github.com/AminIdr/CPU-Scheduler-Simulation/blob/main/images/cpu-utilization.png?raw=true)
---

### 7. Testing

In this section, we will perform several test cases to demonstrate the correct implementation of the scheduling algorithms.

#### 7.1 Non-Priority Based Algorithms

For this subsection, we will use the following example test case:

![Non-priority Test Case](https://github.com/AminIdr/CPU-Scheduler-Simulation/blob/main/images/nonpriority-test.png?raw=true)

##### 7.1.1 First-Come, First-Served (FCFS)

The FCFS algorithm works by executing processes in the order they arrive, with no preemption. Here's a screenshot of the scheduling results applied to the test case:

![FCFS Results](https://github.com/AminIdr/CPU-Scheduler-Simulation/blob/main/images/fcfs1.png?raw=true)
![FCFS Results](https://github.com/AminIdr/CPU-Scheduler-Simulation/blob/main/images/fcfs2.png?raw=true)

##### 7.1.2 Shortest Job First (SJF)

The SJF algorithm selects the process with the shortest burst time for execution first, resulting in minimized average waiting time. Here's a screenshot of the scheduling results applied to the test case:

![SJF Results](https://github.com/AminIdr/CPU-Scheduler-Simulation/blob/main/images/sjf1.png?raw=true)
![SJF Results](https://github.com/AminIdr/CPU-Scheduler-Simulation/blob/main/images/sjf2.png?raw=true)

##### 7.1.3 Round Robin (RR)

The Round Robin algorithm allocates a fixed time slice (quantum) to each process in a cyclic manner, allowing fair execution among processes. Here's a screenshot of the scheduling results applied to the test case with a quantum set to 2:

![Round Robin Results](https://github.com/AminIdr/CPU-Scheduler-Simulation/blob/main/images/rr1.png?raw=true)
![Round Robin Results](https://github.com/AminIdr/CPU-Scheduler-Simulation/blob/main/images/rr2.png?raw=true)

#### 7.2 Priority-Based Algorithms

For this subsection, we will use the following test case and evaluate the priority-based scheduling algorithms:
![Priority Test Case](https://github.com/AminIdr/CPU-Scheduler-Simulation/blob/main/images/priority-test.png?raw=true)

##### 7.2.1 Priority Non-Preemptive

The Priority Non-Preemptive algorithm executes the highest priority process in the ready queue without preemption, allowing the currently running process to complete its execution. Here's a screenshot of the scheduling results applied to the test case:

![Priority Non-Preemptive Results](https://github.com/AminIdr/CPU-Scheduler-Simulation/blob/main/images/nonpreemptive1.png?raw=true)
![Priority Non-Preemptive Results](https://github.com/AminIdr/CPU-Scheduler-Simulation/blob/main/images/nonpreemptive2.png?raw=true)

##### 7.2.2 Priority Preemptive

The Priority Preemptive algorithm executes the highest priority process currently in the ready queue, preempting lower priority processes if necessary. Here's a screenshot of the scheduling results applied to the test case:

![Priority Preemptive Results](https://github.com/AminIdr/CPU-Scheduler-Simulation/blob/main/images/preemptive1.png?raw=true)
![Priority Preemptive Results](https://github.com/AminIdr/CPU-Scheduler-Simulation/blob/main/images/preemptive2.png?raw=true)


##### 7.2.3 Priority based Round Robin

The Priority with Round Robin algorithm combines priority-based scheduling with Round Robin, allowing processes with the same priority level to share CPU time fairly. Here's a screenshot of the scheduling results applied to the test case with a quantum set to 2:

![Priority with Round Robin Results](https://github.com/AminIdr/CPU-Scheduler-Simulation/blob/main/images/prr1.png?raw=true)
![Priority with Round Robin Results](https://github.com/AminIdr/CPU-Scheduler-Simulation/blob/main/images/prr2.png?raw=true)

---

### 6. Conclusion

This CPU Scheduling Simulator application provides a comprehensive platform for studying and analyzing process scheduling algorithms. By offering features such as importing processes from CSV, generating random processes, and manually inputting processes, users can explore different scenarios and evaluate the performance of scheduling algorithms. With a user-friendly interface and robust backend implementation, the application facilitates learning, experimentation, and research in the field of operating systems and process management.
