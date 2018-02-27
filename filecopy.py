#!/usr/bin/env python
#!/usr/bin/python
import sys
import os
import hashlib
import shutil
from datetime import datetime
import logging
import json
with open("/home/mediaworker/Config_files/config_filecpy.json") as configfile:
	data = json.load(configfile)


logpath = data["path"]["log"]
initial_source_path = data["path"]["src"]
final_source_path = data["path"]["dest"]
logging.basicConfig(filename = logpath, level = logging.DEBUG)

print initial_source_path
def copy(file):
	shutil.copy2(os.path.join(src,file), dest)
	logging.info("Copying-->" + file)

def filescheck(srclist = [], destlist = []):
	logging.info("Filecheck function Started")
	for x in srclist:
		if x not in destlist:
			copy(x)

def ensure_dir(filepath):
	directory = os.path.dirname(filepath)
	if not os.path.exists(directory):
		os.makedirs(directory)
		logging.info("DEST dir not Presrent//Creating one")


ensure_dir(final_source_path)
src = initial_source_path
dest = final_source_path
initial_source_path_list = os.listdir(initial_source_path)
final_source_path_list = os.listdir(final_source_path)
filescheck(initial_source_path_list, final_source_path_list)
