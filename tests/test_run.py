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


def run_tests():
    """Run the test files dynamically using pytest."""
    test_files = get_test_files()

    if not test_files:
        print("No test files found in the specified directory.")
        return

    for test_file in test_files:
        print(f"Running {test_file}...")
        result = subprocess.run(["pytest", test_file], capture_output=True, text=True)
        print(result.stdout)  # Print the output
        if result.returncode != 0:
            print(f"Test {test_file} failed.")
        else:
            print(f"Test {test_file} passed.")


if __name__ == "__main__":
    run_tests()
