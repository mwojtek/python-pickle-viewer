from argparse import ArgumentParser
from os.path import realpath, abspath
from pickle import load
from pprint import pformat
from pypager.source import StringSource
from pypager.pager import Pager


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file")

    args = parser.parse_args()
    file = abspath(realpath(args.file))

    pager = Pager()
    pager.add_source(StringSource(pformat(load(open(file, "rb"))), None))
    pager.run()
