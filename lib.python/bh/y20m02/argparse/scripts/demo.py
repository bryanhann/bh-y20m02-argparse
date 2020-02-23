from importlib import import_module as imp
from pathlib import Path
import shutil
def path4mod(mod):
    _path=mod.__path__
    if type(_path)==type([]):
        return _path[0]
    else:
        return mod.__path__.__dict__['_path'][0]
def main(args):
    #print(args)
    base = Path(args.pop())
    #print(base)
    #for item in base.iterdir():
    #    print(item)
    #exit()
    #root_dott = __package__.split('.')[0]
    #root_mod = imp(root_dott)
    #base = Path(path4mod(imp(root_dott))).parent
    assert base.is_dir()
    names = ['A', 'B', 'C']
    #print(base/names[0])
    files = list(Path(__file__).parent.parent.glob('files/*'))

    #(base/names[0]).rmdir()
    if (base/names[0]).exists():
        print('first remove %s' % (base/names[0]) )
        exit(-1)
    #print (base, names)
    while names:
        base = base/names.pop(0)
     #   print (base, names)
        base.mkdir()
        for file in files:
      #      print( file, '=>', base )
            shutil.copy(file,base)

    exit()



    _path=root_mod.__path__
    #print(_path.__dict__.keys())
    path=_path.__dict__['_path'][0]
    path=Path(path)
    assert path.is_dir()
    print(path)
    print(root_mod.__dict__['__path__'])
#    _path = root_mod.__path__
#    print(dir(_path))
    #path = root_mod.__path__
    #print(path)
    #path = Path(root)
    #assert not path.is_dir()
