#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, random, time, json

os.system("killall linux-wallpaperengine swaybg hyprpaper")
time.sleep(0.25)
wallpaper = []
file = open("/home/" + os.getlogin() + "/.config/WallpaperSelect/wallpaper.txt", "r")
wallpaperPre = file.read()
wallpaper = wallpaperPre.split(" ")
time.sleep(0.25)
print(wallpaper)
file.close()
os.system("linux-wallpaperengine --silent --fps 48 --screen-root HDMI-A-1 --screen-root HDMI-A-2 --screen-root HDMI-A-3 --screen-root DP-1 --screen-root DP-2 --screen-root DP-3 " + random.choice(wallpaper) + " &")
