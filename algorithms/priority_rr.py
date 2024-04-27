from collections import defaultdict, deque

def priority_round_robin(processes, quantum):
    """
    Simulates Priority-based Round Robin scheduling algorithm using separate queues for each priority level.

    Args:
        processes (list): List of Process objects.
        quantum (int): Time quantum for each process.

    Returns:
        list: List of Process objects representing the order in which processes are scheduled.
    """
    # Initialize scheduler, current time, and temporary list
    scheduler = []
    current_time = 0
    tmp = []

    # Create separate queues for each priority level
    priority_queues = defaultdict(deque)
    processes.sort(key=lambda x: x.arrival_time)
    # Convert the list of processes into a deque for efficient removal from the front
    process_queue = deque(processes)

    # Keep track of the currently running process and remaining time quantum
    current_process = None
    remaining_quantum = 0

   
    # Loop until all processes are completed
    while process_queue or any(priority_queues.values()) or current_process:

        # Check for arriving processes
        while process_queue and process_queue[0].arrival_time <= current_time:
            new_process = process_queue.popleft()
            priority_queues[new_process.priority].append(new_process)

        # If there's no current process or its time quantum is exhausted, select the highest priority non-empty queue
        if not current_process or remaining_quantum <= 0:
            for priority in sorted(priority_queues.keys()):
                if priority_queues[priority]:
                    current_process = priority_queues[priority].popleft()
                    remaining_quantum = quantum
                    break
            else:
                # No process is available, jump to the next arrival time
                current_time = process_queue[0].arrival_time
                continue

        # Execute process for the given quantum or until completion
        execution_time = min(remaining_quantum, current_process.burst_time)
        current_time += execution_time
        remaining_quantum -= execution_time
        current_process.burst_time -= execution_time
        scheduler.append(current_process)

        # Record process completion time if completed
        if current_process.burst_time <= 0:
            current_process.completion_time = current_time
            current_process = None

        # Add process to scheduler
        tmp.append(current_time)

        while process_queue and process_queue[0].arrival_time <= current_time:
            new_process = process_queue.popleft()
            priority_queues[new_process.priority].append(new_process)

        # If the time quantum is exhausted, put the current process back in its queue
        if remaining_quantum <= 0 and current_process:
            priority_queues[current_process.priority].append(current_process)
            current_process = None

    return scheduler, tmp