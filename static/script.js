document.addEventListener('DOMContentLoaded', function() {
    // Variable to store the selected algorithm
    let selectedAlgorithm = document.getElementById('algorithm').value;

    // Object to track added processes
    let addedProcesses = {};

    // Function to toggle the visibility of the Priority column based on the selected algorithm
    function togglePriorityVisibility() {
        const algorithm = document.getElementById('algorithm').value;
        const priorityInput = document.getElementById('priorityInput');
        const priorityNote = document.getElementById('priorityNote');

        if (algorithm === "priority" || algorithm === "priority_p" || algorithm === "priority_rr") {
            priorityInput.style.display = 'block';
            document.getElementById('newPriority').required = true;

            priorityNote.style.display = 'block';
        } else {
            priorityInput.style.display = 'none';
            document.getElementById('newPriority').required = false;

            priorityNote.style.display = 'none';
        }
    }

    // Function to toggle the visibility of the Quantum input based on the selected algorithm
    function toggleQuantumVisibility() {
        const algorithm = document.getElementById('algorithm').value;
        const quantumInput = document.getElementById('quantumInput');

        if (algorithm === "rr" || algorithm === "priority_rr") {
            quantumInput.style.display = 'block';
            document.getElementById('quantum').required = true;
        } else {
            quantumInput.style.display = 'none';
            document.getElementById('quantum').required = false;
        }
    }

    // Call the togglePriorityVisibility and toggleQuantumVisibility functions to initialize visibility based on the default selected algorithm
    togglePriorityVisibility();
    toggleQuantumVisibility();
    
    // Function to toggle the visibility of the Priority column based on the selected algorithm
    function togglePriorityColumnVisibility() {
        const algorithm = document.getElementById('algorithm').value;
        const priorityColumn = document.getElementById('priorityColumn');

        if (algorithm === "priority" || algorithm === "priority_p" || algorithm === "priority_rr") {
            priorityColumn.style.display = 'table-cell';
        } else {
            priorityColumn.style.display = 'none';
        }
    }

    // Call the togglePriorityColumnVisibility function to initialize the visibility of the priority column based on the default selected algorithm
    togglePriorityColumnVisibility();

    // Add event listener to the algorithm select box to update the selected algorithm variable and toggle priority column visibility
    document.getElementById('algorithm').addEventListener('change', function() {
        togglePriorityVisibility();
        toggleQuantumVisibility();

        const newAlgorithm = this.value;

        // Clear the table when changing from priority-based algorithms to other algorithms or vice versa
        if ((selectedAlgorithm === "priority" || selectedAlgorithm === "priority_p" || selectedAlgorithm === "priority_rr") &&
            (newAlgorithm !== "priority"  && newAlgorithm !== "priority_p" && newAlgorithm !== "priority_rr")) {
            clearTable();
        } else if ((selectedAlgorithm !== "priority" && selectedAlgorithm !== "priority_p" && selectedAlgorithm !== "priority_rr") &&
            (newAlgorithm === "priority" || newAlgorithm === "priority_p" || newAlgorithm === "priority_rr")) {
            clearTable();
        }

        // Update the selected algorithm variable
        selectedAlgorithm = newAlgorithm;

        // Toggle the visibility of the priority column based on the selected algorithm
        togglePriorityColumnVisibility();
    });
    
    // Function to clear the table
    function  clearTable() {
        const processTableBody = document.getElementById('processTableBody');
        var rows = processTableBody.querySelectorAll("tr");
        
        rows.forEach(function(row) {
            row.parentNode.removeChild(row);
        });

        addedProcesses = {};

        processTableBody.innerHTML = ''; // Clear the table body

    }


    // Add event listener to the "Add Process" button to validate input fields before adding a new process
    document.getElementById('addProcess').addEventListener('click', function() {
        const form = document.getElementById('processForm');
        if (form.reportValidity()) {
            // Form is valid, proceed to add the new process to the table
    
            // Get the input field values
            const newProcessId = document.getElementById('newProcessID').value.trim();

            // Check if process with the same ID already exists
            if (addedProcesses[newProcessId]) {
                displayErrorMessage('idError', 'A process with the same ID already exists. Please choose a different ID.');
                return;
            }
            document.getElementById('idError').style.display = 'none';

            // Create a new table row
            const newRow = document.createElement('tr');
    
            // Get the input field values
            const newArrivalTime = document.getElementById('newArrivalTime').value.trim();
            const newBurstTime = document.getElementById('newBurstTime').value.trim();
    
            // Create table data cells and add input field values
            const tdProcessId = document.createElement('td');
            tdProcessId.textContent = newProcessId;
    
            const tdArrivalTime = document.createElement('td');
            tdArrivalTime.textContent = newArrivalTime;
    
            const tdBurstTime = document.createElement('td');
            tdBurstTime.textContent = newBurstTime;
    
            // Append table data cells to the new row
            newRow.appendChild(tdProcessId);
            newRow.appendChild(tdArrivalTime);
            newRow.appendChild(tdBurstTime);
    
            // Check if the priority column is visible and append it if needed
            const algorithm = document.getElementById('algorithm').value;
            if (algorithm === "priority" || algorithm === "priority_p" || algorithm === "priority_rr") {
                const newPriority = document.getElementById('newPriority').value.trim();
                const tdPriority = document.createElement('td');
                tdPriority.textContent = newPriority;
                newRow.appendChild(tdPriority);
            }
    
            // Append the new row to the table body
            document.getElementById('processTableBody').appendChild(newRow);
    
            // Add the process ID to the addedProcesses object
            addedProcesses[newProcessId] = true;

            // Clear the input fields
            document.getElementById('newProcessID').value = '';
            document.getElementById('newArrivalTime').value = '';
            document.getElementById('newBurstTime').value = '';
            document.getElementById('newPriority').value = ''; // Clear priority input if it's visible
        }
    });
    

    document.getElementById('calculate').addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default form submission behavior
    
        // Remove the required attribute from input fields
        document.getElementById('newProcessID').removeAttribute('required');
        document.getElementById('newArrivalTime').removeAttribute('required');
        document.getElementById('newBurstTime').removeAttribute('required');
        document.getElementById('newPriority').removeAttribute('required');
    
        // Check if addedProcesses array is not empty
        if (Object.keys(addedProcesses).length === 0) {
            displayErrorMessage('noProcessError', 'Please add processes before calculating.');
            return;
        }
        document.getElementById('noProcessError').style.display = 'none';
    
        // Retrieve data from the table and construct a JSON object
        const processRows = document.querySelectorAll('#processTableBody tr');
        const processes = [];
    
        processRows.forEach(row => {
            const process = {};
            const cells = row.querySelectorAll('td');
            process.pid = cells[0].textContent;
            process.arrival_time = cells[1].textContent;
            process.burst_time = cells[2].textContent;
    
            // Check if priority column is present and add priority if needed
            const algorithm = document.getElementById('algorithm').value;
            if (algorithm === "priority" || algorithm === "priority_p" || algorithm === "priority_rr") {
                process.priority = cells[3].textContent;
            }
    
            processes.push(process);
        });

        let quantum = null;
       // Check if quantum is needed based on the selected algorithm
        if (selectedAlgorithm === "rr" || selectedAlgorithm === "priority_rr") {
            quantum = document.getElementById('quantum').value.trim();
        }

        // Construct the request data object
        const requestData = {
            algorithm: selectedAlgorithm,
            processes: processes
        };

        // Add quantum to request data if needed
        if (quantum !== null) {
            requestData.quantum = quantum;
        }
    
        // Send the data to the server using a POST request
        fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestData)
        })
        .then(response => {
            if (response.ok) {
                // Process the response from the server if needed
                // For now, let's just log a success message
                console.log("Processes sent successfully to server.");
        
                // Parse the response JSON data
                return response.json();
            } else {
                console.error("Failed to send processes to server.");
            }
        })
        .then(data => {
            displaySchedulerResults(data.schedulerResults, data.avgTurnaroundTime, data.avgWaitingTime, data.cpuUtilization);
            // Convert data.detailedSchedulerResults into tasks array
            const tasks = data.detailedSchedulerResults.map(task => {
                return {
                    task: task[0], // Task name
                    startDate: task[1], // Start date
                    endDate: task[2] // End date
                };
            });
            // Call createGanttChart function with the tasks array
            createGanttChart(tasks);
        })
        .catch(error => {
            console.error("Error sending processes to server:", error);
        });
    });
    
    function displayErrorMessage(error, message) {
        const errorMessage = document.getElementById(error);
        errorMessage.textContent = message;
        errorMessage.style.display = 'inline';
    }

    function displaySchedulerResults(schedulerResults, avgTurnaroundTime, avgWaitingTime, cpuUtilization) {
        // Get the table body element
        const tableBody = document.getElementById('schedulerResults');
    
        // Clear existing rows
        tableBody.innerHTML = '';
        
        // Loop through scheduler results and create rows in the table
        schedulerResults.forEach(result => {
            // Convert values to integers
            const processId = parseInt(result[0]);
            const completionTime = parseInt(result[1]);
            const turnaroundTime = parseInt(result[2]);
            const waitingTime = parseInt(result[3]);
    
            // Create a new row
            const row = document.createElement('tr');
    
            // Create cells for each data item in the result tuple
            const processIdCell = document.createElement('td');
            processIdCell.textContent = processId;
            const completionTimeCell = document.createElement('td');
            completionTimeCell.textContent = completionTime;
            const turnaroundTimeCell = document.createElement('td');
            turnaroundTimeCell.textContent = turnaroundTime;
            const waitingTimeCell = document.createElement('td');
            waitingTimeCell.textContent = waitingTime;
    
            // Append cells to the row
            row.appendChild(processIdCell);
            row.appendChild(completionTimeCell);
            row.appendChild(turnaroundTimeCell);
            row.appendChild(waitingTimeCell);
    
            // Append row to the table body
            tableBody.appendChild(row);
        });
    }
    
    function createGanttChart(tasks) {
        // Clear the existing chart
        d3.select("#chart").select("svg").remove();
    
        // Set up the dimensions of the chart
        const margin = { top: 30, right: 30, bottom: 30, left: 60 };
        const width = 800 - margin.left - margin.right;
        const height = 100 - margin.top - margin.bottom; // Reduced height for a single row
    
        // Create the SVG element
        const svg = d3.select("#chart")
            .append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", `translate(${margin.left},${margin.top})`);
    
        // Create scales for x axis
        const xScale = d3.scaleLinear()
            .domain([0, d3.max(tasks, d => d.endDate)])
            .range([0, width]);
    
        // Add x axis with ticks at start and end dates
        svg.append("g")
            .attr("transform", `translate(0,${height})`)
            .call(d3.axisBottom(xScale)
                .tickValues([0, ...tasks.flatMap(d => [d.startDate, d.endDate])]) // Include 0 as a tick value
                .tickFormat(d3.format("d"))); // Display tick values as integers
    
        // Add borders between tasks
        svg.selectAll(".task-border")
            .data(tasks)
            .enter().append("rect")
            .attr("class", "task-border")
            .attr("x", d => xScale(d.startDate))
            .attr("y", 0) // Adjusted y position
            .attr("width", d => xScale(d.endDate) - xScale(d.startDate))
            .attr("height", height) // Adjusted height of the boxes
            .attr("fill", "none")
            .attr("stroke", "black")
            .attr("stroke-width", 1);
    
        // Add bars for tasks
        svg.selectAll(".task")
            .data(tasks)
            .enter().append("rect")
            .attr("class", "task")
            .attr("x", d => xScale(d.startDate) + 1) // Adjusted x position to create borders
            .attr("y", 1) // Adjusted y position to create borders
            .attr("width", d => xScale(d.endDate) - xScale(d.startDate) - 2) // Adjusted width to create borders
            .attr("height", height - 2) // Adjusted height to create borders
            .append("title")
            .text(d => d.task);
    
        // Add task labels
        svg.selectAll(".task-label")
            .data(tasks)
            .enter().append("text")
            .attr("class", "task-label")
            .attr("x", d => (xScale(d.startDate) + xScale(d.endDate)) / 2)
            .attr("y", height / 2)
            .text(d => d.task);
    }
    
    
    

});
