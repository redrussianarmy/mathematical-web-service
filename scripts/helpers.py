import os
import platform
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent.parent.resolve()
OS_TYPE = platform.system()


def set_python_path():
    venv = os.path.join(PROJECT_ROOT, "env")

    if OS_TYPE == "Linux":
        python_path = os.path.join(venv, "bin")
        seperator = ":"
    else:
        python_path = os.path.join(venv, "Scripts")
        seperator = ";"

    os.environ["PATH"] = f"{python_path}{seperator}" + os.environ["PATH"]
