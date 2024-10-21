'''app_controller.py: This module acts as the controller, orchestrating the flow of the application.'''
import pkgutil
import importlib
from typing import Type
from app.commands import CommandHandler, Command
from app.plugins.menu import MenuCommand

class App:
    '''Core class that manages the overall application behavior.'''
    
    def __init__(self):
        '''Initializes the application by setting up the command handler.'''
        self.command_handler = CommandHandler()

    def load_plugins(self):
        '''Loads plugins dynamically from the app.plugins package.'''
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, Command):  # Check if item is a subclass of Command
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        # Skip anything that isn’t a class or doesn’t inherit from Command
                        continue
        # Register MenuCommand for displaying available options
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))

    def start(self):
        '''Starts the application, loading plugins and initiating the REPL loop.'''
        self.load_plugins()
        print("Welcome to the calculator app.")
        print("\tType 'menu' to view available commands. Type 'exit' to close the application.")
        while True:
            # Read, evaluate, print, and loop (REPL)
            self.command_handler.execute_command(input(">>> ").strip())