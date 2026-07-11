# hello.py

from colorama import init, Fore
import argparse

init(autoreset=True)

parser = argparse.ArgumentParser()
parser.add_argument("--name", default="World", help="Name to greet")

args = parser.parse_args()

print(Fore.GREEN + f"Hello, how are you{args.name}!")
