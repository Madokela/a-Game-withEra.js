import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    # base = "Win32GUI"
    base = "Console"

setup(name="测试用狐狸游戏",
      version="0.0.0a",
      description="233333333",
      options={"build_exe": build_exe_options},
      executables=[Executable("Game.py", base=base)])
