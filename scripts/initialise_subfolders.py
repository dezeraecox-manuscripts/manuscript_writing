import os, re
from loguru import logger


logger.info('Import OK')

"""Utility script to establish subfolder setup for new manuscript
Includes folder architecture that is needed for other scripts to function
e.g. the figure copying and conversion steps, pandoc md-->docx steps"""

folders = [
    'archive',
    'collaborators_edits',
    'resources',
    'data_and_analyses',
    'data_and_analyses/resources',
    'figures',
    'figures/utilities',
    'figures/outlines',
]

for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)
