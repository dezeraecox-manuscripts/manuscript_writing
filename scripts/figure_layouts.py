
import os
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from svgutils.compose import *
from loguru import logger
from GEN_Utils import FileHandling

logger.info('Import OK')

# -----------------------------Figure 1-------------------------------------------------

input_folder = 'figures/F1_figure name/'
output_path = 'figures/F1_figure name/figure_1.svg'

fig_1 = Figure("15cm", "15cm",
               Panel(
                   SVG(f'{input_folder}panel_A.svg').scale(2.5).move(10, 10),
                   Text("A", 2, 25, size=14, weight='bold')
               ),
               Panel(
                   SVG(f'{input_folder}panel_B.svg').scale(0.75),
                   Text("B", 0, 25, size=14, weight='bold')
               ).move(220, 0),
               Panel(
                   SVG(f'{input_folder}panel_C.svg').scale(0.75),
                   Text("C", 2, 25, size=14, weight='bold')
               ).move(0, 210),
               Panel(
                   SVG(f'{input_folder}panel_D.svg').scale(0.92),
                   Text("D", 0, 25, size=14, weight='bold')
               ).move(328, 208)
               )

# fig_1.save(output_path)

