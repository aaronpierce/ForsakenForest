import json
import os 
import sys
import errno
import time

def resource_path(relative):
	if hasattr(sys, "_MEIPASS"):
		return os.path.join(sys._MEIPASS, relative)
	return os.path.join(relative)


def load(type):
	data = ''
	# with open('Entities/' + type + '.json', 'r') as f: (Before using resource_path function)
	with open(resource_path(os.path.join('Entities', (type + '.json'))), 'r') as f:
		data = json.load(f)
	return data

# Used only as a utlity to export a file to .json format to be used in game (func not used in game at all)
def to_json_format(data):
	file_name = ''
	with open(os.path.join('Entities', (file_name + '.json')), 'w+') as savefile:
		json.dump(data, savefile, indent = 4)
			
# Make sure appdata folder is created for player save
def check_appdata():
	app_data = os.getenv('LOCALAPPDATA')
	path = os.path.join(app_data, 'TheShadowKingdom')

	try:
		os.makedirs(path)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise

	player_file = os.path.join(path, 'player.json')
	return player_file

def game_help():
	help = '''
Help Menu:

Action - Description
--------------------------
- (n, s, e, w) : Moves player in the relative direction.
- (a) : Attack - Best weapon is equipped automatically for attacking.
- (t) : Trade - Access trade menu when Trader is present to buy/sell items.
- (h) : Heal - If player has received damage and has an item for healing in inventory.
- (i) : Inventory - Displays a list of the items in players inventory. ('+' Denotes equipped item)
- (+) : Save - Commits game save to file. (Overwrites previous save)
- (-) : Load -  Restores previously saved game. (Lose current game progress)
- (?) : Help - Displays help menu for game functions.
'''

	print(help)



def title():
	title = '''
                         .                                               
                     /   ))     |\         )               ).           
               c--. (\  ( `.    / )  (\   ( `.     ).     ( (           
               | |   ))  ) )   ( (   `.`.  ) )    ( (      ) )          
               | |  ( ( / _..----.._  ) | ( ( _..----.._  ( (           
 ,-.           | |---) V.'-------.. `-. )-/.-' ..------ `--) \._        
 | /===========| |  (   |      ) ( ``-.`\/'.-''           (   ) ``-._   
 | | / / / / / | |--------------------->  <-------------------------_>=-
 | \===========| |                 ..-'./\.`-..                _,,-'    
 `-'           | |-------._------''_.-'----`-._``------_.-----'         
               | |         ``----''            ``----''                  
               | |                                                       
               c--`     
          _______ _             _____ _               _               
         |__   __| |           / ____| |             | |              
            | |  | |__   ___  | (___ | |__   __ _  __| | _____      __
            | |  | '_ \ / _ \  \___ \| '_ \ / _` |/ _` |/ _ \ \ /\ / /
            | |  | | | |  __/  ____) | | | | (_| | (_| | (_) \ V  V / 
            |_|  |_| |_|\___| |_____/|_| |_|\__,_|\__,_|\___/ \_/\_/  
                    _  ___                 _                 
                   | |/ (_)               | |                
                   | ' / _ _ __   __ _  __| | ___  _ __ ___  
                   |  < | | '_ \ / _` |/ _` |/ _ \| '_ ` _ \ 
                   | . \| | | | | (_| | (_| | (_) | | | | | |
                   |_|\_\_|_| |_|\__, |\__,_|\___/|_| |_| |_|
                                  __/ |                      
                                 |___/                 
'''

	for line in title.splitlines():
		print(line)
		time.sleep(.1)



def title_new():
	title = """
                                                  !_
                                                  |*~=-.,
                                                  |_,-'`
                                                  |
                                                  |
                                                 /^\
                   !_                           /   \
                   |*`~-.,                     /,    \
                   |.-~^`                     /#"     \
                   |                        _/##_   _  \_
              _   _|  _   _   _            [ ]_[ ]_[ ]_[ ]
             [ ]_[ ]_[ ]_[ ]_[ ]            |_=_-=_ - =_|
           !_ |_=_ =-_-_  = =_|           !_ |=_= -    |
           |*`--,_- _        |            |*`~-.,= []  |
           |.-'|=     []     |   !_       |_.-"`_-     |
           |   |_=- -        |   |*`~-.,  |  |=_-      |
          /^\  |=_= -        |   |_,-~`  /^\ |_ - =[]  |
      _  /   \_|_=- _   _   _|  _|  _   /   \|=_-      |
     [ ]/,    \[ ]_[ ]_[ ]_[ ]_[ ]_[ ]_/,    \[ ]=-    |
      |/#"     \_=-___=__=__- =-_ -=_ /#"     \| _ []  |
     _/##_   _  \_-_ =  _____       _/##_   _  \_ -    |\
    [ ]_[ ]_[ ]_[ ]=_0~{_ _ _}~0   [ ]_[ ]_[ ]_[ ]=-   | \
    |_=__-_=-_  =_|-=_ |  ,  |     |_=-___-_ =-__|_    |  \
     | _- =-     |-_   | ((* |      |= _=       | -    |___\
     |= -_=      |=  _ |  `  |      |_-=_       |=_    |/+\|
     | =_  -     |_ = _ `-.-`       | =_ = =    |=_-   ||+||
     |-_=- _     |=_   =            |=_= -_     |  =   ||+||
     |=_- /+\    | -=               |_=- /+\    |=_    |^^^|
     |=_ |+|+|   |= -  -_,--,_      |_= |+|+|   |  -_  |=  |
     |  -|+|+|   |-_=  / |  | \     |=_ |+|+|   |-=_   |_-/
     |=_=|+|+|   | =_= | |  | |     |_- |+|+|   |_ =   |=/
     | _ ^^^^^   |= -  | |  <&>     |=_=^^^^^   |_=-   |/
     |=_ =       | =_-_| |  | |     |   =_      | -_   |
     |_=-_       |=_=  | |  | |     |=_=        |=-    |
^^^^^^^^^``^`^`^^`^`^`^^^^`^^`^``^^`^^`^^`^`^``^`^``^``^^
  _______ _             _____ _               _               
 |__   __| |           / ____| |             | |              
    | |  | |__   ___  | (___ | |__   __ _  __| | _____      __
    | |  | '_ \ / _ \  \___ \| '_ \ / _` |/ _` |/ _ \ \ /\ / /
    | |  | | | |  __/  ____) | | | | (_| | (_| | (_) \ V  V / 
    |_|  |_| |_|\___| |_____/|_| |_|\__,_|\__,_|\___/ \_/\_/  
            _  ___                 _                 
           | |/ (_)               | |                
           | ' / _ _ __   __ _  __| | ___  _ __ ___  
           |  < | | '_ \ / _` |/ _` |/ _ \| '_ ` _ \ 
           | . \| | | | | (_| | (_| | (_) | | | | | |
           |_|\_\_|_| |_|\__, |\__,_|\___/|_| |_| |_|
                          __/ |                      
                         |___/                 
"""
	for line in title.splitlines():
		print(line)
		time.sleep(.1)