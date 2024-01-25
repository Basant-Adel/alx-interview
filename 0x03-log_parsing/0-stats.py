#!/usr/bin/python3
"""Log parsing"""
import re


def extract_input(input_line):
    """extract"""
    pattern = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {'status_code': 0, 'file_size': 0}
    log_format = '{}\\-{}{}{}{}\\s*'.format(*pattern)
    match = re.fullmatch(log_format, input_line)
    if match:
        info['status_code'] = match.group('status_code')
        info['file_size'] = int(match.group('file_size'))
    return info


def print_statistics(total_file_size, status_codes_stats):
    """print"""
    print(f'File size: {total_file_size}', flush=True)
    for status_code, num in sorted(status_codes_stats.items()):
        if num > 0:
            print(f'{status_code}: {num}', flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    """update"""
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    status_codes_stats[status_code] += 1
    return total_file_size + line_info['file_size']


def run():
    """run"""
    line_num = 0
    total_file_size = 0
    status_codes_stats = {str(code): 0 for code in [
        200,
        301,
        400,
        401,
        403,
        404,
        405,
        500
        ]}
    try:
        while True:
            line = input()
            total_file_size = update_metrics(
                    line,
                    total_file_size,
                    status_codes_stats
                    )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
