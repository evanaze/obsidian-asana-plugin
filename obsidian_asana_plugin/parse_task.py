""" Parses a Markdown file in the Task.md format. 
    :params doc:
    :returns: a dictionary containing the main fields of the task.
"""

def parse_md(filename):
    "Parses a markdown file in the Task.md format"
    # initialize the task object
    task = {"description": ''}
    # start reading the input file
    with open(filename, "r") as read_obj:
        count = 0
        while True:
            line = read_obj.readline()
            if not line:
                break
            if count == 2:
                task['title'] = ' '.join(line.split()[1:])
            if count == 3:
                task['status'] = line.split()[1]
            if count == 4:
                task['priority'] = line.split()[1]
            if count == 5:
                task['due_date'] = line.split()[2]
            if count == 6:
                task['start_date'] = line.split()[2]
            if count == 7:
                task['deliverable'] = ' '.join(line.split()[1:])
            if count >= 9:
                task['description'] += line
            count += 1
    print(task)
    return task


if __name__ == "__main__":
    parse_md("tests/tasks/sampleTask.md")