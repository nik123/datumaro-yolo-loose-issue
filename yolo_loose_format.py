import os
from pathlib import Path
import shutil

import datumaro as dm

yolo_loose_dir = "yolo-loose-ds"

ds = dm.Dataset.import_from(str(yolo_loose_dir), "yolo_loose")
print(type(ds))
print(ds)
