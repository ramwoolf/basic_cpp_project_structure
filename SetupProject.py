#!/bin/python

import argparse
import os
import sys

def main(args):
    root_dir = sys.argv[0]
    print("Run with:")
    print(args)
    print(root_dir)


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description="Setup base CPP projest structure")
    arg_parser.add_argument(
        "--std",
        type=str,
        default="c++17",
        choices=["c++11", "c++14", "c++17", "c++20"],
        help="Version of used standard of C++"
    )

    arg_parser.add_argument(
        "--type",
        type=str,
        default="exec",
        choices=["exec", "shared", "static", "header"],
        help="Type of project"
    )

    arg_parser.add_argument(
        "--unittests",
        type=str,
        default="gtest",
        choices=["gtest", "no"],
        help="Which UT framework to use"
    )

    arg_parser.add_argument(
        "--makefiles",
        type=str,
        default="gnu",
        choices=["gnu", "ninja"],
        help="Type of makefiles to use"
    )

    args = arg_parser.parse_args()

    main(args)