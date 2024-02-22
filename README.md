# HIDS Docker

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
git clone https://github.com/gabrielruschel/hids-docker
```

And install the dependencies using pip3:
```
cd hids-docker/
pip3 install -r requirements.txt
```

## Examples ##

To run the tests, just use the following command:
```
python3 main.py [-d {sbseg,iscc}] [-f {raw,filter}] <window_size>
python3 -u TCC/scripts/rf.py --dataset histograma.csv
```
* `-d`: specifies which dataset to use (default: iscc)
* `-f`: specifies which filter mode to use (default: raw)
* `window_size`: specifies the size of the window be used in the tests.

The `-h` argument shows the help message. It is possible to edit in the main section of the code which specific methods you want to test.
