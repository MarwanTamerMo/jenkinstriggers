#!/usr/bin/env python3
"""
Simple test file that prints a cool diamond shape
"""

def print_diamond():
    """Print a diamond pattern"""
    size = 5

    # Upper half (including middle)
    for i in range(size):
        print(' ' * (size - i - 1) + '*' * (2 * i + 1))

    # Lower half
    for i in range(size - 2, -1, -1):
        print(' ' * (size - i - 1) + '*' * (2 * i + 1))

if __name__ == "__main__":
    print("Cool Diamond Shape:")
    print()
    print_diamond()
