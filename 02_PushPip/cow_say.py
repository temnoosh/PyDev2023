import cowsay
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("message")
args = vars(parser.parse_args())
msg = args["message"]

print(cowsay.cow(msg))
