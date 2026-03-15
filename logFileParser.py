import re
from collections import Counter
def log_error_count(file_path):
    error_pattern=re.compile(r'\b([45][0-9]{2})\b')
    error_counts=Counter()
    try:
        with open(file_path,'r') as file:
            for line in file:
                matches=error_pattern.findall(line)
                error_counts.update(matches)
        return dict(error_counts)
    except FileNotFoundError:
        return "Error: File Not Found"
    except Exception as e:
        return f"An Unexpected error found: {e}"
    
log_results=log_error_count("production.log")
print(f"{'Error_code':<12}|{'Count'}")
print("-"*25)
for code,count in sorted(log_results.items()):
    print(f"{code:<12}|{count}")

