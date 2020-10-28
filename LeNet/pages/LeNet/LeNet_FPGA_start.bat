@echo off
if not exist E:\XAMPP_Workspace\pages\LeNet\cache\LeNet_FPGA.running (
CALL D:\Program_Files\Anaconda3\Scripts\activate.bat D:\Program_Files\Anaconda3\envs\pytorch
python LeNet_FPGA.py
)