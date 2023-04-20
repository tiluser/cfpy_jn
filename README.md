Creole Forth for Python in a Jupyter notebook demo
--------------------------------------------------

Intro
-----

Examples of use of Jupyter Notebook as a simple IDE for Creole Forth for Python. 

Methodology
-----------

Import CreoleForth and set up magic commands to compile and run Forth code.

Demos
-----

The notebook shows usage of simple commands and has a machine learning example
plus a simple todo list/daily log app that uses the Dropbox API. The last example
runs on Windows only but the other code should be able to run on Linux or the Mac.

What you need
-------------
This notebook was developed on top of Anaconda 2.4.0. Other setups might work. 
It's advisable to create a separate virtual environment with the command 
conda create --name <env_name> and then add packages as needed to run the notebook 
code.

If not already installed, the following packages should be installed either with
the conda or pip command as below:

conda install pyserial
conda install series
pip install numpy
pip install PyMsgBox
pip install pandas
pip install scikit-learn
pip install matplotlib
pip install dropbox
pip install "tensorflow<2.11"

The Tensorflow version is limited so as to not deal with the complexities
of GPU support, which isn't needed for the demo.  