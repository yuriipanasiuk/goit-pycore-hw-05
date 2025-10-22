def parse_log_line(line: str) -> dict:
    try:
        date, time, status, message = line.strip().split(maxsplit=3)

        result = {"date": date, 
                "time": time, 
                'level': status, 
                'message': message}
        
        return result
    
    except ValueError:
        return None