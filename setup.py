import sys
import os
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only

build_exe_options = {"excludes": ["tkinter"], "include_files":["usuario.db", "screens", "src", "projeto.db", "cliente.db", "financeiro.db"]}
build_msi_options = {"initial_target_dir": "C:\\Gerencia Arquitetura"}
# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Gerência Arquitetura Pereira",
    author= "devfab",
    version = "1.0",
    description = "Aplicativo de gerenciamento financeiro da Arquitetura Pereira",
    executables = [Executable(script="AppController.py", base=base, icon='se.ico', shortcutName="Gerência Arquitetura", shortcutDir="DesktopFolder")],
    options = {
        "build_exe": build_exe_options,
        'bdist_msi': build_msi_options
    },
)
