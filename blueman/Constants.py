__all__ = ["VERSION", "PACKAGE", "WEBSITE", "ICON_PATH", "PIXMAP_PATH", "UI_PATH", "BIN_DIR"]

VERSION = "2.3.5"
PACKAGE = "blueman"
WEBSITE = "https://github.com/blueman-project/blueman"
PREFIX = "/usr/local"
BIN_DIR = "/usr/local/bin"
LOCALEDIR = "/usr/local/share/locale"
ICON_PATH = "/usr/local/share/icons"
PIXMAP_PATH = "/usr/local/share/blueman/pixmaps"
UI_PATH = "/usr/local/share/blueman/ui"
DHCP_CONFIG_FILE = "/etc/dhcp3/dhcpd.conf"
POLKIT = False
GETTEXT_PACKAGE = "blueman"
RFCOMM_WATCHER_PATH = "/usr/local/libexec/blueman-rfcomm-watcher"

import os

if 'BLUEMAN_SOURCE' in os.environ:
    _dirname = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    BIN_DIR = os.path.join(_dirname, 'apps')
    ICON_PATH = os.path.join(_dirname, 'data', 'icons')
    PIXMAP_PATH = os.path.join(_dirname, 'data', 'icons', 'pixmaps')
    UI_PATH = os.path.join(_dirname, 'data', 'ui')
