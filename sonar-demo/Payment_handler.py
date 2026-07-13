"""
Payment handler added for the demo PR.

This file is intentionally introduced on a feature branch so that, when opened
as a pull request, SonarQube Cloud analyzes it as NEW CODE. The planted issues
below are enough to fail a new-code quality gate (new bugs / vulnerabilities /
security hotspots), and each is eligible for AI CodeFix so the fixes can be
generated live in the demo.

Do NOT use in production.
"""

import hashlib
import sqlite3
import subprocess
import random


# VULNERABILITY (SQL Injection): user input concatenated straight into a query.
def get_customer(db_path, customer_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = "SELECT * FROM customers WHERE id = '" + customer_id + "'"
    cursor.execute(query)
    return cursor.fetchall()


# VULNERABILITY (OS Command Injection): unsanitized input passed to the shell.
def ping_host(host):
    return subprocess.call("ping -c 1 " + host, shell=True)


# SECURITY HOTSPOT: hardcoded secret / credential in source.
DB_PASSWORD = "P@ssw0rd123!"


# SECURITY HOTSPOT: weak hashing (MD5) used for a security-sensitive value.
def token_for(user_id):
    return hashlib.md5(str(user_id).encode()).hexdigest()


# VULNERABILITY / BUG: insecure randomness used for a security token.
def session_id():
    return str(random.random())


# BUG: broad exception silently swallowed, hides failures.
def charge(amount, account):
    try:
        balance = account["balance"]
        account["balance"] = balance - amount
        return True
    except:
        return False
