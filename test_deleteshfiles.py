import os
import pytest

@pytest.fixture
def run_deleteshfiles_script():
    os.system("python deleteshfiles.py")

def test_deleteshfiles(run_deleteshfiles_script):
    found_unexpected_files = False  # A flag to track if any unexpected files are found

    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".sh"):
                assert not os.path.exists(os.path.join(root, file)), "File {} was not deleted".format(file)
                found_unexpected_files = True

    if not found_unexpected_files:
        print("Test successful: All .sh files were deleted.")

if __name__ == "__main__":
    pytest.main([__file__])
