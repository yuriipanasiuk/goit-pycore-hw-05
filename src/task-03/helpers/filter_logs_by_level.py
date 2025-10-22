def filter_logs_by_level(logs: list, level: str) -> list:
    filter_logs = list(filter(lambda log: log['level'].upper() == level.upper(), logs))
    
    return filter_logs