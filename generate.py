import cv2
import json
import random

import argparse
from datetime import datetime

def overlay(data):
    pass

def main():
    # parse arguments
    parser = argparse.ArgumentParser(description='Options for NFT generation.')
    parser.add_argument('--n', default=1, type=int, help='number of NFTs to generate.')
    args = parser.parse_args()

    # load in configurations
    data = None
    with open('config.json') as file:
        data = json.load(file)

    for _ in range(args.n):
        # random generation
        config = []
        for layer in data.keys():
            w = [int(data[layer][x]) for x in data[layer].keys()]
            v = list(data[layer].keys())
            config.append((layer, random.choices(v, weights=w, k=1)))
        
        # write image result
        nft = overlay(config)
        path = "results/" + str(datetime.now()) + ".png"
        print(path)
        cv2.imwrite(nft, path)

if __name__ == "__main__":
    main()
