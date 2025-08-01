import sys
from pathlib import Path

# Add the parent directory of "tests" to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Now import the local "here" module
from here import get_root_directory, here

print()
print(get_root_directory())

print(here(".."))

print()
