@echo off
:start
call python appk.py
timeout /t 10
goto start
