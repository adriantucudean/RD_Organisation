@echo off
cls
SET INFO= [42m[INFO][0m
SET ERROR= [41m[ERROR][0m





:Install_numpy
    ::Instaling Numpy
    echo %INFO% install Numpy
    py -m pip install dependencies\numpy-1.13.3-cp36-none-win_amd64.whl


:Install_OpenCV
    ::Installing Opencv
    echo %INFO% Installing OpenCV
    py -m pip install dependencies\opencv_python-4.5.4.60-cp36-cp36m-win_amd64.whl

:Install_Pillow
    ::Installing Tkinter
    echo %INFO% Installing Pillow
    py -m pip install dependencies\Pillow-8.3.2-cp36-cp36m-win_amd64.whl




