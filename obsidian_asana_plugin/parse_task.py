""" Parses a Markdown file in the Task.md format. 
    :params doc:
    :returns: a dictionary containing the main fields of the task.
"""

def remove_obsidian_syntax(string):
    "Removes Obsidian syntax from a string, namely []'s, [[]]'s and #'s"
    pass

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
                task['title'] = remove_obsidian_syntax(' '.join(line.split()[1:]))
            if count == 3:
                task['status'] = remove_obsidian_syntax(line.split()[1])
            if count == 4:
                task['priority'] = remove_obsidian_syntax(line.split()[1])
            if count == 5:
                task['due_date'] = line.split()[2]
            if count == 6:
                task['start_date'] = line.split()[2]
            if count == 7:
                task['deliverable'] = remove_obsidian_syntax(' '.join(line.split()[1:]))
            if count >= 9:
                task['description'] += remove_obsidian_syntax(line)
            count += 1
    print(task)
    return task


if __name__ == "__main__":
    parse_md("tests/tasks/sampleTask.md")