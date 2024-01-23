#!/usr/bin/python3
""" Log parsing """
import sys


def print_statistics(total_size, status_code_count):
    """ Print Statistics """
    print(f"File size: {total_size}")
    for code, count in sorted(status_code_count.items()):
        print(f"{code}: {count}")


def parse_line(line):
    """ Parse Line """
    try:
        parts = line.split()
        ip_address, date, method, path, http_version, status_code,
        file_size = (
            parts[0],
            parts[3][1:],
            parts[5][1:],
            parts[6],
            parts[7],
            int(parts[8]),
            int(parts[9])
        )
        return ip_address, date, method, path, http_version, status_code,
    file_size
    except (IndexError, ValueError):
        return None


def main():
    """ Main """
    total_size = 0
    status_code_count = {}
    lines_processed = 0

    try:
        for line in sys.stdin:
            data = parse_line(line.strip())
            if data:
                ip_address, date, method, path, http_version,
                status_code, file_size = data
                total_size += file_size
                status_code_count[status_code] = status_code_count.get(
                        status_code,
                        0) + 1

                lines_processed += 1
                if lines_processed % 10 == 0:
                    print_statistics(total_size, status_code_count)

    except KeyboardInterrupt:
        print_statistics(total_size, status_code_count)
        sys.exit(0)


if __name__ == "__main__":
    main()
