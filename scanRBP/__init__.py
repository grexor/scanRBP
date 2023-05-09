"""
scanRBP

Scanning and plotting RNA-protein binding from PWM and CLIP data.

Github: https://github.com/grexor/scanRBP
"""

import os
import json
import scanRBP.config
import scanRBP.pwm
import scanRBP.database

scanRBP_path = os.path.abspath(__file__)
scanRBP_folder = os.path.dirname(scanRBP_path)
version = open(os.path.join(scanRBP_folder, "version"), "rt").readlines()[0].replace("\n", "").replace("\r", "")

# initialize path module
scanRBP.config.init()
scanRBP.database.init()
scanRBP.pwm.init()
