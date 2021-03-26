import os
import pytest
from obsidian_asana_plugin.parse_task import parse_md

class ParseTests:
    def __init__(self):
        # the base directory for test markdown files
        self.basedir = os.path.join(os.getcwd(), "tasks/") 

    def test_parse_task(self):
        filename = os.path.join(self.basedir, "sampleTask.md")
        print(filename)
        print(parse_md(filename))
        assert 0