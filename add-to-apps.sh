#!/bin/bash/

cd /usr/bin/
sudo wget https://raw.githubusercontent.com/Mato1111/WallpaperEngine-Waypaper-Selector/main/Scripts/wallpaper-select

cd ~/.local/share/applications/
wget https://raw.githubusercontent.com/Mato1111/WallpaperEngine-Waypaper-Selector/main/Scripts/wallpaper-select.desktop

sudo chmod +x /usr/bin/wallpaper-select
sudo chmod +x /usr/share/applications/wallpaper-select.desktop
