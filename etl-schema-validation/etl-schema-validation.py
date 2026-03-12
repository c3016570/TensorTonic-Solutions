def validate_records(records, schema):
    """
    Validate records against a schema definition.
    """
    
    output = []
    for i,record in enumerate(records):
        errors = []
    
        for ele in schema:
            column = ele["column"]
            if column not in record:
                errors.append(f"{column}: missing")
            elif record[column] is None:
                if ele["nullable"] is False:
                    errors.append(f"{column}: null")
            else:
                expected_type = ele["type"]
                actual_type = type(record[column]).__name__

                type_valid = True
                if actual_type != expected_type:
                    if not (expected_type == "float" and actual_type == "int"):
                        errors.append(f"{column}: expected {expected_type}, got {actual_type}")
                        type_valid = False
                        
                if type_valid == True:
                    if "min" in ele and "max" in ele:
                        if record[column] > ele["max"] or record[column] < ele["min"]:
                            errors.append(f"{column}: out of range")
                            
        is_valid = len(errors) == 0
        thistuple = (i, is_valid, errors)
        output.append(thistuple)
            
    return output     
                           
    # Write code here
    pass