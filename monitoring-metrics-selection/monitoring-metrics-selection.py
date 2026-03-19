import math
import operator
def compute_monitoring_metrics(system_type, y_true, y_pred):
    """
    Compute the appropriate monitoring metrics for the given system type.
    """
    output = []
    if system_type == "classification":
        tp = tn = fp = fn = 0
        for i in range(len(y_true)):
            if y_true[i] == 1 and y_pred[i] == 1:
                tp += 1
            elif y_true[i] == 0 and y_pred[i] == 0:
                tn += 1
            elif y_true[i] == 1 and y_pred[i] == 0:
                fn += 1
            elif y_true[i] == 0 and y_pred[i] == 1:
                fp += 1

        if ((tp + tn + fp + fn) == 0):
            accuracy = 0.0
        else:
            accuracy = (tp + tn)/(tp + tn + fp + fn)

        t1 = ("accuracy", accuracy)
            
        if (tp + fp) == 0:
            precision = 0.0
        else:
            precision = tp / (tp + fp)

        t2 = ("precision", precision)
            
        if (tp + fn == 0):
            recall = 0.0
        else:
            recall = tp / (tp + fn)

        t3 = ("recall", recall)
            
        if ((2 * tp) + fp + fn) == 0:
            f1 = 0.0
        else:
            f1 = (2 * tp) /((2 * tp) + fp + fn)

        t4 = ("f1", f1)

        output.append(t1)
        output.append(t2)
        output.append(t3)
        output.append(t4)
        
    elif system_type == "regression":
        summation_mae = 0
        summation_rmse = 0
        for i in range(len(y_true)):
            absolute_value = abs(y_true[i] - y_pred[i])
            summation_mae += absolute_value
            summation_rmse += absolute_value * absolute_value
        if len(y_true) == 0:
            mae = 0.0
            rmse = 0.0
        else:
            mae = summation_mae / len(y_true)
            rmse = math.sqrt(summation_rmse / len(y_true))   

        t1 = ("mae", mae)
        t2 = ("rmse", rmse)

        output.append(t1)
        output.append(t2)
            
    elif system_type == "ranking":
        k = 3
        pairs = list(zip(y_pred, y_true))
        
        pairs.sort(key = lambda x : x[0], reverse = True)

        top_k = pairs[:k]
    
        rel_in_k = sum([rel for _, rel in top_k])
        total_rel = sum(y_true)
        if k == 0:
            p_at_k = 0.0
        else:
            p_at_k = rel_in_k / k

        t1 = ("precision_at_3", p_at_k)
        output.append(t1)

        if total_rel == 0:
            r_at_k = 0.0
        else:
            r_at_k = rel_in_k / total_rel

        t2 = ("recall_at_3", r_at_k)

        output.append(t2)


    return output
    
    # Write code here
    pass