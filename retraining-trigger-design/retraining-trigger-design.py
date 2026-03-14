def retraining_policy(daily_stats, config):
    """
    Decide which days to trigger model retraining.
    """

    output = []
    days_since_retrain = config["cooldown"]
    retrain_budget = config["budget"]

    for stat in daily_stats:
    
        if (
            stat["drift_score"] > config["drift_threshold"] or 
            stat["performance"] < config["performance_threshold"] or 
            days_since_retrain >= config["max_staleness"]
        ):
            if (
                days_since_retrain >= config["cooldown"] and 
                retrain_budget >= config["retrain_cost"]
            ):
                output.append(stat["day"])
                days_since_retrain = 0
                retrain_budget -= config["retrain_cost"]

        days_since_retrain += 1

    return sorted(output)
        
    # Write code here
    pass