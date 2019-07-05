import sys
from lib2to3.main import main as lib2to3main


def main():
    sys.exit(lib2to3main("drop2.fixes"))
