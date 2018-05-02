# ROP_Search
This command is for searching gadget in CTF's PWN problem.

Please use it for problem solving of CTF.

I do not have responsibility for other uses

## Usage
```
[-l dynlibray] [-s ""instruction code""]
```


## Install
```
python setup.py install
rg -h
usage: rg [-h] [-l [LIBRARY] LOAD] -s ["ORDER"] SEARCH

argparse sample.

optional arguments:
  -h, --help            show this help message and exit
  -l [LIBRARY] LOAD, --load [LIBRARY] LOAD
                        Specify target library. (Example: -l
                        /usr/local/lib.so)
  -s ["ORDER"] SEARCH, --search ["ORDER"] SEARCH
                        Specify the instruction to be searched from the
                        library. (Example: -s "mov eax,al" -s "pop eax")

```

