def calculate_discount(order_amount, total_spent_before):
    # Tính tổng giá trị sau khi cộng đơn hàng mới
    total_accumulated = order_amount + total_spent_before
    
    if total_accumulated >= 50000000:
        return 0.1
    else:
        return 0
