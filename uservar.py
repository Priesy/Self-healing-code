#@@@@@@@coding: latin-1@@@@@@@
#                                +-+-+-+-+-+-+
#                                |P|R|I|E|S|Y|
#                                +-+-+-+-+-+-+
import xbmcaddon
import os

#########################################################
#         Global Variables - DON'T EDIT!!!              #
#########################################################
ADDON_ID = xbmcaddon.Addon().getAddonInfo('id')
PATH = xbmcaddon.Addon().getAddonInfo('path')
ART = os.path.join(PATH, 'resources', 'media')

#########################################################

#########################################################
#        User Edit Variables                            #
#########################################################
ADDONTITLE = '[B][COLOR lime]Priesy Wizard[/COLOR]'
BUILDERNAME = 'PRIESY 19 Wizard'
EXCLUDES = [ADDON_ID, 'repository.priesy']
# Text File with build info in it.
BUILDFILE = 'https://xzotiks.com/TeXTtExt/build19.php'
# How often you would like it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK = 0
# Text File with apk info in it.  Leave as 'http://' to ignore
APKFILE = 'https://raw.githubusercontent.com/techecoyote/LooNaticsAsylum/master/text/wizard/apks.txt'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE = 'Loonatics / MadHouse Family YouTube'
YOUTUBEFILE = 'https://raw.githubusercontent.com/techecoyote/LooNaticsAsylum/master/text/wizard/youtube.txt'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE = 'https://raw.githubusercontent.com/techecoyote/LooNaticsAsylum/master/text/wizard/addons.txt'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE = 'https://raw.githubusercontent.com/techecoyote/LooNaticsAsylum/master/text/wizard/advanced.txt'

#########################################################

#########################################################
#        Theming Menu Items                             #
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'https://www.yourhost.com/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS = os.path.join(ART, 'builds.png')
ICONMAINT = os.path.join(ART, 'maintenance.png')
ICONSPEED = os.path.join(ART, 'speed.png')
ICONAPK = os.path.join(ART, 'apkinstaller.png')
ICONADDONS = os.path.join(ART, 'addoninstaller.png')
ICONYOUTUBE = os.path.join(ART, 'youtube.png')
ICONSAVE = os.path.join(ART, 'savedata.png')
ICONTRAKT = os.path.join(ART, 'keeptrakt.png')
ICONREAL = os.path.join(ART, 'keepdebrid.png')
ICONLOGIN = os.path.join(ART, 'keeplogin.png')
ICONCONTACT = os.path.join(ART, 'information.png')
ICONSETTINGS = os.path.join(ART, 'settings.png')
# Hide the section separators 'Yes' or 'No'
HIDESPACERS = 'No'
# Character used in separator
# Character used in seperator <wizard.py - LINE 1261> CHANGE VALUES
#SPACER         = 'XjÇ•' #40-40-90 NO COLOR ADDED / DEFAULT THEMEIT
#SPACER         = '•  •' #40-40-154 NO COLOR ADDED / DEFAULT THEMEIT
#SPACER         = '[COLOR yellow] • [/COLOR][COLOR springgreen] • [/COLOR]' #40-40-794 COLOR ADDED
#SPACER         = '•  ' #130-130-130 NO COLOR ADDED DEFAULT THEMEIT
#SPACER         = '•·•' #40-40-161 NO COLOR ADDED DEFAULT THEMEIT
#SPACER          = '•  ' AEON NOX SILVO
SPACER          = '*'
#SPACER CHARACTERS THAT DISPLAY ÷ ≈ ° · √ ⁿ ² • ‼ ¶ § α ß Γ π Σ σ µ τ Φ Θ Ω δ ∞ φ ε

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1 = 'deepskyblue'
COLOR2 = 'blue'
# Primary menu items   / {0} is the menu item and is required
#THEME1 = u'[COLOR {color1}][I]([COLOR {color1}][B]Open[/B][/COLOR][COLOR {color2}]Wizard[COLOR {color1}])[/I][/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
THEME1 = u'[COLOR {color1}][I]([COLOR {color1}][B]A[/B][/COLOR][COLOR {color2}][B]C[/B][/COLOR][COLOR {color1}][B]M[/B][/COLOR][COLOR {color2}][B]E[/B][COLOR {color1}])[/I][/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
# Build Names          / {0} is the menu item and is required
THEME2 = u'[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR1)
# Alternate items      / {0} is the menu item and is required
THEME3 = u'[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR1)
# Current Build Header / {0} is the menu item and is required
THEME4 = u'[COLOR {color1}]Current Build:[/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
# Current Theme Header / {0} is the menu item and is required
THEME5 = u'[COLOR {color1}]Current Theme:[/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT = 'No'
# You can add \n to do line breaks
CONTACT = '\n\n\n\n[B][COLOR deepskyblue]Thank you for choosing [COLOR blue]A[COLOR deepskyblue]C[COLOR blue]M[COLOR deepskyblue]E [COLOR red]Wizard.[/B]\n\n\n[COLOR yellow]Contact me on Telegram at @Tech_E_Coyote[/COLOR]'
# Images used for the contact window.  http:// for default icon and fanart
CONTACTICON = os.path.join(ART, 'qricon.png')
CONTACTFANART = 'http://'
#########################################################

#########################################################
#        Auto Update For Those With No Repo             #
#########################################################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE = 'No'

#########################################################

#########################################################
#        Auto Install Repo If Not Installed             #
#########################################################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL = 'No'
# Addon ID for the repository
REPOID = 'repository.loonaticsasylum'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML = 'https://raw.githubusercontent.com/techecoyote/LooNaticsAsylum/master/zips/addons.xml'
# Url to folder zip is located in
REPOZIPURL = 'https://raw.githubusercontent.com/techecoyote/LooNaticsAsylum/master/zips/'
#########################################################

#########################################################
#        Notification Window                            #
#########################################################
# Enable Notification screen Yes or No
ENABLE = 'Yes'
# Url to notification file
NOTIFICATION = 'https://raw.githubusercontent.com/techecoyote/LooNaticsAsylum/master/text/wizard/notify.txt'
# Use either 'Text' or 'Image'
HEADERTYPE = 'Text'
# Font size of header
FONTHEADER = 'Font14'
HEADERMESSAGE = '[B][COLOR deepskyblue]A[/COLOR][/B][B][COLOR blue]C[/COLOR][/B][B][COLOR deepskyblue]M[/COLOR][/B][B][COLOR blue]E[/COLOR][/B] [COLOR deepskyblue]Wizard[/COLOR]'
# url to image if using Image 424x180
HEADERIMAGE = 'http://'
# Font for Notification Window
FONTSETTINGS = 'Font13'
# Background for Notification Window
BACKGROUND = 'http://'
#########################################################
