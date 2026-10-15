# Follow-Up Reliability Stack

**Team Neuromot** · AI Synergy Hackathon 2026 · Round 1 · Case 03 (Healthcare)

Staff-facing decision-support tool for a high-volume district hospital **without an EHR**.

It helps hospital staff:
1. Confirm patient understanding at discharge (fixed Hindi teach-back)
2. Suggest quieter follow-up dates inside a doctor-set window
3. Produce a ranked, reason-coded worklist for community health workers

**Clinicians stay in charge at every step.**

> Synthetic data only · No patient messaging · No auto-booking · No inferred urgency · No generative medical text

---

## Problem (CASE EVIDENCE)

| Signal | Value |
|--------|-------|
| Daily OPD volume | ~900 visits |
| Missed follow-up window | 28% (3-month sample) |
| Shared household numbers | 19% |
| Unreachable numbers | 7% |

Three failures stack: understanding fails → date is overcrowded → small records team cannot prioritise.

## Solution – Three Layers

| Layer | What the system does | What it never does |
|-------|----------------------|--------------------|
| **L1 Teach-back** | Plays fixed doctor-approved Hindi audio + records Pass/Fail → nurse alert on Fail | Write medical wording or re-explain itself |
| **L2 Date choice** | Shows least-busy dates inside doctor window | Auto-book or change the clinical window |
| **L3 Clinician intelligence** | Quote-only note structuring + transparent scoring → ranked worklist | Infer urgency or decide who to call |

## Architecture

```
Streamlit UI (4 screens)
    ↓
Python Rules Engine (deterministic)
    ↓
SQLite (local, synthetic data only)
    + Full Audit Log
```

- No EHR integration
- No cloud / SMS / telephony
- Runs on ordinary hospital hardware

## Priority Scoring (illustrative – not clinically validated)

| Signal | Points |
|--------|--------|
| Failed teach-back | +40 |
| No phone / unreachable | +35 |
| Clinician wrote High urgency | +25 |
| Shared phone | +20 |
| Outstation patient | +15 |
| Passed teach-back / Routine | +5 |

**Example (synthetic):** Ramesh = 40 + 35 + 15 + 25 = **115** → top of worklist with all four reasons shown.

## Safety Rules (hard)

- Never diagnoses or changes treatment
- Never writes free medical instructions
- Never invents urgency
- Never books without patient/relative confirmation
- Failed teach-back always goes to a nurse
- Final contact decision stays with CHW / records staff

## Repository Structure

```
├── app/                  # Streamlit UI
├── src/                  # Rules engine modules
├── data/                 # Schema + synthetic data
├── docs/                 # SRS, Case Brief, Decision Trail
├── tests/                # Acceptance tests (AT-1 to AT-8)
└── assets/               # Hindi audio placeholder
```

## Status (Round 1)

This repository demonstrates technical feasibility of the architecture described in the SRS and presentation.  
Features are marked **Built / Mock / Planned** in the accompanying solution presentation.

## Team

- **Leader:** Shridhar Sharma
- **Members:** Pragya Singh, Pragati Chauhan, Zahbiya Husain, [5th member]

Madhav Institute of Technology and Science, Gwalior

## Key References (EXTERNAL EVIDENCE)

- Mahajan et al., EM-TeBa study, *Int J Emerg Med* 2020
- Haimovich et al., *Acad Emerg Med* 2024
- Oh et al., *J Patient Saf* 2021
- Gurol-Urganci et al., Cochrane Database 2013
- Werner et al., *BMC Health Serv Res* 2023
- Sambasivan et al., SOUPS 2018
- AHRQ Teach-Back Tool 5
- WHO Digital Interventions for Health System Strengthening, 2019
- India Digital Personal Data Protection Act 2023 / Rules 2025

## License

MIT
