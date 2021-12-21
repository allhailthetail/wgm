import os, sys, subprocess
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
    # Get arguments:
    args = get_args()

    # Check if root before continuing:
    if is_root():
        print(len(get_args()))
    
    # If not root,
    elif not is_root():
        # -h or --help opens man page without privileges:
        if len(args) == 1 and (args[0] == '-h' or args[0] == '--help'):
            help.manpage()
        elif len(args) == 1 and (args[0] != '-h' or args[0] != '--help'):
            help.warn_no_root()
    # Panic Condition:
    else: 
        help.panic_exit()




if __name__== "__main__":
    main()