# WinBox credentials stealer
winbox_stealer.py is a simple Python script for Windows that retrieves host, login and password from an unencrypted "settings.cfg.viw" file.
I wrote this script, because earlier I downloaded WinBox and noticed that it runs pretty fast with no lags whatsoever. I was searching where are the files for the WinBox app stored. I encountered a file named "settings.cfg.viw", opened it and found out the credentials are stored here.

# Problem
This isn't any type of an exploit or a serious vulnerability, but it might be a problem sometimes. Really anyone can run this script or even manually view the file. It can be a problem for anybody who shares a PC with this file and cares about security and privacy. 

# Solution
There isn't any solution to people who have a tons of WinBox sessions stored, or it's not comfortable for them to manually type their password. I believe only possible solution is to uncheck "Keep Password" (which still leaks the host and login) in the right corner in WinBox app.

# Warning
This script is for your own and legal use only. Hacking without permission is illegal and I am not responsible for any illegal use.

# Usage
```python 
python winbox_stealer.py 
```
or call it directly - ```cmd /k winbox_stealer.py```
