import os
import pytest

class ParseTests:
    def __init__(self):
        # the base directory for test markdown files
        self.basedir = os.path.join(os.getcwd(), "tasks/") 

    def test_parse_task(self):
        filename = os.path.join(self.basedir, "sampleTask.md")
        print(filename)
        print(parse_task.parse_md(filename))
        assert 0