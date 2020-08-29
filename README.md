<img src="./img/zawnbe.png" alt="Zawnbe.png"/>

# Zawnbe
Zanotti's youtube videos downloader is a python program which reads a text file with links of youtube videos and then download these videos.

## Requirements
It's necessary to have python 3.7 and pytube3 installed to run the program.
```bash
# To install pytube3 in python 3.7 run:
$ pip3 install pytube3      # linux
$ pip install pytube3       # windows
```

## Running
To use the program do:
```bash
# Clone the repository
$ git clone https://github.com/LeonardoZanotti/Zawnbe.git

# Enter the program folder
$ cd Zawnbe/

# Run the program
$ python3 zawnbe.py     # linux
$ python .\zawnbe.py    # windows
```

#### Error solving
Probably when you run the program first time you will get an error.
This error is "KeyError: 'cipher' and you will need to go to the pytube folder.

For **Linux** go to

    /home/{user}/.local/lib/python3.7/site-packages/pytube

For **Windows**, if you install python in the default location it should stay on

	C:\Users\{user}\AppData\Local\Programs\Python\Python37\Lib\site-packages\pytube


In this folder, open the `extract.py` file and change 

    parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats)

to

    parse_qs(formats[i]["signatureCipher"]) for i, data in enumerate(formats)

Then save and the program should run :D

### Leonardo Zanotti
