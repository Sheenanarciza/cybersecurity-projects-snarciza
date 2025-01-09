How to Create a nmap module port scannner using Python and nmap tool

What does it need to do?
- allow user to speciy target
- make requests to every port
- Return open ports
https://youtu.be/t3fuSapseS4?si=ozlp0Pb846Puau8k

Notes
- Ideally you do not want any open ports in your network.
- nmap is free open source
- have to be careful. Have to be careful when doing nmap scans with other people's networks is illegal. 

important commands
- on mac/linux 
    python3 --version
- install nmap in vscode terminal
    brew install nmap
    nmap --version


purpose:
- we will use our local host
    - To find your localhost on a Mac, open the Apple menu, go to "System Settings", then select "General" in the sidebar and click "Sharing" - your local hostname will be displayed at the bottom of the window; to access your localhost in a browser, simply type "localhost" in the address bar, which usually translates to the IP address "127.0.0.1" on your machine.

MacBook-Air-4:cybersecurity-projects-snarciza Sheena$ sudo pip3 install python-nmap
Password:
WARNING: The directory '/Users/Sheena/Library/Caches/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.
Collecting python-nmap
  Downloading python-nmap-0.7.1.tar.gz (44 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: python-nmap
  Building wheel for python-nmap (pyproject.toml) ... done
  Created wheel for python-nmap: filename=python_nmap-0.7.1-py2.py3-none-any.whl size=20681 sha256=cf3ad360062074ea6c6c33daa059282ae6ee6030a05f894d57f27719ce0aa014
  Stored in directory: /private/tmp/pip-ephem-wheel-cache-84nxfdt1/wheels/06/fc/d4/0957e1d9942e696188208772ea0abf909fe6eb3d9dff6e5a9e
Successfully built python-nmap
Installing collected packages: python-nmap
Successfully installed python-nmap-0.7.1
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable.It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.

[notice] A new release of pip is available: 24.2 -> 24.3.1
[notice] To update, run: pip3 install --upgrade pip
MacBook-Air-4:cybersecurity-projects-snarciza Sheena$ pip3 install --upgrade pip
Requirement already satisfied: pip in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (24.2)
Collecting pip
  Downloading pip-24.3.1-py3-none-any.whl.metadata (3.7 kB)
Downloading pip-24.3.1-py3-none-any.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 5.5 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 24.2
    Uninstalling pip-24.2:
      Successfully uninstalled pip-24.2
Successfully installed pip-24.3.1
MacBook-Air-4:cybersecurity-projects-snarciza Sheena$ 

Sheena$ ifconfig


MacBook-Air-4:cybersecurity-projects-snarciza Sheena$ python3 python-nmap-practice.py
Port 75 is closed.
Port 76 is closed.
Port 77 is closed.
Port 78 is closed.
Port 79 is closed.
Port 80 is closed.

- this is a good sign, all my ports are closed and secured. 


========================================================
protect yourself from hackers scanning ports
- Vanilla: where the hacker tests every virtual port 
- sweep: system wide attack, hackers ping oen port across several computers. This enables them to see which computers on the network are active
- Stealth: 
- ftp Bounce: