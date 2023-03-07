# LogParse
# By EikDaMike and TRC-Loop
# Licensed under MIT License

# Basic Initilazation
from rich import console
from rich import print
from rich import progress
from rich import prompt
import rich # Install rich with "pip install rich"
import os
console = console.Console()

# User Input for the path
if prompt.Confirm("Do you want to scan all Logs in a specified path?", default=True):
    path = prompt.Prompt("Enter the path to scan all the files", default=os.getcwd())
else:
    path = prompt.Prompt("Enter the path to scan one file", default=os.getcwd())

