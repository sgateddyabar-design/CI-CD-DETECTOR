def detect_anomaly(log):
    suspicious_words = [
        "curl", "wget", "http", "https",
        "ftp", "ssh", "scp", "telnet"
    ]

    for word in suspicious_words:
        if word in log.lower():
            return "⚠️ Anomaly Detected: Suspicious Activity Found!"

    return "✅ Normal Pipeline Execution"