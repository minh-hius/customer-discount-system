def calculate_discount(revenue: float) -> float:
    """
    Calculate the discount rate based on customer purchase revenue.
    If revenue is 50,000,000 or more, return 0.1 (10% discount).
    Otherwise, return 0.0 (0% discount).
    """
    if revenue >= 50000000:
        return 0.1
    return 0.0
