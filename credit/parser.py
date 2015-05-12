"""
Command line parsing
"""

import argparse
from credit import main

try:
    from credit import __desc__ # try to get version number
except ImportError:
    __desc__ = 'UNKNOWN'


def setup_parser():
    parser = gen_parent_parser()
    add_subparsers(parser)
    return parser


def gen_parent_parser():
    """
    Generates the parser
    """
    description = 'Maintain your credit easily.'
    parser = argparse.ArgumentParser(add_help=True, \
                                     conflict_handler='resolve',\
                                     description=description)

    help = "Current version of credit"
    parser.add_argument('--version', '-v',  action='version', help=help, \
                        version=__desc__)

    return parser


def add_subparsers(parser):
    """
    Adds various subparsers to the main parser
    """
    subparsers = parser.add_subparsers(help='sub-command help')

    # all the subparsers
    add_new_subparser(subparsers)
    add_print_subparser(subparsers)
    add_display_subparser(subparsers)
    add_net_subparser(subparsers)
    add_reset_subparser(subparsers)
    add_delete_subparser(subparsers)


def add_new_subparser(subparsers):
    """
    Subparser for the new command
    """
    parser_new = subparsers.add_parser('new')

    help = "Creates a new credit sheet with the supplied name"
    parser_new.add_argument('sheet', type=str, help=help)

    help = "Change the creation date. Defaults to current date"
    parser_new.add_argument('--date', '-d', type=str, default=main.timestamp(),\
                            help=help)


def add_print_subparser(subparsers):
    """
    Subparser for the display command
    """
    parser_print = subparsers.add_parser('print')

    help = "Prints the contents of the credit sheet"
    parser_print.add_argument('print', type=str, help=help)


def add_display_subparser(subparsers):
    """
    Subparser for the display command
    """
    parser_display = subparsers.add_parser('display')

    help = "Displays all the credit sheets in the current account"
    parser_display.add_argument('display', action='store_true', help=help)

    help = "To hide the totals of the sheets "
    parser_display.add_argument('--nototal', action='store_true', help=help)


def add_net_subparser(subparsers):
    """
    Subparser for the net command
    """
    parser_net = subparsers.add_parser('net')

    help = "Gives the net balance. Totals over all the sheets of the current \
        account"
    parser_net.add_argument('net', action='store_true', help=help)

    help = "To hide the totals of the sheets "
    parser_net.add_argument('--nototal', action='store_true', help=help)


def add_reset_subparser(subparsers):
    """
    Subparser for the reset command
    """
    parser_reset = subparsers.add_parser('reset')

    help = "Reset a credit sheet"
    parser_reset.add_argument('reset', type=str, help=help)

    help = "Change the creation date. Defaults to current date"
    parser_reset.add_argument('--date', '-d', type=str, default=main.timestamp(),\
                            help=help)


def add_delete_subparser(subparsers):
    """
    Subparser for the delete command
    """
    parser_delete = subparsers.add_parser('delete')

    help = "Deletes an existing credit sheet"
    parser_delete.add_argument('sheet', type=str, help=help)
