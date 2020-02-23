from importlib import import_module as imp
import sys
if __name__ == '__main__':
    args = sys.argv[1:] or ['']
    cmd = args.pop(0)
    try:
        mod=imp( '%s.scripts.%s' % (__package__,cmd) )
    except ModuleNotFoundError:
        print( "Cannot handle '%s'" % cmd )
        exit()
    mod.main(args)
