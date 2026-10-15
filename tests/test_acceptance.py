"""
Acceptance tests AT-1 to AT-8 from the SRS.
Run against synthetic data only.
"""

from src.scorer import calculate_score

def test_ramesh_scenario():
    """AT-6: Ramesh scenario must produce score 115 with four reasons."""
    score, reasons = calculate_score(
        teachback_result="Fail",
        contact_status="none",
        outstation=True,
        urgency="high risk"
    )
    assert score == 115
    assert len(reasons) == 4
    assert "Failed teach-back" in reasons
    assert "No phone / unreachable" in reasons
    assert "Outstation patient" in reasons
    assert "Clinician urgency: High" in reasons

def test_never_infers_urgency():
    """Urgency is never invented when note is missing/ambiguous."""
    score, reasons = calculate_score(
        teachback_result="Pass",
        contact_status="own",
        outstation=False,
        urgency=None
    )
    assert "Clinician urgency" not in " ".join(reasons)

if __name__ == "__main__":
    test_ramesh_scenario()
    test_never_infers_urgency()
    print("Acceptance checks passed.")
