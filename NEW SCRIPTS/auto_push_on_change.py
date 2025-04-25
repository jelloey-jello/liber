import os
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Function to run a shell command
def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr)
    else:
        print(result.stdout)

# Function to commit and push changes to GitHub
def commit_and_push():
    commit_message = "Auto-commit: changes detected"
    print(f"Committing changes with message: {commit_message}")
    run_command("git add .")
    run_command(f'git commit -m "{commit_message}"')
    run_command("git push")
    print("Changes successfully pushed to GitHub!")

# Define the event handler for file changes
class GitChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Trigger commit and push on any file modification
        if event.is_directory:
            return  # Ignore directories
        print(f"File modified: {event.src_path}")
        commit_and_push()

    def on_created(self, event):
        # Trigger commit and push when a new file is created
        if event.is_directory:
            return  # Ignore directories
        print(f"File created: {event.src_path}")
        commit_and_push()

    def on_deleted(self, event):
        # Trigger commit and push when a file is deleted
        if event.is_directory:
            return  # Ignore directories
        print(f"File deleted: {event.src_path}")
        commit_and_push()

# Step 1: Set up the project directory (ensure we are in the correct folder)
repo_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(repo_directory)

# Step 2: Set up the watchdog observer
observer = Observer()
event_handler = GitChangeHandler()
observer.schedule(event_handler, path=repo_directory, recursive=True)

# Start watching the directory
print("Watching for changes in the project directory...")
observer.start()

try:
    while True:
        time.sleep(1)  # Keep the script running and monitoring for changes
except KeyboardInterrupt:
    observer.stop()

observer.join()

"""

Steps to Set It Up:
Install Watchdog: If you don't have the watchdog library installed, you can install it via pip: pip install watchdog

Save the script: Save the code above as auto_push_on_change.py in your project directory
(where your Git repository is located).

Run the script: Run the script from your terminal: python auto_push_on_change.py

Keep the script running: The script will now keep running and monitor the project directory for any file changes
(modifications, creations, or deletions). Whenever it detects a change, it will automatically add, commit, and push
the changes to your GitHub repository.

How it Works:
Watching for Changes: The script uses watchdog to monitor the directory for changes like file modifications, creations,
and deletions.

Automatic Commit and Push: Whenever any change is detected, it triggers the commit_and_push() function, which adds,
commits with a default message, and pushes the changes to your GitHub repository.

Continuous Monitoring: The script runs indefinitely until you stop it (e.g., via Ctrl+C).

Customizing:
You can modify the commit message within the commit_and_push() function if you'd like it to be more specific.

If you want to exclude certain files or directories from being watched, you can modify the on_modified(), on_created(),
and on_deleted() methods to filter out specific file types or paths.

"""