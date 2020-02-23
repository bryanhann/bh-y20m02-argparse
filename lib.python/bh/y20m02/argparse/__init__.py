from importlib import import_module
def __parents4dott(dott):
    def _iter_parents4dott(dott):
        parts = dott.split('.')
        while parts:
            yield '.'.join( parts )
            parts.pop()
    return list(_iter_parents4dott(dott))


_D = import_module( __package__ + '.dott' )

class Namespace: pass
_P=Namespace()
_P.fun4mod = lambda mod : getattr(mod, 'parser' )
_P.dot4dot = lambda dot : dot + '.__parse'
_P.mod4dot = lambda dot : import_module(_P.dot4dot(dot))
_P.fun4dot = lambda dot : _P.fun4mod(_P.mod4dot(dot))

def parent_parsers( dott ):
    """ dott -> list of parsers """
    dotS = __parents4dott(dott)
    return list(map( _P.fun4dot, dotS ))

def parse_demo(parents, parser, opt):
    def show(xx): print( '  ' + str(xx)[:90] + '...' )
    print("parents: ") , list(map(show,parents))
    print("parser: " ) , show(parser)
    print("opt: ")     , show(opt)

