#!/bin/bash/

cd /home/$USER/.local/share/applications/
wget https://raw.githubusercontent.com/Mato1111/WallpaperEngine-Waypaper-Selector/main/Scripts/wallpaper-select.desktop
chmod +x ~/.local/share/applications/wallpaper-select.desktop

cd /usr/bin/
sudo wget https://raw.githubusercontent.com/Mato1111/WallpaperEngine-Waypaper-Selector/main/Scripts/wallpaper-select
sudo chmod +x /usr/bin/wallpaper-select

