from collections import Counter


def count_logs_by_level(logs: list) -> dict:
    levels = [log['level'] for log in logs]
    count_logs = dict(Counter(levels))

    return count_logs

