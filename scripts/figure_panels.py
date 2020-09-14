from IPython.core.interactiveshell import InteractiveShell
import os
import re
import pandas as pd
import numpy as np
from shutil import copyfile


from loguru import logger
from GEN_Utils import FileHandling

logger.info('Import OK')

input_folder = 'data_and_analysis/experiments/'
output_folder = 'figures/'

if not os.path.exists(output_folder):
    os.mkdir(output_folder)


def collect_panels(panel_paths, output_path):

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    for position, panel in panel_paths.items():
        old_path = f'{input_folder}{panel}'
        __, file_extension = os.path.splitext(old_path)
        new_path = f'{output_path}panel_{position}{file_extension}'
        new_path
        copyfile(old_path, new_path)


def collect_supp(supp_paths, output_path):

    if not os.path.exists(output_path):
        os.mkdir(output_path)
    for file_name, file_path in supp_paths.items():
        old_path = f'{input_folder}{file_path}'
        new_path = f'{output_path}{file_name}'
        copyfile(old_path, new_path)


"""Collect individual svg versions of figure panels and deposit here for editing. ONLY cosmetic edits can be performed manually once inside this folder. Consider eventually using pylustrator and svgutils to completely automate the figure construction process"""


# Figure 1: Figure name
output_path = f'{output_folder}F1_Figure name/'
panel_paths = {
    'A': 'path_to_panel.png',
    'B1': 'path_to_panel.svg',
    'B2': 'path_to_panel.svg',
    'C': 'path_to_panel.svg',
}

# collect_panels(panel_paths, output_path)


# Figure S1: Supp figure
output_path = f'{output_folder}S1_Supp figure name/'
panel_paths = {
    'A': 'path_to_panel.png',
    'B': 'path_to_panel.svg',
}

# collect_panels(panel_paths, output_path)


"""Collect supp info and deposit here for editing. ONLY cosmetic edits can be performed manually once inside this folder. Consider eventually using pylustrator and svgutils to completely automate the figure construction process"""

# Supp Table 1: Supp datasets
output_path = f'{output_folder}T1_data/'
supp_paths = {'supplementary_table_S1.xlsx': 'path_to_fle.xlsx'}
collect_supp(supp_paths, output_path)
