# ImageOverlay

### Getting Started
Clone the repo by running the following command:
```
git clone https://github.com/kyuds/imageoverlay.git
```
Create a new anaconda environment to install packages based on `requirements.txt`. Also, delete the gen.csv file to start clean. 

### Setting Up Configurations
The python program parses the JSON config file. Note that the weights are relative weights, not absolute weights, so the addition of new items will impact the probability of the other items (as it should). Furthermore, it should be setup such that the keys should be the file names (without the file extensions). The system assumes that all image files use the .png extension. Upon running generate.py, a random image will be created in the `results` folder. 

### Running
You can either run using the python command or using the shell script provided. Examples are below:
```
python3 generate.py --n 4
```
```
./run.sh 5
```
To generate one NFT:
```
python3 generate.py
```
```
./run.sh
```