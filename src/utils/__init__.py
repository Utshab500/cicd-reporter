import os
import glob

def get_module_names(directory):
  """Gets a list of module names from a directory."""
  return [os.path.splitext(f)[0] for f in glob.glob(os.path.join(directory, "*.py"))
          if not f.startswith("__")]

__all__ = get_module_names(".")