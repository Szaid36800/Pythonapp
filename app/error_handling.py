import os

class DirectoryError(Exception):
    """Custom exception for directory-related errors."""
    pass

def check_directory_exists(path):
    if os.path.exists(path):
        raise DirectoryError(f"Directory '{path}' already exists.")
    if not os.path.isdir(os.path.dirname(path)):
        raise DirectoryError(f"Parent directory '{os.path.dirname(path)}' does not exist.")
