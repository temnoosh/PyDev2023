import cowsay
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("message")
parser.add_argument('-e', '--eyes')
parser.add_argument('-T', '--tongue')
parser.add_argument('-W', '--width', default=40, type=int)
parser.add_argument('-l', '--list', action='store_true', default=False)
parser.add_argument('-b', action='store_true', default=False)
parser.add_argument('-d', action='store_true', default=False)
parser.add_argument('-g', action='store_true', default=False)
parser.add_argument('-p', action='store_true', default=False)
parser.add_argument('-s', action='store_true', default=False)
parser.add_argument('-t', action='store_true', default=False)
parser.add_argument('-w', action='store_true', default=False)
parser.add_argument('-y', action='store_true', default=False)
parser.add_argument('-f', '--cowfile')
#[-e eye_string] [-f cowfile] [-h] [-l] [-n] [-T tongue_string] [-W column]
args = vars(parser.parse_args())

if args['b']:
    args["preset"] = "b"
del args['b']

if args['d']:
    args["preset"] = "d"
del args['d']

if args['g']:
    args["preset"] = "g"
del args['g']

if args['p']:
    args["preset"] = "p"
del args['p']

if args['s']:
    args["preset"] = "s"
del args['s']

if args['t']:
    args["preset"] = "t"
del args['t']

if args['w']:
    args["preset"] = "w"
del args['w']

if args['y']:
    args["preset"] = "y"
del args['y']
    
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
