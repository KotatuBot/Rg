import re
import argparse
import os

from subprocess import *

def syscall_address(fpath):
    """
    get instruction data of syscall(int 0x80)
    args:
        fpath: libc file path
    """
    p1 = Popen(['objdump', '-d', '%s'% fpath], stdout=PIPE)
    p2 = Popen(['grep', 'int '], stdin=p1.stdout, stdout=PIPE)
    p3 = Popen(['head'],stdin=p2.stdout,stdout=PIPE)
    stdout, stderr = p3.communicate()
    print(stdout)

def link_lib(binary_path):
    resultlib = check_output(["ldd","%s" % binary_path])
    lib_pattern = r"libc.so.*"
    for i in resultlib.split("\t"):
       lib_list =  re.findall(lib_pattern,i)
       if lib_list:
        split_libc = str(lib_list).split(" ")
        print("File_name: {0}".format(split_libc[0].lstrip('[\'')))
        print(split_libc[2])
        

def one_search(search_data,data):
    """
    get instruction data from /tmp/gadget.txt

    args:
        search_data: search instructions
        data: data from /tmp/gadget.txt
    """
    search_data2 = search_data.replace("[","\[")
    search_data3 = search_data2.replace("+","\+")
    search_data = search_data3.replace("]","\]")
    hit_data = []
    # one nominic
    for one_data in data:
        address = one_data.split(":")
        nmonic = address[1].split("\t")[1:]
        for operand in nmonic:
            instruction = operand.replace("    "," ").rstrip("\n")
            # found Search nmonic in strings txt
            answer = re.findall(search_data+".*",instruction)
            if len(answer)!=0:
                hit_data.append(one_data)

    return hit_data

def gadget(searchs):
    """
    get /tmp/gadget.txt
    args:
        searchs: search instructions 
    """
    try:
        with open("/tmp/gadget.txt","r") as fd:
            hit_data = fd.readlines()

        for searh_imperative in searchs:
            hit_data = one_search(searh_imperative,hit_data)

        for hit in hit_data:
            print(hit)
    except IOError:
        print("No such file or directory: '/tmp/gadget.txt'.")
        print("You need to create the library with -l.")
        print("Specify target library. \n(Example: -l /usr/local/lib.so)")

def file_check():
    """
    /tmp/gadget.txt is exit
    """
    checker = os.path.exists("/tmp/gadget.txt")
    if checker == True:
        os.remove("/tmp/gadget.txt")


def output_gadget(fpath):
    """
    output /tmp/gadget.txt from libc 
    args:
        fpath: libc.so path
    """
    # check file
    file_check()

    with open(fpath, 'rb') as f:
        blob = f.read()

    try:
        i = -1
        while True:
            i = blob.index('\xc3', i+1)
            for j in range(4):
                p1 = Popen(['objdump', '-M', 'intel', '-D', '-b', 'binary', '-m', 'i386', "--start-address=%d" % (i-j-1), "--stop-address=%d" % (i+1), fpath], stdout=PIPE)
                p2 = Popen(['grep', '^ '], stdin=p1.stdout, stdout=PIPE)
                stdout, stderr = p2.communicate()
                if not stdout or '(bad)' in stdout or '<internal disassembler error>' in stdout:
                    continue
                lines = stdout.splitlines()
                with open("/tmp/gadget.txt","a") as fd:
                    if lines[-1].endswith('\tret    '):
                        fd.write(lines[0].split('\t',1)[0] + '\t'+'; \t'.join(line.split('\t')[2] for line in lines[:-1])+"\n")
    except ValueError:
        pass


def main():
    """
    rg is main function
    """
    parser = argparse.ArgumentParser(description='argparse sample.')

    parser.add_argument('-l [LIBRARY]','--load [LIBRARY]', type=str,nargs=None,help='Specify target library. (Example: -l /usr/local/lib.so)',dest='load')
    parser.add_argument('-s ["ORDER"]','--search ["ORDER"]',type=str,nargs=None,help='Specify the instruction to be searched from the library. (Example: -s "mov eax,al" -s "pop eax")',action='append',dest='search')
    parser.add_argument('-S [LIBRARY]','--Syscall [LIBRARY]',type=str,nargs=None,help='Specify target address of int 0x80(Example: -S /usr/local/libc.so)',dest='syscall')

    parser.add_argument('-L ["Link"]','--Link',type=str,nargs=None,dest='link')

    args = parser.parse_args()
    if args.syscall != None:
        filepath = args.syscall
        syscall_address(filepath)

    elif args.link != None:
        binary_path = args.link
        link_lib(binary_path)
        
    else:
        if args.load != None:
            output_gadget(args.load)
        if args.search != None:
            search_data = args.search
            gadget(search_data)
        else:
            print("Please you look help. rg -h")


if __name__== '__main__':
    main()
