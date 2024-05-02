    
#       █████████     ███████    ███████████ █████ █████ ███████████ █████ █████       ██████████
#      ███░░░░░███  ███░░░░░███ ░█░░░░░░███ ░░███ ░░███ ░█░░░███░░░█░░███ ░░███       ░░███░░░░░█
#     ███     ░░░  ███     ░░███░     ███░   ░░███ ███  ░   ░███  ░  ░███  ░███        ░███  █ ░ 
#    ░███         ░███      ░███     ███      ░░█████       ░███     ░███  ░███        ░██████   
#    ░███         ░███      ░███    ███        ░░███        ░███     ░███  ░███        ░███░░█   
#    ░░███     ███░░███     ███   ████     █    ░███        ░███     ░███  ░███      █ ░███ ░   █
#     ░░█████████  ░░░███████░   ███████████    █████       █████    █████ ███████████ ██████████
#      ░░░░░░░░░     ░░░░░░░    ░░░░░░░░░░░    ░░░░░       ░░░░░    ░░░░░ ░░░░░░░░░░░ ░░░░░░░░░░ 
#
#                                                                                    - DARKKAL44
  
import os
import subprocess

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from time import sleep

mod = "mod4"
terminal = "alacritty"

audR = "audacious"
bakG = "nitrogen"
filM = "thunar"
ligD = "gtksu lightdm-gtk-greeter-settings"
logO = "archlinux-logout"
locK = "betterlockscreen -l"
menR = "rofi -show drun"
runP = "gmrun"
scrS = "xfce4-screenshooter"
texE = "code"
theM = "lxappearance"
webB = "firefox"


# █▄▀ █▀▀ █▄█ █▄▄ █ █▄░█ █▀▄ █▀
# █░█ ██▄ ░█░ █▄█ █ █░▀█ █▄▀ ▄█

keys = [

#  D E F A U L T
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),

    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),

    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    Key([mod, "shift"], "f", lazy.window.toggle_floating()),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "e", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
 
# C U S T O M

    # Volume control
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%")),

    Key([mod, "shift"], "m", lazy.spawn("amixer -q set Master toggle")),
    Key([mod, "shift"], "minus", lazy.spawn("pactl set-sink-volume 0 -5%")),
    Key([mod, "shift"], "plus", lazy.spawn("pactl set-sink-volume 0 +5%")),
    
    # Control multimedia player:
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

    Key([mod, "control"], "p", lazy.spawn("mpc toggle")),
    Key([mod, "control"], "n", lazy.spawn("mpc next")),
    Key([mod, "control"], "b", lazy.spawn("mpc prev")),
    Key([mod, "control"], "s", lazy.spawn("mpc stop")),




    # Brightness:
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # Apps
    Key([mod], "F1", lazy.spawn(webB), desc="Launch web browser"),
    Key([mod], "F2", lazy.spawn(filM), desc="Launch file manager"),
    Key([mod], "F3", lazy.spawn(texE), desc="Launch text editor"),
    Key([mod], "F4", lazy.spawn(theM), desc="Launch gtk themes settings"),
    Key([mod], "F5", lazy.spawn(bakG), desc="Launch background screen"),
    Key([mod], "F6", lazy.spawn(audR), desc="Launch audoplayer"),
    Key([mod], "F7", lazy.spawn(ligD), desc="Launch settings lightdm"),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "d", lazy.spawn(runP), desc="Launch run program window"),
    Key([mod], "l", lazy.spawn(locK), desc="Lockscreen"),
    Key([mod], "m", lazy.spawn(menR), desc="Launch menu rofi"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "x", lazy.spawn(logO), desc="Launch logout"),
    Key([mod], "h", lazy.spawn("roficlip"), desc='clipboard'),
    Key([mod], "s", lazy.spawn("flameshot gui"), desc='Screenshot'),
    Key([mod], "t", lazy.spawn("sh -c ~/.config/rofi/scripts/themes"), desc='theme_switcher'),
    Key([mod], "p", lazy.spawn("sh -c ~/.config/rofi/scripts/power"), desc='powermenu'),
    Key([], "Print", lazy.spawn(scrS), desc="Launch screenshoots"),    
]



# █▀▀ █▀█ █▀█ █░█ █▀█ █▀
# █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█



groups = [Group(f"{i+1}", label="󰏃") for i in range(6)]

for i in groups:
    keys.extend(
            [
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                    ),
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(i.name),
                    ),
                ]
            )




# L A Y O U T S



layouts = [
    layout.Columns( margin= [10,10,10,10], border_focus='#1F1D2E',
	    border_normal='#1F1D2E',
        border_width=0,
    ),

     layout.Matrix(	border_focus='#1F1D2E',
	    border_normal='#1F1D2E',
	    margin=10,
	    border_width=0,
	),

    layout.Max(	border_focus='#1F1D2E',
	    border_normal='#1F1D2E',
	    margin=10,
	    border_width=0,
    ),

    layout.Floating(	border_focus='#1F1D2E',
	    border_normal='#1F1D2E',
	    margin=10,
	    border_width=0,
	),
    # Try more layouts by unleashing below layouts
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    
     layout.MonadTall(	border_focus='#1F1D2E',
	    border_normal='#1F1D2E',
        margin=10,
	    border_width=0,
	),
    #layout.MonadWide(	border_focus='#1F1D2E',
	#    border_normal='#1F1D2E',
	#    margin=10,
	#    border_width=0,
	#),

   #  layout.RatioTile(),
     layout.Tile(	border_focus='#1F1D2E',
	    border_normal='#1F1D2E',
    ),
   #  layout.TreeTab(),
   #  layout.VerticalTile(),
   #  layout.Zoomy(),
]



