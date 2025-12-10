def generate_report(results: dict):
    report = "=== Import Analysis Report ===\n\n"
    for k, v in results.items():
        report += f"{k}: {v}\n"
    return report
