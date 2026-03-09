def deduplicate(records, key_columns, strategy):
    """
    Deduplicate records by key columns using the given strategy.
    """

    output = {}

    for record in records:
        key = tuple(record[col] for col in key_columns)
        
        if strategy == "first":
            if key not in output:
                output[key] = record
                
        elif strategy == "last":
            output[key] = record

        elif strategy == "most_complete":
            none_count = sum(1 for v in record.values() if v is None)
            if key not in output:
                output[key] = record
            else:
                existing_none = sum(1 for v in output[key].values() if v is None)
                if none_count < existing_none:
                    output[key] = record
                
    return list(output.values())
        
    # Write code here
    pass