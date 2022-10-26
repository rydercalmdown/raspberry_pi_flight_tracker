#!/bin/bash
# install.sh
# general installation script

currDir=${PWD##*/}

echo "Downloading dump1090";

cd ../
git clone https://github.com/flightaware/dump1090 dump1090
cd dump1090
make

cd ../$currDir

echo "Installing python requirements";
virtualenv env && . env/bin/activate
pip install -r src/requirements.txt


echo "Installation complete";
