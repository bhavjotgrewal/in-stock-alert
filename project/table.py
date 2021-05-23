from rich.console import Console
from rich.live import Live
from rich.table import Table
from datetime import datetime
import pyttsx3
from typing import List, Union
from project import memoryexpress, newegg, canadacomp, load


engine = pyttsx3.init()
engine.setProperty('rate', 190)

console = Console()

table = Table(show_header=True, header_style="bold magenta")

table.add_column("Store", width=12)
table.add_column("Product")
table.add_column("Available?", justify="right")
table.add_column("Last Checked", justify="right")

list_newegg = load.load_data('data/newegg_products.txt')
list_m_e = load.load_data('data/memory_express_products.txt')

# with Live(table, refresh_per_second=2, vertical_overflow="visible"):
#     while True:
#         now = datetime.now()
#         dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#
#         # list_newegg = newegg.in_stock_list(list_newegg)
#         list_m_e = in_stock_list(list_m_e, memoryexpress.in_stock_checker)
#
#         # for product in list_newegg:
#         #     try:
#         #         if product[1] is False:
#         #             table.add_row("[yellow]Newegg[/yellow]", product[0], "[red]out of stock[/red]",
#         #                           dt_string)
#         #         else:
#         #             table.add_row("[yellow]Newegg[/yellow]", product[0], "[green]in stock[/green]",
#         #                           dt_string)
#         #     except:
#         #         continue
#
#         for product in list_m_e:
#             try:
#                 if product[1] is False:
#                     table.add_row("[green]Memory Express[/green]", product[0], "[red]out of "
#                                                                                "stock[/red]",
#                                   dt_string)
#                 else:
#                     table.add_row("[yellow]Newegg[/yellow]", product[0], "[green]in stock[/green]",
#                                   dt_string)
#             except:
#                 continue
