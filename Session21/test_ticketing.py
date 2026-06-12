import pytest
from BTTH_ss20 import calculate_revenue
def test_revenue_booked_and_cancelled_tickets():
    ticket_db = [
        {"ticket_id": "T01", "buyer_name": "Nguyen Van A", "price": 500.0, "status": "Booked", "seat": ("A", 1)},
        {"ticket_id": "T02", "buyer_name": "Tran Thi B", "price": 300.0, "status": "Cancelled", "seat": ("B", 5)},
        {"ticket_id": "T03", "buyer_name": "Le Van C", "price": 500.0, "status": "Booked", "seat": ("A", 2)}
    ]
    result = calculate_revenue(ticket_db)
    assert result == 1000.0

def test_revenue_with_empty_list():
    ticket_db = []
    result = calculate_revenue(ticket_db)
    assert result == 0.0