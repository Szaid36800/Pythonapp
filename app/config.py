import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Generate a directory from a parent location to a specified directory.")
    parser.add_argument("parent", help="Parent directory path")
    parser.add_argument("child", help="Child directory path")
    return parser.parse_args()
