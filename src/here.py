from pathlib import Path
import os

def get_project_root():
    """
    Detects if the code is being run in a Jupyter notebook or a .py script
    and returns the project root accordingly.
    """
    try:
        if 'get_ipython' in globals() and hasattr(get_ipython(), 'config'):
            return Path.cwd()
        else:
            return Path(__file__).resolve().parent.parent
    except NameError:
        return Path.cwd()

def here(path=""):
    """
    Builds a path from the project root, supporting relative navigation.
    Allows for paths like "../data" and "data/output".
    
    Args:
        path: str, a single string representing the relative path.
    
    Returns:
        A Path object with the full path to the specified file or folder.
    """
    project_root = get_project_root()
    # Split the path on "/" and join with project_root
    return project_root.joinpath(*path.split("/")).resolve()