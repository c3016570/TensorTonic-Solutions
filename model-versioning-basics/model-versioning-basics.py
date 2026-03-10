def promote_model(models):
    """
    Decide which model version to promote to production.
    """
    num = len(models)
    accuracy = models[0]["accuracy"]
    key = 0
    for i in range(1,num):
        if models[i]["accuracy"] > accuracy :
            accuracy = models[i]["accuracy"]
            key = i
        elif models[i]["accuracy"] == accuracy:
            if models[key]["latency"] == models[i]["latency"]:
                if models[key]["timestamp"] > models[i]["timestamp"]:
                    return models[key]["name"]
                elif models[key]["timestamp"] < models[i]["timestamp"]:
                    return models[i]["name"]
            elif models[key]["latency"] < models[i]["latency"]:
                return models[key]["name"]
            else:
                return models[i]["name"]
        else:
            continue           
            
    return models[key]["name"]
    # Write code here
    pass