@echo off
if not exist E:\XAMPP_Workspace\PPT\LeNet\pages\LeNet\cache\LeNet_GPU.running (
CALL C:\Program_Files\Anaconda3\Scripts\activate.bat C:\Program_Files\Anaconda3\envs\pytorch
python LeNet_GPU.py
)