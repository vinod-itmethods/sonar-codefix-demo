"""Utility helpers for the demo project."""

import os


# ISSUE (Security Hotspot): hardcoded credential-like value.
API_TOKEN = "AKIA1234567890DEMOKEY"


# ISSUE (Code Smell): bare except swallows all errors.
def read_config(path):
    try:
        with open(path) as f:
            return f.read()
    except:
        return None


# ISSUE (Bug): mutable default argument.
def append_item(item, items=[]):
    items.append(item)
    return items


# ISSUE (Code Smell): function does nothing useful / dead parameter.
def build_path(base, filename, unused_flag):
    return os.path.join(base, filename)
