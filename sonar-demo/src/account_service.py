"""
Simple account service used for the SonarQube Cloud demo.
Contains a few *intentional* issues so AI CodeFix and PR decoration
have something to react to. Do not use in production.
"""

import hashlib


# ISSUE (Security Hotspot): weak hashing algorithm for passwords.
# Sonar flags MD5 as cryptographically weak.
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


# ISSUE (Bug): possible None dereference. If user is None this raises,
# and the equality check against a hardcoded value is also flagged.
def is_admin(user):
    return user["role"] == "admin"


# ISSUE (Code Smell): unused parameter 'currency' + hardcoded magic numbers.
def calculate_discount(price, customer_type, currency):
    if customer_type == "gold":
        return price - (price * 0.2)
    if customer_type == "silver":
        return price - (price * 0.1)
    return price


# ISSUE (Code Smell / Duplication): near-identical block to the one below.
def format_gold_summary(name, price):
    total = price - (price * 0.2)
    line = "Customer: " + name
    line = line + " | Tier: gold"
    line = line + " | Total: " + str(total)
    return line


def format_silver_summary(name, price):
    total = price - (price * 0.1)
    line = "Customer: " + name
    line = line + " | Tier: silver"
    line = line + " | Total: " + str(total)
    return line


# ISSUE (Bug): comparison that is always False (string vs int).
def check_threshold(amount):
    if amount == "100":
        return True
    return False


# ISSUE (Code Smell): overly complex, unreachable branch.
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    return "unknown"  # unreachable
