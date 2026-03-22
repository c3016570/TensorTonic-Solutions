def schedule_pipeline(tasks, resource_budget):
    """
    Schedule ETL tasks respecting dependencies and resource limits.
    """
    waiting = []
    ready = []
    running = []
    completed = []
    
    start_time = 0
    output = []

    for task in tasks :
        task["finish_time"] = None
        if task["depends_on"] == []:
            ready.append(task)
        else:
            waiting.append(task)

    ready.sort(key=lambda x : x["name"])

    current_usage = 0  

    while True:
        if not ready and not waiting:
            break

        if not ready and not running:
            continue

        for item in ready[:]:
            
            if current_usage + item["resources"] <= resource_budget:
                running.append(item)
                ready.remove(item)
                item["finish_time"] = start_time + item["duration"]
                current_usage = current_usage + item["resources"]
                output.append((item["name"], start_time))

        if running:
                start_time = min(item["finish_time"] for item in running)


        for item in running[:]:
            if item["finish_time"] <= start_time:
                completed.append(item)
                running.remove(item)
                current_usage = current_usage - item["resources"]

        completed_names = [t["name"] for t in completed]
        for task in waiting[:]:
            if all(dep in completed_names for dep in task["depends_on"]): 
                ready.append(task)
                waiting.remove(task)

        if not ready and not running and not waiting:
            break

    return output

    