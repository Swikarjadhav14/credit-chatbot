# tools/mock_apis.py
from datetime import date
from typing import Dict, Any, List

USERS: Dict[str, Dict[str, Any]] = {
    "user_123": {
        "name": "Alex",
        "card_last4": "4321",
        "status": "active",
        "credit_limit": 100000,
        "available_limit": 65000,
        "current_outstanding": 35000,
        "due_date": str(date.today().replace(day=25)),
        "overdue": False,
        "transactions": [
            {"id": "txn_001", "amount": 1500, "merchant": "Amazon", "date": "2025-12-01"},
            {"id": "txn_002", "amount": 2000, "merchant": "Uber", "date": "2025-12-03"},
        ],
    }
}

def get_summary(user_id: str) -> Dict[str, Any]:
    user = USERS.get(user_id)
    if not user:
        return {"success": False, "message": "User not found"}
    return {"success": True, "data": user}

def block_card(user_id: str) -> Dict[str, Any]:
    user = USERS.get(user_id)
    if not user:
        return {"success": False, "message": "User not found"}
    user["status"] = "blocked"
    return {
        "success": True,
        "message": "Your card has been blocked.",
        "status": user["status"],
    }

def pay_bill(user_id: str, amount: float) -> Dict[str, Any]:
    user = USERS.get(user_id)
    if not user:
        return {"success": False, "message": "User not found"}
    user["current_outstanding"] = max(user["current_outstanding"] - amount, 0)
    user["available_limit"] += amount
    return {
        "success": True,
        "message": f"Payment of ₹{amount:.2f} received.",
        "current_outstanding": user["current_outstanding"],
        "available_limit": user["available_limit"],
    }

def list_recent_transactions(user_id: str, limit: int = 5) -> Dict[str, Any]:
    user = USERS.get(user_id)
    if not user:
        return {"success": False, "message": "User not found"}
    txns: List[Dict[str, Any]] = user["transactions"][:limit]
    return {"success": True, "transactions": txns}
