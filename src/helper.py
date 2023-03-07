# Basic Initilazation
from rich import console
from rich import print
from rich import progress
from rich import prompt
import rich # Install rich with "pip install rich"
import os
import gzip
import shutil
import glob
import pprint

console = console.Console()

LOG_DIR_PATH = "/Users/kockeike/MyFiles/Shared/mc_logs/"

def setLogDirPath(path):
    LOG_DIR_PATH = path

def unzipLogFiles():
	for file in glob.glob(LOG_DIR_PATH + "*.gz"):
		out_file = file.replace(".log.gz", ".log")
		with gzip.open(file, 'rb') as f_in:
			with open(out_file, 'wb') as f_out:
				shutil.copyfileobj(f_in, f_out)

def whoJoinedWhen():
	players_joined = {}
	for file in glob.glob(LOG_DIR_PATH + "*.log"):
		f = open(file, 'r', errors='replace')
		lines = f.readlines()
		f.close()
		for line in lines:
			if "joined the game" in line:
				# [18:51:13] [Server thread/INFO]: AR07_TRC_Loop joined the game
				line = line.replace("[Server thread/INFO]: ", "")
				l = line.split(" ")
				data_date = os.path.basename(file)[0:10]
				data_time = l[0].replace("[", "").replace("]", "")
				data_player = l[1]
				if not (data_player in players_joined):
					players_joined[data_player] = []
				players_joined[data_player].append(data_date + " " + data_time)
	return players_joined

def numberOfJoins():
	joins = {}
	joins_dict = whoJoinedWhen()
	for key in joins_dict:
		joins[key] = len(joins_dict[key])
	return joins

# Example usage
setLogDirPath("/Users/kockeike/MyFiles/Shared/mc_logs/")
unzipLogFiles()
joins = whoJoinedWhen()
pprint.pprint(joins)
joins = numberOfJoins()
pprint.pprint(joins)