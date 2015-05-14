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
    subparsers = parser.add_subparsers(dest='action', title='sub-commands', \
                                       help='sub-command -h for help')

    # all the subparsers
    add_new_subparser(subparsers)
    add_print_subparser(subparsers)
    add_update_subparser(subparsers)
    add_net_subparser(subparsers)
    add_report_subparser(subparsers)
    add_reset_subparser(subparsers)
    add_delete_subparser(subparsers)


def add_new_subparser(subparsers):
    """
    Subparser for the new command
    """
    parser_new = subparsers.add_parser('new')

    help = "Creates a new credit sheet with the supplied name"
    parser_new.add_argument('sheet', type=str, help=help)


def add_print_subparser(subparsers):
    """
    Subparser for the display command
    """
    parser_print = subparsers.add_parser('print')

    help = "Prints the contents of the credit sheet"
    parser_print.add_argument('sheet', type=str, help=help)

    help = "Returns the raw contents of the credit sheet"
    parser_print.add_argument('--raw', action='store_true', help=help)


def add_update_subparser(subparsers):
    """
    Subparser for the update command
    """
    parser_update = subparsers.add_parser('update')

    help = "Name of the sheet in which update takes place."
    parser_update.add_argument('sheet', type=str, help=help)

    help = "amount to be added.(+/- number)."
    parser_update.add_argument('amount', type=str, help=help)

    help = "Change the date. Defaults to current date."
    parser_update.add_argument('--date', default=main.timestamp(), help=help)


def add_net_subparser(subparsers):
    """
    Subparser for the net command
    """
    parser_net = subparsers.add_parser('net')

    help = "Gives the net balance. Totals over all the sheets of the current \
        account. By default ignores sheet with name me."
    parser_net.add_argument('net', action='store_true', help=help)


def add_report_subparser(subparsers):
    """
    Subparser for the report command
    """
    parser_report = subparsers.add_parser('report')

    help = "Gives the full report."
    parser_report.add_argument('report', action='store_true', help=help)

    help = "Gives the report for a particular date. By default, full report is \
        given"
    parser_report.add_argument('--date', default=None, help=help)


def add_reset_subparser(subparsers):
    """
    Subparser for the reset command
    """
    parser_reset = subparsers.add_parser('reset')

    help = "Reset a credit sheet"
    parser_reset.add_argument('sheet', type=str, help=help)


def add_delete_subparser(subparsers):
    """
    Subparser for the delete command
    """
    parser_delete = subparsers.add_parser('delete')

    help = "Deletes an existing credit sheet"
    parser_delete.add_argument('sheet', type=str, help=help)
