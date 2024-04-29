def priority_preemptive(processes):
    current_time = 0
    n = len(processes)
    completed_processes = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    queue = []
    execution_order = []
    remaining_time = {p.pid: p.burst_time for p in processes}
    scheduler = []
    while completed_processes < n:
        available_processes = [p for p in processes if p.arrival_time <= current_time and remaining_time[p.pid] > 0]
        if available_processes:
            highest_priority_process = min(available_processes, key=lambda x: x.priority)
            queue.append(highest_priority_process)
            remaining_time[highest_priority_process.pid] -= 1
            if(execution_order and execution_order[-1][0] == highest_priority_process.pid):
                execution_order[-1][2] += 1
            else:
                execution_order.append([highest_priority_process.pid, current_time, current_time + 1])
            
            current_time += 1
            if remaining_time[highest_priority_process.pid] == 0:
                completed_processes += 1
                turnaround_time = current_time - highest_priority_process.arrival_time 
                total_turnaround_time += turnaround_time
                waiting_time = turnaround_time - highest_priority_process.burst_time
                total_waiting_time += waiting_time
                highest_priority_process.completion_time = current_time 
                scheduler.append([highest_priority_process, turnaround_time, waiting_time])

        else:
            current_time += 1
    print("Total Waiting Time: ", total_waiting_time)
    avg_waiting_time = total_waiting_time / n
    
    avg_turnaround_time = total_turnaround_time / n
    cpu_utilization = (total_turnaround_time - total_waiting_time) / current_time

    return scheduler, execution_order, avg_turnaround_time, avg_waiting_time, cpu_utilization