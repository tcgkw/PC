import  os

if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts=['Main.py','-w','-F','--icon=hunter.256px.ico']
    run(opts)