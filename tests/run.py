import subprocess
import os
import sys

# Define the directory containing test files
TEST_DIRECTORY = os.path.dirname(__file__)  # You can change this to your specific path if needed


def get_test_files():
    """Retrieve test files that end with '_tool.py' and start with 'test'."""
    test_files = [
        os.path.join(TEST_DIRECTORY, file)
        for file in os.listdir(TEST_DIRECTORY)
        if file.endswith("_tool.py") and file.startswith("test")
    ]
    return test_files


def display_tool_selection(test_files):
    """Display a list of test tools to select from."""
    if not test_files:
        print("No test files found in the specified directory.")
        return None

    print("Please select the test tool to run:")
    for idx, test_file in enumerate(test_files, 1):
        print(f"{idx}. {os.path.basename(test_file)}")

    try:
        choice = int(input("Enter the number of the test to run: "))
        if 1 <= choice <= len(test_files):
            return test_files[choice - 1]
        else:
            print("Invalid choice, please select a valid number.")
            return None
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None


def run_tests():
    """Run the test files dynamically using pytest."""
    test_files = get_test_files()

    # Set up an infinite loop to keep asking for a test to run
    while True:
        selected_test_file = display_tool_selection(test_files)
        if selected_test_file:
            print(f"Running {selected_test_file}...")
            result = subprocess.run(["pytest", selected_test_file], capture_output=True, text=True)
            print(result.stdout)  # Print the output
            if result.returncode != 0:
                print(f"Test {selected_test_file} failed.")
            else:
                print(f"Test {selected_test_file} passed.")
        
        # Re-run the process without asking to exit
        print("\nNext test will be executed...\n")


if __name__ == "__main__":
    run_tests()
