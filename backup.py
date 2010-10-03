import subprocess
import sys
import fileinput
import os
from github2.client import Github

filename1 = sys.argv[1]
filename2 = sys.argv[2]
file = open(filename1,"r")
uname = file.readline()
newfile = open(filename2,"r")
token =newfile.readline()
uname = uname.rstrip(os.linesep)
token = token.rstrip(os.linesep)
github = Github(username=uname,api_token =token)
repos = github.repos.list("memlab")
print repos
for i in range(len(repos)):
	subprocess.call([ 'bash','clone.sh',repos[i].name])
	 
	 

