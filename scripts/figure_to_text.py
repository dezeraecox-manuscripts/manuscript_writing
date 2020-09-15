import os
import re
import subprocess
from shutil import copyfile

from loguru import logger

logger.info('Import OK')

input_folder = 'figures/'
output_folder = 'text/figures/'

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

def collect_figures(filename, input_folder, output_folder):

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    copyfile(f'{input_folder}{filename}', f'{output_folder}{filename}')


def convert_with_inkscape(filename, input_folder, output_folder):
    try:
        inkscape_path = subprocess.check_output(["where", "inkscape"]).strip()
    except subprocess.CalledProcessError:
        logger.info("ERROR: You need inkscape installed to use this script.")
        exit(1)

    args = [
        'inkscape',
        '--export-area-page',
        '--export-dpi=500',
        f'--export-filename={output_folder}{filename}.png',
        f'{input_folder}{filename}.svg'
    ]
    logger.info(args)
    subprocess.check_call(args)

"""Collects edited versions of figure layouts as svg from figures folder, then export png version according to document settings"""

# Collect all figures and tables
figures = [fig for fig in os.listdir(input_folder) if len(fig.split('_')) > 1]

labels = {
    'F': ('figure_', '.svg'),
    'S': ('figure_S', '.svg'),
    'T': ('table_', '.xlsx'),
    'ST': ('table_S', '.xlsx')
}

for figure_folder in figures:
    fig_type = re.split(r"\d", figure_folder.split('_')[0])[0]
    fig_number = re.split(r"[a-zA-Z]", figure_folder.split('_')[0])[-1]
    logger.info(fig_type)
    logger.info(fig_number)
    collect_figures(f'{labels[fig_type][0]}{fig_number}{labels[fig_type][1]}',
                    f'{input_folder}{figure_folder}/', output_folder)

# Convert all figures to png
figures = [fig for fig in os.listdir(output_folder) if '.svg' in fig]

for fig in figures:
    convert_with_inkscape(f'{fig.strip(".svg")}', output_folder, output_folder)
