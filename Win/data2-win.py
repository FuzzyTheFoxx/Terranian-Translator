import os; from os import system as sys
import argparse
_parser = argparse.ArgumentParser(
    exit_on_error=1, description=' --execution file--'
)
_parser.add_argument('--translation',
                     help=' --execiution file--'
                     )
_arg = _parser.parse_args()

letter = input('\n\n > ')

if _arg.translation == 'trlt':
    sys(f'py data1 --letter "{letter}" --translation trlt')
    sys('py data2')
elif _arg.translation == 'lttr':
    sys(f'py data1 --letter "{letter}" --translation lttr')
    sys('py data2')
