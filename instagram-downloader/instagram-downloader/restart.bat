@echo off
set dir=%cd%
cd %dir%\stuff\Instagram-Downloader
Taskkill /im Instagram-Downloader.exe
start Instagram-Downloader.exe