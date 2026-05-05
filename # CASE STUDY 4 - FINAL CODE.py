# CASE STUDY 4 - FINAL CODE
# MUKESH KUMAR
# 202501100700200

file_name = "/content/CS4.txt"

# TASK 1: BASIC FILE READING

print("\n===== TASK 1: BASIC FILE READING =====")

with open(file_name, "r") as file:
    content = file.read()
    print("\nFull Content:\n", content)

with open(file_name, "r") as file:
    print("\nFirst line using readline():")
    print(file.readline())

with open(file_name, "r") as file:
    lines = file.readlines()

    print("\nTotal number of lines:", len(lines))

    print("\nFirst 2 lines:")
    print("".join(lines[:2]))

    print("Last 2 lines:")
    print("".join(lines[-2:]))

# TASK 2: LOG CLASSIFICATION

print("\n===== TASK 2: LOG CLASSIFICATION =====")

log_count = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0
}

for line in lines:
    if "INFO" in line:
        log_count["INFO"] += 1
    if "WARNING" in line:
        log_count["WARNING"] += 1
    if "ERROR" in line:
        log_count["ERROR"] += 1

print("Log Count Dictionary:")
print(log_count)

# TASK 3: WRITE FILTERED FILES

print("\n===== TASK 3: WRITE FILTERED FILES =====")

info_lines = []
warning_lines = []
error_lines = []

for line in lines:
    if "INFO" in line:
        info_lines.append(line)
    if "WARNING" in line:
        warning_lines.append(line)
    if "ERROR" in line:
        error_lines.append(line)

with open("info_logs.txt", "w") as f:
    f.writelines(info_lines)

with open("warning_logs.txt", "w") as f:
    f.writelines(warning_lines)

with open("error_logs.txt", "w") as f:
    f.writelines(error_lines)

print("Files created successfully!")


# TASK 4: SEARCH FEATURE

print("\n===== TASK 4: SEARCH FEATURE =====")

keyword = input("Enter keyword (INFO/WARNING/ERROR): ").upper()

matched_lines = []

print("\nMatching lines:")
for line in lines:
    if keyword in line:
        print(line.strip())
        matched_lines.append(line)

with open("search_result.txt", "w") as f:
    f.writelines(matched_lines)

print("Search results saved in search_result.txt")

# FILE POINTER (SEEK) OPERATIONS

print("\n===== FILE POINTER (SEEK) OPERATIONS =====")

with open(file_name, "r") as file:
    # First 50 characters
    print("\nFirst 50 characters:")
    print(file.read(50))

    # Move to beginning
    file.seek(0)
    print("\nAfter seek(0):")
    print(file.read(50))

    # Move to middle
    file.seek(0)
    content = file.read()
    middle = len(content) // 2
    file.seek(middle)

    print("\nFrom middle:")
    print(file.read(50))


    print("\nLast 100 characters:")
    print(content[-100:])

print("\n===== PROGRAM COMPLETED SUCCESSFULLY =====")