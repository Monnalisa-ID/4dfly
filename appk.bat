@echo off
:start
call python appk.py
timeout /t 5
goto start
