def display_logs(logs: list, level: str):
    if len(logs) <1:
       return print('[WARNING]: Logs list are empty')

    print (f"\nLog details for the level '{level.upper()}':")

    for log in logs:
        print(f'{log['date']} {log["time"]} - {log["message"]}')
