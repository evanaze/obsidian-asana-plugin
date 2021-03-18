# obsidian-asana-plugin
A plugin to sync tasks from a Project folder in Obsidian to Asana.

## Usage
**Important** Please copy `templates/Task.md` into the Templates directory in your vault.
This will be the template for new tasks that you create.

Each task has the following fields, which correspond to a section on an Asana task.
* **Status**: This follows Asana's hierarchy and naming conventions and is one of the following:
    * `#todo`: has not yet been started
    * `#doing`: in progress
    * `#done`: completed
* **Priority**: Again, this follows Asana's hierarchy.
    * `#low`: lowest priority
    * `#medium`: medium priority
    * `#high`: highest priority
* **Due Date**: When the task is due for completion.
* **Start Date**: (Optional) When the task is started.
* **Deliverable**: This is the plain English deliverable for the task. It will be put as its own separate sentence at the top of the task description.

### Note: Acceptable Date Formats
Currently the only supported date format is `MM/DD/YYYY`, however more will be implemented soon.