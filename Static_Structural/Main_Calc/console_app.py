import sys
import os
import click
import click.exceptions


PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from Main_Calc.models import Model
from Main_Calc.simple_beam_1 import Write

@click.group()
def cli():
    pass

@cli.command()
@click.argument('simple_beam_point_load')
def newfuncion():

   """
   Calculations of 1 loaded beam construction
   :param simple_beam_point_load:
   :return:
   """
   car01 = Model('tak', 'nie')
   car01.show()




if __name__ == "__main__":
    cli()
