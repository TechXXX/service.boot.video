import xbmc, xbmcaddon

ADDON = xbmcaddon.Addon()
if __name__ == '__main__':

    intDelay = int(ADDON.getSetting(id='delay')) * 1000
    videoLocation = ADDON.getSetting(id='location')
    xbmc.sleep(intDelay)
    xbmc.executebuiltin("PlayMedia("+videoLocation+")")
