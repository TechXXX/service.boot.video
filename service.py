import xbmc, xbmcaddon, xbmcgui

ADDON = xbmcaddon.Addon()
if __name__ == '__main__':

    intDelay = int(ADDON.getSetting(id='delay')) * 1000
    videoLocation = ADDON.getSetting(id='location')
    playerControl = ADDON.getSetting(id='control')
    xbmc.sleep(intDelay)

    if videoLocation.lower().endswith(('.png','.jpg','.jpeg','.gif','.bmp')):
        xbmc.executebuiltin("ShowPicture("+videoLocation+")")

    elif videoLocation.lower().endswith(('.avi','.mpg','.mp4','.mov','.flv','.wmv','mp3','m3u')):
        if ADDON.getSetting(id='control') != '':
            xbmc.executebuiltin("PlayMedia("+videoLocation+")")
            xbmc.executebuiltin( "PlayerControl("+playerControl+")" )
        else:
            xbmc.executebuiltin("PlayMedia("+videoLocation+")")

    elif videoLocation.lower().endswith('.py'):
        xbmc.executebuiltin("RunScript("+videoLocation+")")

    else:
        xbmcgui.Dialog().ok("Boot File Error", "The selected boot file is not playable", "Please select different file")
