#!/usr/bin/python3
"""A Script that reads stdin line by line and computes metrics """

import sys


def print_statistics(status_codes, total_file_size):
    print("File size: {}".format(total_file_size))
    for code, count in sorted(status_codes.items()):
        if count != 0:
            print("{}: {}".format(code, count))


total_file_size = 0
status_code = ""
line_count = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                "404": 0, "405": 0, "500": 0}

try:
    for line in sys.stdin:
        parts = line.split()
        parts = parts[::-1]

        if len(parts) > 2:
            line_count += 1

            total_file_size += int(parts[0])
            status_code = parts[1]

            if status_code in status_codes:
                status_codes[status_code] += 1

            if line_count == 10:
                print_statistics(status_codes, total_file_size)
                line_count = 0

finally:
    print_statistics(status_codes, total_file_size)
