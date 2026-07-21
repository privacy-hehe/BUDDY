#All faces are no working in the main project make sure , only 2 are working other's are under development I am planning to connect with ai so it can react every time.


import time
import sys
from rich.console import Console
from rich.panel import Panel

console = Console()

BUDDY_HEADER = r"""
 ____     _   _   ____     ____   __   __ 
U | __")uU |"|u| | |  _"\   |  _"\  \ \ / / 
 \|  _ \/ \| |\| |/| | | | /| | | |  \ V /  
  | |_) |  | |_| |U| |_| |\U| |_| |\U_|"|_u 
  |____/  <<\___/  |____/ u |____/ u  |_|   
 _|| \\_ (__) )(    |||_     |||_ .-,//|(_  
(__) (__)    (__)  (__)_)   (__)_) \_) (__) 
"""

def get_buddy_face(emotion="neutral", color="green"):
    """
    Generates Buddy's compact robot face with dynamic expressions.
    
    Supported Emotions:
        "neutral" -> Standard operational look [ o_o ]
        "happy"   -> Successful operation     [ ^_^ ]
        "think"   -> Processing / Compiling   [ -_- ]
        "shock"   -> Unexpected input         [ O_O ]
        "error"   -> Strict mode / Failure    [ x_x ]
    """
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


def render_interface(emotion="neutral", color="green"):
    """ Clears the console and draws Buddy inside a structured panel. """
    console.clear()
    face_art = get_buddy_face(emotion, color)
    
    # Combine the logo and the face inside a uniform Rich Panel
    console.print(
        Panel.fit(
            f"[bold {color}]{BUDDY_HEADER}[/bold {color}]\n{face_art}", 
            border_style=color
        )
    )
    console.print(f"[bold {color}]>[/bold {color}] [bold white]EMOTION ENGINE ONLINE: {emotion.upper()}[/bold white]\n")


if __name__ == "__main__":
    
    demo_states = [
        ("neutral", "green"),
        ("think", "green"),
        ("happy", "green"),
        ("shock", "yellow"),
        ("error", "red")
    ]
    
    try:
        for emotion, color in demo_states:
            render_interface(emotion, color)
            time.sleep(2.0)
            
       
        render_interface("neutral", "green")
        console.print("[bold green]Demo complete. Integration ready.[/bold green]")
        
    except KeyboardInterrupt:
        console.print("\n[bold red]Demo interrupted.[/bold red]")
