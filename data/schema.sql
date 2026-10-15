-- Follow-Up Reliability Stack – SQLite Schema (synthetic data only)

CREATE TABLE IF NOT EXISTS patients (
    patient_id TEXT PRIMARY KEY,
    name TEXT,
    contact_status TEXT,          -- 'own', 'shared', 'unreachable', 'none'
    outstation INTEGER DEFAULT 0, -- 1 if outstation
    created_at TEXT
);

CREATE TABLE IF NOT EXISTS teachback_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id TEXT,
    result TEXT,                  -- 'Pass' or 'Fail'
    played_at TEXT,
    nurse_alerted INTEGER DEFAULT 0,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

CREATE TABLE IF NOT EXISTS followup_windows (
    patient_id TEXT PRIMARY KEY,
    window_start_day INTEGER,
    window_end_day INTEGER,
    confirmed_date TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

CREATE TABLE IF NOT EXISTS clinician_notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id TEXT,
    original_text TEXT,
    structured_urgency TEXT,      -- only if explicitly written
    source_span TEXT,             -- link back to original text
    needs_review INTEGER DEFAULT 0,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

CREATE TABLE IF NOT EXISTS worklist_scores (
    patient_id TEXT PRIMARY KEY,
    score INTEGER,
    reasons TEXT,                 -- JSON array of reason strings
    calculated_at TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

CREATE TABLE IF NOT EXISTS audit_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    action TEXT,
    patient_id TEXT,
    details TEXT,
    timestamp TEXT
);
