from rich.traceback import install
install(show_locals=True)

from rich.panel import Panel
from rich import box
from rich.console import Console

import winsound

console = Console()

def beep():
    beep = Panel("BEEP", border_style="Bold Red", title="- - - -", title_align = "left")
    
    for i in range(0, 10):
        console.log(beep)
        winsound.Beep(2500, 100)
    

beep()