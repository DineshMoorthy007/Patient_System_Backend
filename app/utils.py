def calculate_priority(age, condition_severity):
    """
    Calculate patient priority based on age and condition severity
    Condition severity should be a number from 1-5
    """
    age_factor = 1
    if age < 12 or age > 65:
        age_factor = 1.5
        
    return int(condition_severity * age_factor)