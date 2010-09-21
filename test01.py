import subprocess
import sys
from github2.client import Github


for i in range(len(repos)):
	subprocess.call([ 'bash','clone.sh',repos[i].name])
	 
	 

