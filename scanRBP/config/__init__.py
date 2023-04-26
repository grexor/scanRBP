import os
import sys

def init():
    config_module = sys.modules[__name__]
    scanRBP_folder = os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")) 
    config_file = os.path.abspath(os.path.join(scanRBP_folder, "scanRBP.config"))
    config_example_file = os.path.abspath(os.path.join(scanRBP_folder, "scanRBP.config.example"))
    if not os.path.exists(config_file):
        print("Please first check configuration parameters.")
        change()
        sys.exit(1)
    config_lines = open(config_file).readlines()
    for cline in config_lines:
        if cline.startswith("#"):
            continue
        k, v = cline.split("=")
        if k.find("folder")!=-1:
            if not v.startswith("/"):
                v = "\"" + os.path.join(scanRBP_folder, eval(v)) + "\""
        setattr(config_module, k, eval(v))

def change(data_folder=None):
    config_module = sys.modules[__name__]
    scanRBP_folder = os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")) 
    config_file = os.path.abspath(os.path.join(scanRBP_folder, "scanRBP.config"))
    config_example_file = os.path.abspath(os.path.join(scanRBP_folder, "scanRBP.config.example"))
    if not os.path.exists(config_file):
        os.system(f"cp {config_example_file} {config_file}")
    config_lines = open(config_file).readlines()
    print(f"Note: you can specify absolute or relative paths.\nRelative paths are relative to: {scanRBP_folder}")
    print()
    new_config = []
    for cline in config_lines:
        if cline.startswith("#"):
            continue
        k, v = cline.split("=")
        v = v.replace("\n", "").replace("\r", "").replace("\"", "").replace("'", "")
        v = os.path.expanduser(v)
        if k=="data_folder" and data_folder!=None:
            v = data_folder
        else:
            v = input(f"{k} [{v}]: ") or v
        v = os.path.expanduser(v)
        new_config.append((k, str(v)))
        setattr(config_module, k, v)
    f = open(config_file, "wt")
    for (k, v) in new_config:
        f.write(f"{k}=\"{v}\"\n")
    f.close()
