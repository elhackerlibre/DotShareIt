#!/bin/bash

xrandr --output VGA1 --primary --mode 1600x900 --pos 0x0 --rotate normal --output VIRTUAL1 --mode 1600x900 --pos 1600x0 --rotate normal --output VIRTUAL2 --off

nitrogen --restore &
exec nm-applet &
exec mpd &
exec numlockx on &
exec start-pulseaudio-x11 &
exec /usr/lib/xfce-polkit/xfce-polkit &
exec dunst -config ~/.config/dunst/dunstrc &
exec picom -b & 
source ~/.scripts/conky_start.sh &
