import os
import sys
import time
import json
import requests
import datetime
import win32com.client
import re
from google import genai
from google.genai import types
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.markdown import Markdown
from rich.prompt import Prompt

console = Console()





console.clear()
console.print("\n[bold green]Initializing Buddy Systems...[/bold green]")

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    API_KEY = Prompt.ask("[bold cyan]Enter your Gemini API Key to connect the brain[/bold cyan]")

if not API_KEY or not API_KEY.strip():
    console.print("[bold red]Fatal Error: No API key provided. Aborting boot sequence.[/bold red]")
    sys.exit()

client = genai.Client(api_key=API_KEY.strip())
MEMORY_FILE = "buddy_memory.json"

SYSTEM_INSTRUCTION = (
    "You are Buddy, an elite senior software engineer and hacker who lives in the terminal. "
    "CRITICAL RULE: You MUST begin every single response with a short, 1-sentence summary of your answer enclosed in <voice> tags. "
    "Example: <voice>I have written the Python script you requested, optimizing it for speed.</voice>\n"
    "After the <voice> tag, provide your full, detailed explanation and code. Keep explanations concise and terminal-friendly."
)

chat_history = []
if os.path.exists(MEMORY_FILE):
    try:
        with open(MEMORY_FILE, 'r') as f:
            saved_data = json.load(f)
            for msg in saved_data:
                chat_history.append(
                    types.Content(role=msg['role'], parts=[types.Part.from_text(text=msg['text'])])
                )
    except Exception as e:
        console.print(f"[bold red]Failed to load memory:[/bold red] {e}")

chat = client.chats.create(
    model="gemini-3.5-flash", 
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_INSTRUCTION,
        temperature=0.4, 
    ),
    history=chat_history
)






console.print("[dim]Initializing Native Windows Audio Drivers...[/dim]")
try:
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Rate = 2  
except Exception as e:
    speaker = None
    console.print(f"[bold red]Audio Driver Failed:[/bold red] {e}")

def type_text(text, base_speed=0.010): 
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in ['.', '!', '?']: time.sleep(base_speed * 15)
        elif char in [',', ':', ';']: time.sleep(base_speed * 8)
        else: time.sleep(base_speed)
    print() 

def speak_response(text):
    if not speaker: 
        return
    try:
        clean_text = text.replace('*', '').replace('`', '').replace('#', '')
        speaker.Speak(clean_text) 
    except Exception as e:
        console.print(f"\n[bold red](Voice Error: {e})[/bold red]")




buddy_text = r"""
 ____     _   _   ____     ____   __   __ 
U | __")uU |"|u| | |  _"\   |  _"\  \ \ / / 
 \|  _ \/ \| |\| |/| | | | /| | | |  \ V /  
  | |_) |  | |_| |U| |_| |\U| |_| |\U_|"|_u 
  |____/  <<\___/  |____/ u |____/ u  |_|   
 _|| \\_ (__) )(    |||_     |||_ .-,//|(_  
(__) (__)    (__)  (__)_)   (__)_) \_) (__) 
"""

def get_buddy_face(emotion="neutral", color="green"):
    emotions = {
        "neutral": "[ o_o ]",
        "happy":   "[ ^_^ ]",
        "think":   "[ -_- ]",
        "shock":   "[ O_O ]",
        "error":   "[ x_x ]"
    }
    eyes = emotions.get(emotion, emotions["neutral"])
    return f"""[bold {color}]
   _..._ 
  {eyes}
   =>B<= 
  /|   |\\
 (_|___|_)
[/bold {color}]"""

current_emotion = "neutral"
current_color = "green"

console.clear()
with Progress(
    SpinnerColumn(spinner_name="dots2", style="green"),
    TextColumn("[bold green]{task.description}[/bold green]"),
    transient=True,
) as progress:
    progress.add_task("Bypassing mainframe security...", total=None)
    time.sleep(0.5)
    progress.add_task("Waking up Pro Buddy...", total=None)
    time.sleep(0.5)

