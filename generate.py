import cv2
import json

def overlay(data):
    pass

def main():
    # load in configurations
    data = None
    with open('config.json') as file:
        data = json.load(file)

    for layer in data.keys():
        

if __name__ == "__main__":
    main()
