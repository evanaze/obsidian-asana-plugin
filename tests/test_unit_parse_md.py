import os
import pytest
from obsidian_asana_plugin.parse_task import parse_md

def test_parse_task():
    filename = os.path.join(os.getcwd(), "tests/tasks/sampleTask.md")
    result = parse_md(filename)
    assert result == {}
