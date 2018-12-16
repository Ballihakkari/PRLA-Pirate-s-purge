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


Stuff 


1. Tekur inn tvö paths, Download folder og Structured folder
2. Ef hægt er að finna nafn á þátta seríu er gerð yfir mappa með nafni á þáttaröðinni
Þar sem allar kommur, bandstrik, undirstik og fleirra sambærilegt er fjarlægt og bil sett í staðinn
Þ.e. t.d . The-Big.Bang_Theory => The Big Bang Theory
3. Ef hægt er að finna seríu númer á þætti þá er gerð undirmappa inní yfirmöppu þátaraðarinnar með nafni seríunnar 
4. Þættir eru færðir út downloads yfir í þá skrá sem þeir eiga heima í.


AUKAKRÖFUR
Sækja nöfn á þáttum og bæta því við nafn á þætti.
Flokka meira en bara myndir/Þætti
Misc metadata t.d. Útgáfudag og Texta
Sækja synopsis af seríunni
Synopsis





Hlutir sem hægt er að gera 


      1)Búa til fall sem notar Glob og sækja alla þætti/myndir út frá download directory setja í lista
      Returnar listanum.
      
      2) Búa til fall inn stak úr listanum frá fetch data, Greinir nafnið á þátt/mynd, seríu númer og þáttanúmer
	    Skilar tuple með hreinsuðu nafni, seríunúmeri og þáttanúmeri( seríu og þáttanúmer ef það á við )
	    Ef seríunúmer/þáttaheiti finst ekki þá er skilað none í þeim dálkum.
      
      3)  Tekur inn þáttaheiti og seríunúar, leitar í structured data möppunni að möppu með því heiti ef það finnst ekki er sú mappa búin til, ef seríu númer er ekki none þá gerir það, það sama inn í möppunni sem bar búin til.



add_file_to_dest(tuple(Show name, Season), str)
	Tekur við tuple sem segir til um þátta nafn og seríu, býr til þær möppur sem á við
	Gerir ekkert ef viðeigandi möppur eru nú þegar til
	TODO auðvelt að bæta við virkni til þess að láta fallið færa möppurnar sjálfar yfir og endurskýra þær 
