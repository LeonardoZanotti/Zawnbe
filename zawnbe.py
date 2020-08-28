#!/usr/bin/env python3
# Leonardo José Zanotti
# https://github.com/LeonardoZanotti/Zawnbe

# -*- coding: utf-8 -*-
import sys,os,platform
from optparse import OptionParser
from pytube import YouTube

file = sys.argv

##### colors
colors = True	# output colored c:
machine = sys.platform 		# detecting the os
checkPlatform = platform.platform()	# get current version of os
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
	colors = False 	# Mac and Windows shouldn't display colors :c
if checkPlatform.startswith("Windows-10") and int(platform.version().split(".")[2]) >= 10586:
	color = True	# coooolorssss \o/
	os.system('')	# Enables the ANSI -> standard encoding that reads that colors
if not colors:
	BGreen = BYellow = BPurple = BCyan = Yellow = Green = Red = Blue = On_Black = ''
else:
	BGreen = "\033[1;32m"     # Bold Green
	BYellow = "\033[1;33m"    # Bold Yellow
	BPurple = "\033[1;35m"    # Bold Purple
	BCyan = "\033[1;36m"      # Bold Cyan
	Yellow = "\033[0;33m"     # Yellow
	Green = "\033[0;32m"      # Green
	Red = "\033[0;31m"      # Red
	Blue = "\033[0;34m"     # Blue

	# Background
	On_Black="\033[40m"       # Black Background

if len(file) == 1:
	print('''
		{On_Black}{BCyan}
		\t _____                   _          
		\t|__  /__ _ _ ____      _| |__   ___ 
		\t  / // _` | '_ \ \ /\ / / '_ \ / _ \\
		\t / /| (_| | | | \ V  V /| |_) |  __/
		\t/____\__,_|_| |_|\_/\_/ |_.__/ \___|
		\t
		{BYellow} # Zanotti's youtube videos downloader{Green}

For {BGreen}help {Green}type:
\t
{BGreen}$ python3 zawnbe.py --help                             
		'''.format(BCyan=BCyan,BGreen=BGreen,Green=Green,BYellow=BYellow,On_Black=On_Black))                                   

	sys.exit()


##### Options

def helper():
	print('''
{BGreen}Usage: zanwbe.py [options] (arg)

{BPurple}Options:{Yellow}
	-h, --help 		| show this message
	--helplink 		| show the help for the -l/--link option
	--helpfile 		| show the help for the -f/--file option
	-l, --link 		| download a single youtube video
	-f, --file 		| read a text file and download the videos of the links in the file
	'''.format(BGreen=BGreen,BPurple=BPurple,Yellow=Yellow))
	return

def helperLink():
	print('''
{BGreen}Usage:
\t {BCyan}$ python3 zawnbe.py --link [youtube video link]

{BPurple}Example:
\t {BCyan}$ python3 zawnbe.py --link https://www.youtube.com/watch?v=edC-dxfyr20

{Green}Your video will be saved in ./videos
	'''.format(BGreen=BGreen,BCyan=BCyan,BPurple=BPurple,Green=Green))
	return

def helperFile():
	print('''
{BGreen}Usage:
{Green}Put all the youtube videos links that you want to download in a links.txt text file like this:
{Yellow}	
	links.txt:
	________________________________________________________
	|https://www.youtube.com/watch?v=A-tiTBdFe68		|
	|https://www.youtube.com/watch?v=6EOrL6i5C98		|
	|https://www.youtube.com/watch?v=oNFMjW-s-SU 		|
	|							|
	|							|
	|							|
	|							|													
	|_______________________________________________________|

{Green}Put one link per line. Then do:
	\t
	{BCyan}$ python3 zawnbe.py --file links.txt

{Green}Your videos will be saved in ./videos
		'''.format(BGreen=BGreen,BCyan=BCyan,Green=Green,Yellow=Yellow))
	return

parser = OptionParser(add_help_option=False)
parser.add_option('-h','--help',action='store_true',dest='help')
parser.add_option('--helplink',action='store_true',dest='helplink')
parser.add_option('--helpfile',action='store_true',dest='helpfile')
parser.add_option('-l','--link',type='string',dest='link')
parser.add_option('-f','--file',type='string',dest='file')
opts, args = parser.parse_args()

def download(video):
	print('{Green}Downloading video...'.format(Green=Green))
	YouTube(video).streams.first().download('./videos')
	print('Downloaded!')
	# Fazer barra de progresso
	# Colocar aquela barrinha girando print(\b \|/-\|/-)
	return

if (opts.help):
	helper()
if (opts.helplink):
	helperLink()
if (opts.helpfile):
	helperFile()
if (opts.link):
	download(opts.link)
if (opts.file):
	if (opts.file.split('.')[1] == "txt"):
		print('{Green}Reading the file...'.format(Green=Green))
		fileOpened = open(opts.file, 'r', encoding="utf8")
		print('Read!')
		for line in fileOpened:
			download(line)
		fileOpened.close()
	else:
		print('{Red}This is not a text file!'.format(Red=Red))

sys.exit()