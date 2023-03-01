import cowsay
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("message")
parser.add_argument('-e', '--eyes')
parser.add_argument('-T', '--tongue')
parser.add_argument('-W', '--width', default=40, type=int)
parser.add_argument('-l', '--list', action='store_true', default=False)
parser.add_argument('-f', '--cowfile')
#[-e eye_string] [-f cowfile] [-h] [-l] [-n] [-T tongue_string] [-W column]
args = vars(parser.parse_args())
msg = args["message"]

del args["message"]
if args["eyes"] is None:
    del args["eyes"]
if args["tongue"] is None:
    del args["tongue"]

if not args["list"]:
    del args["list"]
    print(cowsay.cowsay(msg, **args))
else:
    print(cowsay.list_cows())
