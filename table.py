from rich.console import Console
from rich.live import Live
from rich.table import Table
from datetime import datetime
import pyttsx3
import newegg

engine = pyttsx3.init()
engine.setProperty('rate', 190)

console = Console()

table = Table(show_header=True, header_style="bold magenta")

table.add_column("Store", width=12)
table.add_column("Product")
table.add_column("Available?", justify="right")
table.add_column("Last Checked", justify="right")

list_3060_newegg = newegg.load_data('newegg_products.txt')

with Live(table, refresh_per_second=2, vertical_overflow="visible"):
    while True:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        list_newegg = newegg.in_stock_list(list_3060_newegg)

        for product in list_newegg:
            try:
                if product[1] == False:
                    table.add_row("[yellow]Newegg[/yellow]", product[0], "[red]out of stock[/red]",
                                  dt_string)
                else:
                    table.add_row("[yellow]Newegg[/yellow]", product[0], "[green]in stock[/green]",
                                  dt_string)
            except:
                continue
