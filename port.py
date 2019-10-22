import argparse
from socket import *


def connect(host, port):
    setdefaulttimeout(5)
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host, port))
        return s
    except:
        pass


def scanner(host, port):
    s = connect(host, port)
    if s:
        print("open ====> " + host + ":" + str(port))
    else:
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--server", dest='server')
    parser.add_argument("-p", "--port", dest='ports', type=int, nargs='+')
    args = parser.parse_args()

    if args.server and args.ports:
        for port in args.ports:
            scanner(gethostbyname(args.server), port)
    else:
        print("nothing !!")


if __name__ == '__main__':
    main()
