def calculate_discount(previous_revenue: float, new_order_value: float = 0.0) -> float:
    """
    Calculate the discount rate based on customer purchase history in the current year.
    - If previous_revenue is 50,000,000 or more, the customer is already a loyal customer, returning 0.1.
    - If previous_revenue + new_order_value is 50,000,000 or more, the new order qualifies the customer for loyal status, returning 0.1.
    - Otherwise, return 0.0.
    """
    if previous_revenue >= 50000000 or (previous_revenue + new_order_value) >= 50000000:
        return 0.1
    return 0.0
