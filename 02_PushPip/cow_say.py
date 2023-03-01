import cowsay
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("message")
parser.add_argument('-e', '--eyes')
parser.add_argument('-f', '--cowfile')
#[-e eye_string] [-f cowfile] [-h] [-l] [-n] [-T tongue_string] [-W column]
args = vars(parser.parse_args())
msg = args["message"]

del args["message"]
if args["eyes"] is None:
    del args["eyes"]

print(cowsay.cowsay(msg, **args))
