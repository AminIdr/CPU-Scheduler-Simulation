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

        if (algorithm === "priority" || algorithm === "priority_rr") {
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

        if (algorithm === "priority" || algorithm === "priority_rr") {
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
        if ((selectedAlgorithm === "priority" || selectedAlgorithm === "priority_rr") &&
            (newAlgorithm !== "priority" && newAlgorithm !== "priority_rr")) {
            clearTable();
        } else if ((selectedAlgorithm !== "priority" && selectedAlgorithm !== "priority_rr") &&
            (newAlgorithm === "priority" || newAlgorithm === "priority_rr")) {
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
            if (algorithm === "priority" || algorithm === "priority_rr") {
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
            if (algorithm === "priority" || algorithm === "priority_rr") {
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
    

        console.log(requestData);
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
                console.log("Data sent successfully to server.");
                // Log the response from the server
                response.text().then(data => {
                    console.log("Response from server:", data);
                });
            } else {
                console.error("Failed to send data to server.");
            }
        })
        .catch(error => {
            console.error("Error sending data to server:", error);
        });
    });
    
    function displayErrorMessage(error, message) {
        const errorMessage = document.getElementById(error);
        errorMessage.textContent = message;
        errorMessage.style.display = 'inline';
    }
    

});
