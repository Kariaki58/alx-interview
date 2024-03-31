#!/usr/bin/python3
"""
log parsing
"""
import sys
import re


lines_processed = 0
status_code_counts = {}
total_file_size = 0

try:
    for line in sys.stdin:
        lines_processed += 1
        match = re.search(
            line)
        match = re.search(
            '^\\d{1,3}.\\d{1,3}.\\d{1,3}.\\d{1,3}\\s-\\s\\[[\\d -:.]*\
\\]\\s"GET\\s\\/projects\\/260\\sHTTP\\/1.1"\\s\\d{1,3}\\s\\d{1,4}$',
            line)
        if match:
            status_match = re.search("(?<=1.1\" )\\d{1,3}", line)
            file_size_match = re.search("\\d{1,4}$", line)
            if status_code_counts.get(status_match.group()):
                status_code_counts[status_match.group()] = status_code_counts.get(
                    status_match.group()) + 1
            else:
                status_code_counts[status_match.group()] = 1
            total_file_size += int(file_size_match.group())
        else:
            continue

        if lines_processed % 10 == 0:
            print(f"File size: {total_file_size}")
            for status_code in sorted(status_code_counts):
                print(f"{status_code}: {status_code_counts[status_code]}")

finally:
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_code_counts):
        print(f"{status_code}: {status_code_counts[status_code]}")