widget_defaults = dict(
    font="Terminess Nerd Font Mono",
    fontsize=12,
    padding=3,
)
extension_defaults = [ widget_defaults.copy()
        ]



def search():
    qtile.cmd_spawn("rofi -show drun")

def power():
    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/power")


# █▄▄ ▄▀█ █▀█
# █▄█ █▀█ █▀▄


screens = [

    Screen(
        top=bar.Bar(
            [
            # Left side
				widget.Spacer(length=15,
                    background='#282738',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/launch_Icon.png',
                    margin=2,
                    background='#282738',
                    mouse_callbacks={"Button1":search},
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                ),

                widget.GroupBox(
                    fontsize=24,
                    borderwidth=3,
                    highlight_method='block',
                    active='#CAA9E0',
                    block_highlight_text_color="#91B1F0",
                    highlight_color='#4B427E',
                    inactive='#282738',
                    foreground='#4B427E',
                    background='#353446',
                    this_current_screen_border='#353446',
                    this_screen_border='#353446',
                    other_current_screen_border='#353446',
                    other_screen_border='#353446',
                    urgent_border='#353446',
                    rounded=True,
                    disable_drag=True,
                 ),

                widget.Spacer(
                length=8,
                background='#353446',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/1.png',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/layout.png',
                    background="#353446"
                ),

                widget.CurrentLayout(
                    background='#353446',
                    foreground='#CAA9E0',
                    fmt='{}',
                    font="Terminess Nerd Font Mono",
                    fontsize=13,
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/search.png',
                    margin=2,
                    background='#282738',
                ),

                widget.Prompt(
                    background='#282738',
                    font="Terminess Nerd Font Mono",
                    fontsize=13,
                    foreground='#CAA9E0',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/4.png',
                ),

                widget.WindowName(
                    background = '#353446',
                    format = "{name}",
                    font="Terminess Nerd Font Mono",
                    fontsize=13,
                    foreground='#CAA9E0',
                    empty_group_string = 'Desktop',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/3.png',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/Misc/ram.png',
                    background='#282738',
                ),

                widget.Spacer(
                    length=-7,
                    background='#282738',
                ),

            # Right side
                widget.Memory(
                    background='#282738',
                    format='{MemUsed: .0f}{mm}',
                    foreground='#CAA9E0',
                    font="Terminess Nerd Font Mono",
                    fontsize=13,
                    update_interval=5,
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                    background='#353446',
                ),

                #widget.Net(
                #    format=' {up}  {down} ',
                #    background='#353446',
                #    foreground='#CAA9E0',
                #    font="Terminess Nerd Font Mono",
                #    prefix='k',
                #),

                #widget.Image(
                #    filename='~/.config/qtile/Assets/2.png',
                #),

                widget.TextBox(
                    font="Font Awesome 6 Free",
                    fontsize=13,
                    text="",
                    foreground="CAA9E0",
                    background="353446",                   
                ),
                widget.CPU(
                    foreground="CAA9E0",
                    background="353446",
                    format= 'CPU {freq_current}GHz',
                    #**powerline,
                ),             

                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                ),
                widget.TextBox(
                    font="Font Awesome 6 Free",
                    fontsize=10,
                    text="",
                    foreground='CAA9E0',
                    background='353446', 
                ),

                widget.CheckUpdates(
                    foreground='CAA9E0',
                    background='353446', 
                    distro = "Arch_checkupdates",
                    colour_have_updates = "de935f",
                    no_update_string='No updates',
                    colour_no_updates='CAA9E0',
                    update_interval = 30,
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                ),

                widget.Spacer(
                    length=8,
                    background='#353446',
                ),

                widget.Volume(
                    font="Terminess Nerd Font Mono",
                    fontsize=13,
                    theme_path='~/.config/qtile/Assets/Volume/',
                    emoji=True,
                    background='#353446',
                ),

                widget.Spacer(
                    length=-5,
                    background='#353446',
                ),

                widget.Volume(
                    font="Terminess Nerd Font Mono",
                    fontsize=13,
                    background='#353446',
                    foreground='#CAA9E0',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                ),

                widget.Spacer(
                    length=8,
                    background='#353446',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/Misc/clock.png',
                    background='#353446',
                    margin_y=6,
                    margin_x=5,
                ),

                widget.Clock(
                    format='%I:%M %p',
                    background='#353446',
                    foreground='#CAA9E0',
                    font="Terminess Nerd Font Mono",
                    fontsize=13,
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                    background='#353446',
                ),

                widget.Systray(
                    background='#282738',
                    fontsize=2,
                ),

                widget.Spacer(
                    length=12,
                    background='#282738',
                ),

                widget.Image(
                    filename='~/.config/qtile/Assets/on-off.png',
                    margin=2,
                    background='#282738',
                    mouse_callbacks={"Button1":power},
                ),

                widget.Spacer(
                    length=12,
                    background='#282738',
                ),
            ],
            28,
            border_color = '#282738',
            border_width = [0,0,0,0],
            margin = [10,10,4,10],
            #margin = [15,60,6,60],

        ),
    ),

    Screen (),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
	border_focus='#1F1D2E',
	border_normal='#1F1D2E',
	border_width=0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="Nitrogen"),
        Match(wm_class="Lxappearancer"),
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

# stuff
@hook.subscribe.startup_once
def autostart():
    subprocess.call([os.path.expanduser('~/.config/qtile/autostart_once.sh')])

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "qtile"



# E O F
