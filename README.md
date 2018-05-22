# ROP_Search
This command is for searching gadget in CTF's PWN problem.  
**Please use it for problem solving of CTF.**  
**I do not have responsibility for other uses**

## Usage
```
[-l dynlibray] [-s "instruction code"] [-S dynlibrary] [-h help]
```

[option]
```
-l,--load: Specify target library  
-s,--search: Specify the instruction to be searched from the library
-S,--Syscall: Specify target address of "int 0x80"
```

[example]
```
[If you load the library and look for "pop eax"]

rg -l /home/Users/libc-2.15.so -s "pop eax"

[If you are looking for "pop eax" without loading the library]

rg -s "pop eax"

[If you want to search for multiple instructions]

rg -s "pop eax" -s "pop esp"

[If you want to investigate int 0x80 which is the command of systemcall]

rg -S /home/Users/libc-2.15.so
```

__Once loaded, the loaded file is saved as /tmp/gadget.txt.__  
__So, when using the same library, you need to load the library with -l.__  
__If gadget.txt does not exist, an error occurs.__



## Install
You need setuptools in the python module.
```
sudo python setup.py install

usage: rg.py [-h] [-l [LIBRARY] LOAD] [-s ["ORDER"] SEARCH] [-S [LIBRARY]
             SYSCALL]

argparse sample.

optional arguments:
  -h, --help            show this help message and exit
  -l [LIBRARY] LOAD, --load [LIBRARY] LOAD
                        Specify target library. (Example: -l
                        /usr/local/lib.so)
  -s ["ORDER"] SEARCH, --search ["ORDER"] SEARCH
                        Specify the instruction to be searched from the
                        library. (Example: -s "mov eax,al" -s "pop eax")
  -S [LIBRARY] SYSCALL, --Syscall [LIBRARY] SYSCALL
                        Specify target address of int 0x80(Example: -S
                        /usr/local/libc.so)

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

# Licence
[MIT](https://github.com/KotatuBot/Rop/blob/master/LICENSE.txt)



