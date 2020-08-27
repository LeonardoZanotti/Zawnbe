#!/usr/bin/env python3

# -*- coding: utf-8 -*-
import sys,os,platform
from optparse import OptionParser

file = sys.argv

colors = True	# output colored c:
machine = sys.platform 		# detecting the os
checkPlatform = platform.platform()	# get current version of os
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
	colors = False 	# Mac and Windows shouldn't display colors :c
if checkPlatform.startswith("Windows-10") and int(platform.version().split(".")[2]) >= 10586:
	color = True	# coooolorssss \o/
	os.system('')	# Enables the ANSI -> standard encoding that reads that colors
if not colors:
	BGreen = BYellow = BPurple = BCyan = Yellow = Green = On_Black = ''
else:
	BGreen = "\033[1;32m"      # Bold Green
	BYellow = "\033[1;33m"     # Bold Yellow
	BPurple = "\033[1;35m"     # Bold Purple
	BCyan = "\033[1;36m"       # Bold Cyan
	Yellow = "\033[0;33m"      # Yellow
	Green = "\033[0;32m"      # Green

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


# Options

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
	'''.format(BGreen=BGreen,BCyan=BCyan,BPurple=BPurple))
	return

def helperFile():
	print('''
{BGreen}Usage:
{Green}Put all the youtube videos links that you want to download in a links.txt text file like this:
{Yellow}	
	links.txt:
	________________________________________________________
	|https://www.youtube.com/watch?v=A-tiTBdFe68,		|
	|https://www.youtube.com/watch?v=6EOrL6i5C98,		|
	|https://www.youtube.com/watch?v=oNFMjW-s-SU 		|
	|							|
	|							|
	|							|
	|							|													
	|_______________________________________________________|

{Green}Put one link per line and a comma in the end of each one. Then do:
	\t
	{BCyan}$ python3 zawnbe.py --file links.txt

		'''.format(BGreen=BGreen,BCyan=BCyan,Green=Green,Yellow=Yellow))
	return

parser = OptionParser(add_help_option=False)
parser.add_option('-h','--help',action='store_true',dest='help')
parser.add_option('--helplink',action='store_true',dest='helplink')
parser.add_option('--helpfile',action='store_true',dest='helpfile')
parser.add_option('-l','--link',type='string',dest='link')
parser.add_option('-f','--file',type='string',dest='file')
opts, args = parser.parse_args()

if (opts.help):
	helper()
if (opts.helplink):
	helperLink()
if (opts.helpfile):
	helperFile()
if (opts.link):
	print(opts.link)
if (opts.file):
	print(opts.file)
	

	# http://devfuria.com.br/python/manipulando-arquivos-de-texto/
	# https://www.google.com/search?q=baixar+v%C3%ADdeo+do+youtube+com+python3
	# https://www.it-swarm.dev/pt/python/faca-o-download-do-video-do-youtube-usando-o-python-para-um-determinado-diretorio/829550136/
	# https://towardsdatascience.com/the-easiest-way-to-download-youtube-videos-using-python-2640958318ab
	# https://blog.usejournal.com/how-to-download-youtube-videos-in-python-a48701e70389