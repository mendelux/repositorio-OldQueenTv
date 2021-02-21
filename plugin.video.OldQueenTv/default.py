# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Thanks to the Authors of the base code
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
#------------------------------------------------------------

import os, re
import sys
import plugintools
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
import requests
import base64
from resolveurl.plugins.lib import jsunpack 
myaddon =xbmcaddon .Addon ()


  
def log(message):
    xbmc.log(str(message),xbmc.LOGINFO)  
def run():
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec (action+"(params)")
    
    plugintools.close_item_list()
def keyboard_input(default_text="", title="", hidden=False):

    keyboard = xbmc.Keyboard(default_text,title,hidden)
    keyboard.doModal()
    
    if (keyboard.isConfirmed()):
        tecleado = keyboard.getText()
    else:
        tecleado = ""

    return tecleado
def base64dec(string):
  base64_message = string
  base64_bytes = base64_message.encode('ascii')
  message_bytes = base64.b64decode(base64_bytes)
  message = message_bytes.decode('ascii')
  return(message) 
  
# Menu

def main_list(params):    
    plugintools.add_item( #Television
        action="television", 
        title="[COLOR gold]Tv[/COLOR]",
        thumbnail="https://i.imgur.com/lXhpJT1.jpg",
        url= "",
		fanart="https://i.imgur.com/lXhpJT1.jpg",
        folder=True )     
    plugintools.add_item( #Cine
        action="cine", 
        title="[COLOR gold]Cine[/COLOR]",
        thumbnail="https://i.imgur.com/zmUgTUk.jpg",
        url= "",
		fanart="https://i.imgur.com/zmUgTUk.jpg",
        folder=True )               
    plugintools.add_item( #Serie
        action="series", 
        title="[COLOR gold]Series[/COLOR] ",
        thumbnail="https://i.imgur.com/q7oS0RX.jpg",
        url= "",
		fanart="https://i.imgur.com/q7oS0RX.jpg",
        folder=True )  
    plugintools.add_item( #Anime
        action="anime", 
        title="[COLOR gold]Anime[/COLOR] ",
        thumbnail="https://i.imgur.com/TlMq9f7.jpg",
        url= "",
		fanart="https://i.imgur.com/TlMq9f7.jpg",
        folder=True )      
    plugintools.add_item( #Infantil
        action="infantil", 
        title="[COLOR gold]Infantil[/COLOR]",
        thumbnail="https://i.imgur.com/0y0fpZe.jpg",
        url= "",
		fanart="https://i.imgur.com/0y0fpZe.jpg",
        folder=True )      
    plugintools.add_item( #Documentales
        action="documentales", 
        title="[COLOR gold]Documentales[/COLOR]",
        thumbnail="https://i.imgur.com/kQ9LJ8Y.jpg",
        url= "",
		fanart="https://i.imgur.com/kQ9LJ8Y.jpg",
        folder=True )   
    plugintools.add_item( #tuberika 
        action="tuberika", 
        title="[COLOR gold]QueenTube[/COLOR]",
        thumbnail="https://i.imgur.com/TVICOIG.jpg",
        url= "",
		fanart="https://i.imgur.com/TVICOIG.jpg", 
        folder=True )               

# Submenu Televisión
  
def television (params) : 
    plugintools.add_item(  #Guia TV   
        action="guiatv", 
        title="[COLOR gold]Guia TV[/COLOR]",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/71ik1wFIPOL.png",
        url= "https://www.formulatv.com/programacion/movistarplus/",
        fanart="https://images-na.ssl-images-amazon.com/images/I/71ik1wFIPOL.png",
        folder=True )  
    plugintools.add_item(  #adictos  
        action="adictos", 
        title="[COLOR gold]Tdt+Premium[/COLOR] [COLOR red]NECESARIO VPN[/COLOR]",
        thumbnail="https://i.imgur.com/msnvpNz.jpg",
        url= "https://adictosalatele.com/canales-de-espana/",
        fanart="https://i.imgur.com/msnvpNz.jpg",
        folder=True )
    plugintools.add_item(  #latinos  
        action="adictos", 
        title="[COLOR gold]Latinos[/COLOR] [COLOR red]NECESARIO VPN[/COLOR]",
        thumbnail="https://i.imgur.com/tTT0lFz.jpg",
        url= "https://adictosalatele.com/canales-latinos/",
        fanart="https://i.imgur.com/tTT0lFz.jpg",
        folder=True )        
    plugintools.add_item(  #Tv infantil  
        action="adictos", 
        title="[COLOR gold]Tv infantil[/COLOR] [COLOR red]NECESARIO VPN[/COLOR]",
        thumbnail="https://i.imgur.com/w5alGoX.jpg",
        url= "https://adictosalatele.com/infantiles/",
        fanart="https://i.imgur.com/w5alGoX.jpg",
        folder=True ) 
    plugintools.add_item(  #Daqueen TV  
        action="daqueen_tv", 
        title="[COLOR gold]Tv Premium[/COLOR]",
        thumbnail="https://i.imgur.com/gyrXGxr.jpg",
        url= "https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/canales%20vergol",
        fanart="https://i.imgur.com/gyrXGxr.jpg",
        folder= True )      
    plugintools.add_item(  #Seccion Daqueen  
        action="daqueen", 
        title="[COLOR gold]Deportes[/COLOR]",
        thumbnail="https://i.imgur.com/sR5eZMj.jpg",
        url= "",
        fanart="https://i.imgur.com/sR5eZMj.jpg",
        folder= True )     
    plugintools.add_item(  #Tdtchannels.com   
        action="tdtchannels", 
        title="[COLOR gold]TDTChannels[/COLOR]",
        thumbnail="https://i.imgur.com/mN2YQ8p.jpg",
        url= "https://www.tdtchannels.com/lists/tv.m3u",
        fanart="https://i.imgur.com/mN2YQ8p.jpg",
        folder=True )  
    plugintools.add_item(  #TeleOnline.org    
        action="canales", 
        title="[COLOR gold]TeleOnline.org[/COLOR]",
        thumbnail="https://i.imgur.com/mN2YQ8p.jpg",
        url= "https://teleonline.org/",
        fanart="https://i.imgur.com/mN2YQ8p.jpg",
        folder=True )            
    plugintools.add_item(  #Television Mundial   
        action="tdtmun", 
        title="[COLOR gold]Television Mundial[/COLOR]",
        thumbnail="https://i.imgur.com/CCcdjsY.jpg",
        url= "https://raw.githubusercontent.com/telegrambotdev/iptv/ba58c7c0b2c9c7653f6b2cd3b4b64012d854d81e/index.m3u",
        fanart="https://i.imgur.com/CCcdjsY.jpg",
        folder=True )    
    plugintools.add_item(  #Fluxus   
        action="fluxus", 
        title="[COLOR gold]Fluxus[/COLOR]",
        thumbnail="https://i.imgur.com/N2r6pj6.jpg",
        url= "https://fluxustvespanol.blogspot.com/p/fluxus-iptv.html",
        fanart="https://i.imgur.com/N2r6pj6.jpg",
        folder=True )
def daqueen(params): 
    plugintools.add_item(  #DailySport   
        action="daily", 
        title="[COLOR gold]Agenda DailySport[/COLOR]",
        thumbnail="https://i.imgur.com/kHOtn4i.jpg",
        url= "https://dailysport.bar",
        fanart="https://i.imgur.com/kHOtn4i.jpg",
        folder=True )   
    plugintools.add_item(  #Agenda Zona deportes Iberiko   
        action="daddylive", 
        title="[COLOR gold]Agenda DaddyLive[/COLOR]",
        thumbnail="https://i.imgur.com/2bsfGN5.jpg",
        url= "https://daddylive.club/",
        fanart="https://i.imgur.com/2bsfGN5.jpg",
        folder=True )  
    plugintools.add_item(  #Agenda SportZonline  
        action="SportZonline", 
        title="[COLOR gold]Agenda SportZonline[/COLOR]",
        thumbnail="https://i.imgur.com/N0YcFQR.jpg",
        url= "https://v3.sportzonline.to/prog.txt",
        fanart="https://i.imgur.com/N0YcFQR.jpg",
        folder=True )       
    plugintools.add_item(  #acestream  
        action="acestream", 
        title="[COLOR gold]Acestream 1080[/COLOR]",
        thumbnail="https://i.imgur.com/FjbBFzQ.jpg",
        url= "https://textbin.net/raw/F5zvW0F0IP",
        fanart="https://i.imgur.com/FjbBFzQ.jpg",
        folder=True )      
    plugintools.add_item(  #adictosaldeporte  
        action="adictosdeporte", 
        title="[COLOR gold]Canales de Deportes[/COLOR] [COLOR red]NECESARIO VPN[/COLOR]",
        thumbnail="https://i.imgur.com/RjQPYIB.jpg",
        url= "https://adictosaldeporte.com/",
        fanart="https://i.imgur.com/RjQPYIB.jpg",
        folder=True )
# Submenu Cine

def cine (params):
    plugintools.add_item( #CineMudo    
        action="CineMudo", 
        title="[COLOR gold]Cine Mudo[/COLOR]",
        thumbnail="https://imparcialoaxaca.mx/wp-content/uploads/2018/04/the-kid.jpg",
        url= "",
        fanart="https://imparcialoaxaca.mx/wp-content/uploads/2018/04/the-kid.jpg",     
        folder=True ) 
    plugintools.add_item( #cortosdemetraje    
        action="cortosdemetraje", 
        title="[COLOR gold]Cortos de metraje[/COLOR]",
        thumbnail="https://i.imgur.com/Es3s2z5.jpg",
        url= "",
        fanart="https://i.imgur.com/Es3s2z5.jpg",     
        folder=True )    
    plugintools.add_item( #DivxTotal    
        action="divxtotal", 
        title="[COLOR gold]DivxTotal[/COLOR] ",
        thumbnail="https://i.imgur.com/gg3nuQl.jpg",
        url= "",
        fanart="https://i.imgur.com/gg3nuQl.jpg",     
        folder=True )         
    plugintools.add_item( #Doramas MP4    
        action="doreamasmp4", 
        title="[COLOR gold]Doramas MP4[/COLOR]",
        thumbnail="https://i.imgur.com/fEIWKhj.jpg",
        url= "https://www25.doramasmp4.com/catalogue?format[]=movie",
        fanart="https://i.imgur.com/fEIWKhj.jpg",     
        folder=True )          
    plugintools.add_item( #EstrenosGo    
        action="EstrenosGo", 
        title="[COLOR gold]EstrenosGo[/COLOR]",
        thumbnail="https://estrenosgo.site/themes/default/css/imgs/BodyMainTop.png",
        url= "",
        fanart="https://estrenosgo.site/themes/default/css/imgs/BodyMainTop.png",     
        folder=True )          
    plugintools.add_item( #GranTorrent    
        action="grantorrent", 
        title="[COLOR gold]Grantorrent[/COLOR]",
        thumbnail="https://grantorrents.org/wp-content/uploads/2020/03/LOGOTEST.png",
        url= "",
	    fanart="https://grantorrents.org/wp-content/uploads/2020/03/LOGOTEST.png",
        folder=True )                      
    plugintools.add_item( #MiTorrent      
        action="mitorrent", 
        title="[COLOR gold]Mitorrent[/COLOR]",
        thumbnail="https://mitorrent.org/wp-content/uploads/2018/12/logo.png",
        url= "https://mitorrent.org/",
        fanart="https://mitorrent.org/wp-content/uploads/2018/12/logo.png",
        page="1",
        folder=True )   
    plugintools.add_item( #NewPelis    
        action="NewPelis", 
        title="[COLOR gold]NewPelis[/COLOR]",
        thumbnail="https://newpelis.nl/wp-content/themes/allcine/images/logoss.png",
        url= "https://www.newpct.me/peliculas/",
        fanart="https://newpelis.nl/wp-content/themes/allcine/images/logoss.png",     
        folder=True )
    plugintools.add_item( #NewPct    
        action="NewPct", 
        title="[COLOR gold]Newpct[/COLOR]",
        thumbnail="https://i.imgur.com/2neSJix.jpg",
        url= "",
        fanart="https://i.imgur.com/2neSJix.jpg",     
        folder=True )           
    plugintools.add_item( #PeliculasFLV    
        action="peliculasflv", 
        title="[COLOR gold]PeliculasFLV[/COLOR]",
        thumbnail="https://pbs.twimg.com/profile_images/626976217611259904/pd2VyRXn.png",
        url= "",
        fanart="https://pbs.twimg.com/profile_images/626976217611259904/pd2VyRXn.png",     
        folder=True )        
    plugintools.add_item( #PCTFenix    
        action="pctfenix", 
        title="[COLOR gold]PCTFenix[/COLOR]",
        thumbnail="https://pctfenix.com/view/template/assets/img/pctfenix.png",
        url= "",
        fanart="https://pctfenix.com/view/template/assets/img/pctfenix.png",
        folder=True )
    plugintools.add_item( #PCTmix    
        action="pctmix", 
        title="[COLOR gold]PCTmix[/COLOR]",
        thumbnail="https://pctmix.com/pctn/library/content/template/images/logos/pctmix.png",
        url= "",
        fanart="https://pctmix.com/pctn/library/content/template/images/logos/pctmix.png",     
        folder=True )                
    plugintools.add_item( #PCTReload    
        action="pctreload", 
        title="[COLOR gold]PCTReload[/COLOR]",
        thumbnail="https://pctreload1.com/pctn/library/content/template/images/logos/pctreload1.png",
        url= "",
        fanart="https://pctreload1.com/pctn/library/content/template/images/logos/pctreload1.png",     
        folder=True ) 
    plugintools.add_item( #Repelis    
        action="repelis", 
        title="[COLOR gold]Repelis [/COLOR]",
        thumbnail="https://i.imgur.com/uY8mqqG.jpg",
        url= "",
        fanart="https://i.imgur.com/uY8mqqG.jpg",     
        folder=True )
    plugintools.add_item( #repelis.uno    
        action="repelis_uno", 
        title="[COLOR gold]Repelis.uno[/COLOR]",
        thumbnail="https://i.imgur.com/uY8mqqG.jpg",
        url= "",
        fanart="https://i.imgur.com/uY8mqqG.jpg",     
        folder=True )            
    plugintools.add_item( #Tu_cine_clasico    
        action="Tu_cine_clasico", 
        title="[COLOR gold]Tu Cine Clásico[/COLOR]",
        thumbnail="https://yt3.ggpht.com/a/AATXAJxkK3l9W5hBG-wqzaEYhL8dzpMUAogW_20FEIufJw=s900-c-k-c0x00ffffff-no-rj",
        url= "",
        fanart="https://yt3.ggpht.com/a/AATXAJxkK3l9W5hBG-wqzaEYhL8dzpMUAogW_20FEIufJw=s900-c-k-c0x00ffffff-no-rj",     
        folder=True )
    plugintools.add_item( #zonatorrent_tv_pelis  
        action="zonatorrent_tv_pelis", 
        title="[COLOR gold]Zonatorrent[/COLOR]",
        thumbnail="https://i.imgur.com/KDZ2sgt.jpg",
        url= "https://zonatorrent.tv/pelicula-3/",
        fanart="https://i.imgur.com/KDZ2sgt.jpg",     
        folder=True )        
def CineMudo (params):
    plugintools.add_item( #Cine Mudo Español    
        action="infantil_playlist_Youtube", 
        title="[COLOR gold]Cine Mudo Español[/COLOR]",
        thumbnail="https://imparcialoaxaca.mx/wp-content/uploads/2018/04/the-kid.jpg",
        url= "https://www.youtube.com/playlist?list=PLHTdwgezn5j2e6oelA5-luAXJH4ns71J5",
        fanart="https://imparcialoaxaca.mx/wp-content/uploads/2018/04/the-kid.jpg",
        page="1",        
        folder=True )  
    plugintools.add_item( #Cine Mudo Internacional    
        action="resolve_playlist_Youtube", 
        title="[COLOR gold]Cine Mudo Internacional[/COLOR]",
        thumbnail="https://imparcialoaxaca.mx/wp-content/uploads/2018/04/the-kid.jpg",
        url= "https://www.youtube.com/watch?v=qtGaM_sAL-g&list=PLHTdwgezn5j1-pGAKI6gMwtrvQk9u5DQV",
        fanart="https://imparcialoaxaca.mx/wp-content/uploads/2018/04/the-kid.jpg",
        page="1",        
        folder=True )          
def Tu_cine_clasico (params):
    plugintools.add_item( #Tu_cine_clasico_search    
        action="clasico_peliculas_search", 
        title="[COLOR gold]Buscador Tu Cine Clasico[/COLOR]",
        thumbnail="https://yt3.ggpht.com/a/AATXAJxkK3l9W5hBG-wqzaEYhL8dzpMUAogW_20FEIufJw=s900-c-k-c0x00ffffff-no-rj",
        url= "https://online.tucineclasico.es/?s=",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",        
        folder=True )  
    plugintools.add_item( #Tu_cine_clasico    
        action="clasico_peliculas", 
        title="[COLOR gold]Películas[/COLOR]",
        thumbnail="https://yt3.ggpht.com/a/AATXAJxkK3l9W5hBG-wqzaEYhL8dzpMUAogW_20FEIufJw=s900-c-k-c0x00ffffff-no-rj",
        url= "https://online.tucineclasico.es/peliculas/",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",        
        folder=True )  
    plugintools.add_item( #Tu_cine_clasico_Genero    
        action="clasico_peliculas_genero", 
        title="[COLOR gold]Películas Por Genero[/COLOR]",
        thumbnail="https://yt3.ggpht.com/a/AATXAJxkK3l9W5hBG-wqzaEYhL8dzpMUAogW_20FEIufJw=s900-c-k-c0x00ffffff-no-rj",
        url= "https://pastebin.com/raw/7YaNMeqA",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",        
        folder=True )          
def peliculasflv (params):
    plugintools.add_item( #peliculas_flv_search    
        action="peliculas_flv_search", 
        title="Buscar en Películas FLV",
        thumbnail="https://pbs.twimg.com/profile_images/626976217611259904/pd2VyRXn.png",
        url= "https://www.peliculasflv.io/buscar/",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",        
        folder=True )  
    plugintools.add_item( #peliculas_flv_estrenos    
        action="peliculas_flv_estrenos", 
        title="[COLOR gold]Películas[/COLOR]",
        thumbnail="https://pbs.twimg.com/profile_images/626976217611259904/pd2VyRXn.png",
        url= "https://www.peliculasflv.io/estrenos/",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",        
        folder=True )  
    plugintools.add_item( #peliculas_flv_genero    
        action="peliculas_flv_genero", 
        title="[COLOR gold]Películas Por Genero[/COLOR]",
        thumbnail="https://pbs.twimg.com/profile_images/626976217611259904/pd2VyRXn.png",
        url= "https://www.peliculasflv.io/estrenos/",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",        
        folder=True )          
