# Fókusklukka með outro

## Yfirlit

Byggt með Python og Tkinter. Gerir notanda kleift að setja tíma fyrir fókusvinnu eða lærdóm. Eftir að niðurteljarinn er kominn í 57 sekúntur byrjar hvetjandi og goðsagnarkennt outro lag sem markar enda á vinnu með dramatískum hætti.

## Kröfur

- Python 3
- Pygame fyrir playback á outro lagi
- Tkinter fyrir GUI (kemur yfirleitt með Python 3)
- Threading fyrir samkvæma framkvæmd

## Uppsetning

1. Vertu viss um að þú sért með Python 3 uppsett.
2. Settu upp Pygame library.
3. Klónaðu eða downloadaðu þetta repo.

### Pygame uppsetning

`pip install pygame`

## Notkun

1. Keyrðu `main.py` til þess að hefja forritið.
2. Settu inn klst, mínútur og sekúntur í inntökin.
3. Smelltu á "Byrja fókus" til þess að hefja niðurtalningu.
4. Byrjaðu að vinna þangað til að goðsagnakennda outro lagið byrjar.
5. Tíminn mun síðan klárast í droppinu og þá poppa upp skilaboð.

## Sérsnið

- Ef þú vilt breyta laginu getur þú skipt út "output.mp3" í 'play_audio' fallinu með hvaða mp3 skrá af þínu vali.
- Það er einnig hægt að breyta tímasetningu á innkomu lagsins með því að breyta `if time_left == 57:` í main.py.
