import sys
from helpers import load_logs, display_log_counts, count_logs_by_level, filter_logs_by_level, display_logs

VALID_LEVELS = ['INFO', 'DEBUG', 'ERROR', 'WARNING']

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"[ERROR] You must pass a directory path!")
        print(f"[INFO] Example: python hw03.py /path/to/logfile.log")
        print(f"[INFO] Example: python hw03.py /path/to/logfile.log info | debug | error | warning")

        sys.exit(1)
    
    logfile_path = sys.argv[1]
    all_logs = load_logs(logfile_path)
    logs_count = count_logs_by_level(all_logs)
    display_log_counts(logs_count)
    
    if len(sys.argv) >= 3:
        log_level_input = sys.argv[2].upper()

        if log_level_input not in VALID_LEVELS:
            print(f"\n[ERROR] Invalid log level '{sys.argv[2]}'. Must be one of: {', '.join([lvl.lower() for lvl in VALID_LEVELS])}")
            sys.exit(1)

        filtered_logs = filter_logs_by_level(all_logs, log_level_input)
        display_logs(filtered_logs, log_level_input)