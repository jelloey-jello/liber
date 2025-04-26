import os
import time

FOLDER_TO_WATCH = '.'  # or the path to your project
POLL_INTERVAL = 5  # seconds

def has_changes():
    return os.system('git diff --quiet') != 0

def push_changes():
    os.system('git add .')
    os.system('git commit -m "Auto update from local changes"')
    os.system('git push')

print("Watching for changes... Press Ctrl+C to stop.")
try:
    while True:
        if has_changes():
            push_changes()
        time.sleep(POLL_INTERVAL)
except KeyboardInterrupt:
    print("Stopped watching.")

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