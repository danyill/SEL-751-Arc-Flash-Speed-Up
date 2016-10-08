#!/usr/bin/python
import argparse     # command line options
import anyconfig    # toml file reading
import os           # file system operations
import sys          # system operations

# read in the blessedly few configuration options
parser = argparse.ArgumentParser(description='Automate tedious SEL-751 arc flash settings')
parser.add_argument('--debug', action='store_true', help='show debugging information')
parser.add_argument('CONFIG_FILE', help='name of configuration file')
args = parser.parse_args()

# check existence of toml file and load configuration
mypath = os.path.abspath(os.path.dirname(sys.argv[0]))
fullpath = os.path.join(mypath, args.CONFIG_FILE)
if os.path.isfile(fullpath):
    print 'Looking for file'
    conf = anyconfig.load(fullpath, ac_parser='toml')
else:
    print "Need a configuration file. Duh."
    sys.exit(1)

def dprint(str):
    """ print debugging information
    """
    if args.CONFIG_FILE:
        print str

class PrimaryBay

print conf['Primary']['Bus']
print conf['Primary']['Coupler']
print conf['Secondary']
