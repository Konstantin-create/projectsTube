from commands.server import *
from .parser import subparsers

import os
from argparse import Namespace


def server_route(args: Namespace):
    """Handler for server args"""

    path = os.getcwd()
    mode = 'dir'
    if args.dir:
        path = args.dir
        mode = 'dir'
    elif args.filename:
        path = args.filename
        mode = 'file'

    server = Server(path=path, mode=mode)

    server.run()


server_parser = subparsers.add_parser('share', help='command to create projectsTube server')
server_parser.add_argument(
    '-f', '--file',
    metavar='filename',
    dest='filename',
    help='share file'
)

server_parser.add_argument(
    '-d', '--dir',
    metavar='dir',
    dest='dir',
    help='share dir'
)

server_parser.add_argument(
    '-p', '--password',
    metavar='password',
    dest='password',
    help='set password on file or folder'
)

# todo: ignores files
