# Asort yerr plunder and stash yerr booty old salt!
For the tides are turning and the purveyors of ex-birds and curators of the flying circus are here to 
put their hands on deck.

### Using the script:
The script can be run from a terminal with zero or two arguments on a computer that has python 3.7+ installed ( maybe older versions work aswell )

to run the script you simply write this into any termal

```
>> python clean_downloads.py <Path_to_the_origin_dir> <Path_to_the_destination_dir>

or

>> python clean_downloads.py
```
The latter will guide the user with their operating systems directory selection dialog window to select the directories. using commndline and file explorer

### Functionality:
The script will search the origin directory for all video files excluding samples and move them to the destination directory in the following structure:

```
Destination
  - Misc
      - file
	  - ...

  - Movies
	  - file
	  - ...
	  
  - TV Shows
	  - <Show name>
		  - Season <0>	
		   	  - <Show name> S<00>E<00>
			  - ...
		  - ...
	  - ...
```
Where all the files have been renamed and cleaned with the execution of the miscellaneous files which are files with complecated naming schemes that the script could only partially clean, We did clean it a bit [_i.e. stripped the symbols_] for easier manual review after the script has been run.

##### Know issues:
* The script can not distinguish between an miscellaneous video file and a movie without a release date  in the title which will be classified as miscellaneous files in the destination directory. 
* The script will move Specials and Extras into Misc instead of the correct folder as there was no series of episode name, and the cleaning process cut on that, The "extras/specials" name was at a very random place and we could not use that as a pivot for finding the title
* The script was created for all platforms but has only been tested on Windows 10 
* The script may not move files if it's path's langth exceeds 260 charecters unless python was installed to do so
* The script will not remove folders which originally contained the desired files  