#!/usr/bin/python3
"""A Script that reads stdin line by line and computes metrics """

import sys


def print_statistics(status_codes, total_file_size):
    """Prints the file size and the count of each status code"""
    print("File size: {:d}".format(total_file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {:d}".format(code, status_codes[code]))


status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                "404": 0, "405": 0, "500": 0}
total_file_size = 0
line_count = 0

try:
    for line in sys.stdin:
        if line_count != 0 and line_count % 10 == 0:
            print_statistics(status_codes, total_file_size)

        line_count += 1
        parts = line.split()

        try:
            total_file_size += int(parts[-1])
        except (IndexError, ValueError):
            pass

        try:
            status_code = parts[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1
        except IndexError:
            pass

    print_statistics(status_codes, total_file_size)

except KeyboardInterrupt:
    print_statistics(status_codes, total_file_size)
    raise
