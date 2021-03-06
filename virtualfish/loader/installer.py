import os
import sys

import xdg.BaseDirectory

from virtualfish.loader import load

XDG_CONFIG_HOME = xdg.BaseDirectory.xdg_config_home
INSTALL_DIR = os.path.join(XDG_CONFIG_HOME, "fish", "conf.d")
INSTALL_FILE = os.path.join(INSTALL_DIR, "virtualfish-loader.fish")


def install(plugins):
    # Calculate the script to write.
    lines = load(plugins)

    # Write the script.
    os.makedirs(INSTALL_DIR, exist_ok=True)
    with open(INSTALL_FILE, "w") as f:
        f.write("\n".join(lines))


def uninstall():
    os.unlink(INSTALL_FILE)


if __name__ == "__main__" and sys.argv[1] == "uninstall":
    uninstall()
