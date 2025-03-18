import sys
from password_generator import core
import argparse

def positive_int(val):
    pass

def parser():
    parser = argparse.ArgumentParser(
        description="Generate a funny or serious password"
    )

    parser.add_argument(
        "-g",
        "--generate",
        dest="generate",
        choices=["neutral", "chuck", "all"],
        default="neutral",
        help="Joke category.",
    )
    return parser
def main(): 
    pass 

if __name__ == "__main__":
    main()