def print_ui():
    console.clear()
    face_art = get_buddy_face(current_emotion, current_color)
    console.print(Panel.fit(f"[bold {current_color}]{buddy_text}[/bold {current_color}]\n{face_art}", border_style=current_color))
    console.print(f"[bold {current_color}]>[/bold {current_color}] [bold white]PRO DESKTOP CONNECTION ESTABLISHED[/bold white]")
    console.print(f"[bold {current_color}]>[/bold {current_color}] [bold white]TYPE '/help' FOR COMMANDS, 'exit' TO DISCONNECT.[/bold white]\n")

print_ui()






while True:
    try:
        console.print(f"\n[bold {current_color}]>[/bold {current_color}] ", end="")
        user_input = input().strip()
        
        if not user_input: continue

        if user_input.startswith('/'):
            cmd = user_input.lower()
            if cmd == '/help':
                console.print(f"[{current_color}]Available commands: /clear, /time, /weather [city], /mode strict, /mode normal[/{current_color}]")
            elif cmd == '/clear':
                print_ui()
            elif cmd == '/time':
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                console.print(f"[{current_color}]System Time:[/{current_color}] {now}")
            elif cmd.startswith('/weather'):
                city = cmd.replace('/weather', '').strip() or 'London'
                with console.status(f"[bold {current_color}]Pinging weather satellites...[/bold {current_color}]"):
                    try:
                        weather_req = requests.get(f"[https://wttr.in/](https://wttr.in/){city}?format=3", timeout=5)
                        console.print(f"[{current_color}]Live Weather:[/{current_color}] {weather_req.text}")
                        speak_response(f"The current weather for {city} is fetched.")
                    except Exception as e:
                        console.print(f"[bold red]Failed to fetch weather:[/bold red] {e}")
            elif cmd == '/mode strict':
                current_emotion, current_color = "error", "red"
                print_ui()
                speak_response("Strict developer mode activated.")
            elif cmd == '/mode normal':
                current_emotion, current_color = "neutral", "green"
                print_ui()
                speak_response("Returning to normal mode.")
            elif cmd in ['/exit', '/quit']:
                break
            continue

        if user_input.lower() in ['exit', 'quit', 'bye']:
            break

        with console.status(f"[bold {current_color}]⚙ Compiling response...[/bold {current_color}]", spinner="point"):
            response = chat.send_message(user_input)
            ai_text = response.text if response.text else "Response generated."

        console.print(f"\n[bold {current_color}]Buddy:[/bold {current_color}]")
        
       
        voice_match = re.search(r'<voice>(.*?)</voice>', ai_text, re.IGNORECASE | re.DOTALL)
        
        if voice_match:
            spoken_summary = voice_match.group(1).strip()
            printed_text = re.sub(r'<voice>.*?</voice>', '', ai_text, flags=re.IGNORECASE | re.DOTALL).strip()
        else:
            spoken_summary = "Here is the information you requested."
            printed_text = ai_text
   
        current_face_art = get_buddy_face(current_emotion, current_color)
        console.print(f"\n{current_face_art}")
        console.print(f"[bold {current_color}]Buddy:[/bold {current_color}]")
        
        console.print(f"[dim italic] {spoken_summary}[/dim italic]\n")
        speak_response(spoken_summary)

        
        if "```" in printed_text:
            md = Markdown(printed_text)
            console.print(md)
        else:
            if current_color == "green": sys.stdout.write("\033[92m") 
            else: sys.stdout.write("\033[91m") 
            type_text(printed_text, base_speed=0.010) 
            sys.stdout.write("\033[0m")  

    except KeyboardInterrupt:
        break
    except Exception as e:
        console.print(f"\n[bold red]System Error:[/bold red] {e}\n")









goodbye = "Saving memory to hard drive. Catch you later, boss."
console.print(f"\n[bold {current_color}]Buddy:[/bold {current_color}] ", end="")
sys.stdout.write(f"\033[92m") if current_color == "green" else sys.stdout.write(f"\033[91m")
type_text(goodbye, base_speed=0.03)
sys.stdout.write("\033[0m")
speak_response("Catch you later, boss.")

raw_history = []
for message in chat.get_history():
    try:
        raw_history.append({
            "role": message.role,
            "text": message.parts[0].text
        })
    except (IndexError, AttributeError):
        pass 

with open(MEMORY_FILE, 'w') as f:
    json.dump(raw_history, f)