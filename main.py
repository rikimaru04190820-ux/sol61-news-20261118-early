import os,struct
from pathlib import Path

root=Path(__file__).resolve().parent
out=Path(os.environ.get('MAKEFUN_OUTPUT_DIR','/output'))
out.mkdir(parents=True,exist_ok=True)
data=(root/'world.png').read_bytes()
if data[:8]!=b'\x89PNG\r\n\x1a\n' or len(data)>1048576:
    raise ValueError('The committed artwork must be a PNG of at most 1 MiB')
width,height=struct.unpack('>II',data[16:24])
if not (1<=width<=1024 and 1<=height<=1024):
    raise ValueError('The committed artwork must fit within 1024 by 1024 pixels')
(out/'entry.png').write_bytes(data)
