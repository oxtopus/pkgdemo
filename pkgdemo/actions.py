from optparse import OptionParser

def foo(*args):
    parser = OptionParser()
    
    parser.add_option("-b", "--bar", 
        dest="bar",
        help="Hello, bar!", 
        metavar="BAR")
    
    (options, args) = parser.parse_args()
    
    print ("%s:foo(" % __name__), ", ".join(args), "): ", vars(options)

def main(*args, **kwargs):
    parser = OptionParser()
    
    parser.add_option("-f", "--foo", 
        dest="foo",
        help="Hello, foo!", 
        metavar="FOO")

    (options, args) = parser.parse_args()

    cmd = args.pop(0) if args else None

    print __name__, cmd, options
