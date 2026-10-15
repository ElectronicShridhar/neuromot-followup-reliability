"""
Transparent, rule-based priority scoring.
Weights are ILLUSTRATIVE and not clinically validated.
"""

SCORE_TABLE = {
    "failed_teachback": 40,
    "passed_teachback": 5,
    "no_phone": 35,
    "shared_phone": 20,
    "outstation": 15,
    "high_urgency": 25,
    "routine": 5,
}

def calculate_score(teachback_result: str, contact_status: str, 
                    outstation: bool, urgency: str | None) -> tuple[int, list[str]]:
    score = 0
    reasons = []

    if teachback_result == "Fail":
        score += SCORE_TABLE["failed_teachback"]
        reasons.append("Failed teach-back")
    else:
        score += SCORE_TABLE["passed_teachback"]
        reasons.append("Passed teach-back")

    if contact_status in ("none", "unreachable"):
        score += SCORE_TABLE["no_phone"]
        reasons.append("No phone / unreachable")
    elif contact_status == "shared":
        score += SCORE_TABLE["shared_phone"]
        reasons.append("Shared phone number")

    if outstation:
        score += SCORE_TABLE["outstation"]
        reasons.append("Outstation patient")

    if urgency and "high" in urgency.lower():
        score += SCORE_TABLE["high_urgency"]
        reasons.append("Clinician urgency: High")
    elif urgency and "routine" in urgency.lower():
        score += SCORE_TABLE["routine"]
        reasons.append("Clinician urgency: Routine")

    return score, reasons


# Ramesh example from SRS
if __name__ == "__main__":
    score, reasons = calculate_score(
        teachback_result="Fail",
        contact_status="none",
        outstation=True,
        urgency="high risk"
    )
    print(f"Ramesh score = {score}")
    print("Reasons:", reasons)
    assert score == 115
