# HIDS Docker

In this repository we present a docker dataset based on system calls and the source code used for its experimental evaluation, more details are presented in [HIDS Docker Information] (you can also read the same README in [portuguese](README.pt.md)):

## Table of Contents ##
- [How do I get set up?](#how-do-i-get-set-up?)
    - [Install](#install)
    - [Setup](#setup)
- [Examples](#examples)
- [Contribution guidelines](#contribution-guidelines)
- [License](#license)

## How do I get set up? ##

The following components should be installed:

```
* python 3.8.5
* pip3 20.0.2
  * scikit-learn 0.22.2
```

### Install ###

Python3 and pip3 are required for testing. Arch linux installation guide:
```
sudo pacman -S python python-pip
```

Debian installation guide:
```
sudo apt install python3 python3-pip
```

### Setup ###

Clone this repository:
```
git clone https://github.com/Carmofrasao/hids-docker
```

And install the dependencies using pip3:
```
cd hids-docker/
pip3 install -r requirements.txt
```

## Examples ##

To run the tests, just use the following command:

```
python3 histogram.py > <histogram>
```

```
python3 rf.py --dataset <histogram>
```
* `-d`: specifies which dataset to use
