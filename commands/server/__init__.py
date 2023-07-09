import os
from rich import print


class Server:
    def __init__(self, path: str = '', mode: str = 'dir'):
        self.path = path
        self.mode = 'dir'

    def create_infrastructure(self):
        """Make projectsTube structure"""

        try:
            os.mkdir()

        except Exception as e:
            print(f'[red]Error: [/red]{e}\n[yellow]hint: try to use sudo[/yellow]')

    def make_archive(self):
        """Make archive"""

        pass

    def create_snapshot(self):
        """Create files snapshot"""

        pass

    def run(self):
        """Run server"""

        self.create_snapshot()
