def feature_store_lookup(feature_store, requests, defaults):
    """
    Join offline user features with online request-time features.
    """
    output = []
    for request in requests:
        d = {}
        user_id = request["user_id"]
        if user_id in feature_store:
            d.update(feature_store[user_id])
        else:
            d.update(defaults)
        
        d.update(request["online_features"])
    
        output.append(d)

    return output 
    # Write code here
    pass