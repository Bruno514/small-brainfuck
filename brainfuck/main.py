import argparse

from brainfuck.interpreter import Brainfuck


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")

    args = parser.parse_args()

    with open(args.file, "r") as f:
        code = f.read()

    to_run = Brainfuck(code)

    to_run.execute()
