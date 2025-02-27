# Here

This code allows relative file imports. 

It's useful when you run a python script from a shell that `cd`s elsewhere, such that it can't use code like `from .. import xyz` or `from .abc import xyz`. 

Instead, you can use it like this:
```python
from here import get_file_working_directory, here

# Get the file working directory
file_working_directory = get_file_working_directory()
print(f"File working directory: {file_working_directory}")

# Resolve a relative path using the here function
resolved_path = here("data/output")
print(f"Resolved path: {resolved_path}")
```

It works on both .py and .ipynb files!
