import fade
import time
import asyncio
from rich import box
from rich.live import Live
from rich.table import Table
from rich.console import Console
from contextlib import contextmanager
import pandas as pd


class TransferData:
    def __init__(self):
        self.console = Console()
        self.hide_visualisation_data = False  # Скрывать данные или нет
        self.table = Table(show_header=True, header_style="bold magenta")

    def start(self):
        self.draw_logo()
        asyncio.run(self.move_from_channel_to_bot())

    def draw_logo(self):
        logo = """
███╗   ███╗███████╗██████╗  ██████╗ ██╗███╗   ██╗ ██████╗     ██████╗ ██████╗  ██████╗  ██████╗███████╗███████╗███████╗
████╗ ████║██╔════╝██╔══██╗██╔════╝ ██║████╗  ██║██╔════╝     ██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔════╝██╔════╝██╔════╝
██╔████╔██║█████╗  ██████╔╝██║  ███╗██║██╔██╗ ██║██║  ███╗    ██████╔╝██████╔╝██║   ██║██║     █████╗  ███████╗███████╗
██║╚██╔╝██║██╔══╝  ██╔══██╗██║   ██║██║██║╚██╗██║██║   ██║    ██╔═══╝ ██╔══██╗██║   ██║██║     ██╔══╝  ╚════██║╚════██║
██║ ╚═╝ ██║███████╗██║  ██║╚██████╔╝██║██║ ╚████║╚██████╔╝    ██║     ██║  ██║╚██████╔╝╚██████╗███████╗███████║███████║
╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚══════╝╚══════╝╚══════╝
        """
        result_text = fade.fire(logo).split('\n')
        for line in result_text:
            print(line)
            time.sleep(0.15)
        self.print_string_to_screen("[+] Starts the merge process\n")

    def print_string_to_screen(self, text):
        self.console.print(text, style="bold yellow")

    @contextmanager
    def beat(self, length: int = 1) -> None:
        yield
        wait_update = 0.04
        time.sleep(length * wait_update)

    def draw_user_table(self, user_data: list, hide_data=False):
        self.table.box = box.MINIMAL
        hidden_characters = ["************"] * len(user_data[0])

        with Live(self.table, console=self.console, screen=False, refresh_per_second=20):
            with self.beat(9):
                self.table.add_column("#", justify="center", width=9, style="cyan", header_style="bold yellow")

            with self.beat(9):
                self.table.add_column("first/last name", justify="center", width=20, style="cyan", header_style="bold yellow")

            with self.beat(9):
                self.table.add_column("Date of Birth", justify="center", width=20, style="cyan", header_style="bold yellow")

            with self.beat(9):
                self.table.add_column("Parents' first and last name", justify="center", width=20, style="cyan", header_style="bold yellow")

            with self.beat(9):
                self.table.add_column("Courses", justify="center", width=36, style="cyan", header_style="bold yellow")

            for number, row in enumerate(user_data, start=1):
                with self.beat(9):
                    self.table.add_row(
                        str(number),
                        *row if not hide_data else hidden_characters
                    )

    async def move_from_channel_to_bot(self):
        file_errors_location = 'I:\Py project\DBTGSchwerin\gesamte Information.xlsx'
        df = pd.read_excel(file_errors_location)
        result_data = []
        for person in df.values:
            result_data.append([str(x) for x in person])
        self.draw_user_table(result_data, hide_data=self.hide_visualisation_data)


if __name__ == "__main__":
    t = TransferData()
    t.start()
