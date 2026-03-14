def evaluate_shadow(production_log, shadow_log, criteria):
    """
    Evaluate whether a shadow model is ready for promotion.
    """
    output = {}
    metrics = {}

    
    production_log_count = len(production_log)
    shadow_log_count = len(shadow_log)

    shadow_latency = []
    shadow_prediction = []
    correct = 0
    for input in shadow_log:
        shadow_prediction.append(input["prediction"])
        wrong = 0
        if input["prediction"] == input["actual"]:
            correct += 1
        else:
            wrong += 1
        shadow_latency.append(input["latency_ms"])
    shadow_accuracy = correct / shadow_log_count

    metrics["shadow_accuracy"] = shadow_accuracy

    correct = 0

    production_prediction = []
    for input in production_log:
        production_prediction.append(input["prediction"])
        wrong = 0
        if input["prediction"] == input["actual"]:
            correct += 1
        else:
            wrong += 1
    production_accuracy = correct / production_log_count

    metrics["production_accuracy"] = production_accuracy

    accuracy_gain = shadow_accuracy - production_accuracy

    metrics["accuracy_gain"] = accuracy_gain

    index = math.ceil(0.95 * production_log_count) - 1

    sorted_shadow_latency = sorted(shadow_latency)

    shadow_latency_p95 = shadow_latency[index]

    metrics["shadow_latency_p95"] = shadow_latency_p95

    count = 0

    for i, j in zip(production_prediction, shadow_prediction):
        if i == j:
            count += 1

    agreement_rate = count/production_log_count

    metrics["agreement_rate"] = agreement_rate

    promote = True

    if accuracy_gain >= criteria["min_accuracy_gain"]:
        if shadow_latency_p95 <= criteria["max_latency_p95"]:
            if agreement_rate >= criteria["min_agreement_rate"]:
                promote = True
            else:
                promote = False
        else:
            promote = False
    else:
        promote = False

    
    output["promote"] = promote
    output["metrics"] = metrics

    return output
            
    # Write code here
    pass