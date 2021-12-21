import os, sys

import help

def is_root():
    if os.geteuid() == 0:
        return True
    else:
        return False

def get_args():
        return sys.argv[1:]

# def newhost():

def main():
    # Get arguments in order to run:
    # args needs an interactive mode that will guide you step-by-step, for ease of use.
    # then, also needs the option to script-ify the process and make a one-liner out of it.  
    args = get_args()

    if is_root():
        print(len(get_args()))
        
    elif not is_root():
        # queue manual page without root privileges:
        if len(args) == 1 and (args[0] == '-h' or args[0] == '--help'):
            help.manpage()
        elif len(args) == 1 and (args[0] != '-h' or args[0] != '--help'):
            help.manpage()
    
    else: 
        help.panic_exit()




if __name__== "__main__":
    main()