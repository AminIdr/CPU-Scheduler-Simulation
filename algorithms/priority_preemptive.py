def priority_preemptive(processes):
    current_time = 0
    n = len(processes)
    completed_processes = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    queue = []
    execution_order = []
    remaining_time = {p.pid: p.burst_time for p in processes}

    while completed_processes < n:
        available_processes = [p for p in processes if p.arrival_time <= current_time and remaining_time[p.pid] > 0]
        if available_processes:
            highest_priority_process = min(available_processes, key=lambda x: x.priority)
            queue.append(highest_priority_process)

            if len(queue) > 1 and highest_priority_process != queue[-2]:
                total_waiting_time += current_time - queue[-2].arrival_time

            remaining_time[highest_priority_process.pid] -= 1
            execution_order.append(highest_priority_process)

            if remaining_time[highest_priority_process.pid] == 0:
                completed_processes += 1
                total_turnaround_time += current_time - highest_priority_process.arrival_time + 1
                highest_priority_process.completion_time = current_time + 1

            current_time += 1
        else:
            current_time += 1

    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    return  execution_order, avg_waiting_time, avg_turnaround_time