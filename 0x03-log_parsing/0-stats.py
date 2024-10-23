#!/usr/bin/python3
import sys
import signal

total_file_size = 0
status_codes_count = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_count = 0

def print_stats():
    """Print the accumulated metrics"""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def process_line(line):
    """Process a single line and extract metrics"""
    global total_file_size
    try:
        parts = line.split()
        if len(parts) < 7:
            return
        file_size = int(parts[-1])
        status_code = parts[-2]
        total_file_size += file_size
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1
    except (IndexError, ValueError):
        pass

try:
    for line in sys.stdin:
        process_line(line.strip())
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

print_stats()
