import os
import re

# Define patterns for 18+ content and abuse
patterns = [
    re.compile(r'\b(?:porn|sex|xxx|adult|18\+)\b', re.IGNORECASE),
    re.compile(r'\b(?:abuse|harass|violence|explicit)\b', re.IGNORECASE)
]

# Global variable to track the state of the command
command_enabled = True

def scan_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        for pattern in patterns:
            if pattern.search(content):
                return True
    return False

def scan_and_delete_files(directory):
    if not command_enabled:
        print("Command is disabled.")
        return

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if scan_file(file_path):
                # Warn the user before deleting the file
                print(f"Warning: The file {file_path} will be deleted.")
                confirmation = input("Do you want to proceed? (yes/no): ").strip().lower()
                if confirmation == 'yes':
                    print(f"Deleting file: {file_path}")
                    os.remove(file_path)
                else:
                    print(f"Skipping file: {file_path}")

def enable_command():
    global command_enabled
    command_enabled = True
    print("Command enabled.")

def disable_command():
    global command_enabled
    command_enabled = False
    print("Command disabled.")

if __name__ == "__main__":
    # Set the directory to the root of your local repository
    repo_directory = "path/to/your/local/Rudra02"

    # Simple CLI to enable, disable, or run the command
    while True:
        user_input = input("Enter 'enable' to enable the command, 'disable' to disable the command, 'run' to run the command, or 'exit' to quit: ").strip().lower()
        if user_input == 'enable':
            enable_command()
        elif user_input == 'disable':
            disable_command()
        elif user_input == 'run':
            scan_and_delete_files(repo_directory)
        elif user_input == 'exit':
            break
        else:
            print("Invalid input. Please try again.")
