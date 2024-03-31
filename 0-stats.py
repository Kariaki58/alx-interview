#!/usr/bin/python3
"""log parsing"""
import sys


total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 7 and parts[5].isdigit() and parts[6].isdigit():
            status_code = int(parts[5])
            file_size = int(parts[6])
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            line_count += 1
            if line_count % 10 == 0:
                print(f"Total file size: {total_file_size}")
                for code, count in sorted(status_code_counts.items()):
                    if count > 0:
                        print(f"{code}: {count}")

        if line_count % 10 == 0:
            try:
                sys.stdin.__next__()
            except KeyboardInterrupt:
                print(f"Total file size: {total_file_size}")
                for code, count in sorted(status_code_counts.items()):
                    if count > 0:
                        print(f"{code}: {count}")
                break

except KeyboardInterrupt:
    print(f"Total file size: {total_file_size}")
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{code}: {count}")