def repelis (params):
    plugintools.add_item( #Repelis Añadidos    
        action="repelis_aniadidos", 
        title="[COLOR gold]Repelis Añadidos[/COLOR]",
        thumbnail="http://pm1.narvii.com/6826/16d2ff57b64d571f43df6fb94b44ab1b4807e8c8v2_00.jpg",
        url= "https://www.repelisplus.vip/peliculas/",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",        
        folder=True )      
    plugintools.add_item( #Repelis estrenos    
        action="repelis_estrenos", 
        title="[COLOR gold]Repelis Estrenos [/COLOR]",
        thumbnail="http://pm1.narvii.com/6826/16d2ff57b64d571f43df6fb94b44ab1b4807e8c8v2_00.jpg",
        url= "https://www.repelisplus.vip/peliculas/estrenos/",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True ) 
    plugintools.add_item( #Repelis Popular    
        action="repelis_popular", 
        title="[COLOR gold]Repelis Popular[/COLOR]",
        thumbnail="http://pm1.narvii.com/6826/16d2ff57b64d571f43df6fb94b44ab1b4807e8c8v2_00.jpg",
        url= "https://www.repelisplus.vip/peliculas/popular/",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",        
        folder=True )          
    plugintools.add_item( #Repelis search   
        action="Repelis_search", 
        title="[COLOR gold]Repelis Buscador[/COLOR]",
        thumbnail="http://pm1.narvii.com/6826/16d2ff57b64d571f43df6fb94b44ab1b4807e8c8v2_00.jpg",
        url= "https://www.repelisplus.vip/buscar/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True ) 
def grantorrent (params):
    plugintools.add_item( #grantorrent_search   
        action="grantorrent_search", 
        title="[COLOR gold]Grantorrent Buscador[/COLOR]",
        thumbnail="https://grantorrents.org/wp-content/uploads/2020/03/LOGOTEST.png",
        url= "https://grantorrent.nl/?s=",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )  
    plugintools.add_item( #hdrip    
        action="hdrip", 
        title="[COLOR gold]Grantorrent HDRip[/COLOR]",
        thumbnail="https://grantorrents.org/wp-content/uploads/2020/03/LOGOTEST.png",
        url= "https://grantorrent.nl/categoria/HDRip-2/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )   
    plugintools.add_item( #blueray    
        action="blueray", 
        title="[COLOR gold]Grantorrent Bluray-1080p[/COLOR]",
        thumbnail="https://grantorrents.org/wp-content/uploads/2020/03/LOGOTEST.png",
        url= "https://grantorrent.nl/categoria/BluRay-1080p/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )   
    plugintools.add_item( #4K    
        action="cuatrok", 
        title="[COLOR gold]Grantorrent 4K[/COLOR]",
        thumbnail="https://grantorrents.org/wp-content/uploads/2020/03/LOGOTEST.png",
        url= "https://grantorrent.nl/categoria/4k-2/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )                    
def pctfenix (params): 
    plugintools.add_item( #fullbluray_1080p    
        action="fullbluray_1080p", 
        title="[COLOR gold]PCTFenix FullBluRay-1080p[/COLOR]",
        thumbnail="https://i.imgur.com/maslpiV.jpg",
        url= "https://pctfenix.com/descargar-peliculas/fullbluray-1080p/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )   
    plugintools.add_item( #bluray_1080p    
        action="bluray_1080p", 
        title="[COLOR gold]PCTFenix BluRay-1080p[/COLOR]",
        thumbnail="https://i.imgur.com/maslpiV.jpg",
        url= "https://pctfenix.com/descargar-peliculas/bluray-1080p/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )       
    plugintools.add_item( #dbremux_1080p    
        action="dbremux_1080p", 
        title="[COLOR gold]PCTFenix DBremux-1080p[/COLOR]",
        thumbnail="https://i.imgur.com/maslpiV.jpg",
        url= "https://pctfenix.com/descargar-peliculas/bdremux-1080p/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )
    plugintools.add_item( #cuatrok_uhdremux    
        action="cuatrok_uhdremux", 
        title="[COLOR gold]PCTFenix 4k-UHDremux[/COLOR]",
        thumbnail="https://i.imgur.com/maslpiV.jpg",
        url= "https://pctfenix.com/descargar-peliculas/4k-uhdremux/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )              
    plugintools.add_item( #4k uhdmicro   
        action="cuatrok_uhdmicro", 
        title="[COLOR gold]PCTFenix 4k-UHDmicro[/COLOR]",
        thumbnail="https://i.imgur.com/maslpiV.jpg",
        url= "https://pctfenix.com/descargar-peliculas/4k-uhdmicro/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )              
    plugintools.add_item( #4k uhdrip   
        action="cuatrok_uhdrip", 
        title="[COLOR gold]PCTFenix 4k-UHDrip[/COLOR]",
        thumbnail="https://i.imgur.com/maslpiV.jpg",
        url= "https://pctfenix.com/descargar-peliculas/4k-uhdrip/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )             
    plugintools.add_item( #4k webrip   
        action="cuatrok_webrip", 
        title="[COLOR gold]PCTFenix 4k-WEBrip[/COLOR]",
        thumbnail="https://i.imgur.com/maslpiV.jpg",
        url= "https://pctfenix.com/descargar-peliculas/4k-webrip/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )                     
    plugintools.add_item( #Full UHD4K    
        action="full_uhdcuatrok", 
        title="[COLOR gold]PCTFenix Full-UHD4K[/COLOR]",
        thumbnail="https://i.imgur.com/maslpiV.jpg",
        url= "https://pctfenix.com/descargar-peliculas/full-uhd4k/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )                    
    plugintools.add_item( #MicroHD 1080p    
        action="microhd_1080p", 
        title="[COLOR gold]PCTFenix MicroHD-1080p[/COLOR]",
        thumbnail="https://i.imgur.com/maslpiV.jpg",
        url= "https://pctfenix.com/descargar-peliculas/microhd-1080p/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )                                     
def pctreload (params): 
    plugintools.add_item( #pctreload_cast    
        action="pctreload_cast", 
        title="[COLOR gold]Peliculas en Catellano[/COLOR]",
        thumbnail="https://pctreload1.com/pctn/library/content/template/images/logos/pctreload1.png",
        url= "https://pctreload1.com/peliculas/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",
        folder=True )   
    plugintools.add_item( #pctreload_lat    
        action="pctreload_cast", 
        title="[COLOR gold]Peliculas en Latino[/COLOR]",
        thumbnail="https://pctreload1.com/pctn/library/content/template/images/logos/pctreload1.png",
        url= "https://pctreload1.com/peliculas-latino/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",
        folder=True ) 
    plugintools.add_item( #pctreload_cine    
        action="pctreload_cast", 
        title="[COLOR gold]Estrenos de Cine[/COLOR]",
        thumbnail="https://pctreload1.com/pctn/library/content/template/images/logos/pctreload1.png",
        url= "https://pctreload1.com/estrenos-de-cine/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",
        folder=True )
    plugintools.add_item( #pctreload_HD    
        action="pctreload_cast", 
        title="[COLOR gold]Peliculas HD[/COLOR]",
        thumbnail="https://pctreload1.com/pctn/library/content/template/images/logos/pctreload1.png",
        url= "https://pctreload1.com/peliculas-hd/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",
        folder=True )   
    plugintools.add_item( #pctreload_3d    
        action="pctreload_cast", 
        title="[COLOR gold]Peliculas en 3D[/COLOR]",
        thumbnail="https://pctreload1.com/pctn/library/content/template/images/logos/pctreload1.png",
        url= "https://pctreload1.com/peliculas-3d/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",
        folder=True )
    plugintools.add_item( #pctreload_x264.mkv   
        action="pctreload_cast", 
        title="[COLOR gold]Peliculas en x264.mkv[/COLOR]",
        thumbnail="https://pctreload1.com/pctn/library/content/template/images/logos/pctreload1.png",
        url= "https://pctreload1.com/peliculas-x264-mkv/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",
        folder=True ) 
    plugintools.add_item( #pctreload_V.O.   
        action="pctreload_cast", 
        title="[COLOR gold]Peliculas en V.O.[/COLOR]",
        thumbnail="https://pctreload1.com/pctn/library/content/template/images/logos/pctreload1.png",
        url= "https://pctreload1.com/peliculas-vo/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",
        folder=True )           
def pctmix (params): 
    plugintools.add_item( #pctmix_cast    
        action="pctmix_cast", 
        title="[COLOR gold]Peliculas en Catellano[/COLOR]",
        thumbnail="https://pctmix.com/pctn/library/content/template/images/logos/pctmix.png",
        url= "https://pctmix.com/peliculas/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",
        folder=True )   
    plugintools.add_item( #pctmix_lat    
        action="pctmix_cast", 
        title="[COLOR gold]Peliculas en Latino[/COLOR]",
        thumbnail="https://pctmix.com/pctn/library/content/template/images/logos/pctmix.png",
        url= "https://pctmix.com/peliculas-latino/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",
        folder=True ) 
    plugintools.add_item( #pctmix_cine    
        action="pctmix_cast", 
        title="[COLOR gold]Estrenos de Cine[/COLOR]",
        thumbnail="https://pctmix.com/pctn/library/content/template/images/logos/pctmix.png",
        url= "https://pctmix.com/estrenos-de-cine/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",
        folder=True )
    plugintools.add_item( #pctmix_HD    
        action="pctmix_cast", 
        title="[COLOR gold]Peliculas HD[/COLOR]",
        thumbnail="https://pctmix.com/pctn/library/content/template/images/logos/pctmix.png",
        url= "https://pctmix.com/peliculas-hd/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",
        folder=True )   
    plugintools.add_item( #pctmix_3d    
        action="pctmix_cast", 
        title="[COLOR gold]Peliculas en 3D[/COLOR]",
        thumbnail="https://pctmix.com/pctn/library/content/template/images/logos/pctmix.png",
        url= "https://pctmix.com/peliculas-3d/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",
        folder=True )
    plugintools.add_item( #pctmix_x264.mkv   
        action="pctmix_cast", 
        title="[COLOR gold]Peliculas en x264.mkv[/COLOR]",
        thumbnail="https://pctmix.com/pctn/library/content/template/images/logos/pctmix.png",
        url= "https://pctmix.com/peliculas-x264-mkv/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",
        folder=True ) 
    plugintools.add_item( #pctmix_V.O.   
        action="pctmix_cast", 
        title="[COLOR gold]Peliculas en V.O.[/COLOR]",
        thumbnail="https://pctmix.com/pctn/library/content/template/images/logos/pctmix.png",
        url= "https://pctmix.com/peliculas-vo/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",
        folder=True )  
def EstrenosGo (params): 
    plugintools.add_item( #EstrenosGo_cartelera    
        action="EstrenosGo_cartelera", 
        title="[COLOR gold]EstrenosGo Cartelera[/COLOR]",
        thumbnail="https://estrenosgo.site/themes/default/css/imgs/BodyMainTop.png",
        url= "https://estrenosflex.com/descarga-0-58126-0-0-fx-1-1-.fx",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",
        folder=True )          
    plugintools.add_item( #EstrenosGo_DVDRip    
        action="EstrenosGo_cartelera", 
        title="[COLOR gold]EstrenosGo DVDRip[/COLOR]",
        thumbnail="https://estrenosgo.site/themes/default/css/imgs/BodyMainTop.png",
        url= "https://estrenosflex.com/descarga-0-581210-0-0-fx-1-1-.fx",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",
        folder=True )  
    plugintools.add_item( #EstrenosGo_HDRip    
        action="EstrenosGo_cartelera", 
        title="[COLOR gold]EstrenosGo HDRip[/COLOR]",
        thumbnail="https://estrenosgo.site/themes/default/css/imgs/BodyMainTop.png",
        url= "https://estrenosflex.com/descarga-0-58128-0-0-fx-1-1-.fx",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        page="1",
        folder=True ) 
def NewPelis (params): 
    plugintools.add_item( #NewPelis    
        action="NewPelis_peliculas", 
        title="[COLOR gold]Todas las Peliculas[/COLOR]",
        thumbnail="https://newpelis.nl/wp-content/themes/allcine/images/logoss.png",
        url= "https://newpelis.nl/",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True ) 
    plugintools.add_item( #NewPelis    
        action="NewPelis_peliculas_top", 
        title="[COLOR gold]EL Top de Peliculas[/COLOR]",
        thumbnail="https://newpelis.nl/wp-content/themes/allcine/images/logoss.png",
        url= "https://newpelis.nl/favorites",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True )         
    plugintools.add_item( #NewPelis    
        action="NewPelis_peliculas_genero", 
        title="[COLOR gold]Peliculas Por Genero[/COLOR]",
        thumbnail="https://newpelis.nl/wp-content/themes/allcine/images/logoss.png",
        url= "https://pastebin.com/raw/ZUYcPEDh",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True )    
def cortosdemetraje (params): 
    plugintools.add_item( #cortosdemetrajecine    
        action="cortosdemetrajecine", 
        title="[COLOR gold]Cine[/COLOR]",
        thumbnail="https://i.imgur.com/Es3s2z5.jpg",
        url= "https://cortosdemetraje.com/cine/",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True )     
    plugintools.add_item( #cortosdemetrajedocus    
        action="cortosdemetrajedocus", 
        title="[COLOR gold]Documentales[/COLOR]",
        thumbnail="https://i.imgur.com/Es3s2z5.jpg",
        url= "https://cortosdemetraje.com/documental/",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True )  
    plugintools.add_item( #cortosdemetrajevuestroscortos    
        action="cortosdemetrajecine", 
        title="[COLOR gold]Vuestros Cortos[/COLOR]",
        thumbnail="https://i.imgur.com/Es3s2z5.jpg",
        url= "https://cortosdemetraje.com/vuestros-cortos/",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True ) 
    plugintools.add_item( #cortosdemetrajeanimacion    
        action="cortosdemetrajecine", 
        title="[COLOR gold]Animacion[/COLOR]",
        thumbnail="https://i.imgur.com/Es3s2z5.jpg",
        url= "https://cortosdemetraje.com/animacion/",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True )         
def NewPct (params): 
    plugintools.add_item( #NewPct    
        action="NewPcttodas", 
        title="[COLOR gold]Newpct Todas[/COLOR]",
        thumbnail="https://i.imgur.com/2neSJix.jpg",
        url= "https://www.newpct.me/peliculas/",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True )        
    plugintools.add_item( #NewPct    
        action="NewPcttodas", 
        title="[COLOR gold]Newpct En Castellano[/COLOR]",
        thumbnail="https://i.imgur.com/2neSJix.jpg",
        url= "https://www.newpct.me/idioma/castellano/",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True )
    plugintools.add_item( #NewPct    
        action="NewPcttodas", 
        title="[COLOR gold]Newpct En Latino[/COLOR]",
        thumbnail="https://i.imgur.com/2neSJix.jpg",
        url= "https://www.newpct.me/idioma/latino/",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True )
    plugintools.add_item( #NewPct    
        action="NewPcttodas", 
        title="[COLOR gold]Newpct Subtituladas[/COLOR]",
        thumbnail="https://i.imgur.com/2neSJix.jpg",
        url= "https://www.newpct.me/idioma/subtituladas/",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True )    
    plugintools.add_item( #NewPct    
        action="NewPct_search", 
        title="[COLOR gold]Newpct Buscar[/COLOR]",
        thumbnail="https://i.imgur.com/2neSJix.jpg",
        url= "https://www.newpct.me/?s=",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True )          
def repelis_uno (params): 
    plugintools.add_item( #repelis_uno   
        action="repelis_uno_peliculas", 
        title="[COLOR gold]Repelis.uno Peliculas[/COLOR]",
        thumbnail="https://i.imgur.com/uY8mqqG.jpg",
        url= "https://repelis.uno/",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True )        
    plugintools.add_item( #repelis_Estrenos   
        action="repelis_uno_peliculas", 
        title="[COLOR gold]Repelis.uno Estrenos[/COLOR]",
        thumbnail="https://i.imgur.com/uY8mqqG.jpg",
        url= "https://repelis.uno/estrenos",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True )  
    plugintools.add_item( #repelis_Marvel   
        action="repelis_uno_peliculas_pag2", 
        title="[COLOR gold]Repelis.uno Marvel Comics[/COLOR]",
        thumbnail="https://i.imgur.com/uY8mqqG.jpg",
        url= "https://repelis.uno/genero/marvel-comics?page=1",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True )
    plugintools.add_item( #repelis_DC   
        action="repelis_uno_peliculas", 
        title="[COLOR gold]Repelis.uno DC Comics[/COLOR]",
        thumbnail="https://i.imgur.com/uY8mqqG.jpg",
        url= "https://repelis.uno/genero/dc-comics",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True )  
    plugintools.add_item( #repelis_Disney   
        action="repelis_uno_peliculas_pag3", 
        title="[COLOR gold]Repelis.uno Disney[/COLOR]",
        thumbnail="https://i.imgur.com/uY8mqqG.jpg",
        url= "https://repelis.uno/genero/disney",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True )
    plugintools.add_item( #repelis_Genero   
        action="repelis_uno_peliculas_gen", 
        title="[COLOR gold]Repelis.uno Buscar Por Genero[/COLOR]",
        thumbnail="https://i.imgur.com/uY8mqqG.jpg",
        url= "https://repelis.uno/",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True )            
    plugintools.add_item( #repelis_año   
        action="repelis_uno_peliculas_year", 
        title="[COLOR gold]Repelis.uno Buscar Por Año[/COLOR]",
        thumbnail="https://i.imgur.com/uY8mqqG.jpg",
        url= "https://repelis.uno/",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True )       
def divxtotal (params): 
    plugintools.add_item( #divxtotal_Peliculas  
        action="divxtotal_peliculas", 
        title="DivxTotal Todas las Peliculas",
        thumbnail="https://i.imgur.com/gg3nuQl.jpg",
        url= "https://www.divxtotal.in/peliculas/",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True )        
    plugintools.add_item( #divxtotal_Peliculas   
        action="divxtotal_peliculas", 
        title="DivxTotal Subtituladas",
        thumbnail="https://i.imgur.com/gg3nuQl.jpg",
        url= "https://www.divxtotal.in/peliculas-sub/",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True ) 
    plugintools.add_item( #divxtotal_Peliculas   
        action="divxtotal_peliculas", 
        title="DivxTotal HD",
        thumbnail="https://i.imgur.com/gg3nuQl.jpg",
        url= "https://www.divxtotal.in/peliculas-hd/",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True )
    plugintools.add_item( #divxtotal_Peliculas   
        action="divxtotal_peliculas", 
        title="DivxTotal DVDRip",
        thumbnail="https://i.imgur.com/gg3nuQl.jpg",
        url= "https://www.divxtotal.in/peliculas-dvdr/",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True )         
    plugintools.add_item( #divxtotal_search   
        action="divxtotal_search", 
        title="DivxTotal Buscar",
        thumbnail="https://i.imgur.com/gg3nuQl.jpg",
        url= "https://www.divxtotal.in/?s=",
        fanart="special://home/addons/plugin.video.iberika/tenor.gif",     
        folder=True )         
                

# Submenu Series

def series (params):
    plugintools.add_item( #SeriesFlix    
        action="seriesflix", 
        title="[COLOR gold]SeriesFlix[/COLOR] ",
        thumbnail="https://i.imgur.com/gg3nuQl.jpg",
        url= "https://seriesflix.to/",
        fanart="https://i.imgur.com/gg3nuQl.jpg",     
        folder=True )
    plugintools.add_item( #divxtotal_Series  
        action="divxtotal_Series", 
        title="[COLOR gold]DivxTotal[/COLOR]",
        thumbnail="https://i.imgur.com/gg3nuQl.jpg",
        url= "https://www.divxtotal.in/series/",
	    fanart="https://i.imgur.com/gg3nuQl.jpg",                  
        page="1",
        folder=True )         
    plugintools.add_item( #Grantorrent_Series  
        action="Grantorrent_Series", 
        title="[COLOR gold]Gran Torrent[/COLOR]",
        thumbnail="https://grantorrents.org/wp-content/uploads/2020/03/LOGOTEST.png",
        url= "",
	    fanart="https://grantorrents.org/wp-content/uploads/2020/03/LOGOTEST.png",                  
        page="1",
        folder=True ) 
    plugintools.add_item( #mitorrent_Series  
        action="Mi_Torrent_Series", 
        title="[COLOR gold]Mi Torrent[/COLOR]",
        thumbnail="https://mitorrent.org/wp-content/uploads/2018/12/logo.png",
        url= "",
	    fanart="https://mitorrent.org/wp-content/uploads/2018/12/logo.png",                  
        page="1",
        folder=True )
    plugintools.add_item( #NewPelis _Series  
        action="NewPelis_series", 
        title="[COLOR gold]NewPelis[/COLOR] ",
        thumbnail="https://newpelis.nl/wp-content/themes/allcine/images/logoss.png",
        url= "https://newpelis.nl/series",
	    fanart="https://newpelis.nl/wp-content/themes/allcine/images/logoss.png",                  
        page="1",
        folder=True )           
    plugintools.add_item( #pctreload_series  
        action="pctreload_series", 
        title="[COLOR gold]PCTReload[/COLOR]",
        thumbnail="https://pctreload1.com/pctn/library/content/template/images/logos/pctreload1.png",
        url= "",
	    fanart="https://pctreload1.com/pctn/library/content/template/images/logos/pctreload1.png",                  
        page="1",
        folder=True )    
    plugintools.add_item( #pctmix_series  
        action="pctmix_series", 
        title="[COLOR gold]PCTmix[/COLOR]",
        thumbnail="https://pctmix.com/pctn/library/content/template/images/logos/pctmix.png",
        url= "",
	    fanart="https://pctmix.com/pctn/library/content/template/images/logos/pctmix.png",                  
        page="1",
        folder=True )      
    plugintools.add_item( #seriesly  
        action="seriesly_ultimas_series", 
        title="[COLOR gold]Seriesly[/COLOR]",
        thumbnail="https://comparaiso.es/sites/default/files/styles/_default/public/images/series-ly-200x280.png?itok=emlrWJrk",
        url= "https://seriesly.org/",
	    fanart="https://comparaiso.es/sites/default/files/styles/_default/public/images/series-ly-200x280.png?itok=emlrWJrk",                  
        page="1",
        folder=True )      
    plugintools.add_item( #retro_series 
        action="retroseriesmenu", 
        title="[COLOR gold]Retro Series[/COLOR]",
        thumbnail="https://seriesretro.com/wp-content/uploads/2020/06/5ed8d22a4ac42_originalcursi1.png",
        url= "",
	    fanart="https://seriesretro.com/wp-content/uploads/2020/06/5ed8d22a4ac42_originalcursi1.png",                  
        page="1",
        folder=True )   
    plugintools.add_item( #vernovelasonline
        action="vernovelasonline", 
        title="[COLOR gold]Vernovelasonline[/COLOR]",
        thumbnail="https://i.imgur.com/Dr6dHz0.jpg",
        url= "https://vernovelasonline.xyz/listado-de-telenovelas/",
	    fanart="https://i.imgur.com/Dr6dHz0.jpg",                  
        page="1",
        folder=True )           
def Grantorrent_Series (params):
    plugintools.add_item( #Series_Grantorrenr  
        action="grantorrent_series_nor", 
        title="[COLOR gold]Gran Torrent[/COLOR]",
        thumbnail="https://grantorrents.org/wp-content/uploads/2020/03/LOGOTEST.png",
        url= "https://grantorrent.nl/series/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",                  
        page="1",
        folder=True )
    plugintools.add_item( #Series_Grantorren categoria
        action="grantorrent_series_categoria", 
        title="[COLOR gold]Gran Torrent Por Categoría[/COLOR]",
        thumbnail="https://grantorrents.org/wp-content/uploads/2020/03/LOGOTEST.png",
        url= "https://grantorrent.nl/series/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",                  
        page="1",
        folder=True )    
def Mi_Torrent_Series (params):
    plugintools.add_item( #Series_mitorrent  
        action="mitorrent_series", 
        title="[COLOR gold]Mi Torrent Series[/COLOR]",
        thumbnail="https://i.imgur.com/DcBBOBf.jpg",
        url= "https://mitorrent.org/series/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",                  
        page="1",
        folder=True )
    plugintools.add_item( #Mi_torrent_Genero  
        action="Mi_torrent_Genero", 
        title="[COLOR gold]Mi Torrent Genero[/COLOR]",
        thumbnail="https://i.imgur.com/DcBBOBf.jpg",
        url= "https://pastebin.com/raw/4HBrcHX0",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",                  
        page="1",
        folder=True )
def pctreload_series (params):
    plugintools.add_item( #pctreload_series  
        action="pctreload_series_normal", 
        title="[COLOR gold]PCTReload Series[/COLOR]",
        thumbnail="https://pctreload1.com/pctn/library/content/template/images/logos/pctreload1.png",
        url= "https://pctreload1.com/series/pg/1",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",                  
        page="1",
        folder=True ) 
    plugintools.add_item( #pctreload_series_HD  
        action="pctreload_series_normal", 
        title="[COLOR gold]PCTReload Series HD[/COLOR]",
        thumbnail="https://pctreload1.com/pctn/library/content/template/images/logos/pctreload1.png",
        url= "https://pctreload1.com/series-hd/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",                  
        page="1",
        folder=True )         
def pctmix_series (params):
    plugintools.add_item( #pctreload_series  
        action="pctreload_series_normal", 
        title="[COLOR gold]PCTmix Series[/COLOR]",
        thumbnail="https://pctmix.com/pctn/library/content/template/images/logos/pctmix.png",
        url= "https://pctmix.com/series/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",                  
        page="1",
        folder=True ) 
    plugintools.add_item( #PCTmix_series_HD  
        action="pctreload_series_normal", 
        title="[COLOR gold]PCTmix Series HD[/COLOR]",
        thumbnail="https://pctmix.com/pctn/library/content/template/images/logos/pctmix.png",
        url= "https://pctmix.com/series-hd/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",                  
        page="1",
        folder=True )
    plugintools.add_item( #PCTmix_series_HD  
        action="pctreload_series_normal", 
        title="[COLOR gold]PCTmix V.O[/COLOR].",
        thumbnail="https://pctmix.com/pctn/library/content/template/images/logos/pctmix.png",
        url= "https://pctmix.com/series-vo/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",                  
        page="1",
        folder=True )           
def retroseriesmenu (params):
    plugintools.add_item( #todas las series
        action="retro_series", 
        title="[COLOR gold]Todas las series[/COLOR]",
        thumbnail="https://seriesretro.com/wp-content/uploads/2020/06/5ed8d22a4ac42_originalcursi1.png",
        url= "https://seriesretro.com/lista-series/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",                  
        page="1",
        folder=True ) 
    plugintools.add_item( #Series de Animacon
        action="retro_series", 
        title="[COLOR gold]Series de Animacon[/COLOR]",
        thumbnail="https://seriesretro.com/wp-content/uploads/2020/06/5ed8d22a4ac42_originalcursi1.png",
        url= "https://seriesretro.com/category/animacion/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",                  
        page="1",
        folder=True )  
    plugintools.add_item( #Series de Live Acction
        action="retro_series", 
        title="[COLOR gold]Series de Live Acction[/COLOR]",
        thumbnail="https://seriesretro.com/wp-content/uploads/2020/06/5ed8d22a4ac42_originalcursi1.png",
        url= "https://seriesretro.com/category/liveaction/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",                  
        page="1",
        folder=True ) 
    plugintools.add_item( #Series por generos
        action="retro_series_generos", 
        title="[COLOR gold]Series por generos[/COLOR]",
        thumbnail="https://seriesretro.com/wp-content/uploads/2020/06/5ed8d22a4ac42_originalcursi1.png",
        url= "https://seriesretro.com/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",                  
        page="1",
        folder=True )  
    plugintools.add_item( #Series por generos
        action="retro_series_search", 
        title="[COLOR gold]Buscador de Series[/COLOR]",
        thumbnail="https://seriesretro.com/wp-content/uploads/2020/06/5ed8d22a4ac42_originalcursi1.png",
        url= "https://seriesretro.com/?s=",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",                  
        page="1",
        folder=True )          
 


# Submenu Anime

def anime (params):
    plugintools.add_item( #Anime Fenix   
        action="animefenix", 
        title="[COLOR gold]Anime Fenix[/COLOR]",
        thumbnail="https://www.animefenix.com/themes/animefenix-frans185/images/AveFenix.png",
        url= "",
        fanart="https://www.animefenix.com/themes/animefenix-frans185/images/AveFenix.png",
        page="1",        
        folder=True )  
    plugintools.add_item( #Anime YT    
        action="Anime_YT", 
        title="[COLOR gold]Anime YT[/COLOR]",
        thumbnail="https://ytanime.tv/static/img/logo-op.png",
        url= "",
        fanart="https://ytanime.tv/static/img/logo-op.png",
        page="1",        
        folder=True )       
    plugintools.add_item( #Anime FLV   
        action="Anime_flv", 
        title="[COLOR gold]Anime FLV[/COLOR]",
        thumbnail="https://www3.animeflv.net/assets/animeflv/img/logo.png?v=2.3",
        url= "",
        fanart="https://www3.animeflv.net/assets/animeflv/img/logo.png?v=2.3",
        page="1",        
        folder=True ) 
    plugintools.add_item( #Anime JL   
        action="Anime_JL", 
        title="[COLOR gold]AnimeJL[/COLOR]",
        thumbnail="https://i.imgur.com/B1U2sbT.jpg",
        url= "",
        fanart="https://i.imgur.com/B1U2sbT.jpg",
        page="1",        
        folder=True )         
def animefenix (params): 
    plugintools.add_item( #anime_fenix_fin   
        action="anime_fenix_fin", 
        title="[COLOR gold]Anime Fenix Finalizados[/COLOR]",
        thumbnail="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/AveFenix.png",
        url= "https://www.animefenix.com/animes?type%5B%5D=tv&estado%5B%5D=2&order=default",
	    fanart="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/AveFenix.png",
        folder=True )   
    plugintools.add_item( #anime_fenix_emi   
        action="anime_fenix_emi", 
        title="[COLOR gold]Anime Fenix Emisión[/COLOR]",
        thumbnail="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/AveFenix.png",
        url= "https://www.animefenix.com/animes?type%5B%5D=tv&estado%5B%5D=1&order=default",
	    fanart="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/AveFenix.png",
        folder=True )      
    plugintools.add_item( #anime_fenix_pelic   
        action="anime_fenix_pelic", 
        title="[COLOR gold]Anime Fenix Películas[/COLOR]",
        thumbnail="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/AveFenix.png",
        url= "https://www.animefenix.com/animes?type%5B%5D=movie&order=default",
	    fanart="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/AveFenix.png",
        folder=True )   
def Anime_YT (params):        
    plugintools.add_item( #Anime YT Ultimos   
        action="animeyt_ult", 
        title="[COLOR gold]Anime YT Últimos Animes[/COLOR]",
        thumbnail="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/anime%20yt.png",
        url= "https://ytanime.tv/ultimos-animes?page=",
	    fanart="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/anime%20yt.png",
        folder=True )              
    plugintools.add_item( #Anime YT Mas Populares   
        action="animeyt_pop", 
        title="[COLOR gold]Anime YT Mas Populares[/COLOR]",
        thumbnail="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/anime%20yt.png",
        url= "https://ytanime.tv/mas-populares?page=",
	    fanart="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/anime%20yt.png",
        folder=True )                      
def Anime_flv (params): 
    plugintools.add_item( #Anime FLV Peliculas & Series   
        action="anime_flv_peliserie", 
        title="[COLOR gold]Anime FLV Peliculas & Series[/COLOR]",
        thumbnail="https://i.imgur.com/4BiUG2B.jpg",
        url= "https://www3.animeflv.net/browse",
	    fanart="https://i.imgur.com/4BiUG2B.jpg",
        folder=True )   
    plugintools.add_item( #Anime FLV Peliculas  
        action="anime_flv_peli", 
        title="[COLOR gold]Anime FLV Peliculas[/COLOR]",
        thumbnail="https://i.imgur.com/4BiUG2B.jpg",
        url= "https://www3.animeflv.net/browse?type[]=movie&order=default&page=",
	    fanart="https://i.imgur.com/4BiUG2B.jpg",
        page="1",
        folder=True )   
    plugintools.add_item( #Anime FLV Series   
        action="anime_flv_pag", 
        title="[COLOR gold]Anime FLV Series[/COLOR]",
        thumbnail="https://i.imgur.com/4BiUG2B.jpg",
        url= "https://www3.animeflv.net/browse?type%5B%5D=tv&order=default",
	    fanart="https://i.imgur.com/4BiUG2B.jpg",
        folder=True )         
    plugintools.add_item( #anime_flv_episodios   
        action="anime_flv_episodios", 
        title="[COLOR gold]Anime FLV Últimos Episodios[/COLOR]",
        thumbnail="https://i.imgur.com/4BiUG2B.jpg",
        url= "https://www3.animeflv.net/",
	    fanart="https://i.imgur.com/4BiUG2B.jpg",
        folder=True )              
    plugintools.add_item( #Anime FLV Especiales   
        action="anime_flv_epeciales", 
        title="[COLOR gold]Anime FLV Especiales[/COLOR]",
        thumbnail="https://i.imgur.com/4BiUG2B.jpg",
        url= "https://www3.animeflv.net/browse?type%5B%5D=special&order=default",
	    fanart="https://i.imgur.com/4BiUG2B.jpg",
        folder=True )    
    plugintools.add_item( #Anime FLV OVA  
        action="anime_flv_peli", 
        title="[COLOR gold]Anime FLV OVA[/COLOR]",
        thumbnail="https://i.imgur.com/4BiUG2B.jpg",
        url= "https://www3.animeflv.net/browse?type%5B%5D=ova&order=default",
	    fanart="https://i.imgur.com/4BiUG2B.jpg",
        folder=True )
    plugintools.add_item( #Anime FLV Generos  
        action="anime_flv_genero", 
        title="[COLOR gold]Anime FLV Generos[/COLOR]",
        thumbnail="https://i.imgur.com/4BiUG2B.jpg",
        url= "https://pastebin.com/raw/8wCJDnyc",
	    fanart="https://i.imgur.com/4BiUG2B.jpg",
        folder=True )
    plugintools.add_item( #Anime FLV Años  
        action="anime_flv_anios", 
        title="[COLOR gold]Anime FLV Años[/COLOR]",
        thumbnail="https://i.imgur.com/4BiUG2B.jpg",
        url= "https://pastebin.com/raw/5mwvBhDu",
	    fanart="https://i.imgur.com/4BiUG2B.jpg",
        folder=True )     
    plugintools.add_item( #Anime FLV search   
        action="anime_flv_search", 
        title="[COLOR gold]Anime FLV Buscar[/COLOR]",
        thumbnail="https://i.imgur.com/4BiUG2B.jpg",
        url= "https://www3.animeflv.net/browse?q=",
	    fanart="https://i.imgur.com/4BiUG2B.jpg",
        folder=True )           
def Anime_JL (params): 
    plugintools.add_item( #Anime JL Peliculas & Series   
        action="anime_JL_peliserie", 
        title="[COLOR gold]AnimeJL Peliculas & Series[/COLOR]",
        thumbnail="https://i.imgur.com/B1U2sbT.jpg",
        url= "https://www.anime-jl.net/animes",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )   
    plugintools.add_item( #Anime JL Series   
        action="anime_JL_peliserie", 
        title="[COLOR gold]AnimeJL Series[/COLOR]",
        thumbnail="https://i.imgur.com/B1U2sbT.jpg",
        url= "https://www.anime-jl.net/animes?tipo%5B%5D=1&order=created",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )  
    plugintools.add_item( #Anime JL Peliculas   
        action="anime_JL_peliseriepeli", 
        title="[COLOR gold]AnimeJL Peliculas[/COLOR]",
        thumbnail="https://i.imgur.com/B1U2sbT.jpg",
        url= "https://www.anime-jl.net/animes?tipo%5B%5D=3&order=created",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )           
    plugintools.add_item( #Anime JL Ova   
        action="anime_JL_peliserie", 
        title="[COLOR gold]AnimeJL OVA[/COLOR]",
        thumbnail="https://i.imgur.com/B1U2sbT.jpg",
        url= "https://www.anime-jl.net/animes?tipo%5B%5D=2&order=created",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )         
    plugintools.add_item( #Anime JL Series en Emisión   
        action="anime_JL_peliserie", 
        title="[COLOR gold]AnimeJL Series en Emisión[/COLOR]",
        thumbnail="https://i.imgur.com/B1U2sbT.jpg",
        url= "https://www.anime-jl.net/animes?tipo%5B%5D=1&estado%5B%5D=0&order=created",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True ) 
    plugintools.add_item( #Anime JL Series en Finalizadas   
        action="anime_JL_peliserie", 
        title="[COLOR gold]AnimeJL Series en Finalizadas[/COLOR]",
        thumbnail="https://i.imgur.com/B1U2sbT.jpg",
        url= "https://www.anime-jl.net/animes?tipo%5B%5D=1&estado%5B%5D=1&order=created",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )   
    plugintools.add_item( #Anime JL Series en Estreno   
        action="anime_JL_peliserie", 
        title="[COLOR gold]AnimeJL Series en Estreno[/COLOR]",
        thumbnail="https://i.imgur.com/B1U2sbT.jpg",
        url= "https://www.anime-jl.net/animes?tipo%5B%5D=1&estado%5B%5D=1&order=created",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )
    plugintools.add_item( #Anime JL Buscar   
        action="anime_JL_search", 
        title="[COLOR gold]AnimeJL Buscar[/COLOR]",
        thumbnail="https://i.imgur.com/B1U2sbT.jpg",
        url= "https://www.anime-jl.net/animes?q=",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )          


# Submenu infantil

def infantil(params):  
    plugintools.add_item( #Series Infantiles  
        action="series_infantiles", 
        title="[COLOR gold]Series Infantiles Web Danimados[/COLOR]",
        thumbnail="https://i.imgur.com/dxTszIe.jpg",
        url= "https://danimados.com/genero/series-clasicas/",
	    fanart="https://i.imgur.com/dxTszIe.jpg",
        folder=True )
    plugintools.add_item( #Peliculas Infantiles  
        action="peliculas_infantiles", 
        title="[COLOR gold]Peliculas Infantiles Web Danimados[/COLOR]",
        thumbnail="https://i.imgur.com/zqhGLzX.jpg",
        url= "https://danimados.com/peliculas/",
	    fanart="https://i.imgur.com/zqhGLzX.jpg",
        folder=True )         
    plugintools.add_item(  #Tv infantil  
        action="adictos", 
        title="[COLOR gold]Tv infantil[/COLOR] [COLOR red]NECESARIO VPN[/COLOR]",
        thumbnail="https://i.imgur.com/w5alGoX.jpg",
        url= "https://adictosalatele.com/infantiles/",
        fanart="https://i.imgur.com/w5alGoX.jpg",
        folder=True )    
    plugintools.add_item( #audiocuentos menu    
        action="audiocuentosmenu", 
        title="[COLOR gold]Audiocuentos[/COLOR]",
        thumbnail="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/audio%20cuentos.jpg",
        url= "",
	    fanart="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/audio%20cuentos.jpg",
        folder=True )
    plugintools.add_item( #Programasdibus menu    
        action="Infantil_playlist", 
        title="[COLOR gold]Programas y dibujos[/COLOR]",
        thumbnail="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/_110166736_p07x4spf.jpg",
        url= "https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/programasdibusmenu",
	    fanart="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/_110166736_p07x4spf.jpg",
        folder=True )   
    plugintools.add_item( #Aprende Ingles con Smile and Learn menu    
        action="Infantil_playlist", 
        title="[COLOR gold]Aprende Ingles con Smile and Learn[/COLOR]",
        thumbnail="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/smile1%20(2).png",
        url= "https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/ingles_smile_and_learn_menu", 
	    fanart="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/smile1%20(2).png",
        folder=True )   
    plugintools.add_item( #Aprende con Smile and Learn menu    
        action="Infantil_playlist", 
        title="[COLOR gold]Aprende con Smile and Learn[/COLOR]",
        thumbnail="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/smile1%20(2).png",
        url= "https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/ingles_smile_and_learn_menu",
	    fanart="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/smile1%20(2).png",
        folder=True )          
    plugintools.add_item( #Ejercicios fisicos para niños menu    
        action="Infantil_playlist", 
        title="[COLOR gold]Ejercicios fisicos para niños[/COLOR]",
        thumbnail="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/ejer3.jpg",
        url= "https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/ejercicios_fisicos_para_ninios",
	    fanart="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/ejer3.jpg",
        folder=True )
    plugintools.add_item( #Juegos de Disney infantil menu  
        action="Infantil_playlist", 
        title="[COLOR gold]Juegos de Disney infantil[/COLOR]",
        thumbnail="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/dis.jpg",
        url= "https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/juegos_de_disney_infantil",
	    fanart="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/dis.jpg",
        folder=True )        
def audiocuentosmenu (params):  
    plugintools.add_item( #Audiocuentos Clasicos  
        action="audiocuentosclasicos", 
        title="[COLOR gold]Audiocuentos Clasicos[/COLOR]",
        thumbnail="https://cajamusical.com/wp-content/uploads/2020/08/Personajes-Cuentos-Clasicos-1.png",
        url= "https://audiocuentos.net/category/cuentos-clasicos/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )   
    plugintools.add_item( #Audiocuentos Disney    
        action="audiocuentosdisney", 
        title="[COLOR gold]Audiocuentos Disney[/COLOR]",
        thumbnail="https://ar.salvat.com/Content/CategoryImages/cc77a7d5-9c73-48cc-b3c3-e3b5f59fe9f1.png",
        url= "https://audiocuentos.net/category/cuentos-disney/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )  
    plugintools.add_item( #Audiocuentos Halloween   
        action="audiocuentoshalloween", 
        title="[COLOR gold]Audiocuentos Halloween[/COLOR]",
        thumbnail="https://elalmademiaula.files.wordpress.com/2015/03/mi-cuento-por-tu-dibujo.png?w=640",
        url= "https://audiocuentos.net/category/cuentos-halloween/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )  
    plugintools.add_item( #Audiocuentos Navidad  
        action="audiocuentosnavidad", 
        title="[COLOR gold]Audiocuentos De Navidad[/COLOR]",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/4/4d/Tefa-Navidad.png",
        url= "https://audiocuentos.net/category/cuentos-navidad/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )          

         

# Submenu Documentales

def documentales(params):
    plugintools.add_item(  #Documentales
        action="adictos", 
        title="[COLOR gold]Canales de Documentales[/COLOR] [COLOR red]NECESARIO VPN[/COLOR]",
        thumbnail="https://i.imgur.com/1GeFgQZ.jpg",
        url= "https://adictosalatele.com/canales-de-documentales/",
        fanart="https://i.imgur.com/1GeFgQZ.jpg",
        folder=True )    
    plugintools.add_item( #documaniatv    
        action="documaniatv", 
        title="[COLOR gold]DocumaniaTV Series[/COLOR]",
        thumbnail="https://i.imgur.com/qkZYmEu.jpg",
        url= "",
	    fanart="https://i.imgur.com/qkZYmEu.jpg",
        folder=True ) 
    plugintools.add_item( #Documentales Online   
        action="documentales_online", 
        title="[COLOR gold]Documentales Online[/COLOR]",
        thumbnail="https://www.documentales-online.com/img/documentales-online.png",
        url= "",
	    fanart="https://www.documentales-online.com/img/documentales-online.png",
        folder=True )
    plugintools.add_item( #Planetdoc_completos   
        action="planetdoc", 
        title="[COLOR gold]Planetdoc Completos[/COLOR]",
        thumbnail="http://planetdoc.tv/img20105850-1432637081espaaol.png",
        url= "",
	    fanart="http://planetdoc.tv/img20105850-1432637081espaaol.png",
        folder=True )         
def documaniatv(params):         
    plugintools.add_item( #documaniatv    
        action="documaniatvseries", 
        title="[COLOR gold]DocumaniaTV Series[/COLOR]",
        thumbnail="https://i.imgur.com/qkZYmEu.jpg",
        url= "https://www.documaniatv.com/top-series-documentales.html",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )        
    plugintools.add_item( #documaniatv top   
        action="documaniatv_top", 
        title="[COLOR gold]DocumaniaTV Top 100[/COLOR]",
        thumbnail="https://i.imgur.com/qkZYmEu.jpg",
        url= "https://www.documaniatv.com/topvideos.html",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )     
    plugintools.add_item( #documaniatv generos   
        action="documaniatv_gene", 
        title="[COLOR gold]DocumaniaTV Generos y Canales[/COLOR]",
        thumbnail="https://i.imgur.com/qkZYmEu.jpg",
        url= "https://www.documaniatv.com/categorias-y-canales.html",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True ) 
def documentales_online (params):        
    plugintools.add_item( #Documentales Online   
        action="documentales_onlinedocus", 
        title="[COLOR gold]Documentales Online[/COLOR]",
        thumbnail="https://www.documentales-online.com/img/documentales-online.png",
        url= "https://www.documentales-online.com",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )
    plugintools.add_item( #Documentales Online Categorias   
        action="documentales_online_cat", 
        title="[COLOR gold]Documentales Online Por Categorías[/COLOR]",
        thumbnail="https://www.documentales-online.com/img/documentales-online.png",
        url= "https://www.documentales-online.com",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )
    plugintools.add_item( #Documentales Online Top   
        action="documentales_online_top", 
        title="[COLOR gold]Documentales Online Top 100[/COLOR]",
        thumbnail="https://www.documentales-online.com/img/documentales-online.png",
        url= "https://www.documentales-online.com/top/",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True ) 
def planetdoc (params):        
    plugintools.add_item( #Planetdoc_completos   
        action="planetdoc_completos", 
        title="[COLOR gold]Planetdoc Completos[/COLOR]",
        thumbnail="http://planetdoc.tv/img20105850-1432637081espaaol.png",
        url= "http://planetdoc.tv/lista-documentales-completos",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True ) 
    plugintools.add_item( #Planetdoc_expres  
        action="planetdoc_expres", 
        title="[COLOR gold]Planetdoc Documentales Express[/COLOR]",
        thumbnail="http://planetdoc.tv/img20105850-1432637081espaaol.png",
        url= "http://planetdoc.tv/lista-documentales-express",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )
    plugintools.add_item( #Planetdoc_generos  
        action="planetdoc_generos", 
        title="[COLOR gold]Planetdoc Por Generos[/COLOR]",
        thumbnail="http://planetdoc.tv/img20105850-1432637081espaaol.png",
        url= "http://planetdoc.tv/lista-categorias",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )             


def tuberika(params): 
    plugintools.add_item( #trendig_you
        action="trendig_you", 
        title="[COLOR gold]Trending[/COLOR]",
        thumbnail="https://i.imgur.com/dzbcKQ9.jpg",
        url= "https://www.youtube.com/feed/trending",
		fanart="special://home/addons/plugin.video.iberika/tenor.gif", 
        folder=True )
    plugintools.add_item( #Buscar search   
        action="Buscar_search", 
        title="[COLOR gold]Buscar[/COLOR]",
        thumbnail="https://i.imgur.com/V4gm6sn.jpg",
        url= "https://www.youtube.com/results?search_query=",
	    fanart="special://home/addons/plugin.video.iberika/tenor.gif",
        folder=True )         
    plugintools.add_item( #Emisiones_en_Directo_Recientes
        action="Emisiones_en_Directo_Recientes", 
        title="[COLOR gold]Emisiones en Directo Recientes[/COLOR]",
        thumbnail="https://i.imgur.com/qE9UeYX.jpg",
        url= "https://www.youtube.com/watch?v=8nox3KEe6KI&list=PLU12uITxBEPEFpYLxV4XlCnR13q8nwVsv",
		fanart="special://home/addons/plugin.video.iberika/tenor.gif", 
        folder=True )    
    plugintools.add_item( #Proximas Emisiones en Directo
        action="Proximas_en_Directo", 
        title="[COLOR gold]Proximas Emisiones en Directo[/COLOR]",
        thumbnail="https://i.imgur.com/qE9UeYX.jpg",
        url= "https://www.youtube.com/watch?v=n93zCuT_0ZE&list=PLU12uITxBEPHMNFc5X1tQDy79xL29aV1E",
		fanart="special://home/addons/plugin.video.iberika/tenor.gif", 
        folder=True )  
    plugintools.add_item( #En Directo
        action="En_Directo", 
        title="[COLOR gold]En Directo[/COLOR]",
        thumbnail="https://i.imgur.com/E8eFVJy.jpg",
        url= "https://www.youtube.com/playlist?list=PLU12uITxBEPFT10z9aLSQpg0YD4su7JDp",
		fanart="special://home/addons/plugin.video.iberika/tenor.gif", 
        folder=True )             
    plugintools.add_item( #GameYoutube_live
        action="GameYoutube_live", 
        title="[COLOR gold]GameYoutube Live[/COLOR]",
        thumbnail="https://i.imgur.com/xJCLAyq.jpg",
        url= "https://www.youtube.com/gaming/games",
		fanart="special://home/addons/plugin.video.iberika/tenor.gif", 
        folder=True )   
    plugintools.add_item( #Noticias_directos
        action="Noticias_directos", 
        title="[COLOR gold]Noticias en Directos[/COLOR]",
        thumbnail="https://i.imgur.com/4Cw0fuc.jpg",
        url= "https://www.youtube.com/playlist?list=PL3ZQ5CpNulQkW4U3pzruIgDfTPVCRhtwk",
		fanart="special://home/addons/plugin.video.iberika/tenor.gif", 
        folder=True )     
    plugintools.add_item( #Deportes_directos
        action="Deportes_directos", 
        title="[COLOR gold]Deportes en Directos[/COLOR]",
        thumbnail="https://i.imgur.com/x6pyOps.jpg",
        url= "https://www.youtube.com/watch?v=Btv7G0BV45g&list=PL8fVUTBmJhHLS1QmTrewHL3dd4ppUL0eV",
		fanart="special://home/addons/plugin.video.iberika/tenor.gif", 
        folder=True )            


#<--Desarollo-->

#Televisión 

def tdtchannels (params):
 categorias = []
 url = params . get ( "url" )  
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )  
 matches = plugintools.find_multiple_matches(url, 'group-title="([^"]+)') 
 for categoria in sorted(matches): 
    if categoria not in categorias: 
        categorias.append(categoria)
 
 plugintools . add_item ( action = "parse_tdtchannels" , title = "[COLOR aqua]Buscador[/COLOR]", url = "Buscador", thumbnail =  params.get("thumbnail") , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True)

 categorias.append("Todos")
 for x in sorted(categorias):
    plugintools . add_item ( action = "parse_tdtchannels" , title = x, url = x, thumbnail =  params.get("thumbnail") , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True)
def parse_tdtchannels ( params ):  
  categoria = params.get("url")
  if categoria != ( '%s' % ( '' ) . join ( chr ( y ) for y in [66, 117, 115, 99, 97, 100, 111, 114])):
    if categoria == ( '%s' % ( '' ) . join ( chr ( y ) for y in [84, 111, 100, 111, 115])):
        categoria = '[^"]+'
    url = "https://www.tdtchannels.com/lists/tv.m3u" 
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )    
    matches = re.findall(r'tvg-logo="([^"]+)" group-title="{0}" tvg-name="[^"]+",(.*)\s*(.*)'.format(categoria),url)
    for thumb, name, url in matches:
        plugintools . add_item ( action = "resolve_without_resolveurl" , title = name, url = url, thumbnail =  thumb , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False, isPlayable = True)
  else:
    input_channel = keyboard_input("", "Buscar:", False)
    url = "https://www.tdtchannels.com/lists/tv.m3u" 
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )
    regex = ( '%s' % ( '' ) . join ( chr ( y ) for y in [40, 63, 105, 41, 116, 118, 103, 45, 108, 111, 103, 111, 61, 34, 40, 91, 94, 34, 93, 43, 41, 34, 32, 103, 114, 111, 117, 112, 45, 116, 105, 116, 108, 101, 61, 34, 91, 94, 34, 93, 43, 34, 32, 116, 118, 103, 45, 110, 97, 109, 101, 61, 34, 91, 94, 34, 93, 43, 34, 44, 40, 46, 42, 123, 48, 125, 46, 42, 41, 92, 115, 42, 40, 46, 42, 41]))
    matches = re.findall(regex.format(input_channel), url)
    for thumb, name, url in matches:
        plugintools . add_item ( action = "resolve_without_resolveurl" , title = name.capitalize(), url = url, thumbnail =  thumb , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False, isPlayable = True)
def adictosdeporte ( params ):
    url = params.get("url")  
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    header . append ( [ "Referer" , "https://adictosaldeporte.com/" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )    
    bloque = plugintools.find_single_match(url,'<center><div class="imagenes">(.*?)</div></center></div>')
    matches = re.findall(r'(?s)<a href="(.*?)" title="(.*?) en.*?><img src="(.*?)"',bloque)
    for url,title,thumb in matches: 
        plugintools . add_item ( action = 'adictos1' , title = title, url ='https:'+ url,thumbnail ='https://adictosalatele.com'+ thumb , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder =False,isPlayable= True)
def adictos ( params ):
    url = params.get("url")  
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    header . append ( [ "Referer" , "https://adictosaldeporte.com/" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )    
    bloque = plugintools.find_single_match(url,'<div class="imagenes">(.*?)</h4>')
    matches = re.findall(r'(?s)<td>.*?<a href="(.*?)" title="(.*?) en.*?><img src="(.*?)"',bloque)
    for url,title,thumb in matches: 
        plugintools . add_item ( action = 'adictos1' , title = title, url ='https:'+ url,thumbnail ='https://adictosalatele.com'+ thumb , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder =False,isPlayable= True)
def adictos1 ( params ):
    url = params.get('url')
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()    
    if 'adictosalatele' in url:
        url ='https:'+ plugintools.find_single_match(url,'(?s)<div class="video">.*?src="(.*?)"')
    else:
        url ='https:'+ plugintools.find_single_match(url,'(?s)<center><textarea.*?src="(.*?)"')
    #plugintools . add_item ( action = "" , title =url,url = url,thumbnail =  "" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True)
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"])
    request_headers.append(["Referer","https://adictosalatele.com/tve-1-en-directo-online-gratis/"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()   
    url = plugintools.find_single_match(url,'(?s)<iframe src="(https.*?wigistream.*?)"')
    #plugintools . add_item ( action = "" , title =url,url = url,thumbnail =  "" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True)
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"])
    request_headers.append(["Referer","https://adictosalatele.com/tve-1-en-directo-online-gratis/"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()    
    pack = plugintools.find_single_match(url,'(?s)(eval\(function\(p,a,c,k,e,d.*?)</script>')
    unpacked = jsunpack.unpack(pack).replace('\\', '')
    finalurl = plugintools.find_single_match(unpacked,'(?s)player=new Clappr.Player.*?source."(.*?)"')
    plugintools . play_resolved_url ( finalurl )                                
    #plugintools . add_item ( action = "" , title =finalurl,url = finalurl,thumbnail =  "" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder =True)       
def guiatv ( params ):
    url = params.get("url")  
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )    
    matches = re.findall(r'(?s)class="cadena">.*?<a href="([^"]+)" title="Programación ([^"]+)".*?|<div class="(ahora)">\s*(.*?)<.*?|<div class="luego">\s*<span class="date">(\d+:\d+)<\/span>\s*([^<]+)|<div class="mastarde">\s*<span class="date">(\d+:\d+)<\/span>\s*([^<]+)\s*|<span class="remain"><\/span>\s*<a class="mas" href="([^"]+)"><span>(Parrilla completa)<\/span',url)
    for url, channel, nowhour, now, laterhour, later, morelaterhour, morelater, url2, completed in matches:
        nowhour = "\x20" + nowhour
        if url:
            url = url
        else:
            if url2:
                url = url2    
        title = "[B][COLOR snow]" + channel + "[/COLOR][/B]\x20" + nowhour + "\x20" + now + laterhour + "\x20" + later +  morelaterhour + morelater + "[COLOR orange]" + completed + "[/COLOR]"
        plugintools . add_item ( action = "parse_guiatv" , title = title, url = url, thumbnail =  params.get("thumbnail") , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True)
def parse_guiatv ( params ):
    url = params.get("url")  
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )    
    matches = re.findall(r'{"@context":"[^"]+","@type":"Event","name":"(\d+:\d+ - [^"]+)","description":"([^"]+)"',url)
    for title, desc in matches: 
        plugintools . add_item ( action = "" , title = title, url = url, plot=desc,thumbnail =  params.get("thumbnail") , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True)
def parse_sporthd(params):
  if params.get("extra") == "ON":
    matches = plugintools.find_multiple_matches(params.get("url"), r'<a href="([^"]+)".*?"> ([^<]+) ')
    for url, lang in matches:
      host = url
      header = [ ]
      header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
      read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
      url = read_url . strip ( )
      parsing_url = plugintools.find_single_match(url, r"<iframe src='(.*?)'")   
      header . append ( [ "Referer" , host ] )
      read_url , read_header = plugintools . read_body_and_headers ( parsing_url , headers = header )
      url = read_url . strip ( )
      finalurl = plugintools.find_single_match(url, r'source: "([^"]+)"')
    
      plugintools . add_item ( action = "resolvers" , title = lang, url = finalurl + "|Referer=" + parsing_url, thumbnail=params.get("thumbnail") , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True ) 
  else:
      sys.exit(0)
def sporthd(params):   
 url = params . get ( "url" ) 
 host = params.get("url") 
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 if params.get("title") == ( '%s' % ( '' ) . join ( chr ( y ) for y in [65, 103, 101, 110, 100, 97, 32, 67, 111, 109, 112, 108, 101, 116, 97])):
    def rest(params):
        matches =  re.findall(r"""<img src="([^"]+)" style="width:26px;background-color:\#252a2e;border-radius:86px;"> </a> </div> </div> <div class="item-col pull-left item-col-time" style="max-width:85px;"> <div class="item-heading">Time</div> <div> <span class="gmt_m_time" mtime="\d+" stime="\d+"> (\d+:\d+) GMT ([^<]+)</span> </div> </div> <div class="item-col pull-left item-col-match" style="text-align: left;"> <div class="item-heading">Matches</div> <div class="matchname"> <table style="width:\d+%;text-align:center"> <tr> <td style="width:\d+\.\d+%;text-align:right;font-family: 'Titillium Web', sans-serif;;font-weight: \d+;padding-right: \d+px;"> ([^<]+).*?<img src="teams/[^\.]+\.png" style="margin-right:2px;margin-left:2px;width:22px;padding:2px;text-align:center!important;"> </td> <td style="text-align:center;color:\#70b02b"><li class="timeStamp">vs</li></td> <td style="width:46.5%;text-align:left;font-family: 'Titillium Web', sans-serif;font-weight: 400;padding-left: 14px;"> <img src="teams/[^\.]+\.png" style="margin-right:2px;margin-left:2px;width:22px;padding:2px;text-align:center!important;"> ([^<]+).*?<i class="material-icons">(.+?)</a> </li>""", url, re.DOTALL)
        for thumb, atime, gmt, hometeam, awayteam, preurl in matches: 
            if not preurl.startswith("link</i>"): 
                status = "[B][COLOR red]·[/COLOR][/B]"
                configstatus = "OFF"
            else: 
                status = "[B][COLOR lime]·[/COLOR][/B]"
                configstatus = "ON" 
            plugintools . add_item ( action = "parse_sporthd" , title = "{}{} [COLOR white]{}[/COLOR] [COLOR orangered]VS[/COLOR] [COLOR lightskyblue]{}[/COLOR]".format(status, str(int(atime[:2])-1)[-2:] + atime[-3:], hometeam, awayteam) , url = preurl, thumbnail =  "http://www.sporthd.me/{}".format(thumb) , fanart="special://home/addons/plugin.video.iberika/tenor.gif", extra=configstatus, folder = True)
    def motor(params):
        matches =  re.findall(r"""<img src="([^"]+)" style="width:26px;background-color:\#252a2e;border-radius:86px;"> </a> </div> </div> <div class="item-col pull-left item-col-time" style="max-width:85px;"> <div class="item-heading">Time</div> <div> <span class="gmt_m_time" mtime="\d+" stime="\d+"> (\d+:\d+) GMT ([^<]+)</span> </div> </div> <div class="item-col pull-left item-col-match" style="text-align: left;"> <div class="item-heading">Matches</div> <div class="matchname"> <center>([^<]+)<br><a href="[^"]+"> <span style="color:[^"]+">([^<]+)</span></a></center> </div> </div> <div class="[^"]+"> <div class="[^"]+">stream</div> <div> <a href="\#" open-this="\d+" style="text-decoration:none;color:\#fff;background:\#[a-zA-Z|\d]+;text-align: center; padding: 3px 7px 5px 6px; border-radius: 3px; border: 1px solid \#fff;width:52px; height:27px;float: left;" class="open_the_door" id="btnWatch\d+">[^<]+</a> </div> </div> <div class="item-col fixed pull-left item-col-ads"> <div class="item-heading">ads</div> <div> <a href="[^"]+" target="_blank" class="lboss">[^"<]+</a> </div> </div> </div> </li> <li style="padding:10px 20px;display:none;" id="open_this_\d+" class="bahamas"> <span style="color: \#[a-zA-Z|\d]+; position: relative;float: left;margin-bottom: 0;margin-top: -2px;margin-bottom: -7px;margin-left: -4px;"> .*?<i class="material-icons">(.+?)</a> </li>""", url, re.DOTALL) 
        for thumb, atime, gmt, title, event, preurl in matches: 
            if not preurl.startswith("link</i>"): 
                status = "[B][COLOR red]·[/COLOR][/B]"
                configstatus = "OFF"
            else: 
                status = "[B][COLOR lime]·[/COLOR][/B]"
                configstatus = "ON" 
            plugintools . add_item ( action = "parse_sporthd" , title = "{}{} [COLOR white]{}[/COLOR] [COLOR lightskyblue]{}[/COLOR]".format(status, str(int(atime[:2])-1)[-2:] + atime[-3:], event, title) , url = preurl, thumbnail =  "http://www.sporthd.me/{}".format(thumb) , fanart="special://home/addons/plugin.video.iberika/tenor.gif", extra=configstatus, folder = True)
    motor(params); rest(params)
 else:
  if host != ( '%s' % ( '' ) . join ( chr ( y ) for y in [104, 116, 116, 112, 115, 58, 47, 47, 119, 119, 119, 46, 115, 112, 111, 114, 116, 104, 100, 46, 109, 101, 47, 63, 116, 121, 112, 101, 61, 109, 111, 116, 111, 114, 115, 112, 111, 114, 116])):
   matches =  re.findall(r"""<img src="([^"]+)" style="width:26px;background-color:\#252a2e;border-radius:86px;"> </a> </div> </div> <div class="item-col pull-left item-col-time" style="max-width:85px;"> <div class="item-heading">Time</div> <div> <span class="gmt_m_time" mtime="\d+" stime="\d+"> (\d+:\d+) GMT ([^<]+)</span> </div> </div> <div class="item-col pull-left item-col-match" style="text-align: left;"> <div class="item-heading">Matches</div> <div class="matchname"> <table style="width:\d+%;text-align:center"> <tr> <td style="width:\d+\.\d+%;text-align:right;font-family: 'Titillium Web', sans-serif;;font-weight: \d+;padding-right: \d+px;"> ([^<]+).*?<img src="teams/[^\.]+\.png" style="margin-right:2px;margin-left:2px;width:22px;padding:2px;text-align:center!important;"> </td> <td style="text-align:center;color:\#70b02b"><li class="timeStamp">vs</li></td> <td style="width:46.5%;text-align:left;font-family: 'Titillium Web', sans-serif;font-weight: 400;padding-left: 14px;"> <img src="teams/[^\.]+\.png" style="margin-right:2px;margin-left:2px;width:22px;padding:2px;text-align:center!important;"> ([^<]+).*?<i class="material-icons">(.+?)</a> </li>""", url, re.DOTALL)
   for thumb, atime, gmt, hometeam, awayteam, preurl in matches: 
    if not preurl.startswith("link</i>"): 
      status = "[B][COLOR red]·[/COLOR][/B]"
      configstatus = "OFF"
    else: 
      status = "[B][COLOR lime]·[/COLOR][/B]"
      configstatus = "ON" 
    plugintools . add_item ( action = "parse_sporthd" , title = "{}{} [COLOR white]{}[/COLOR] [COLOR orangered]VS[/COLOR] [COLOR lightskyblue]{}[/COLOR]".format(status, str(int(atime[:2])-1)[-2:] + atime[-3:], hometeam, awayteam) , url = preurl, thumbnail =  "http://www.sporthd.me/{}".format(thumb) , fanart="special://home/addons/plugin.video.iberika/tenor.gif", extra=configstatus, folder = True)
  else:
   matches =  re.findall(r"""<img src="([^"]+)" style="width:26px;background-color:\#252a2e;border-radius:86px;"> </a> </div> </div> <div class="item-col pull-left item-col-time" style="max-width:85px;"> <div class="item-heading">Time</div> <div> <span class="gmt_m_time" mtime="\d+" stime="\d+"> (\d+:\d+) GMT ([^<]+)</span> </div> </div> <div class="item-col pull-left item-col-match" style="text-align: left;"> <div class="item-heading">Matches</div> <div class="matchname"> <center>([^<]+)<br><a href="[^"]+"> <span style="color:[^"]+">([^<]+)</span></a></center> </div> </div> <div class="[^"]+"> <div class="[^"]+">stream</div> <div> <a href="\#" open-this="\d+" style="text-decoration:none;color:\#fff;background:\#[a-zA-Z|\d]+;text-align: center; padding: 3px 7px 5px 6px; border-radius: 3px; border: 1px solid \#fff;width:52px; height:27px;float: left;" class="open_the_door" id="btnWatch\d+">[^<]+</a> </div> </div> <div class="item-col fixed pull-left item-col-ads"> <div class="item-heading">ads</div> <div> <a href="[^"]+" target="_blank" class="lboss">[^"<]+</a> </div> </div> </div> </li> <li style="padding:10px 20px;display:none;" id="open_this_\d+" class="bahamas"> <span style="color: \#[a-zA-Z|\d]+; position: relative;float: left;margin-bottom: 0;margin-top: -2px;margin-bottom: -7px;margin-left: -4px;"> .*?<i class="material-icons">(.+?)</a> </li>""", url, re.DOTALL) 
   for thumb, atime, gmt, title, event, preurl in matches: 
    if not preurl.startswith("link</i>"): 
      status = "[B][COLOR red]·[/COLOR][/B]"
      configstatus = "OFF"
    else: 
      status = "[B][COLOR lime]·[/COLOR][/B]"
      configstatus = "ON" 
    plugintools . add_item ( action = "parse_sporthd" , title = "{}{} [COLOR white]{}[/COLOR] [COLOR lightskyblue]{}[/COLOR]".format(status, str(int(atime[:2])-1)[-2:] + atime[-3:], event, title) , url = preurl, thumbnail =  "http://www.sporthd.me/{}".format(thumb) , fanart="special://home/addons/plugin.video.iberika/tenor.gif", extra=configstatus, folder = True)
def tdtchannels (params):
 categorias = []
 url = params . get ( "url" )  
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )  
 matches = plugintools.find_multiple_matches(url, 'group-title="([^"]+)') 
 for categoria in sorted(matches): 
    if categoria not in categorias: 
        categorias.append(categoria)
 categorias.append("Todos")
 for x in sorted(categorias):
    plugintools . add_item ( action = "parse_tdtchannels" , title = x, url = x, thumbnail =  params.get("thumbnail") , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True)
def parse_tdtchannels ( params ):  
 categoria = params.get("url")
 if categoria == "Todos":
    categoria = '[^"]+'
 url = "https://www.tdtchannels.com/lists/tv.m3u" 
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )    
 matches = re.findall(r'tvg-logo="([^"]+)" group-title="{0}" tvg-name="[^"]+",(.*)\s*(.*)'.format(categoria),url)
 for thumb, name, url in matches:
    plugintools . add_item ( action = "resolve_without_resolveurl" , title = name, url = url, thumbnail =  thumb , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False, isPlayable = True)   
def daqueen_tv (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)title.*?=.*?"(.+?)".*?thumb.*?=.*?"(.*?)".*?url.*?=.*?"(.+?)"', url, re.DOTALL)
 for title, thumb, url in matches:  
  plugintools . add_item ( action = "resolvers" , title = title, url = vergol(url) , thumbnail=thumb , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )  
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)(\d+\d+:.*?) <.*?color: #5185c9;">.*?>(.*?)<.*?|strong></span>(.*?)(Channel )(.*?)<', url, re.DOTALL)
 for hora, title, even, channel, url in matches:  
  plugintools . add_item ( action = "wstream1" , title = "[COLOR lime]"+hora+"[/COLOR]" + "  " + "[COLOR darkorange]"+title+"[/COLOR]" + "  " + "[COLOR yellow]"+even+"[/COLOR]" + "  " + channel + url, url = url , thumbnail= "https://i.imgur.com/lnVf69v.jpg" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True ) 
def daddylive (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)(\d\d:\d\d)\s(.+?):\s(.+?)<|href="(.+?)".*?#ff0000;">(.*?)<', url, re.DOTALL)
 for hora, liga, partido, url, canal in matches:  
  plugintools . add_item ( action = "wstream2" , title = "[COLOR lime]"+hora+"[/COLOR]" + "  " + "[COLOR darkorange]"+liga+"[/COLOR]" + "  " + "[COLOR blue]"+partido+"[/COLOR]" + "  " + "[COLOR yellow]"+canal+"[/COLOR]", url = url , thumbnail= "https://i.imgur.com/2bsfGN5.jpg" , fanart="https://i.imgur.com/2bsfGN5.jpg", folder = False , isPlayable = True ) 

def daily (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches = re.findall(r'(?s)<td><b>(.+?)</b>|<td>(\d{1,2}.*?)<|<td>(\b.+?)</td>|<td><a href="(.+?)">(.+?)</a></td>',url, re.DOTALL)
 for time, title, title2, url, day in matches:
    plugintools.add_item(action="daily_1",title="[B]" + "[COLOR lime]" + time + " " + "[/COLOR]" + "[COLOR fuchsia]" + title + "[/COLOR]" + " " + "[COLOR cyan]" + title2 + "[/COLOR]" + day + "[/B]",url=url, thumbnail="ttps://i.imgur.com/E7vzz9Q.jpg", folder=False,isPlayable= True)

def daily_1 (params):
 url = "https://dailysport.bar/" + params . get ( "url" )
 request_headers=[]
 request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"])
 body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
 url = body.strip()
 url = plugintools.find_single_match(url,'(?s)} else {.*?source:\s*.*?atob."(aHR0.*?)"')
 url = message_bytes = base64.b64decode(url)
 url = message_bytes.decode('utf-8')       
 plugintools . play_resolved_url ( url )
 plugintools . add_item ( action = "", title = url, thumbnail="https://i.imgur.com/kHOtn4i.jpg", folder = True )

def tdt (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)#EXTINF:-1.*?logo="(.+?)".*?,(.+?)\n(.+?)\n', url, re.DOTALL)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "resolve_without_resolveurl" , title = title , url = url, thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True ) 
def tdtmun (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)#EXTINF:-1,(.+?)\n.*?(.+?)\s', url, re.DOTALL)
 log(matches)
 for title, url in matches:
  plugintools . add_item ( action = "tdtmun1" , title = title, url = url , thumbnail="https://cdn.pixabay.com/photo/2017/09/12/20/23/globe-png-2743543_960_720.png" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
def tdtmun1 (params): 
 url = (  ( "https://raw.githubusercontent.com/telegrambotdev/iptv/ba58c7c0b2c9c7653f6b2cd3b4b64012d854d81e/" + params . get("url") ) )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)#EXTINF:-1.*?logo="(.+?)".*?title=.*?,(.+?)\n.*?(.+?)\s', url, re.DOTALL)
 log(matches)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "resolve_without_resolveurl" , title = title , url = url , thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )  
def fluxus (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)large;"><b>(.+?)<.*?URL.*?value="(.+?)"', url, re.DOTALL)
 log(matches)
 for title, url in matches:
  plugintools . add_item ( action = "fluxus1" , title = title, url = url , thumbnail = "https://koditips.com/wp-content/uploads/fluxus-tv-kodi.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )  
def fluxus1 (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)#EXTINF:-1.*?logo="(.+?)".*?,(.+?)\n.*?(.+?)\s', url, re.DOTALL)
 log(matches)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "resolve_without_resolveurl" , title = title , url = url , thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )  
def canales ( params ):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header  = plugintools .read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)<header class="entry-.*?href="(.*?)".*?title="(.*?)".*?src="(.*?)"', url, re.DOTALL)
 for url, title,thumb, in matches:
  plugintools . add_item ( action = "canale1" , title = title, thumbnail = thumb , url = url , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
def canale1 ( params ):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header  = plugintools .read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s) - (.+?.m3u8)', url, re.DOTALL)
 for url in matches:
  plugintools . add_item ( action = "resolvers" , title = "Ver Opción", thumbnail = params . get ( "thumbnail" ), url = url , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )
def daqueen_tv_latina ( params ):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header  = plugintools .read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)href="(.+?)".*?alt="(.+?)".*?src="(.+?)"', url, re.DOTALL)
 for url, title, thumb, in matches:
  plugintools . add_item ( action = "daqueen_tv_latina_1" , title = title, thumbnail = thumb , url = url , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
def daqueen_tv_latina_1 ( params ):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header  = plugintools .read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)entry-content.*?<iframe.*?src="(.+?)"', url, re.DOTALL)
 for url in matches:
  plugintools . add_item ( action = "daqueen_tv_latina_2" , title = "Paso uno", url = url ,thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
def daqueen_tv_latina_2 ( params ):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header  = plugintools .read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)vlink.*?href="(.+?)#', url, re.DOTALL) 
 for url in matches: 
  plugintools . add_item ( action = "daqueen_tv_latina_3" , title = "Paso dos", url = url ,thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
def daqueen_tv_latina_3 ( params ):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header  = plugintools .read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)source: "(.+?)"', url, re.DOTALL)
 for url in matches:
  plugintools . add_item ( action = "resolvers" , title = "Ver Canal", url = url ,thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )
def SportZonline (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(\d.*?:\d\d).*?(\w.*?)\|.*?(http.*?.php)', url, re.DOTALL)
 for hora, title, url in matches:  
  plugintools . add_item ( action = "zonlinefin" , title = "[COLOR lime]"+hora+"[/COLOR]" + "  " + "[COLOR darkorange]"+title+"[/COLOR]", url = url , thumbnail= "https://i.imgur.com/N0YcFQR.jpg" , fanart="https://i.imgur.com/N0YcFQR.jpg", folder = False , isPlayable = True ) 
def elixx (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)class="accordion">(\d\d:\d\d).*?(\w.*?)<|href="(.+?)".*?">(.+?)<', url, re.DOTALL)
 for hora, title, url, opcion in matches:  
  plugintools . add_item ( action = "elixx1" , title = "[COLOR lime]"+hora+"[/COLOR]" + "  " + "[COLOR darkorange]"+title+"[/COLOR]" + opcion.replace('STREAM', 'Opcion'), url = url , thumbnail= "https://i.imgur.com/mcvn8mb.jpg" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True ) 
def elixx1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)iframe src="(.*?)".*?width="100%', url, re.DOTALL)
 for url in matches:   
  finalurl = ''
  if url != '':
   url = "http://elixx.me" + url 
   read_url , read_header = plugintools . read_body_and_headers ( url , headers = header ) 
   url = read_url . strip ( )
   finalurl =  re.findall(r'(?s)iframe src="(.*?)".*?width="100%', url, re.DOTALL)[0] 
 
  plugintools . add_item ( action = "zonlinefin" , title = "Ver:  " + params.get("title"), url =  finalurl  , thumbnail= "https://i.imgur.com/mcvn8mb.jpg" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True ) 
def onlyfoot (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)kode_ticket_text">.*?h6>(.+?)<.*?h2>(.+?)<.*?span>(.+?)<.*?h2>(.+?)<.*?p>(.+?)<|a\shref="(ch.*?)">(.+?)<', url, re.DOTALL)
 for liga, equipo1, vs, equipo2, hora, url, canal in matches:  
  plugintools . add_item ( action = "zonlinefin1" , title = "[COLOR lime]"+hora+"[/COLOR]" + "  " + liga + "  " + "[COLOR white]"+equipo1+"[/COLOR]" + "  " +"[COLOR white]"+vs+"[/COLOR]" + "  " +"[COLOR white]"+equipo2+"[/COLOR]" + canal, url = "http://onlyfoot.net/" + url , thumbnail= "https://i.imgur.com/XEhGg4T.jpg" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True ) 
def sportstv_io (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)class="jsx-2612811610 teams"><span class="jsx-2612811610">(.+?)<.*?href="(.+?)"', url, re.DOTALL)
 for title, url in matches:  
  plugintools . add_item ( action = "sportstv_io1" , title = title, url = "https://sportstv.io" + url , thumbnail= "https://i.imgur.com/3V0shid.jpg" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder =True ) 
def sportstv_io1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'webkitallowfullscreen" src="https://sportstvstreams.xyz/broadcast/(.+?)"', url, re.DOTALL)
 for url in matches:  
  plugintools . add_item ( action = "resolvers" , title = "Ver Evento", url = "https://sportstvstreams1.xyz/video/broadcast/" + url , thumbnail= "https://i.imgur.com/3V0shid.jpg" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True ) 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)href="(.+?)".*?title="(.+?)".*?src="(.+?)"', url, re.DOTALL)
 for url, title, src in matches:  
  plugintools . add_item ( action = "canales_deportes_fin" , title = title, url = "https:" + url , thumbnail= "https://adictosalatele.com" + src , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True ) 

 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)iframe src="(.+?)"', url, re.DOTALL)
 for url in matches:  
  plugintools . add_item ( action = "resolvers" , title = "Play" , url = url , thumbnail= params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True ) 


#Repeticiones Deportivas
  
def dascer_f1 (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)class="elementor-post.*?src="(https://dascer.com/wp-content/uploads.+?)".*?href="(.*?)".*?(\d.*?)<', url, re.DOTALL)
 log(matches)
 for thumb, url, title in matches:
  plugintools . add_item ( action = "dascer_f1_1" , title = title, url = url , thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True ) 
def dascer_f1_1 (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)elementor-toggle-title">(.*?)<.*?href="(https://upstream.to/.*?)"', url, re.DOTALL)
 log(matches)
 for title, url in matches:
  plugintools . add_item ( action = "resolvers" , title = title, url = url , thumbnail="https://i.imgur.com/U28DCh1.jpg" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True ) 
def dascer_f2 (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)class="elementor-post.*?src="(https://dascer.com/wp-content/uploads.+?)".*?href="(.*?)".*?(\d.*?)<', url, re.DOTALL)
 log(matches)
 for thumb, url, title in matches:
  plugintools . add_item ( action = "dascer_f1_1" , title = title, url = url , thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True ) 
def dascer_fe (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)class="elementor-post.*?src="(https://dascer.com/wp-content/uploads.+?)".*?href="(.*?)".*?(\d.*?)<', url, re.DOTALL)
 log(matches)
 for thumb, url, title in matches:
  plugintools . add_item ( action = "dascer_f1_1" , title = title, url = url , thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )  
def dascer_motogp (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)class="elementor-post.*?src="(https://dascer.com/wp-content/uploads.+?)".*?href="(.*?)".*?(\d.*?)<', url, re.DOTALL)
 log(matches)
 for thumb, url, title in matches:
  plugintools . add_item ( action = "dascer_motogp_1" , title = title, url = url , thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True ) 
def dascer_motogp_1 (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)elementor-toggle-title">(.*?)<.*?src="(.+?)"', url, re.DOTALL)
 log(matches)
 for title, url in matches:
  plugintools . add_item ( action = "dascer_f1_1" , title = title, url = url , thumbnail="https://i.imgur.com/U28DCh1.jpg" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True ) 
def dascer_moto2 (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)class="elementor-post.*?src="(https://dascer.com/wp-content/uploads.+?)".*?href="(.*?)".*?(\d.*?)<', url, re.DOTALL)
 log(matches)
 for thumb, url, title in matches:
  plugintools . add_item ( action = "dascer_f1_1" , title = title, url = url , thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True ) 
def dascer_moto2_1 (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)elementor-toggle-title">(.*?)<.*?src="(.+?)"', url, re.DOTALL)
 log(matches)
 for title, url in matches:
  plugintools . add_item ( action = "resolve_resolveurl_dascer" , title = title, url = url , thumbnail="https://i.imgur.com/U28DCh1.jpg" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )  
def dascer_moto3 (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)class="elementor-post.*?src="(https://dascer.com/wp-content/uploads.+?)".*?href="(.*?)".*?(\d.*?)<', url, re.DOTALL)
 log(matches)
 for thumb, url, title in matches:
  plugintools . add_item ( action = "dascer_f1_1" , title = title, url = url , thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True ) 
def tokyvideomotor (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)thumb-video\s\s">.*?href="(.+?)".*?alt="(.+?)".*?data-src="(.+?)"', url, re.DOTALL)
 log(matches)
 for url, title, thumb in matches:
  plugintools . add_item ( action = "tokyvideomotor_1" , title = title, url = url , thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )  
def tokyvideomotor_1 (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)source src="(.+?.(m3u8))', url, re.DOTALL)
 log(matches)
 for url, title in matches:
  plugintools . add_item ( action = "resolve_without_resolveurl" , title = title, url = url , thumbnail = "https://i2.wp.com/elrincon.tv/wp-content/uploads/2019/12/Tokyvideo-red-de-videos-internet.jpg?fit=841%2C359&ssl=1", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )
def tokyvideonba (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)thumb-video\s\s">.*?href="(.+?)".*?alt="(.+?)".*?data-src="(.+?)"', url, re.DOTALL)
 log(matches)
 for url, title, thumb in matches:
  plugintools . add_item ( action = "tokyvideonba_1" , title = title, url = url , thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )  
def tokyvideonba_1 (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)src="https://www.youtube.com/embed/(.+?)\?.*?<h1>.*?(\w.+?)<', url, re.DOTALL)
 log(matches)
 for url, title in matches:
  plugintools . add_item ( action = "resolve_resolveurl_youtube" , title = title , url = url , thumbnail = "https://i2.wp.com/elrincon.tv/wp-content/uploads/2019/12/Tokyvideo-red-de-videos-internet.jpg?fit=841%2C359&ssl=1", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )
def tokyvideotenis (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)thumb-video\s\s">.*?href="(.+?)".*?alt="(.+?)".*?data-src="(.+?)"', url, re.DOTALL)
 log(matches)
 for url, title, thumb in matches:
  plugintools . add_item ( action = "tokyvideonba_1" , title = title, url = url , thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True ) 
def Canales_de_Repeticiones (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)(https://www.youtube.com.*?),\s(.+?),\s(.+?),', url, re.DOTALL)
 log(matches)
 for url, title, thumb in matches:
  plugintools . add_item ( action = "channel_playlist_youtube" , title = title , url = url , thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
def Repeticiones_Playlist (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)(https://www.youtube.com.*?),\s(.+?),\s(.+?),', url, re.DOTALL)
 log(matches)
 for url, title, thumb in matches:
  plugintools . add_item ( action = "resolve_playlist_Youtube" , title = title , url = url , thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
def acestream (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  plugintools.find_multiple_matches(url, r'(?s)title\s=\s"([^"]+).*?link.*?url=(.+?)".*?thumb\s=\s"(.+?)".*?fanart\s=\s"(.+?)"')
 for title, url, thumb, fana in matches:
  plugintools . add_item ( action = "resolve_acestream" , title = title, url = url , thumbnail = thumb, fanart = fana, folder = False , isPlayable = True )


#Peliculas

def clasico_peliculas_search (params): 
 url = params . get ( "url" ) + keyboard_input("", "Buscar:", False).replace(" ", "+")
 url = requests.get(url).text 
 matches =  re.findall(r'(?s)class="thumbnail.*?href="(.+?)".*?src="(.+?)".*?alt="(.+?)"', url, re.DOTALL)
 for url, thumb, title in matches:
  plugintools . add_item ( action = "clasico_peliculas_1" , title = title, thumbnail = thumb , url = url , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
def clasico_peliculas_genero ( params ):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header  = plugintools .read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)class="menu.*?custom menu-item.*?href="(.+?)">(.+?)<', url, re.DOTALL)
 for url, title in matches:
  plugintools . add_item ( action = "clasico_peliculas" , title = title , url =  url , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )  
def clasico_peliculas ( params ):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header  = plugintools .read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)poster"><img src="(.+?)".*?star.*?span>(.+?)<.*?data.*?href="(.+?)">(.+?)<.*?span>(.+?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)class=\'arrow_pag.*?href="(.+?)"><i id=\'nextpagination')
 for thumb, punt, url, title, date in matches:
  plugintools . add_item ( action = "clasico_peliculas_1" , title =  title  + "[COLOR darkorange]" +  "  Puntuación  " + "[/COLOR]" + "[COLOR yellow]" + punt  + "[/COLOR]" + "  Fecha de la Película  " + "[COLOR lime]" + date + "[/COLOR]"  , thumbnail = thumb , url = url , fanart="special://home/addons/plugin.video.iberika/tenor.gif",  folder = True )
 plugintools . add_item ( action = "clasico_peliculas" , title ="[COLOR yellow]" + "PAGINA SIGUIENTE" + "[/COLOR]", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def clasico_peliculas_1 ( params ):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header  = plugintools .read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)<IFRAME SRC="(https://aparat.cam.*?)"', url, re.DOTALL)
 for url in matches:
  plugintools . add_item ( action = "resolvers" , title ="[COLOR yellow]" + "Servidor:  "+ "[/COLOR]" + "Aparat", thumbnail = params . get ( "thumbnail" ) , url =  url , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )  
def peliculas_flv_search (params): 
 url = params . get ( "url" ) + keyboard_input("", "Buscar:", False).replace(" ", " ")
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header  = plugintools .read_body_and_headers ( url , headers = header, timeout = 120 * 200  )
 url = read_url . strip ( ) 
 matches =  re.findall(r'(?s)<article>.*?href="(.+?)".*?poster.*?src="(.+?)".*?year".*?(\d\d\d\d).*?title".*?h2>(.+?)<', url, re.DOTALL)
 for url, thumb, year, title in matches:
  plugintools . add_item ( action = "peliculas_flv_estrenos_1" , title = "[COLOR blue]" +title + "[/COLOR]" + "   Año  " + "[COLOR darkorange]" + year + "[/COLOR]" , thumbnail = thumb , url = url , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
def peliculas_flv_genero ( params ):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header  = plugintools .read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)<li>.*?<a href="(.+?)">(.+?)<', url, re.DOTALL)
 for url, title in matches:
  plugintools . add_item ( action = "peliculas_flv_estrenos" , title = title, url = url, thumbnail = "https://pbs.twimg.com/profile_images/626976217611259904/pd2VyRXn.png" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
def peliculas_flv_estrenos ( params ):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header  = plugintools .read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)<article>.*?href="(.+?)".*?poster.*?src="(.+?)".*?year".*?(\d\d\d\d).*?title".*?h2>(.+?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)counter.*?href="(.+?)"')
 for url, thumb, year, title in matches:
  plugintools . add_item ( action = "peliculas_flv_estrenos_1" , title = "[COLOR blue]" +title + "[/COLOR]" + "   Año  " + "[COLOR darkorange]" + year + "[/COLOR]" , thumbnail = thumb , url = url , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
 plugintools . add_item ( action = "peliculas_flv_estrenos" , title ="[COLOR yellow]" + "PAGINA SIGUIENTE" + "[/COLOR]", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def peliculas_flv_estrenos_1 ( params ):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header  = plugintools .read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)<div class="lang-name">(.+?)<|server.*?hash="(.+?)".*?name">(.+?)<.*?quality">(.+?)<', url, re.DOTALL)
 for idio, hash, serv, cali in matches:
  plugintools . add_item ( action = "peliculas_flv_estrenos_2" , title = idio + serv  +"[COLOR yellow]" +"  " + cali + "[/COLOR]", thumbnail = params . get ( "thumbnail" ) , url =  hash , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True ) 
def peliculas_flv_estrenos_2 (params): 
 url = (  ( "https://www.peliculasflv.io/player.php?file=" + params . get("url") ) )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)<iframe src="(.+?)"', url, re.DOTALL)
 log(matches)
 for url in matches:
  plugintools . add_item ( action = "resolvers" , title = "Ver" , url = url , thumbnail = params . get ( "thumbnail" ) , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )  
def repelis_aniadidos ( params ):
 if int(params . get ( "page" )) != 1:
  url = params . get ( "url" ) + params . get ( "page" ) + "/"
 else:
  url = "https://www.repelisplus.vip/peliculas/"
 
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches = plugintools . find_multiple_matches ( url , '(?s)(class="ksaj.*?</h4>)' )
 
 next = plugintools . find_single_match ( url , 'class="jahba".*?href="(.+?)"' )
 for match in matches :
    title = plugintools . find_single_match ( match , 'class="kaiz"><h4>(.+?)<' ) 
    thumb = plugintools . find_single_match ( match , 'src="(.+?)"' )
    url = plugintools . find_single_match ( match , 'class="ksaj".*?href="(.+?)"' ) 
    
    plugintools . add_item ( action = "repelis_1" , title = title, thumbnail = thumb, url = url, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
 next = str(int(params . get ( "page" )) + 1)
 plugintools.add_item( action = "repelis_aniadidos" , title = "Next Page", url= "https://www.repelisplus.vip/peliculas/page/", thumbnail = 'https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png', page=next , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True ) 
def repelis_1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)div class="jshdz"><a class="sfsg" href="(.+?)".*?polygon.*?span>(.+?)<', url, re.DOTALL)

 for url, title in matches:
  plugintools . add_item ( action = "repelis_2" , title = title , url = url , thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
def repelis_2 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header  =plugintools .read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)class="adag"><p>(.+?)<|rel="noindex,.*?href="(.+?)"><span>(.+?)<', url, re.DOTALL)

 for idio, url, title in matches:
  finalurl = ''
  if url != '' :
   url = url
 
   read_url , read_header = plugintools . read_body_and_headers ( url , headers = header, timeout =300 *500 ) 
   url = read_url . strip ( )
   finalurl =  re.findall(r'(?s)iframe.*?scrolling.*?src="(.+?)"', url, re.DOTALL)[0]
  plugintools . add_item ( action = "resolvers" , title = idio + title , url = finalurl , thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False, isPlayable = True )  
def repelis_estrenos (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches = plugintools . find_multiple_matches ( url , '(?s)(class="ksaj.*?</h4>)' )
 
 for match in matches :
    title = plugintools . find_single_match ( match , 'class="kaiz"><h4>(.+?)<' ) 
    thumb = plugintools . find_single_match ( match , 'src="(.+?)"' )
    url = plugintools . find_single_match ( match , 'class="ksaj".*?href="(.+?)"' ) 
    plugintools . add_item ( action = "repelis_1" , title = title, thumbnail = thumb, url = url, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
def repelis_popular ( params ):
 if int(params . get ( "page" )) != 1:
  url = params . get ( "url" ) + params . get ( "page" ) + "/"
 else:
  url = "https://www.repelisplus.vip/peliculas/popular/"
 
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches = plugintools . find_multiple_matches ( url , '(?s)(class="ksaj.*?</h4>)' )
 
 next = plugintools . find_single_match ( url , 'class="jahba".*?href="(.+?)"' )
 for match in matches :
    title = plugintools . find_single_match ( match , 'class="kaiz"><h4>(.+?)<' ) 
    thumb = plugintools . find_single_match ( match , 'src="(.+?)"' )
    url = plugintools . find_single_match ( match , 'class="ksaj".*?href="(.+?)"' ) 
    
    plugintools . add_item ( action = "repelis_1" , title = title, thumbnail = thumb, url = url, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
 next = str(int(params . get ( "page" )) + 1)
 plugintools.add_item( action = "repelis_popular" , title = "Next Page", url= "https://www.repelisplus.vip/peliculas/page/", thumbnail = 'https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png', page=next , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True ) 
def Repelis_search (params): 
 url = params . get ( "url" ) + keyboard_input("", "Buscar:", False).replace(" ", "+")
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)class="ksaj.*?href="(.+?)".*?src="(.+?)".*?h4>(.+?)<', url, re.DOTALL)
 log(matches)
 for url, thumb, title in matches:
  plugintools . add_item ( action = "repelis_1" , title = title, thumbnail = thumb, url = url, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
def grantorrent_search (params): 
 url = params . get ( "url" ) + keyboard_input("", "Buscar:", False).replace(" ", "+")
 url = requests.get(url).text 
 matches =  re.findall(r'(?s)class="imagen.*?href="(.*?nl/(.*?)/)".*?data-lazy-src="([^"]+)', url, re.DOTALL)
 for url, title, thumb in matches:
  plugintools . add_item ( action = "hdrip1" , title = title, thumbnail = thumb , url = url , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
def hdrip (params): 
 url = params . get ( "url" )
 url = requests.get(url).text 
 matches =  re.findall(r'(?s)class="imagen.*?href="(.*?nl/(.*?)/)".*?img src="([^"]+)', url, re.DOTALL)
 next = plugintools.find_single_match(url,'<link rel="next" href="([^"]+)"')
 for url, title, thumb in matches:
  plugintools . add_item ( action = "hdrip1" , title = title, thumbnail = thumb , url = url , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
 plugintools . add_item ( action = "hdrip" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def hdrip1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)lol.*?title=.*?Castellano.*?.*?td>.*?td>(.*?)<.*?u:\s.([^"]+)', url, re.DOTALL)
 log(matches)
 for title, url in matches:
  plugintools . add_item ( action = "elementum_gran" , title = title , url = url , thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True)   
def blueray (params): 
 url = params . get ( "url" )
 url = requests.get(url).text
 
 matches =  re.findall(r'(?s)class="imagen.*?href="(.*?nl/(.*?)/)".*?img src="([^"]+)', url, re.DOTALL)
 next = plugintools.find_single_match(url,'<link rel="next" href="([^"]+)"')
 for url, title, thumb in matches:
  plugintools . add_item ( action = "blueray1" , title = title, thumbnail = thumb , url = url , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
 plugintools . add_item ( action = "blueray" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def blueray1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)lol.*?title=.*?Castellano.*?.*?td>.*?td>(.*?)<.*?u:\s.([^"]+)', url, re.DOTALL)
 log(matches)
 for title, url in matches:
  plugintools . add_item ( action = "elementum_gran" , title = title , url = url , thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True)   
def cuatrok (params): 
 url = params . get ( "url" )
 url = requests.get(url).text
 
 matches =  re.findall(r'(?s)class="imagen.*?href="(.*?nl/(.*?)/)".*?img src="([^"]+)', url, re.DOTALL)
 next = plugintools.find_single_match(url,'<link rel="next" href="([^"]+)"')
 for url,title , thumb in matches:
  plugintools . add_item ( action = "cuatrok1" , title = title, thumbnail = thumb , url = url , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
 plugintools . add_item ( action = "cuatrok" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def cuatrok1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)lol.*?title=.*?Castellano.*?.*?td>.*?td>(.*?)<.*?u:\s.([^"]+)', url, re.DOTALL)
 log(matches)
 for title, url in matches:
  plugintools . add_item ( action = "elementum_gran" , title = title , url = url , thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True)    
def fullbluray_1080p (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header, timeout =300 *500  )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)mv-img.*?src="(.+?)".*?alt="(.+?)".*?href="(.+?)"', url, re.DOTALL)
 log(matches)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "pctfenix_final" , title = title , url = url , thumbnail = ( ( "https:" ) + thumb ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )    
def pctfenix_final (params): 
 url = (  ( "https://pctfenix.com" + params . get("url") ) )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)"ctn-download-(.+?)".*?data-ut="(.+?)"', url, re.DOTALL)
 log(matches)
 for title, url in matches:
  plugintools . add_item ( action = "elementum_pctfenix1" , title = title , url = url , thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )    
def bluray_1080p (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)mv-img.*?src="(.+?)".*?alt="(.+?)".*?href="(.+?)"', url, re.DOTALL)
 log(matches)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "pctfenix_final" , title = title , url = url , thumbnail = ( ( "https:" ) + thumb ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )    
def dbremux_1080p (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)mv-img.*?src="(.+?)".*?alt="(.+?)".*?href="(.+?)"', url, re.DOTALL)
 log(matches)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "pctfenix_final" , title = title , url = url , thumbnail = ( ( "https:" ) + thumb ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )    
def cuatrok_uhdremux (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)mv-img.*?src="(.+?)".*?alt="(.+?)".*?href="(.+?)"', url, re.DOTALL)
 log(matches)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "pctfenix_final" , title = title , url = url , thumbnail = ( ( "https:" ) + thumb ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )      
def cuatrok_uhdmicro (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)mv-img.*?src="(.+?)".*?alt="(.+?)".*?href="(.+?)"', url, re.DOTALL)
 log(matches)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "pctfenix_final" , title = title , url = url , thumbnail = ( ( "https:" ) + thumb ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )     
def cuatrok_uhdrip (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)mv-img.*?src="(.+?)".*?alt="(.+?)".*?href="(.+?)"', url, re.DOTALL)
 log(matches)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "pctfenix_final" , title = title , url = url , thumbnail = ( ( "https:" ) + thumb ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )      
def cuatrok_webrip (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)mv-img.*?src="(.+?)".*?alt="(.+?)".*?href="(.+?)"', url, re.DOTALL)
 log(matches)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "pctfenix_final" , title = title , url = url , thumbnail = ( ( "https:" ) + thumb ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )   
def full_uhdcuatrok (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)mv-img.*?src="(.+?)".*?alt="(.+?)".*?href="(.+?)"', url, re.DOTALL)
 log(matches)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "pctfenix_final" , title = title , url = url , thumbnail = ( ( "https:" ) + thumb ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )    
def microhd_1080p (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)mv-img.*?src="(.+?)".*?alt="(.+?)".*?href="(.+?)"', url, re.DOTALL)
 log(matches)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "pctfenix_final" , title = title , url = url , thumbnail = ( ( "https:" ) + thumb ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )  
def mitorrent ( params ):
 if int(params . get ( "page" )) != 1:
  url = params . get ( "url" ) + params . get ( "page" ) + "/"
 else:
  url = "https://mitorrent.org/"
 
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches = plugintools . find_multiple_matches ( url , '(?s)(img-responsive".*?browse-movie-tags)' )
 
 next = plugintools . find_single_match ( url , '<li><a class="next page-numbers" href="([^"]+)' )
 for match in matches :
    title = plugintools . find_single_match ( match , 'browse-movie-title">([^<]+)<' ) 
    thumb = plugintools . find_single_match ( match , 'sive" src="([^"]+)"' )
    url = plugintools . find_single_match ( match , 'browse-movie-bottom">.*?href="([^"]+)"' ) 
    
    plugintools . add_item ( action = "mitorrent1" , title = title , thumbnail = thumb, url = url, folder = True )
 next = str(int(params . get ( "page" )) + 1)
 plugintools.add_item( action = "mitorrent" , title = "Next Page", url= "https://mitorrent.org/page/", thumbnail = 'https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png', page=next , folder=True ) 
def mitorrent1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)(torrent)\sbutton-green.*?href="(.+?)"', url, re.DOTALL)
 log(matches)
 for title, url in matches:
  plugintools . add_item ( action = "elementum" , title = title , url = url, folder = False , isPlayable = True )  
def pctreload_cast (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)<li> <a href="(.+?)".*?src="(.+?)".*?h2>(.+?)<.*?span>(.+?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)\d\d">\.\.\..*?\d\d.*?href="(.+?)"')
 for url, thumb, title, calidad in matches:
  finalurl = ''
  if url != '':
   url = url 
   read_url , read_header = plugintools . read_body_and_headers ( url , headers = header ) 
   url = read_url . strip ( )
   finalurl =  re.findall(r'(?s)window.location.href\s=\s"(.+?)"', url, re.DOTALL)[0] 
  plugintools . add_item ( action = "elementum" , title = title + calidad , url = "https:" + finalurl , thumbnail = "https:" + thumb , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )
 plugintools . add_item ( action = "pctreload_cast" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def EstrenosGo_cartelera (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)class="MiniFicha">.*?src="(.+?)".*?Torrent Video Online">(.+?)-(.+?)<.*?&raquo;(.+?)<.*?title="Descargas en  Descarga Directa"></a><a href="(.+?)"', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)fx">\d.*?</a>  <b>\d.*?</b> <a href="(.+?)">Siguiente')
 for img, nombre, ano, calidad, url in matches:
  plugintools . add_item ( action = "EstrenosGo_cartelera_1" , title = nombre + "  "+"[COLOR lime]" + ano +"[/COLOR]"+ "  "+"[COLOR yellow]" +calidad+"[/COLOR]" , url = url , thumbnail = "https://estrenosflix.org" + img , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
 plugintools . add_item ( action = "EstrenosGo_cartelera" , title = "PAGINA SIGUIENTE", url= "https://estrenosflex.com/" + next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def EstrenosGo_cartelera_1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)class="content"><a href="(.+?)".*?strong>(.+?)<.*?strong>(.+?)<', url, re.DOTALL) 
 for url, nombre, idioma in matches:
  finalurl = ''
  if url != '':
   url = url 
   read_url , read_header = plugintools . read_body_and_headers ( url , headers = header ) 
   url = read_url . strip ( )
   finalurl =  re.findall(r'(?s)Descargar Torrent:.*?href="(.+?)"', url, re.DOTALL)[0]
  plugintools . add_item ( action = "elementum_estrenosgo" , title ="Ver" + "  " + nombre + "  " + "en" + "  " + "[COLOR lime]"+ idioma + "[/COLOR]" , url = finalurl , thumbnail = params . get ( "thumbnail" ) , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )
def pctmix_cast (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)<li> <a href="(.+?)".*?src="(.+?)".*?h2>(.+?)<.*?span>(.+?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)\d\d">\.\.\..*?\d\d.*?href="(.+?)"')
 for url, thumb, title, calidad in matches:
  finalurl = ''
  if url != '':
   url = url 
   read_url , read_header = plugintools . read_body_and_headers ( url , headers = header ) 
   url = read_url . strip ( )
   finalurl =  re.findall(r'(?s)window.location.href\s=\s"(.+?)"', url, re.DOTALL)[0] 
  plugintools . add_item ( action = "elementum" , title = title + calidad , url = "https:" + finalurl , thumbnail = "https:" + thumb , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )
 plugintools . add_item ( action = "pctreload_cast" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def NewPelis_peliculas (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)col-xs-4">.*?ah-imagge.*?href="(.+?)".*?src="(.+?)".*?alt="(.+?)"', url, re.DOTALL)
 next = plugintools.find_single_match(url,'class="next.*?href="(.+?)"')
 for url, thumb, title in matches:
  plugintools . add_item ( action = "NewPelis_peliculas_1" , title = title , url = url , thumbnail = thumb , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
 plugintools . add_item ( action = "NewPelis_peliculas" , title = "PAGINA SIGUIENTE", url= url, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def NewPelis_peliculas_1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)href="(magnet.*?)"', url, re.DOTALL)
 next = plugintools.find_single_match(url,'class="next.*?href="(.+?)"')
 for url in matches:
  plugintools . add_item ( action = "elementum" , title = "Ver" + "  " + params . get ( "title" ) , url = url , thumbnail = params . get ( "thumbnail" ) , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )
def NewPelis_peliculas_top (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)col-xs-4">.*?ah-imagge.*?href="(.+?)".*?src="(.+?)".*?alt="(.+?)"', url, re.DOTALL)
 for url, thumb, title in matches:
  plugintools . add_item ( action = "NewPelis_peliculas_1" , title = title , url = url , thumbnail = thumb , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
def NewPelis_peliculas_genero (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)href="(.+?)">(.+?)<', url, re.DOTALL)
 for url, title in matches:
  plugintools . add_item ( action = "NewPelis_peliculas" , title = title , url = url , thumbnail = "https://newpelis.nl/wp-content/themes/allcine/images/logoss.png" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
def doreamasmp4 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)mb-3"><a href="(.+?)".*?src="(.+?)".*?500">(.+?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)lass="page-item"><a href="(.+?)"')
 for url, thumb, title in matches:
  plugintools . add_item ( action = "doreamasmp4_1" , title = title , url = url , thumbnail = thumb , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
 plugintools . add_item ( action = "doreamasmp4" , title = "PAGINA SIGUIENTE", url= "https://www20.doramasmp4.com/catalogue" + next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def doreamasmp4_1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)sv_aparat_cam" data-link="(.+?)"', url, re.DOTALL)
 for url in matches:
  plugintools . add_item ( action = "doreamasmp4_2" , title = "Ver:" + "  " + params . get ( "title" ) , url = url , thumbnail = params . get ( "thumbnail" ) , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
def doreamasmp4_2 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)iframe.*?src="(.+?)"', url, re.DOTALL)
 for url in matches:
  finalurl = ''
  if url != '':
   url = url 
   read_url , read_header = plugintools . read_body_and_headers ( url , headers = header ) 
   url = read_url . strip ( )
   finalurl =  re.findall(r'(?s)window.location.href = \'(.+?)\'', url, re.DOTALL)[0]  
  plugintools . add_item ( action = "resolvers" , title = "Servidor: Aparat:" , url = finalurl , thumbnail = params . get ( "thumbnail" ) , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )
def cortosdemetrajecine (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)class=item-thumbnail.*?href=(.+?)\s.*?>.*?height=293 src=(.+?.jpg).*?alt="(.+?)"', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)rel=canonical.*?rel=next href=(.+?)\s')
 for url, src, title in matches:
  plugintools . add_item ( action = "cortosdemetrajecine_1" , title = title , url = url , thumbnail = src , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
 plugintools . add_item ( action = "cortosdemetrajecine" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def cortosdemetrajecine_1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)height=506 src="https://www.youtube.com/embed/(.+?)\?', url, re.DOTALL)
 log(matches)
 for url in matches:
  plugintools . add_item ( action = "resolve_resolveurl_youtube" , title = "Ver:  " + params . get ( "title" ), url = url , thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True)    
def cortosdemetrajedocus (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)class=item-thumbnail.*?href=(.+?)\s.*?height=293 src=(.+?.jpg).*?title=(.+?)>(.+?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)rel=canonical.*?rel=next href=(.+?)\s')
 for url, src, title, title1 in matches:
  plugintools . add_item ( action = "cortosdemetrajecine_1" , title = title1 , url = url , thumbnail = src , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
 plugintools . add_item ( action = "cortosdemetrajedocus" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def NewPcttodas (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)data-src="(.+?)".*?title="(.+?)".*?b>(.+?)<.*?href="(.+?)".*?b>(.+?)<.*?complets.*?b>(.+?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'rel="next" href="(.+?)"')
 for src, title, calidad, href, peso, idioma in matches:
  plugintools . add_item ( action = "NewPcttodas1" , title = title +"  "+"[COLOR lime]"+calidad+"[/COLOR]""  "+"[COLOR yellow]"+peso+"[/COLOR]" + "  "+"[COLOR darkorange]"+idioma+"[/COLOR]"  , url = href , thumbnail = src , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
 plugintools . add_item ( action = "NewPcttodas" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def NewPcttodas1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)top:15px;"> <a href="(.+?)"', url, re.DOTALL)
 for href in matches:
  plugintools . add_item ( action = "elementum" , title ="Ver:  " + params . get ( "title" ), url = "https://www.newpct.me" + href.replace(" ", "%20"), thumbnail = params . get ( "thumbnail" ) , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True)
def NewPct_search (params): 
 url = params . get ( "url" ) + keyboard_input("", "Buscar:", False).replace(" ", "+")
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)data-src="(.+?)".*?title="(.+?)".*?b>(.+?)<.*?href="(.*?peliculas.*?)"', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)"pagina pag_actual.*?href=\'(.+?)\'')
 for src, title, calidad, href in matches:
  plugintools . add_item ( action = "NewPcttodas1" , title = title.replace("&#8211;", " ").replace("&#215;", " ") , url = href , thumbnail = src , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
 plugintools . add_item ( action = "NewPcttodas" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def repelis_uno_peliculas (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)"movie-item"><a href="(https://repelis.uno/pelicula/(.+?))".*?src=(.+?.jpg).*?year.*?center">(.+?)<', url, re.DOTALL)
 for href, title, src, year in matches:
  plugintools . add_item ( action = "repelis_uno_peliculas_1" , title = title.replace("-", " ") + "  " +  "[COLOR lime]" + year + "[/COLOR]", url = href , thumbnail = src , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
def repelis_uno_peliculas_1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)role="presentation" data-player-video="(.+?)".*?icon-play-circle"></i>(.+?)<', url, re.DOTALL)
 for url, title in matches:
  url = base64.b64decode( url )
  plugintools . add_item ( action = "resolvers" , title = title, url = url , thumbnail = params . get ( "thumbnail" ) , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True)
def repelis_uno_peliculas_pag_gen (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)"movie-item"><a href="(https://repelis.uno/pelicula/(.+?))".*?src=(.+?.jpg).*?year.*?center">(.+?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)\.\.\.</span>.*?page=.*?page=.*?page-link.*?href="(.+?)"')

 for href, title, src, year in matches:
  plugintools . add_item ( action = "repelis_uno_peliculas_1" , title = title.replace("-", " ") + "  " +  "[COLOR lime]" + year + "[/COLOR]", url = href , thumbnail = src , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
 plugintools . add_item ( action = "repelis_uno_peliculas_pag_gen" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def repelis_uno_peliculas_pag2 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)"movie-item"><a href="(https://repelis.uno/pelicula/(.+?))".*?src=(.+?.jpg).*?year.*?center">(.+?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)page=.*?href="(.+?)"\srel="next"')

 for href, title, src, year in matches:
  plugintools . add_item ( action = "repelis_uno_peliculas_1" , title = title.replace("-", " ") + "  " +  "[COLOR lime]" + year + "[/COLOR]", url = href , thumbnail = src , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
 plugintools . add_item ( action = "repelis_uno_peliculas_pag2" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def repelis_uno_peliculas_pag3 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)"movie-item"><a href="(https://repelis.uno/pelicula/(.+?))".*?src=(.+?.jpg).*?year.*?center">(.+?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)page=.*?page=.*?href="(.+?)"\srel="next"')

 for href, title, src, year in matches:
  plugintools . add_item ( action = "repelis_uno_peliculas_1" , title = title.replace("-", " ") + "  " +  "[COLOR lime]" + year + "[/COLOR]", url = href , thumbnail = src , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
 plugintools . add_item ( action = "repelis_uno_peliculas_pag3" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def repelis_uno_peliculas_gen (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)href="(https://repelis.uno/genero/.+?)".*?/i>(.+?)<', url, re.DOTALL)
 for href, title in matches:
  plugintools . add_item ( action = "repelis_uno_peliculas_pag_gen" , title = title, url = href , thumbnail = "https://i.imgur.com/uY8mqqG.jpg" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
def repelis_uno_peliculas_year (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)href="(https://repelis.uno/peliculas-\d.*?)".*?>(.+?)<', url, re.DOTALL)
 for href, title in matches:
  plugintools . add_item ( action = "repelis_uno_peliculas_pag_gen" , title = title, url = href , thumbnail = "https://i.imgur.com/uY8mqqG.jpg" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
def zonatorrent_tv_pelis (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)<a href="(https://zonatorrent.tv/peliculas/.+?)".*?src="(.+?)".*?Title">(.+?)\((.+?)\).*?Year">(.+?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'a class="next page-numbers" href="(.+?)"')
 
 for url, src, title, hq,  year in matches:
  plugintools . add_item ( action = "zonatorrent_tv_pelis1" , title = title + "  " + hq + "  " + year, url = url , thumbnail = "https:" + src , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
 plugintools . add_item ( action = "zonatorrent_tv_pelis" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def zonatorrent_tv_pelis1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)" target="_blank" href="(.+?)"', url, re.DOTALL)
 
 for url in matches:
  plugintools . add_item ( action = "elementum" , title = "Ver:  " + params . get ( "title" ), url = url, thumbnail = params . get ( "thumbnail" ) , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True)
def divxtotal_peliculas (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)td.*?href="(.+?)"\stitle="(.+?)".*?</td>.*?">(.+?)<.*?src="(.+?)"', url, re.DOTALL)
 next = plugintools.find_single_match(url,'rel="next" href="(.+?)"')
 
 for url, title, genero, src in matches:
  plugintools . add_item ( action = "divxtotal1" , title = title + "  " + "[COLOR lime]" + "Genero" + "  " + genero + "[/COLOR]", url = url , thumbnail = src , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
 plugintools . add_item ( action = "divxtotal_peliculas" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def divxtotal1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s);border-radius: 0px;"  href="(.*?)"', url, re.DOTALL)
 
 for url in matches:
  plugintools . add_item ( action = "elementum" , title = "Ver:  " + params . get ( "title" ), url = "https://www.divxtotal.in" + url , thumbnail = params . get ( "thumbnail" ) , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True)
def divxtotal_search (params): 
 url = params . get ( "url" ) + keyboard_input("", "Buscar:", False).replace(" ", "+")
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)tr>.*?href="(.+?)".*?title="(.+?)"', url, re.DOTALL)
 log(matches)
 for url, title in matches:
  plugintools . add_item ( action = "divxtotal1" , title = title, thumbnail = "https://i.imgur.com/gg3nuQl.jpg", url = url, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )


#Series

def grantorrent_series_nor (params): 
 url = params . get ( "url" )
 url = requests.get(url).text 
 matches =  re.findall(r'(?s)imagen-post">.*?href="(.+?.nl/series/(.*?)/)".*?src="(.+?)"', url, re.DOTALL)
 next = plugintools.find_single_match(url,'<link rel="next" href="([^"]+)"')
 for url, title, thumb in matches:
  plugintools . add_item ( action = "grantorrent_series_nor2" , title = title, thumbnail = thumb , url = url , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
 plugintools . add_item ( action = "grantorrent_series_nor" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def grantorrent_series_nor2 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)title="(.+?)".*?td>.*?td>(.+?)<.*?td>.*?td>(.+?)<.*?u:\s\'(.+?)\'', url, re.DOTALL)
 log(matches)
 for title, cap, peso, url in matches:
  plugintools . add_item ( action = "elementum_gran" , title = title + "  " + cap +  "  " + peso , url = url , thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True)    
def grantorrent_series_categoria (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header, timeout =300 *500 )
 url = read_url . strip ( )
 
 matches =  re.findall(r'<a href="(.+?)"><li class="(categoria.*?)">(.+?)<', url, re.DOTALL)
 log(matches)
 for url, cat, title in matches:
  plugintools . add_item ( action = "grantorrent_series_nor" , title = cat + "  " + title , url = url , thumbnail="https://grantorrents.org/wp-content/uploads/2020/03/LOGOTEST.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )    
def mitorrent_series ( params ):
 if int(params . get ( "page" )) != 1:
  url = params . get ( "url" ) + params . get ( "page" ) + "/"
 else:
  url = "https://mitorrent.org/series/"
 
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches = plugintools . find_multiple_matches ( url , '(?s)(img-responsive".*?browse-movie-tags)' )
 
 next = plugintools . find_single_match ( url , '<li><a class="next page-numbers" href="([^"]+)' )
 for match in matches :
    title = plugintools . find_single_match ( match , 'browse-movie-title">([^<]+)<' ) 
    thumb = plugintools . find_single_match ( match , 'sive" src="([^"]+)"' )
    url = plugintools . find_single_match ( match , 'browse-movie-bottom">.*?href="([^"]+)"' ) 
    
    plugintools . add_item ( action = "mitorrent_series1" , title = title , thumbnail = thumb, url = url, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
 next = str(int(params . get ( "page" )) + 1)
 plugintools.add_item( action = "mitorrent_series" , title = "Next Page", url= "https://mitorrent.org/series/page/", thumbnail = 'https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png', fanart="special://home/addons/plugin.video.iberika/tenor.gif", page=next , folder=True ) 
def mitorrent_series1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)class="accordion.*?&nbsp;(.+?)<|href="(magnet.+?)".*?Descargar(.+?\d.)', url, re.DOTALL)
 log(matches)
 for temp, url, title in matches:
  plugintools . add_item ( action = "elementum" , title = "[COLOR lime]" + temp + "[/COLOR]" + title , url = url , thumbnail = params . get ( "thumbnail" ),  fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )    
def Mi_torrent_Genero (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)<option value="(.+?)">(.+?)<', url, re.DOTALL)
 log(matches)
 for url, title in matches:
  plugintools . add_item ( action = "Mi_torrent_Genero1" , title = title , url = "https://mitorrent.org/series/search-result/?search_query=&tax_generos=" + url , thumbnail="https://i.imgur.com/DcBBOBf.jpg", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )    
def Mi_torrent_Genero1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)col-lg-.*?<a href="(.+?)".*?src="(.+?)".*?Descargar\s(.+?)"', url, re.DOTALL)
 log(matches)
 for url, thumb, title in matches:
  plugintools . add_item ( action = "mitorrent_series1" , title = title , url = url , thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )    
def pctreload_series_normal (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)class="active".*?class="page-box".*?strong>(.+?)<|\s<a href="(.*?)"\stitle="(.+?)".*?src="(.+?)".*?<span>(.+?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'\d\d">\d\d.*?\d\d">\d\d.*?\d\d">\d\d.*?\d\d">\d\d.*?.*?href="(.+?)">Next')
 for cantidad, url, title, thumb, calidad in matches:
  plugintools . add_item ( action = "pctreload_series_normal_1" , title = cantidad + title + "  " + calidad , url = url , thumbnail = "https:" + thumb , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
 plugintools . add_item ( action = "pctreload_series_normal" , title = "PAGINA SIGUIENTE", url= next,  thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def pctreload_series_normal_1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)padding:0;">(.+?)<.*?none;">(.*?)<.*?span>(.+?)<.*?none;">(.*?)<.*?span>\s.*?span>(.*?)<.*?href="(.+?)"', url, re.DOTALL)
 for serie, capitulos, title, calidad, peso, url in matches:
  finalurl = ''
  if url != '':
   url = url 
   read_url , read_header = plugintools . read_body_and_headers ( url , headers = header ) 
   url = read_url . strip ( )
   finalurl =  re.findall(r'(?s)window.location.href\s=\s"(.+?)"', url, re.DOTALL)[0] 
  plugintools . add_item ( action = "elementum" , title = serie + "  " + capitulos + "  " +title + "  " + calidad + "  " + peso , url = "https:" + finalurl, thumbnail = params . get ( "thumbnail" )  , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )
def seriesly_ultimas_series (params): 
 url = params . get ( "url" )
 request_headers=[]
 request_headers.append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0" ] )
 request_headers.append ( [ "Cookie" , "sucuri_cloudproxy_uuid_ddce1ba0a=2c39acd488e40ab0a783c0d7e3db62ee" ] )
 body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
 url = body.strip()
 matches =  re.findall(r'(?s)TPost C.*?href="(.+?)".*?src="(.+?)".*?Yr">(.+?)<.*?Title">(.+?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'rel="next" href="(.+?)"')
 for url, thumb, year, title in matches:
  plugintools . add_item ( action = "seriesly_ultimas_series_1" , title = title + "  " + "[COLOR yellow]" + "Año" + "  " + "[COLOR lime]" + year + "[/COLOR]" , url = url , thumbnail = "https:" + thumb , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
 plugintools . add_item ( action = "seriesly_ultimas_series" , title = "PAGINA SIGUIENTE", url= next,  thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def seriesly_ultimas_series_1 (params): 
 url = params . get ( "url" )
 request_headers=[]
 request_headers.append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0" ] )
 request_headers.append ( [ "Cookie" , "sucuri_cloudproxy_uuid_ddce1ba0a=2c39acd488e40ab0a783c0d7e3db62ee" ] )
 body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
 url = body.strip()
 matches =  re.findall(r'(?s)data-tab.*?Season.*?span>(.+?)<|"MvTbTtl"><a href="(.+?)">(.+?)<.*?span>(.+?)<', url, re.DOTALL)
 for temporada, url, title, year in matches:
  plugintools . add_item ( action = "seriesly_ultimas_series_2" , title = temporada + title + "  " + "[COLOR yellow]" + "  " + "[COLOR lime]" + year + "[/COLOR]" , url = url , thumbnail = params . get ( "thumbnail" ) , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
def seriesly_ultimas_series_2 (params): 
 url = params . get ( "url" )
 request_headers=[]
 request_headers.append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0" ] )
 request_headers.append ( [ "Cookie" , "sucuri_cloudproxy_uuid_ddce1ba0a=2c39acd488e40ab0a783c0d7e3db62ee" ] )
 body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
 url = body.strip()
 matches =  re.findall(r'(?s)iframe width="560" height="315" src="(.*?)&.*?;(.*?)"', url, re.DOTALL)
 for part1, part2 in matches:
  plugintools . add_item ( action = "seriesly_ultimas_series_3" , title = "Ver Servidores", url = part1 + "&" + part2 , thumbnail = params . get ( "thumbnail" ) , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
def seriesly_ultimas_series_3 (params): 
 url = params . get ( "url" )
 request_headers=[]
 request_headers.append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0" ] )
 request_headers.append ( [ "Cookie" , "sucuri_cloudproxy_uuid_ddce1ba0a=2c39acd488e40ab0a783c0d7e3db62ee" ] )
 body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
 url = body.strip()
 matches =  re.findall(r'(?s)iframe width="560" height="315" src="(.+?)"', url, re.DOTALL)
 for url in matches:
  plugintools . add_item ( action = "resolvers" , title = "Servidor Uqload" , url = url , thumbnail = params . get ( "thumbnail" ) , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )
def NewPelis_series (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)col-xs-4">.*?ah-imagge.*?href="(.+?)".*?src="(.+?)".*?title="(.+?)"', url, re.DOTALL)
 next = plugintools.find_single_match(url,'class="next.*?href="(.+?)"')
 for url, thumb, title in matches:
  plugintools . add_item ( action = "NewPelis_series_1" , title = title , url = url , thumbnail = thumb , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
 plugintools . add_item ( action = "NewPelis_series" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def NewPelis_series_1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)(?s)class="fa fa-server.*?&nbsp;(.+?)<|href="(magnet.*?)".*?Descargar(.+?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'class="next.*?href="(.+?)"')
 for temporada, url, capitulo in matches:
  plugintools . add_item ( action = "elementum" , title = temporada + capitulo , url = url , thumbnail = params . get ( "thumbnail" ) , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True ) 
def retro_series (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)class="TPost C".*?href="(.+?)".*?data-src="(.+?)".*?Title">(.+?)<.*?Year">(.+?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)next page-numbers" href="(.+?)"')
 for url,thumb, title, year in matches:
  plugintools . add_item ( action = "retro_series1" , title = title + "  " + year , url = url , thumbnail = thumb , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
 plugintools . add_item ( action = "retro_series" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def retro_series1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)class="Num">(.+?)<.*?lass="MvTbTtl"><a href="(.+?)">(.+?)<.*?span>(.+?)<', url, re.DOTALL)
 for cap,url, title, year in matches:
  plugintools . add_item ( action = "retro_series2" , title = "Capitulo"+ "  " + cap + "  " + title + "  " + year , url = url , thumbnail = params . get ( "thumbnail" ) , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
def retro_series2 (params): 
 url = params . get ( "url" ) 
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)id="(Opt2)".*?height=.*?src=.*?https://seriesretro.com/\?trembed=(\d&).*?(trid.*?&).*?(trtype.*?\d)', url, re.DOTALL)
 for title, part1, part2, part3 in matches:
  plugintools . add_item ( action = "retro_series3" , title = "Ver" + "  " + params . get ( "title" ) , url = "https://seriesretro.com/?trembed=" + part1 + part2 + part3 , thumbnail = params . get ( "thumbnail" ) , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
def retro_series3 (params): 
 url = params . get ( "url" ) 
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)src="(https://www.(.+?)\/.+?)"', url, re.DOTALL)
 for url , title in matches:
  plugintools . add_item ( action = "resolvers" , title = "Servidor" + "  " + title , url = url , thumbnail = params . get ( "thumbnail" ) , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )
def retro_series_generos (params): 
 url = params . get ( "url" ) 
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 bloque =  plugintools.find_single_match(url,'<a>Genero</a>(.*?)<li id="menu-item-7024"')
 matches =  re.findall(r'(?s)<a href="(.*?)">(.*?)<', bloque, re.DOTALL)
 for url , title in matches:
  plugintools . add_item ( action = "retro_series" , title = title , url = url , thumbnail = "https://seriesretro.com/wp-content/uploads/2020/06/5ed8d22a4ac42_originalcursi1.png" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
def retro_series_search (params): 
 url = params . get ( "url" ) + keyboard_input("", "Buscar:", False).replace(" ", "+")
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)class="TPost C".*?href="(.+?)".*?data-src="(.+?)".*?Title">(.+?)<.*?Year">(.+?)<', url, re.DOTALL)
 for url,thumb, title, year in matches:
  plugintools . add_item ( action = "retro_series1" , title = title + "  " + year , url = url , thumbnail = thumb , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
def vernovelasonline (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)data-src="(.+?)".*?title"><a href="(.+?)".*?>(.+?)<', url, re.DOTALL)
 for thumb, url, title in matches:
  plugintools . add_item ( action = "vernovelasonline1" , title = title  , url = url , thumbnail = thumb , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
def vernovelasonline1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)<a href="(\/.*?)".*?>(.+?)<', url, re.DOTALL)
 for url, title in matches:
  plugintools . add_item ( action = "vernovelasonline2" , title = title  , url = "https://vernovelasonline.xyz" + url , thumbnail = params . get ( "thumbnail" ) , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
def vernovelasonline2 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)<IFRAME SRC="(.*?)"', url, re.DOTALL)
 for url in matches:
  plugintools . add_item ( action = "resolvers" , title = "Ver:" + "  " + params . get ( "title" )   , url = url , thumbnail = params . get ( "thumbnail" ) , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )
def cortosdemetrajewebseries (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)wpb_wrapper vc_figure.*?href=(.*?video-series/(.+?))\s.*?height=120 src=(.*?.jpg)', url, re.DOTALL)
 for url, title, src in matches:
  plugintools . add_item ( action = "cortosdemetrajewebseries1" , title = title  , url =  url , thumbnail = src , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
def cortosdemetrajewebseries1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)height=293 src=(http.*?.jpg).*?<h3><a.*?href=(https://cortosdemetraje.com/(.+?)\/)\s.*?title="(.+?)"', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)rel=canonical.*?rel=next href=(.+?)\s')
 
 for src, url, title, til in matches:
  plugintools . add_item ( action = "cortosdemetrajecine_1" , title = title  , url =  url , thumbnail = src , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
 plugintools . add_item ( action = "cortosdemetrajewebseries1" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def seriesflix (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)<article class="TPost B">\s.*?href="(.*?)".*?data-src="(.*?)".*?Y.*?>(.*?)<.*?Title">(.*?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'rel="next" href="(.+?)"')
 for url,thumb,year,title in matches:
  plugintools . add_item ( action = "seriesflix1" , title = title+"  "+year+" ", url = url , thumbnail =thumb , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
 plugintools . add_item ( action = "seriesflix" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def seriesflix1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)<section class="SeasonBx AACrdn">.*?href="(.*?)">(.*?) .*?>(.*?)<', url, re.DOTALL)
 for url,temp,numb in matches:
  plugintools . add_item ( action = "seriesflix2" , title = temp+"   "+numb+" ", url = url , thumbnail = "" , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
def seriesflix2 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)<tr class="Viewed">.*?href="(https.*?epi.*?(\dx\d{1,2})/)".*?data-src="(.*?)"', url, re.DOTALL)
 for url,epi,thumb in matches:
  plugintools . add_item ( action = "seriesflix3" , title = epi, url = url , thumbnail ='https:'+ thumb , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
def seriesflix3 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches = plugintools.find_multiple_matches(url,'(?s)data-key=".*?" data-id=".*?".*?-language">...*?<.*?-dns">.*?<.*?equalizer">.*?<')
 for match in matches:
    data_key = plugintools.find_single_match(match, 'data-key="(.+?)"')
    data_id = plugintools.find_single_match(match, ' data-id="(.+?)".*?')
    lang = plugintools.find_single_match(match, '-language">..(.*?)</p>')
    qlty = plugintools.find_single_match(match, '-equalizer">(.*?)</p>')
    servidor = plugintools.find_single_match(match, '-dns">(.*?)</p>')
    url = 'https://seriesflix.to/' + '?trembed=%s&trid=%s&trtype=2' % (data_key, data_id)
 plugintools . add_item ( action = "seriesflix4" , title =servidor+"   "+qlty+" ", url = url , thumbnail = '' , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder =True  )
def seriesflix4 (params): 
 thumbnail = params.get("thumbnail")
 url = params.get("url")
 request_headers=[]
 request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"])
 body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
 url = body.strip()
 fid = plugintools.find_single_match(url, "h=([^&]+)")
 url='https://seriesflix.to'+plugintools.find_single_match(url,'<iframe.*?src="(.*?)"').replace('index.php', '').split('?h=')[0] + 'r.php'       
 plugintools.add_item(action = "index" , title =url,page='h='+fid,  folder=True )
 url = params.get("url")
def index(url):
 import re, requests
 url = url
 headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:72.0) Gecko/20100101 Firefox/72.0', 'Referer': url, 'Accept' : '*/*', 'Accept-Language' : 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3', 'X-Requested-With' : 'XMLHttpRequest', 'Pragma' : 'no-cache', 'Cache-Control' : 'no-cache'}
 payload = {'h':'aFMxQjNOOEJPQmN3RG9iSm5zenZjbjczOUsyWERIOFRidDd1VWRkNEtJdk9TWHl0ekdvVEh6Z0luTUJBN2JBQQ'}
 s = requests.Session()
 logueo = s.post(url, headers=headers, data=payload).text
 return logueo
 url=  index(url)
 plugintools.add_item(action = "" , title =payload,folder=True )
def divxtotal_Series (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)tr>.*?href="(.+?)".*?title="(.+?)".*?src="(.+?)"', url, re.DOTALL)
 next = plugintools.find_single_match(url,'rel="next" href="(.+?)"')
 
 for url, title, src in matches:
  plugintools . add_item ( action = "divxtotal_Series1" , title = title, url = url , thumbnail = src , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )
 plugintools . add_item ( action = "divxtotal_Series" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def divxtotal_Series1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)class="titulotemporada".*?title="(.+?)"|<a class="linktorrent" .*?href="(.+?)".*?title="(.+?)"', url, re.DOTALL)
 
 for temp, url, title in matches:
  plugintools . add_item ( action = "elementum" , title = temp + title, url = url , thumbnail = params . get ( "thumbnail" ) , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )


#Anime
  
def anime_fenix_fin (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)<a href="(.*?)" title="(.*?)".*?src="(.+?)"', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)agination-link is-current.*?class="pagination-link" href="(.+?)"')
 for url, title, thumb in matches:
  plugintools . add_item ( action = "anime_fenix_fin_1" , title = title , url = url , thumbnail = thumb , folder = True )  
 plugintools . add_item ( action = "anime_fenix_fin" , title = "PAGINA SIGUIENTE", url = "https://www.animefenix.com/animes" + next, thumbnail = "https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/AveFenix.png", fanart="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/AveFenix.png",  folder=True )
def anime_fenix_fin_1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)circle d-inline.*?href="(.+?)">(.+?)<.*?span(.+?)<', url, re.DOTALL)
 for url, title, cap in matches:
  plugintools . add_item ( action = "anime_fenix_fin_2" , title = title + cap , url = url , thumbnail = params . get ( "thumbnail" ), fanart="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/AveFenix.png", folder = True )  
def anime_fenix_fin_2 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)tabsArray.*?src=\'(.+?(ok.ru|fembed|mp4upload|yourupload).+?)\'', url, re.DOTALL)
 log(matches)
 for url, title in matches:
  plugintools . add_item ( action = "resolve_resolveurl" , title = title , url = url , thumbnail = params . get ( "thumbnail" ), fanart="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/AveFenix.png", folder = False , isPlayable = True)  
def anime_fenix_emi (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)<a href="(.*?)" title="(.*?)".*?src="(.+?)"', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)agination-link is-current.*?class="pagination-link" href="(.+?)"')
 for url, title, thumb in matches:
  plugintools . add_item ( action = "anime_fenix_fin_1" , title = title , url = url , thumbnail = thumb , fanart="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/AveFenix.png", folder = True )  
 plugintools . add_item ( action = "anime_fenix_fin" , title = "PAGINA SIGUIENTE", url = "https://www.animefenix.com/animes" + next, thumbnail = "https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/AveFenix.png", fanart="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/AveFenix.png",  folder=True )
def anime_fenix_pelic (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)<a href="(.*?)" title="(.*?)".*?src="(.+?)"', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)agination-link is-current.*?class="pagination-link" href="(.+?)"')
 for url, title, thumb in matches:
  plugintools . add_item ( action = "anime_fenix_fin_1" , title = title , url = url , thumbnail = thumb , fanart="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/AveFenix.png", folder = True )  
 plugintools . add_item ( action = "anime_fenix_fin" , title = "PAGINA SIGUIENTE", url = "https://www.animefenix.com/animes" + next, thumbnail = "https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/AveFenix.png", fanart="https://raw.githubusercontent.com/daqueenqueen666/dwserv/main/AveFenix.png", folder=True )
def animeyt_ult (params): 
 url = params . get ( "url" )
 url = requests.get(url).text 
 matches =  re.findall(r'(?s)img class="img-fluid" src="(.*?)".*?class="video-title.*?href="(.+?)">(.+?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)page-item active.*?href="(.+?)"')
 for thumb, url, title in matches:
  plugintools . add_item ( action = "animeyt_ult_1" , title = title , url = url , thumbnail = thumb , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )  
 plugintools . add_item ( action = "animeyt_ult" , title = "PAGINA SIGUIENTE", url = next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def animeyt_ult_1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)class="list-group-item"><a href="(.+?(capitulo.*?))"', url, re.DOTALL)

 for url, title in matches:
  plugintools . add_item ( action = "animeyt_ult_2" , title = title , url = url , thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )  
def animeyt_ult_2 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)<iframe src="(.*?(cinemaupload).+?)".*?430', url, re.DOTALL)

 for url, title in matches:
  plugintools . add_item ( action = "resolvers" , title = title , url = url , thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )  
def animeyt_pop (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)img class="img-fluid" src="(.*?)".*?class="video-title.*?href="(.+?)">(.+?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)page-item active.*?href="(.+?)"')
 for thumb, url, title in matches:
  plugintools . add_item ( action = "animeyt_ult_1" , title = title , url = url , thumbnail = thumb , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )  
 plugintools . add_item ( action = "animeyt_pop" , title = "PAGINA SIGUIENTE", url = next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def anime_flv_episodios (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)<a href="(/ver.*?)".*?src="(.+?)".*?Capi">(.*?)<.*?Title">(.+?)<', url, re.DOTALL)
 for url, src, title, cap in matches:
  plugintools . add_item ( action = "anime_flv_episodios1" , title = title + "  " + cap , url = "https://www3.animeflv.net/" + url , thumbnail ="https://www3.animeflv.net/" + src, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )  
def anime_flv_episodios1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)title":"Okru".*?code":"(.*?)"', url, re.DOTALL)
 for url in matches:
  plugintools . add_item ( action = "resolve_resolveurl" , title =  "Ver:  " + params . get ( "title" ),  url =  url.replace('\/','/'), thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )   
def anime_flv_epeciales (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)Anime alt B".*?href="(.*?\/.*?\/(.*?))".*?src="(.+?)"\salt="(.+?)"', url, re.DOTALL)
 for url1, url2, src, title in matches:
  plugintools . add_item ( action = "anime_flv_epeciales1" , title =  title,  url = "https://www3.animeflv.net" + url1, thumbnail = src, extra = url2, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )   
def anime_flv_epeciales1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)\[(\d.*?),\d', url, re.DOTALL)
 for epi in matches:
  plugintools . add_item ( action = "anime_flv_episodios2" , title = params . get ( "title" ) + "  " + "Capitulo:  "  + epi  ,  url = "https://www3.animeflv.net/ver/" + params . get ( "extra" ) + "-" + epi, extra = epi, thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True  )   
def anime_flv_episodios2 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)title":"Okru".*?code":"(.*?)"', url, re.DOTALL)
 for url in matches:
  plugintools . add_item ( action = "resolve_resolveurl" , title =  "Ver Capitulo:  " + params . get ( "extra" ),  url =  url.replace('\/','/'), thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )   
def anime_flv_pag (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)Anime alt B".*?href="(.*?\/.*?\/(.*?))".*?src="(.+?)"\salt="(.+?)"', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)\d\d\d</a></li><li><a href="(.+?)" rel="next')
 for url1, url2, src, title in matches:
  plugintools . add_item ( action = "anime_flv_epeciales1" , title =  title,  url = "https://www3.animeflv.net" + url1, thumbnail = src, extra = url2, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )   
 plugintools . add_item ( action = "anime_flv_pag" , title = "PAGINA SIGUIENTE", url = "https://www3.animeflv.net" + next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def anime_flv_genero (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)value="(.+?)">(.+?)<', url, re.DOTALL)
 for url, title in matches:
  plugintools . add_item ( action = "anime_flv_peli" , title = title , url = "https://www3.animeflv.net/browse?genre[]=" + url + "&order=default"  , thumbnail ="https://raw.githubusercontent.com/iberikakod/wizard/master/Anime%20FLV.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )  
def anime_flv_anios (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)value="(.+?)">(.+?)<', url, re.DOTALL)
 for url, title in matches:
  plugintools . add_item ( action = "anime_flv_peli" , title = title , url = "https://www3.animeflv.net/browse?year[]=" + url + "&order=default"  , thumbnail ="https://raw.githubusercontent.com/iberikakod/wizard/master/Anime%20FLV.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )  
def anime_flv_peliserie (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)Anime alt B".*?href="(.*?\/.*?\/(.*?))".*?src="(.+?)"\salt="(.+?)".*?span class=.*?>(.+?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)\d\d\d</a></li><li><a href="(.+?)" rel="next')
 for url1, url2, src, title, clase in matches:
  plugintools . add_item ( action = "anime_flv_epeciales1" , title =  title + "  " + "[COLOR yellow]" + clase + "[/COLOR]" ,  url = "https://www3.animeflv.net" + url1, thumbnail = src, extra = url2, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )   
 plugintools . add_item ( action = "anime_flv_peliserie" , title = "PAGINA SIGUIENTE", url = "https://www3.animeflv.net" + next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def anime_flv_peli (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)Anime alt B".*?href="(.*?\/.*?\/(.*?))".*?src="(.+?)"\salt="(.+?)".*?span class=.*?>(.+?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)\d\d</a></li><li><a href="(.+?)" rel="next')
 for url1, url2, src, title, clase in matches:
  plugintools . add_item ( action = "anime_flv_epeciales1" , title =  title + "  " + "[COLOR yellow]" + clase + "[/COLOR]" ,  url = "https://www3.animeflv.net" + url1, thumbnail = src, extra = url2, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )   
 plugintools . add_item ( action = "anime_flv_peli" , title = "PAGINA SIGUIENTE", url = "https://www3.animeflv.net" + next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def anime_flv_search (params): 
 url = params . get ( "url" ) + keyboard_input("", "Buscar:", False).replace(" ", "+")
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)Anime alt B".*?href="(.*?\/.*?\/(.*?))".*?src="(.+?)"\salt="(.+?)".*?span class=.*?>(.+?)<', url, re.DOTALL)
 for url1, url2, src, title, clase in matches:
  plugintools . add_item ( action = "anime_flv_epeciales1" , title =  title + "  " + "[COLOR yellow]" + clase + "[/COLOR]" ,  url = "https://www3.animeflv.net" + url1, thumbnail = src, extra = url2, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )   
def anime_JL_peliserie (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)Anime alt B.*?href=\'(.+?)\'.*?src=\'(.+?)\'.*?alt=\'(.+?)\'.*?color.*?>(.+?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)class="page-link">.*?</li>.*?<a class="page-link" href="(.+?)"')
 for url, src, title, clase in matches:
  plugintools . add_item ( action = "anime_JL_peliserie1" , title =  title + "  " + "[COLOR yellow]" + clase + "[/COLOR]" ,  url = url, thumbnail = "https://www.anime-jl.net" + src, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )   
 plugintools . add_item ( action = "anime_JL_peliserie" , title = "Siguiente", url = next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def anime_JL_peliserie1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)\[.*?,"(episodio.*?)"', url, re.DOTALL)
 for url in matches:
  plugintools . add_item ( action = "anime_JL_peliserie2" , title = "Ver:  " + url.replace("-", " ") , url = params . get ( "url" ) + "/" + url  , thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )  
def anime_JL_peliserie2 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)video.*?iframe src="(https://(.+?)\/.*?)"', url, re.DOTALL)
 for url, server in matches:
  plugintools . add_item ( action = "resolvers" , title = "Servidor  " + server , url = url  , thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True )  
def anime_JL_peliseriepeli (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)Anime alt B.*?href=\'(.+?)\'.*?src=\'(.+?)\'.*?alt=\'(.+?)\'.*?color.*?>(.+?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)class="page-link">.*?</li>.*?<a class="page-link" href="(.+?)"')
 for url, src, title, clase in matches:
  plugintools . add_item ( action = "anime_JL_peliseriepeli1" , title =  title + "  " + "[COLOR yellow]" + clase + "[/COLOR]" ,  url = url, thumbnail = "https://www.anime-jl.net" + src, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )   
 plugintools . add_item ( action = "anime_JL_peliseriepeli" , title = "Siguiente", url = next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def anime_JL_peliseriepeli1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)\[\d,"(.+?)"', url, re.DOTALL)
 for url in matches:
  plugintools . add_item ( action = "anime_JL_peliserie2" , title = "Ver en:  " + url , url = params . get ( "url" ) + "/" + url  , thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )  
def anime_JL_search (params): 
 url = params . get ( "url" ) + keyboard_input("", "Buscar:", False).replace(" ", "+")
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)Anime alt B.*?href=\'(.+?)\'.*?src=\'(.+?)\'.*?alt=\'(.+?)\'.*?color.*?>(.+?)<', url, re.DOTALL)
 for url, src, title, clase in matches:
  plugintools . add_item ( action = "anime_JL_peliserie1" , title =  title + "  " + "[COLOR yellow]" + clase + "[/COLOR]" ,  url = url, thumbnail = "https://www.anime-jl.net" + src, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )   


#Infantil
 
def audiocuentosclasicos (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)itemprop="headline".*?href=(.+?)\s.*?bookmark>(.+?)<.*?srcset="(.+?.jpg)', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)rel=next href=(.+?)\s')
 for url, title, thumb in matches:
  plugintools . add_item ( action = "audiocuentosfinal" , title = title, thumbnail = thumb , url = url  , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
 plugintools . add_item ( action = "audiocuentosclasicos" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def audiocuentosdisney (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)itemprop="headline".*?href=(.+?)\s.*?bookmark>(.+?)<.*?srcset="(.+?.jpg)', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)rel=next href=(.+?)\s')
 for url, title, thumb in matches:
  plugintools . add_item ( action = "audiocuentosfinal" , title = title, thumbnail = thumb , url = url  , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
 plugintools . add_item ( action = "audiocuentosdisney" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def audiocuentoshalloween (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)itemprop="headline".*?href=(.+?)\s.*?bookmark>(.+?)<.*?srcset="(.+?.jpg)', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)rel=next href=(.+?)\s')
 for url, title, thumb in matches:
  plugintools . add_item ( action = "audiocuentosfinal" , title = title, thumbnail = thumb , url = url , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
 plugintools . add_item ( action = "audiocuentoshalloween" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def audiocuentoshalloween (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)itemprop="headline".*?href=(.+?)\s.*?bookmark>(.+?)<.*?srcset="(.+?.jpg)', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)rel=next href=(.+?)\s')
 for url, title, thumb in matches:
  plugintools . add_item ( action = "audiocuentosfinal" , title = title, thumbnail = thumb , url = url  , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
 plugintools . add_item ( action = "audiocuentoshalloween" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def audiocuentosnavidad (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)itemprop="headline".*?href=(.+?)\s.*?bookmark>(.+?)<.*?srcset="(.+?.jpg)', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)rel=next href=(.+?)\s')
 for url, title, thumb in matches:
  plugintools . add_item ( action = "audiocuentosfinal" , title = title, thumbnail = thumb , url = url  , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
 plugintools . add_item ( action = "audiocuentoshalloween" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def audiocuentosfinal (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)(mp3)>(.+?)<', url, re.DOTALL)
 for title, url in matches:
  plugintools . add_item ( action = "resolve_without_resolveurl" , title = title , url = url , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False, isPlayable = True )  
def Infantil_playlist (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)title.*?=.*?"(.+?)".*?thumb.*?=.*?"(.*?)".*?url.*?=.*?"(.+?)"', url, re.DOTALL)
 for title, thumb, url in matches:
  plugintools . add_item ( action = "infantil_playlist_Youtube" , title = title , url = url, thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )   
def Canales_Infantiles (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)"(.+?)","(.+?)","(.+?)"', url, re.DOTALL)
 for url, title, thumb in matches:
  plugintools . add_item ( action = "daqueen_tv_latina_1" , title = title , url = url, thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )   
def series_infantiles (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)class=poster><img.*?src=(.+?)\s.*?class=data><h3><a.*?href=(.+?)\s>(.+?)<.*?span>(\d.*?)<.*?class=imdb>(.+?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)rel=next href=(.*?)\s')
 for src, href, title, year, point in matches:
  plugintools . add_item ( action = "series_infantiles_clasicas1" , title =  title + "  Año  " + "[COLOR yellow]" + year + "[/COLOR]" + "   Puntuacion  " + "[COLOR lime]" + point + "[/COLOR]",  url = href, thumbnail = src, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )   
 plugintools . add_item ( action = "series_infantiles" , title = "PAGINA SIGUIENTE", url = next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def series_infantiles_clasicas1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)class=title>(Temporada.*?)<|class=eps><div.*?href=(.+?)\s.*?class=numerando>(.+?)<', url, re.DOTALL)
 for temporada, url, title in matches:
  plugintools . add_item ( action = "series_infantiles_clasicas2" , title = "[COLOR yellow]" + temporada + "[/COLOR]" + title , url = url, thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )   
def series_infantiles_clasicas2 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)data-sv=(OpRu).*?data-user="(.+?)"', url, re.DOTALL)
 for url, url2 in matches:
  plugintools . add_item ( action = "series_infantiles_clasicas3" , title = "Servidor:  OK.ru" , url = "https://sv.danimados.com/gilberto.php?id=" + url2 + "&sv=" + url, thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )   
def series_infantiles_clasicas3 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)<iframe data-source="(.+?)"', url, re.DOTALL)
 for url in matches:
  message_bytes = base64.b64decode(url)
  finalurl = message_bytes.decode('utf-8')
  plugintools . add_item ( action = "resolve_resolveurl" , title = "Ver Capitulo" , url = finalurl, thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False, isPlayable = True )   
def peliculas_infantiles (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)class=poster><img.*?src=(.+?)\s.*?class=data><h3><a.*?href=(.+?)\s>.*?h4>(.+?)<.*?span>(.+?)<.*?span>(\d.*?)<', url, re.DOTALL)
 next = plugintools.find_single_match(url,'(?s)rel=next href=(.*?)\s')
 for src, href, title, year, min in matches:
  plugintools . add_item ( action = "peliculas_infantiles_clasicas2" , title =  title,  url = href, thumbnail = src, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )   
 plugintools . add_item ( action = "peliculas_infantiles" , title = "PAGINA SIGUIENTE", url = next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def peliculas_infantiles_clasicas2 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)data-sv=(LoadUQ|UploadYour).*?data-user="(.+?)"', url, re.DOTALL)
 for url, url2 in matches:
  plugintools . add_item ( action = "peliculas_infantiles_clasicas3" , title = "Servidor:  " + url , url = "https://sv.danimados.com/gilberto.php?id=" + url2 + "&sv=" + url, thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )   
def peliculas_infantiles_clasicas3 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)<iframe data-source="(.+?)"', url, re.DOTALL)
 for url in matches:
  message_bytes = base64.b64decode(url)
  finalurl = message_bytes.decode('utf-8')
  plugintools . add_item ( action = "resolvers" , title = "Ver Pelicula" , url = finalurl, thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False, isPlayable = True )   
         
  
#Documentales

def documaniatvseries (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)clip.*?src="(.+?)".*?class="vertical-align".*?h3.*?href="(.+?)".*?white.*?>(.+?)<', url, re.DOTALL)
 log(matches)
 for thumb, url, title in matches:
  plugintools . add_item ( action = "documaniatv1" , title = title, url = url, thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
def documaniatv1 (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)fa-clock-o.*?href="(.+?)".*?title="(.+?)".*?data-echo="(.+?)"', url, re.DOTALL)
 log(matches)
 for url, title, thumb in matches:
  plugintools . add_item ( action = "documaniatv2" , title = title, url = url, thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
def documaniatv2 (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)name":"(.+?)".*?contentUrl":"(.+?)"', url, re.DOTALL)
 log(matches)
 for title, url in matches:
  plugintools . add_item ( action = "resolve_without_resolveurl" , title = title, url = url, thumbnail = params . get ( "thumbnail" ), fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False, isPlayable = True )  
def documaniatv_top (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)data-echo="(.*?)".*?href="(.+?)".*?title="(.+?)"', url, re.DOTALL)
 log(matches)
 for thumb, url, title in matches:
  plugintools . add_item ( action = "documaniatv2" , title = title, url = url, thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True ) 
def documaniatv_gene (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)category">.*?<a href="(.*?)"\stitle="(.*?)".*?src="(.*?)"', url, re.DOTALL)
 log(matches)
 for url, title, thumb in matches:
  plugintools . add_item ( action = "documaniatv_gene_1" , title = title, url = url, thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True ) 
def documaniatv_gene_1 (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)fa-clock-o.*?href="(.+?)".*?title="(.+?)".*?data-echo="(.+?)"', url, re.DOTALL)
 next = plugintools.find_single_match(url,'<link rel="next" href="(.+?)"')
 for url, title, thumb in matches:
  plugintools . add_item ( action = "documaniatv2" , title = title, url = url, thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )   
 plugintools . add_item ( action = "documaniatv_gene_1" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )
def documentales_onlinedocus (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)<h2><a href="(https://www.documentales-online.com.*?)">(.*?)<.*?src="(.*?)"', url, re.DOTALL)
 next = plugintools.find_single_match(url,'rel="next" href="(.+?)"')
 for url, title, thumb in matches:
  plugintools . add_item ( action = "documentales_online_1" , title = title, thumbnail = thumb , url = url , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
 plugintools . add_item ( action = "documentales_onlinedocus" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True ) 
def documentales_online_1 (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)<title>(.*?)<.*?src="(https://www.youtube.com/embed/(.+?))\?', url, re.DOTALL)
 for title, thumb, url  in matches:  
  plugintools . add_item ( action = "resolve_resolveurl_youtube" , title = title , url = url , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False, isPlayable = True )
def documentales_online_cat (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)<a href="(/categorias/.*?)">(.*?)<', url, re.DOTALL)
 for url, title  in matches:  
  plugintools . add_item ( action = "documentales_online_cat_1" , title = title , url = url , thumbnail = "https://www.documentales-online.com/img/documentales-online.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )  
def documentales_online_cat_1 (params): 
 url = (  ( "https://www.documentales-online.com" + params . get("url") ) )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)<h2><a href="(https://www.documentales-online.com.*?)">(.*?)<.*?src="(.*?)"', url, re.DOTALL)
 next = plugintools.find_single_match(url,'rel="next" href="(.+?)"')
 for url, title, thumb in matches:
  plugintools . add_item ( action = "documentales_online_1" , title = title, thumbnail = thumb , url = url , fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
 plugintools . add_item ( action = "documentales_online_cat_1" , title = "PAGINA SIGUIENTE", url= next, thumbnail = "https://2.bp.blogspot.com/-q5yGYcBCQzg/Uv1E2m4c6oI/AAAAAAAAA7I/mK2JPXZh1w0/s1600/SIGUIENTE.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder=True )  
def documentales_online_top (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)href="(.+?)"\stitle="(.+?)".*?</a>(.+?)<', url, re.DOTALL)
 for url, title, pun  in matches:  
  plugintools . add_item ( action = "documentales_online_1" , title = title + pun , url = url , thumbnail = "https://www.documentales-online.com/img/documentales-online.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )    
def planetdoc_completos (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)<a\shref="(.*?)".*?image:url.(.*?).".*?class="h2">(.*?)<', url, re.DOTALL)
 for url, thumb, title  in matches:  
  plugintools . add_item ( action = "planetdoc_completos_1" , title = title , url = url , thumbnail = "http://planetdoc.tv/" + thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )  
def planetdoc_completos_1 (params): 
 url = (  ( "http://planetdoc.tv/" + params . get("url") ) )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)link.*?<title>(.+?)</title>.*?<iframe class="embed.*?src="//www.youtube.com/embed/(.+?)\?', url, re.DOTALL)
 for title, url  in matches:  
  plugintools . add_item ( action = "resolve_resolveurl_youtube" , title = title , url = url , thumbnail = "http://planetdoc.tv/img20105850-1432637081espaaol.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False, isPlayable = True )   
def planetdoc_expres (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)<a\shref="(.*?)".*?image:url.(.*?).".*?class="h2">(.*?)<', url, re.DOTALL)
 for url, thumb, title  in matches:  
  plugintools . add_item ( action = "planetdoc_completos_1" , title = title , url = url , thumbnail = "http://planetdoc.tv/" + thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True ) 
def planetdoc_generos (params): 
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)<li><a href="(.*?)".*?center">(.*?)<', url, re.DOTALL)
 for url, title  in matches:  
  plugintools . add_item ( action = "planetdoc_generos_1" , title = title , url = url , thumbnail = "http://planetdoc.tv/img20105850-1432637081espaaol.png", fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )
def planetdoc_generos_1 (params): 
 url = (  ( "http://planetdoc.tv/" + params . get("url") ) )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)<a\shref="(.*?)".*?image:url.(.*?).".*?class="h2">(.*?)<', url, re.DOTALL)
 for url, thumb, title  in matches:  
  plugintools . add_item ( action = "planetdoc_completos_1" , title = title , url = url , thumbnail = "http://planetdoc.tv/" + thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = True )  


#Youtube

def trendig_you (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)height":138},{"url":"(.*?)\?sqp.*?label":"(.*?)".*?"videoId":"(.*?)".*?', url, re.DOTALL)
 log(url)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "resolve_resolveurl_youtube" , title = title, url = url , thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True ) 
def GameYoutube_live (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)boxArt.*?thumbnails":\[{"url":"([^"]+).*?simpleText":"(.+?)".*?url":"(.+?)"', url, re.DOTALL)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "GameYoutube_live_1" , title = title, url = url , thumbnail = "https:" + thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif",  folder = True )
def GameYoutube_live_1 (params):
 url = (  ( "https://www.youtube.com" + params . get("url") + "/live" ) )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)height":138},{"url":"(.*?)\?sqp.*?label":"(.*?)".*?"videoId":"(.*?)".*?', url, re.DOTALL)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "resolve_resolveurl_youtube" , title = title, url = url , thumbnail = thumb, folder = False , fanart="special://home/addons/plugin.video.iberika/tenor.gif",  isPlayable = True) 
def Emisiones_en_Directo_Recientes (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)height":138},{"url":"(https://i.ytimg.*?)\?sqp.*?"text":"(.*?)".*?videoId":"(.*?)"', url, re.DOTALL)
 log(matches)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "resolve_resolveurl_youtube" , title = title, url = url , thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif",  folder = False , isPlayable = True ) 
def Proximas_en_Directo (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)height":138},{"url":"(https://i.ytimg.*?)\?sqp.*?"text":"(.*?)".*?videoId":"(.*?)"', url, re.DOTALL)
 log(matches)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "resolve_resolveurl_youtube" , title = title, url = url , thumbnail = thumb, folder = False , fanart="special://home/addons/plugin.video.iberika/tenor.gif",  isPlayable = True ) 
def Noticias_directos (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)height":138},{"url":"(https://i.ytimg.*?)\?sqp.*?"text":"(.*?)".*?videoId":"(.*?)"', url, re.DOTALL)
 log(matches)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "resolve_resolveurl_youtube" , title = title, url = url , thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True ) 
def Deportes_directos (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)height":138},{"url":"(https://i.ytimg.*?)\?sqp.*?"text":"(.*?)".*?videoId":"(.*?)"', url, re.DOTALL)
 log(matches)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "resolve_resolveurl_youtube" , title = title, url = url , thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif",  folder = False , isPlayable = True ) 
def Buscar_search (params): 
 url = params . get ( "url" ) + keyboard_input("", "Buscar:", False).replace(" ", "+")
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)height":202},{"url":"(.+?)".*?title.*?text":"(.+?)"}.*?"videoId":"(.*?)"', url, re.DOTALL)
 log(matches)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "resolve_resolveurl_youtube" , title = title, url = url , thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True ) 
def En_Directo (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)height":138},{"url":"(https://i.ytimg.*?)\?sqp.*?"text":"(.*?)".*?videoId":"(.*?)"', url, re.DOTALL)
 log(matches)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "resolve_resolveurl_youtube" , title = title, url = url , thumbnail = thumb, fanart="special://home/addons/plugin.video.iberika/tenor.gif", folder = False , isPlayable = True ) 

 
# Finales 

def channel_playlist_youtube (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'height":138.*?"(https.*?jpg)\?sqp(?s).*?text":"(.*?)"(?s).*?playlist.*?:"(.*?)".*?"height":138', url, re.DOTALL)
 log(matches)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "channel_playlist_youtube_1" , title = title, url = url , thumbnail = thumb, folder = True ) 
def channel_playlist_youtube_1 (params):
 url = (  ( "https://www.youtube.com/playlist?list=" + params . get("url") ) )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)height":138},{"url":"(.*?)\?sqp.*?label":"(.*?)".*?"videoId":"(.*?)".*?', url, re.DOTALL)
 log(matches)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "resolve_resolveurl_youtube" , title = title, url = url , thumbnail = thumb, folder = False , isPlayable = True ) 
def infantil_playlist_Youtube (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 
 matches =  re.findall(r'(?s)height":138},{"url":"(.*?)\?sqp.*?label":"(.*?)".*?"videoId":"(.*?)".*?', url, re.DOTALL)
 log(matches)
 for thumb, title, url in matches:
  plugintools . add_item ( action = "resolve_resolveurl_youtube" , title = title, url = url , thumbnail = thumb, folder = False , isPlayable = True ) 
def resolve_playlist_Youtube (params):
 url = params . get ( "url" )
 header = [ ]
 header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
 read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
 url = read_url . strip ( )
 matches =  re.findall(r'(?s)playlistPanel.*?title.*?simpleText":"(.+?)".*?thumbnail.*?url":"(.+?)".*?videoId":"(.+?)"', url, re.DOTALL)
 log(matches)
 for title, thumb, url in matches:
  plugintools . add_item ( action = "resolve_resolveurl" , title = title, url = "https://www.youtube.com/watch?v=" + url , thumbnail = thumb, folder = False , isPlayable = True )  
def vergol (url): 
  url =url 
  finalurl = ''
  if "vergol"in url :
    origname =plugintools.find_single_match (url ,r'live\/([^\.]+)').capitalize ()
    if not origname :origname =os .path .basename (url ).split (".")[0 ].capitalize ()
    headers_dict ={}
    headers_dict ['User-Agent']='Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0'
    headers_dict ['Referer']=url 
    headers_dict ['Accept']='*/*'
    post ={'manzana66':'12345'}
    response =requests .Session ()
    read_response =response .post (url ,headers =headers_dict ,data =post )  
    matches =re .findall (r"""(?s)<script src="/player/player.js">.*?source: '(.*?)'""",read_response .content.decode("utf-8") )
    for finalurl in matches :
        finalurl =("https:{}|User-Agent={}&referer={}&origin={}".format (finalurl ,"Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0",url ,"https://vergol.com/"))
  else :
      finalurl =url 
  return finalurl  
def resolve_acestream ( params ) :
  import resolveurl
  finalurl = "plugin://program.plexus/?url={}&mode=1&name={}".format(params.get("url"),params.get("title"))
  plugintools . play_resolved_url ( finalurl )  
def resolve_resolveurl ( params ) :
  import resolveurl
  finalurl = resolveurl . resolve ( params . get ( "url" ) ) 
  plugintools . play_resolved_url ( finalurl ) 
def resolve_resolveurl_dascer ( params ) :
  import resolveurl
  finalurl = resolveurl . resolve (  ( "https:" + params . get("url") ) )
  plugintools . play_resolved_url ( finalurl )
def resolve_without_resolveurl ( params ) :
  import resolveurl
  finalurl =  ( params . get ( "url" ) ) 
  plugintools . play_resolved_url ( finalurl )  
def elementum ( params ) :
  import resolveurl
  finalurl =  (  ( "plugin://plugin.video.elementum/play?uri=" + params . get("url") ) )
  plugintools . play_resolved_url ( finalurl )
def elementum_gran ( params ) :
  import resolveurl
  finalurl =  (  ( "plugin://plugin.video.elementum/play?uri=https://grantorrent.nl/download_tt.php?u=" + params . get("url") ) )
  plugintools . play_resolved_url ( finalurl ) 
def elementum_pctfenix1 ( params ) :
  import resolveurl
  finalurl =  (  ( "plugin://plugin.video.elementum/play?uri=https:" + params . get("url") ) )
  plugintools . play_resolved_url ( finalurl )  
def elementum_estrenosgo ( params ) :
  import resolveurl
  finalurl =  (  ( "plugin://plugin.video.elementum/play?uri=https://estrenosflex.com/" + params . get("url") ) )
  plugintools . play_resolved_url ( finalurl )  
def resolve_resolveurl_youtube ( params ) :
  import resolveurl
  finalurl = resolveurl . resolve ( "https://www.youtube.com/watch?v=" + params . get ( "url" ) ) 
  plugintools . play_resolved_url ( finalurl )  
  log(finalurl)   
def resolvers ( params ):
    url = params.get("url")
    if "mixdrop" in url: 
        from resolveurl .plugins .lib import jsunpack  
        header = [ ]
        header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
        header.append ( [ "Cookie" , "sucuri_cloudproxy_uuid_ddce1ba0a=2c39acd488e40ab0a783c0d7e3db62ee" ] )
        read_url , read_header = plugintools . read_body_and_headers ( url )
        url = read_url . strip ( )
        pack = plugintools.find_single_match(url,r'(?s)Spanish.*?(eval\(function\(p,a,c,k,e,d.*?)</script>')
        unpacked = jsunpack.unpack(pack).replace('\\', '')
        finalurl = plugintools.find_single_match(unpacked,'MDCore.wurl="([^"]+)')
        plugintools . play_resolved_url ( "https:" + finalurl )      
    elif "upstream" in url:
        from resolveurl .plugins .lib import jsunpack 
        header = [ ] 
        header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] ) 
        read_url , read_header = plugintools . read_body_and_headers ( url ) 
        url = read_url . strip ( ) 
        pack = plugintools.find_single_match(url,r'(?s)(eval\(function\(p,a,c,k,e,d.*?)</script>')
        unpacked = jsunpack.unpack(pack).replace('\\', '')
        finalurl = plugintools.find_single_match(unpacked,'(?s)else.*?sources.*?file:"([^"]+)"')
        finalurl+='|Referer={}'.format(params.get("url"))
        plugintools . play_resolved_url ( finalurl ) 
    elif "gamovideo" in url:        
        from resolveurl .plugins .lib import jsunpack 
        header = [ ] 
        header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] ) 
        read_url , read_header = plugintools . read_body_and_headers ( url ) 
        url = read_url . strip ( ) 
        pack = plugintools.find_single_match(url,r'(?s)jwplayer.key=.*?(eval\(function\(p,a,c,k,e,d.*?)</script>')
        unpacked = jsunpack.unpack(pack).replace('\\', '')
        finalurl = plugintools.find_single_match(unpacked,'(?s)sources:.*?,.*?file:"([^"]+)"')
        finalurl+='|Referer={}'.format(params.get("url"))
        plugintools . play_resolved_url ( finalurl ) 
    elif "clipwatching" in url:        
        from resolveurl .plugins .lib import jsunpack 
        header = [ ] 
        header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] ) 
        read_url , read_header = plugintools . read_body_and_headers ( url ) 
        url = read_url . strip ( ) 
        url = plugintools.find_single_match(url,'(?s)sources: \[\{src: "(.+?)"')
        url+='|Referer={}'.format(params.get("url"))
        plugintools . play_resolved_url ( url )         
    elif "aparat.cam" in url:        
        from resolveurl .plugins .lib import jsunpack 
        header = [ ] 
        header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] ) 
        read_url , read_header = plugintools . read_body_and_headers ( url ) 
        url = read_url . strip ( ) 
        url = plugintools.find_single_match(url,'(?s)sources: \[\{src: "(.+?)"')
        url+='|Referer={}'.format(params.get("url"))
        plugintools . play_resolved_url ( url )      
    elif "vidtobo" in url: 
        from resolveurl .plugins .lib import jsunpack  
        header = [ ]
        header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
        read_url , read_header = plugintools . read_body_and_headers ( url )
        url = read_url . strip ( )
        pack = plugintools.find_single_match(url,r'(?s)javascript\'>(eval\(function\(p,a,c,k,e,d\).*?)</script>')
        unpacked = jsunpack.unpack(pack).replace('\\', '')
        finalurl = plugintools.find_single_match(unpacked,'(?s)file:"(.+?.mp4)"')
        plugintools . play_resolved_url ( finalurl )  
    elif "embed_cload_video" in url:        
        from resolveurl .plugins .lib import jsunpack 
        header = [ ] 
        header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] ) 
        read_url , read_header = plugintools . read_body_and_headers ( url ) 
        url = read_url . strip ( ) 
        url = plugintools.find_single_match(url,'(?s)jwplayer.*?file:\s"([^"]+)"')
        url+='|Referer={}'.format(params.get("url"))
        plugintools . play_resolved_url ( url )
    elif "uqload" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'sources: \["([^"]+)"\]')
        finalurl = regex
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url(finalurl) 
    elif "yourupload" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'(?s)jwplayerOptions.*?file: \'(.+?)\'')
        finalurl = regex
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url(finalurl)                     
    elif "jawcloud" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'(?s)height="510"><source src="(.+?)"')
        finalurl = regex
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url(finalurl)                     
    elif "v2.zplayer" in url: 
        from resolveurl .plugins .lib import jsunpack  
        header = [ ]
        header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
        read_url , read_header = plugintools . read_body_and_headers ( url )
        url = read_url . strip ( )
        pack = plugintools.find_single_match(url,r'(?s)(eval\(function\(p,a,c,k,e,d.*?)</script>')
        unpacked = jsunpack.unpack(pack).replace('\\', '')
        finalurl = plugintools.find_single_match(unpacked,'(?s)sources.*?file:"(.+?)"')
        plugintools . play_resolved_url ( finalurl )          
    elif "zplayer" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'(?s)else.*?"file": "(.+?)"')
        finalurl = regex
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url(finalurl)         
    elif "4shared" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'(?s)source src="(.+?)"')
        finalurl = regex
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url(finalurl)
    elif "assia1" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'(?s)Clappr.Player.*?source:\s\'(.+?)\'')
        finalurl = regex
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url(finalurl)          
    elif "m3u8" in url:
        plugintools . play_resolved_url ( url )
    elif "emb.apl19.me" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'(?s)pl.init(\'(.+?)\'')
        finalurl = regex
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url(finalurl)   
    elif "livestream" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'mp4","m3u8_url":"(.+?)"')
        finalurl = regex
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url(finalurl)    
    elif "pcast" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'(?s)Clappr.Player\(.*?source: "(.+?)"')
        finalurl = regex
        finalurl += "|Referer={}".format("https:" + url)
        plugintools.play_resolved_url(finalurl)         
    elif "sports24.club" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'(?s)var xurl = atob\(\'(.+?)\'')
        finalurl = regex
        finalurl = base64.b64decode(finalurlurl)
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url("https:" + finalurl)   
    elif "espn-live" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'(?s)Clappr.Player.*?source: \'(.+?)\'')
        finalurl = regex
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url(finalurl)
    elif "yandex" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'(?s)Clappr.Player.*?source: \'(.+?)\'')
        finalurl = regex
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url(finalurl)
    elif "sportstvstreams" in url:
        header =[]
        header .append (["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        read_url ,read_header =plugintools .read_body_and_headers (url,headers =header)
        content2 =read_url .strip () 
        regex = plugintools.find_single_match(content2, r'(?s)player.src\({.*?src:\s"(.+?)"')
        finalurl = regex
        finalurl += "|Referer={}".format(url)
        plugintools.play_resolved_url(finalurl)                            
def wstream1(params):    
    url = "https://sportscart.xyz/ch/scplayer-" + params.get("url")+ ".php"
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])

    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    url = body.strip().decode('utf-8')
    url = plugintools.find_single_match(url,'iframe.+?src="(.+?)"') 
    def wstram (url):
        import re, requests, resolveurl
        from resolveurl.plugins.lib import jsunpack 
        url=url
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Upgrade-Insecure-Requests": "1", "Referer":"https://sportscart.xyz/ch/scplayer-82.php"
    }
 
        marcador = requests.get(url, headers=headers, verify=False)
        r = marcador.text
        pack=re.findall("(eval\(function\(p,a,c,k,e,d.*m3u8.*)", r)[0]
        unpack=jsunpack.unpack(pack).replace('\\', '')
        return re.findall('source:"(.*?)"', unpack)[0].replace('ul.cdn946.net', '185.39.10.72')

    url=wstram(url)
    
    plugintools.play_resolved_url( url)    
def wstream2(params):    
    url = params.get("url")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])

    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    url = body.strip()
    url = plugintools.find_single_match(url,'iframe.+?src="(.+?)" width="100.*?allowfullscreen="true') 
    def wstram (url):
        import re, requests, resolveurl
        from resolveurl.plugins.lib import jsunpack 
        url=url
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Upgrade-Insecure-Requests": "1", "Referer":"https://daddylive.club/stream/stream-1.php"
    }
          
        marcador = requests.get(url, headers=headers, verify=False)
        r = marcador.text
        pack=re.findall("(eval\(function\(p,a,c,k,e,d.*m3u8.*)", r)[0]
        unpack=jsunpack.unpack(pack).replace('\\', '')
        return re.findall('source:"(.*?)"', unpack)[0].replace('ul.cdn946.net', '185.39.10.72')

    url=wstram(url)
    
    plugintools.play_resolved_url( url)  
def zonlinefin(params): 
    url = params.get("url")
    thumbnail = params.get("thumbnail")
    def dailyy(url):
        import re, requests 
 
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0', 'Referer': 'https://sportzonline.co/channels/hd/hd1.php', 'Accept' : 'application/json, text/plain, */*', 'Accept-Language' : 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3'}   
        r = requests.get(url,headers=headers, verify=False)
        contenido = r.text
        return contenido
    url=dailyy(url)
    url = 'https:'+plugintools.find_single_match(url,'iframe.+?src="(.+?)"')
    def wstram(url):
        import re, requests, resolveurl
        from resolveurl.plugins.lib import jsunpack 
        url=url
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Upgrade-Insecure-Requests": "1", "Referer":"https://sportzonline.to/channels/pt/sporttv1.php"
    }
 
        marcador = requests.get(url, headers=headers, verify=False)
        r = marcador.text
        pack=re.findall("(eval\(function\(p,a,c,k,e,d.*m3u8.*)", r)[0]
        unpack=jsunpack.unpack(pack).replace('\\', '')
        return re.findall('source:"(.*?)"', unpack)[0].replace('ul.cdn946.net', '185.39.10.72')

    url=wstram(url)
    
    plugintools.play_resolved_url( url)
def zonlinefin1(params): 
    url = params.get("url")
    thumbnail = params.get("thumbnail")
    def dailyy(url):
        import re, requests 
 
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0', 'Referer': 'http://onlyfoot.net/ch2u.html', 'Accept' : 'application/json, text/plain, */*', 'Accept-Language' : 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3'}   
        r = requests.get(url,headers=headers, verify=False)
        contenido = r.text
        return contenido
    url=dailyy(url)
    url = plugintools.find_single_match(url,'(?s)iframe src="(.+?)"')
    def wstram(url):
        import re, requests, resolveurl
        from resolveurl.plugins.lib import jsunpack 
        url=url
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Upgrade-Insecure-Requests": "1", "Referer":"http://onlyfoot.net/ch2u.html"
    }
 
        marcador = requests.get(url, headers=headers, verify=False)
        r = marcador.text
        pack=re.findall("(eval\(function\(p,a,c,k,e,d.*m3u8.*)", r)[0]
        unpack=jsunpack.unpack(pack).replace('\\', '')
        return re.findall('source:"(.*?)"', unpack)[0].replace('ul.cdn946.net', '185.39.10.72')

    url=wstram(url)
    
    plugintools.play_resolved_url( url) 
def canales_deportes_fin(params): 
    url = params.get("url")
 
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    url = body.strip()
    url1 = 'https:'+plugintools.find_single_match(url,'iframe.*? src="(//adictos.*?)"')    
    body,response_headers = plugintools.read_body_and_headers( url1, headers=request_headers)
    url = body.strip()
    url2 = 'https:'+plugintools.find_single_match(url,'<iframe src="https:(.*?)"') 
 
    if 'generator' in url2:
        def fincanal(url2):
            import re, base64, requests, resolveurl, xbmc
            from resolveurl.plugins.lib import jsunpack
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3","Upgrade-Insecure-Requests": "1", "Referer": "https://adictosalatele.com/TV/espana/canal-0-plus/"}
            url=url2
            marcador = requests.get(url, headers=headers, verify=False)
            r = marcador.text
            pack = re.findall("(eval\(function\(p,a,c,k,e,d.*)", r)[0]
            unpack=jsunpack.unpack(pack).replace('\\', '')
            base= re.findall('source.*?"(.*?)"',unpack)[0]

            return base
        url=fincanal(url2)
        import base64
        url= base64.b64decode(url)
        url= base64.b64decode(url)
 
        url= base64.b64decode(url)
 
        url= base64.b64decode(url)
        plugintools.play_resolved_url( url)    
def wstream3(params):    
    url = params.get("url")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])

    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    url = body.strip().decode('utf-8')
    url = plugintools.find_single_match(url,'iframe.+?src="(.+?)"') 
    def wstram (url):
        import re, requests, resolveurl
        from resolveurl.plugins.lib import jsunpack 
        url=url
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Upgrade-Insecure-Requests": "1", "Referer":"https://sportsworldnet.eu/update/ch13.html"
    }
 
        marcador = requests.get(url, headers=headers, verify=False)
        r = marcador.text
        pack=re.findall("(eval\(function\(p,a,c,k,e,d.*m3u8.*)", r)[0]
        unpack=jsunpack.unpack(pack).replace('\\', '')
        return re.findall('source:"(.*?)"', unpack)[0].replace('ul.cdn946.net', '185.39.10.72')

    url=wstram(url)
    
    plugintools.play_resolved_url( url)    
def resolve_F4mtester ( params ) :
  import resolveurl
  finalurl = "plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;url=" + params . get("url") + "&amp;name=" + "[COLOR deepskyblue][B]"+ params . get("title") + "[/B][/COLOR]"
  plugintools . play_resolved_url ( finalurl )  
def resolve_resolveurl12 ( params ) :
  import resolveurl
  finalurl = resolveurl . resolve ( params . get ( "url" ) ) 
  plugintools . play_resolved_url ( finalurl ) 
run()     