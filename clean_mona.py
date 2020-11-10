import sys

if 'mona' in sys.modules:
    reload(mona)
    reload(mona.dbglib)
    reload(mona.dbglib.pykd)
else:
    import mona
	
if 'monaFile' in sys.modules:
    reload(monaFile)
    reload(mona.dbglib)
    reload(mona.dbglib.pykd)
else:
    import monaFile