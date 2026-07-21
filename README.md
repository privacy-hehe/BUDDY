!THE IN DEMO IS CREATED BY AI TO RUN ON ONLINE COMPILER SO DON'T RELY ON IT, THE CODE CREATED BY ME IS IN THE BUDDY FOLDER 




<div align="center">

```text
 
 ____     _   _   ____     ____   __   __ 
U | __")uU |"|u| | |  _"\   |  _"\  \ \ / / 
 \|  _ \/ \| |\| |/| | | | /| | | |  \ V /  
  | |_) |  | |_| |U| |_| |\U| |_| |\U_|"|_u 
  |____/  <<\___/  |____/ u |____/ u  |_|   
 _|| \\_ (__) )(    |||_     |||_ .-,//|(_  
(__) (__)    (__)  (__)_)   (__)_) \_) (__)


# Buddy

Buddy is a CLI assistant I built to feel like something out of an old hacker movie — green text, a little face in the corner, that kind of thing. Under the hood it's using Google's Gemini API to actually write code, debug stuff, and answer questions, but the whole point was making it feel less like "chat with an API" and more like you've got a weird little terminal companion.

A few things it does:

Talks out loud. Buddy hooks into Windows' native SAPI voice engine through `win32com`, so instead of just dumping a wall of text, it'll pull out a one-sentence summary of what it just did and read it to you before the rest prints out. Kind of unnecessary, honestly, but it's my favorite part.

It remembers you between sessions — everything gets saved to a local `buddy_memory.json` file when you exit, so you're not starting from zero every time you open it back up.

There's also a strict/dev mode toggle (`/mode strict`) that flips the whole UI red and changes Buddy's face to `[ x_x ]`, mostly because I thought it looked cool. Normal mode is green with `[ o_o ]`.

## Setup

You'll need Python 3.8+, and — this only works on Windows right now because of the SAPI voice stuff.

```bash
python -m pip install google-genai rich requests pywin32
```

You'll also need your own Gemini API key — grab one at ai.google.dev.

## Commands

A handful of commands run locally without touching the Gemini API at all:

| Command | What it does |
|---|---|
| `/help` | Lists everything below |
| `/clear` | Clears the terminal and redraws the UI |
| `/time` | Prints your local system time |
| `/weather [city]` | Pulls a quick live report from wttr.in |
| `/mode strict` | Dev mode — red UI, `[ x_x ]` face |
| `/mode normal` | Back to hacker mode — green UI, `[ o_o ]` face |
| `/exit` or `quit` | Saves your session to `buddy_memory.json` and closes out |

Anything else you type just gets sent straight to Gemini.

## Known limitations

Voice only works in English for now — haven't touched other locales yet. And obviously the SAPI piece means this won't run on Mac or Linux without swapping out the audio backend, which is on my list eventually.

![screenshot](https://github.com/user-attachments/assets/1962c7a4-eb79-41b4-bf98-7b9e05ed7e7c)
