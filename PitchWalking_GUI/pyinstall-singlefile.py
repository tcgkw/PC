import os

if __name__ == '__main__':
    from PyInstaller.__main__ import run
    options = ['Main.py',  '-F', '--icon=fuze.ico', '--debug']

    # options = ['Main.py', '-w', '-F', '--icon=fuze.ico']
    run(options)
