Python 3.9 - Tested on Linux

Simple code that allows the mouse to move automatically.
The program will end when the 'esc' key is pressed.
Or it can be run in thread with a timer. In this case, the program will end when the 'esc' key is pressed or when the timer ends.
The aim is to ensure that the programs used remains active, without giving any signs of being absent.
For example when observing a log, so that the mouse doesn't move all the time. 


Problem encountered: the more seconds given as input in the sleep() function ( in mouse() ), the longer the time for event number 1 to occur.
