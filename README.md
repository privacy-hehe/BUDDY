<div align="center">

```text
 ____     _   _   ____     ____   __   __ 
U | __")uU |"|u| | |  _"\   |  _"\  \ \ / / 
 \|  _ \/ \| |\| |/| | | | /| | | |  \ V /  
  | |_) |  | |_| |U| |_| |\U| |_| |\U_|"|_u 
  |____/  <<\___/  |____/ u |____/ u  |_|   
 _|| \\_ (__) )(    |||_     |||_ .-,//|(_  
(__) (__)    (__)  (__)_)   (__)_) \_) (__)

# Buddy is a highly optimized Command Line Interface (CLI) AI assistant powered by Google's gemini-3.5-flash model. Designed to look and feel like a retro-hacker terminal. He writes code, debugs, fetches live data, and speaks his summaries out loud using native Windows audio drivers.

# Gemini 3.5 Brain: Powered by the official google-genai SDK for lightning-fast, highly accurate coding assistance. 

# Native OS Voice (SAPI): Utilizes win32com to plug directly into the Windows audio core. Buddy extracts a 1-sentence summary from his AI generation and reads it out loud before typing the rest of the code. 

# Persistent JSON Memory: Automatically saves your chat history to a local buddy_memory.json file when you exit, allowing him to remember previous context across sessions. 




# How to run the code for demo:

--> RUN THIS BASH CODE IN TERMINAL

   ** python -m pip install google-genai rich requests pywin32 **



Buddy includes local commands that execute without using API tokens or contacting the Google servers. Type these directly into the terminal prompt:

Command                Action
/help                Displays the list of available commands.
/clear               Wipes the terminal history clean and redraws the UI.
/time                Prints the current local system time.
/weather [city]      Pings wttr.in to fetch a live, formatted weather report for the specified city.
/mode strict         Activates Developer Mode. Turns the UI red and changes Buddy's face to [ x_x ].
/mode normal         Returns to standard Hacker Mode. Turns the UI green and changes Buddy's face to [ o_o ].
/exit (or quit)      Safely terminates the script, compiles your session data, and saves it to buddy_memory.json.



Requirements:-
--> Python 3.8 or higher.
--> A Windows Operating System (required for the Native SAPI audio engine).
--> A valid Google Gemini API Key.


<img width="437" height="390" alt="Screenshot 2026-07-20 223231" src="https://github.com/user-attachments/assets/1962c7a4-eb79-41b4-bf98-7b9e05ed7e7c" />
