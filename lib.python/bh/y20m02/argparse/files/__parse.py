from argparse import ArgumentParser as AP
FLAG = '--' + __package__.split('.')[-1]
PROG = __name__
parser = AP(prog=PROG, add_help=False)
parser.add_argument(FLAG, action="store_true")
