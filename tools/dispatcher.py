# tools/dispatcher.py
from typing import Dict, Any
from . import mock_apis

def execute_tool(action: str, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Map high-level action names to specific mock functions.
    """
    user_id = params.get("user_id")
    if action == "get_summary":
        return mock_apis.get_summary(user_id)
    if action == "block_card":
        return mock_apis.block_card(user_id)
    if action == "pay_bill":
        amount = float(params.get("amount", 0))
        return mock_apis.pay_bill(user_id, amount)
    if action == "list_recent_transactions":
        limit = int(params.get("limit", 5))
        return mock_apis.list_recent_transactions(user_id, limit)

    return {"success": False, "message": f"Unknown action: {action}"}
