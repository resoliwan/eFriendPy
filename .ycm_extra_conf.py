# .ycm_extra_conf.py
import os


def Settings(**kwargs):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return {
        "interpreter_path": dir_path + "/.venv/bin/python",
        "sys_path": [
            dir_path + "/.venv/lib/python3.8/site-packages",
        ],
    }
