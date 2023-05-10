import glob
import os
import sys
from Bio import motifs
import scanRBP

pssm = {}

def download_pwm():
    # PWMs not present? download
    download = False
    pwm_folder = f"{scanRBP.config.data_folder}/pwm"
    if not os.path.exists(pwm_folder):
        os.makedirs(pwm_folder)
        download = True
    files = glob.glob(pwm_folder+"/*.mat")
    if len(files)==0 or download:
        data_folder = f"{scanRBP.config.data_folder}"
        os.system(f"wget http://zhanglab.c2b2.columbia.edu/data/mCross/eCLIP_mCross_PWM.tgz --no-check-certificate -O {data_folder}/eCLIP_mCross_PWM.tgz >/dev/null 2>&1")
        os.system(f"tar xfz {data_folder}/eCLIP_mCross_PWM.tgz -C {data_folder} >/dev/null 2>&1")
        os.system(f"mv {data_folder}/eCLIP_PWM/* {data_folder}/pwm >/dev/null 2>&1")
        os.system(f"rm {data_folder}/eCLIP_PWM/* >/dev/null 2>&1")
        os.system(f"rmdir {data_folder}/eCLIP_PWM >/dev/null 2>&1")
        os.system(f"rm {data_folder}/eCLIP_mCross_PWM.tgz >/dev/null 2>&1")

def init():
    download_pwm()
    for scan_id, data in scanRBP.database.proteins.items():
        fname = data["pwm_path"]
        fname = os.path.join(scanRBP.config.data_folder, data["pwm_path"])
        record = motifs.parse(open(fname), "TRANSFAC", strict=False)
        try:
            motif = record[0]
            motif.pseudocounts = 3
            pssm_temp = motif.pwm.log_odds()
            pssm[scan_id] = pssm_temp
        except:
            pass

