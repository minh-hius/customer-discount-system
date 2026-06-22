import pytest
from discount import calculate_discount

def test_vip_customer():
    # TC01: Đã là khách VIP (60M), đơn mới 2M -> Giảm 10%
    assert calculate_discount(2000000, 60000000) == 0.1 

def test_normal_customer():
    # TC02: Chưa đủ điều kiện (30M), đơn mới 2M -> Không giảm (0)
    assert calculate_discount(2000000, 30000000) == 0 

def test_boundary_case():
    # TC03: Cận biên (49M), đơn mới 2M làm tổng đạt 51M -> Phải giảm 10%
    # Đây là test case quan trọng nhất để phát hiện bug [3]
    assert calculate_discount(2000000, 49000000) == 0.1 