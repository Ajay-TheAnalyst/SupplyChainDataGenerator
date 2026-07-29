validation_results = []


def add_result(validation_type, rule_name, status, issue_count):

    validation_results.append({
        "Validation": validation_type,
        "Rule": rule_name,
        "Status": status,
        "Issues": issue_count
    })


def print_report():

    print()
    print("=" * 65)
    print("               SUPPLY CHAIN VALIDATION REPORT")
    print("=" * 65)

    for result in validation_results:

        print(
            f"{result['Validation']:<20}"
            f"{result['Rule']:<50}"
            f"{result['Status']:<8}"
            f"Issues: {result['Issues']}"
        )

    print("=" * 65)

    failed = sum(
        1
        for result in validation_results
        if result["Status"] == "FAIL"
    )

    if failed == 0:
        print("Overall Status : ✅ PASS")
    else:
        print(f"Overall Status : ❌ FAIL ({failed} failed checks)")

    print("=" * 65)