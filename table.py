from rich.console import Console
from rich.live import Live
from rich.table import Table
from datetime import datetime
import gpu
import consoles
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 190)

console = Console()

table = Table(show_header=True, header_style="bold magenta")

table.add_column("Store", width=12)
table.add_column("Product")
table.add_column("Available?", justify="right")
table.add_column("Last Checked", justify="right")

with Live(table, refresh_per_second=1, vertical_overflow="visible"):
    while True:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        if gpu.in_stock_tuf_3080_updated():
            table.add_row("[yellow]Newegg[/yellow]", "RTX 3080 TUF OC", "[green]in stock[green]",
                          dt_string)
            engine.say("30 80 New Egg")
            engine.runAndWait()
        else:
            table.add_row("[yellow]Newegg[/yellow]", "RTX 3080 TUF OC", "[red]out of stock[/red]",
                          dt_string)
            engine.say("30 80 No where")
            engine.runAndWait()

        if consoles.in_stock_ps5_disc_updated():
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            table.add_row("[blue]Best Buy[/blue]", "PS5 Disc", "[blue]in stock[blue]",
                          dt_string)
            engine.say("PS5 Disc Best Buy")
            engine.runAndWait()
        else:
            table.add_row("[blue]Best Buy[/blue]", "PS5 Disc", "[red]out of stock[red]",
                          dt_string)
            engine.say("PS5 no where")
            engine.runAndWait()
