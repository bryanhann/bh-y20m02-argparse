from argparse import ArgumentParser
import bh.y20m02.argparse as _ABC_
if __name__=='__main__':
    parents = _ABC_.parent_parsers(__package__)
    parser = ArgumentParser(parents=parents, prog='python -m ' + __package__ )
    opt=parser.parse_args()
    _ABC_.parse_demo(parents, parser, opt)
