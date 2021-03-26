""" Parses a Markdown file in the Task.md format. 
    :params doc:
    :returns: a dictionary containing the main fields of the task.
"""

def parse_md(filename):
    "Parses a markdown file in the Task.md format"
    # initialize the task object
    task = {}
    # start reading the input file
    with open(filename, "r") as read_obj:
        while True:
            line = read_obj.readline
            if not line:
                break
            print(line)