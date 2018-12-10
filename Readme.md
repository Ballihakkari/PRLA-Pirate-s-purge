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
