<img src="./img/poster.png" width="400">

A corresponding tutorial can be found at [https://epwalsh.com/2017-04-10-pandas-data-wrangling/](https://epwalsh.com/2017-04-10-pandas-data-wrangling/).


## Python installation instructions

### OS X (Mac)

The first thing you will need is Xcode (available on the app store) 
or just the [Command Line Tools for Xcode](http://developer.apple.com/downloads) (recommended).

The recommended way to install anything else on a Mac is via [Homebrew](https://brew.sh).
Install Homebrew and then open a terminal and enter the following commands:

```bash
brew install python
brew link --overwrite python
brew install gfortran
```

Now we can actually start installing some important Python modules:

```bash
pip install numpy
pip install scipy
pip install matplotlib
pip install ipython
pip install jupyter
pip install pandas
```


### Linux

Many of the latest versions of Linux distros, such as CentOS, Fedora, and Ubuntu come with 
a newer versions of Python 2 out-of-the-box. Check the version with `python --version` and make sure it's at least 2.7.6.

Once you have verified your Python version is new enough, follow the instructions 
[here](https://www.scipy.org/install.html#install-systemwide-via-a-linux-package-manager) to install some 
important packages that we will be using.
