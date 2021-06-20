import os

files = os.listdir("task_3")


def calculate_most_big_file(all_files):
    max_count = 0
    for file in all_files:
        with open(f"task_3/{file}", encoding="utf-8") as current_file:
            count = 0
            for _ in current_file:
                count += 1
            if count > max_count:
                max_count = count
                biggest_file = file
    return max_count, biggest_file


def record_file(file_name, sum_string):
    with open(f"task_3/{file_name}", encoding="utf-8") as read_file:
        argument = read_file.read()

    with open("result_task3.txt", "a", encoding="utf-8") as write_file:
        write_file.write(f"{file_name}\n")
        write_file.write(f"{sum_string}\n")
        write_file.write(argument)
        write_file.write("\n")


while len(files) != 0:
    count_str, big_file = calculate_most_big_file(files)
    record_file(big_file, count_str)
    files.remove(big_file)
