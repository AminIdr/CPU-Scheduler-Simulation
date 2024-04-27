def fcfs(processes):
    """
    Simulates First-Come, First-Served (FCFS) scheduling algorithm.

    Args:
        processes (list): List of Process objects.

    Returns:
        list: List of Process objects representing the order in which processes are scheduled.
    """
    # Sort processes based on arrival time
    sorted_processes = sorted(processes, key=lambda x: x.arrival_time)

    # Initialize scheduler and current time
    scheduler = []
    current_time = 0

    # Schedule processes in order of arrival
    for process in sorted_processes:
        # If process arrives after current time, wait until it arrives
        if process.arrival_time > current_time:
            current_time = process.arrival_time
        # Update current time to finish time of this process
        current_time += process.burst_time
        # Record process completion time
        process.completion_time = current_time
        # Add process to scheduler
        scheduler.append(process)

    return scheduler
