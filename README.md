# PinkPad

![PinkPad](pics/PinkPad_front_close.jpg)

*The most black metal toy laptop out there running Arch Linux.*

PinkPad started life as a children’s learning laptop and ended up as a fully functional tiny Linux machine because apparently I looked at a pink toy computer during lockdown and thought:

> “yeah, that needs Arch Linux.”

So that’s exactly what happened.

The full (minimally) chaotic write-up, hardware details, software setup, assembly process, and mistakes live on my blog:

➡️ Full build log: https://missmolerat.com/posts/pinkpad/

---

# Gallery

<table>
<tr>
<td width="50%">
<img src="pics/PinkPad_hail_satan.jpg">
</td>
<td width="50%">
<img src="pics/PinkPad_top.jpg">
</td>
</tr>

<tr>
<td width="50%">
<img src="pics/pinkpad_intestines.jpg">
</td>
<td width="50%">
<img src="pics/pinkpad_desktop.jpg">
</td>
</tr>
</table>


# What is this?

PinkPad is a heavily modified toy laptop based on:

- Raspberry Pi Zero W (v2 with Zero 2 W, Arch Linux Arm dropped their armv6 support :( )
- 5" touchscreen display
- Rii wireless keyboard
- Way too much glue
- Pink nail polish, obviously

The original shell came from a toy learning laptop and was modified to fit actual hardware inside.
You find the STLs for this modification in this repo.

It is tiny.  
It is impractical.  
It is Black Metal.

And yes, it runs Arch, btw.

---

# Highlights

- Fully functional Arch Linux system
- WiFi
- herbstluftwm
- emacs of course
- my weird touch keyboard hack
- fully functional paw mouse (STLs + code for my "original PCB disappeared so lets 3D print one" follow)

---

# Hardware

Main components used:

- Raspberry Pi Zero W (or Zero 2, any Pi if you use the printed middle part)
- 5" LCD touch display
- Rii X1 mini wireless keyboard
- LiPo + Boost (or USB powerbank in case you fried your boost just like I did...)
- Random wires from the cable dimension

The exact parts, assembly notes, and build process are documented in the blog post above.

---

# WIP: Repository Contents

WIP! I was completely surprised this project gained attention six years after its birth, so have some patience, detailed configs and docs follow ;)

```text
.
├── pics/        # README images
├── configs/     # Useful configuration snippets
├── docs/        # Additional notes
└── misc/        # Random supporting files
