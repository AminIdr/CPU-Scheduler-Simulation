def priority_preemptive(processes):
    """
    Simulates Priority Preemptive scheduling algorithm.

    Args:
        processes (list): List of Process objects.

    Returns:
        list: List of tuples containing Process objects, turnaround times, and waiting times.
        list: List representing the order of process execution.
        float: Average turnaround time.
        float: Average waiting time.
        float: CPU utilization.
    """
    # Initialize variables
    current_time = 0
    n = len(processes)
    completed_processes = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    queue = []  # Queue to hold processes
    execution_order = []  # Tracks the order of process execution
    remaining_time = {p.pid: p.burst_time for p in processes}  # Dictionary to track remaining burst time for each process
    scheduler = []  # Stores scheduling information for each process

    # Main loop until all processes are completed
    while completed_processes < n:
        # Select processes that have arrived and still have remaining burst time
        available_processes = [p for p in processes if p.arrival_time <= current_time and remaining_time[p.pid] > 0]
        
        if available_processes:
            # Select process with the highest priority among available ones
            highest_priority_process = min(available_processes, key=lambda x: x.priority)
            
            # Add process to the queue
            queue.append(highest_priority_process)
            # Decrease remaining time for the selected process
            remaining_time[highest_priority_process.pid] -= 1
            
            # Update execution order for the gantt chart
            if(execution_order and execution_order[-1][0] == highest_priority_process.pid):
                execution_order[-1][2] += 1
            else:
                execution_order.append([highest_priority_process.pid, current_time, current_time + 1])
            
            # Increment current time
            current_time += 1
            
            # If the remaining time for the process becomes zero, mark it as completed
            if remaining_time[highest_priority_process.pid] == 0:
                completed_processes += 1
                # Calculate turnaround time and waiting time for the completed process
                turnaround_time = current_time - highest_priority_process.arrival_time 
                total_turnaround_time += turnaround_time
                waiting_time = turnaround_time - highest_priority_process.burst_time
                total_waiting_time += waiting_time
                # Update completion time for the process
                highest_priority_process.completion_time = current_time 
                # Store process information in the scheduler list
                scheduler.append([highest_priority_process, turnaround_time, waiting_time])
        else:
            # If no process is available, increment current time
            current_time += 1
    
    # Calculate average waiting time, average turnaround time, and CPU utilization
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n
    cpu_utilization = (total_turnaround_time - total_waiting_time) / current_time * 100
    
    # Return scheduling information
    return scheduler, execution_order, avg_turnaround_time, avg_waiting_time, cpu_utilization
