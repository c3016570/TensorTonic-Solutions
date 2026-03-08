def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    total_reference_counts = sum(reference_counts)
    total_production_counts = sum(production_counts)
    reference_normalized = [count/total_reference_counts for count in reference_counts]
    production_normalized = [count/total_production_counts for count in production_counts]
    num = len(reference_counts)
    diff_sum = 0
    
    for i in range(num):
        diff_sum = diff_sum +  abs(production_normalized[i] - reference_normalized[i])

        
    tvd = float(diff_sum / 2)
    drift_detected = False
    
    if tvd > threshold:
        drift_detected = True

    dict = {}
    
    dict["score"] = tvd
    dict["drift_detected"] = drift_detected
    return dict
        # Write code here
    pass