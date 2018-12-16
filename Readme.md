# Asort yerr plunder and stash yerr booty old salt!
For the tides are turning and the purveyors of ex-birds and curators of the flying circus are here to 
put their hands on deck.

### Using the script:
The script can be run from a terminal with zero or two arguments
```
>> python clean_downloads.py <Path_to_the_origin_dir> <Path_to_the_destination_dir>

or

>> python clean_downloads.py
```
The latter will guide the user with their operating systems directory selection dialog window to select the directories.

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
Where all the files have been renamed and cleaned with the execution of the miscellaneous files which have only been partially cleaned [_i.e. striped of symbols an titled_] for easier manual review after the script has been run.  The script will also move all folders which contained video files to a "Delete me" folder in the origin directory.

##### Know issues:
* The script can not distinguish between an miscellaneous video file and a movie without a release date  in the title which will be classified as miscellaneous files in the destination directory. 
* **The scrip will move folders to the "delete me" in origin even if it is not empty!** 
	* although in most cases it will only include subtitles, cover images and information files.
* The script will move Specials and Extras into Misc instead of the correct folder