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

## test

You can test by loading libc - 2.15.so in the TEST directory.

Please specify libc - 2.15.so as an absolute path. (We will assume that Rg is in the home directory below.) 

The following is an example of examining pop eax

```
rg -l /home/Users/Rg-master/TEST/libc-2.15.so -s "pop eax"

   <Omission>

   fe3f7:	pop    eax; 	add    esp,0x5c

   ff828:	pop    eax; 	add    esp,0x5c

  111aec:	pop    eax; 	add    esp,0x5c

  1121ae:	pop    eax; 	add    esp,0x5c

  115d8d:	pop    eax; 	add    esp,0x5c

  116c9e:	pop    eax
```
