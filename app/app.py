import os
from config import PARENT_DIR, CHILD_DIR
from error_handling import check_directory_exists, DirectoryError

def create_directory(parent, child):
    path = os.path.join(parent, child)
    try:
        check_directory_exists(path)
        os.makedirs(path)
        print(f"Directory '{path}' created successfully.")
    except DirectoryError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    create_directory(PARENT_DIR, CHILD_DIR)
