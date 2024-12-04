# prep
with open("input2.txt", "r") as f:
    reports = []
    for line in f.readlines():
        reports.append([int(num) for num in line.strip().split()])

# part 1
report_num = 0
for report in reports:
    i = 0
    increase = 0
    decrease = 0
    while i < len(report) - 1:
        if report[i] > report[i+1] and 1 <= report[i] - report[i+1] <= 3:
            # decreasing check
            decrease += 1
        elif report[i] < report[i+1] and 1 <= report[i+1] - report[i] <= 3:
            # increasing check
            increase += 1
        i += 1
    if decrease + 1 == len(report) or increase + 1 == len(report):
        report_num += 1

print(f'Number of safe reports before dampener problem: {report_num}.')

# part 2

def safe(report):
    # checks reports
    increase = 0
    decrease = 0
    for i in range(len(report) - 1):
        if report[i] > report[i + 1] and 1 <= report[i] - report[i + 1] <= 3:
            decrease += 1
        elif report[i] < report[i + 1] and 1 <= report[i + 1] - report[i] <= 3:
            increase += 1
    return decrease + 1 == len(report) or increase + 1 == len(report)

def dampener_check(report):
    # checks if removing a number makes the report safe
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if safe(new_report):
            return True
    return False

safe_reports = 0
for report in reports:
    if safe(report) or dampener_check(report):
        safe_reports += 1

print(f'Number of safe reports after dampener problem: {safe_reports}.')
