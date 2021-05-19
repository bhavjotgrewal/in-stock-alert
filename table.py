from rich.console import Console
from rich.live import Live
from rich.table import Table
from datetime import datetime
import gpu

console = Console()

table = Table(show_header=True, header_style="bold magenta")

table.add_column("Store", width=12)
table.add_column("Product")
table.add_column("Available?", justify="right")
table.add_column("Last Checked", justify="right")

with Live(table, refresh_per_second=4, vertical_overflow="visible"):  # update 4 times a second to feel fluid
    while True:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        if gpu.in_stock_tuf_3080_updated():
            table.add_row("[yellow]Newegg[/yellow]", "RTX 3080 TUF OC", "[green]in stock[green]",
                          dt_string)
        else:
            table.add_row("[yellow]Newegg[/yellow]", "RTX 3080 TUF OC", "[red]out of stock[/red]",
                          dt_string)
