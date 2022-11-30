import cv2
import json
import random

import argparse
from datetime import datetime

def overlay(img, ovrly):
    row, col, _ = img.shape
    for r in range(row):
        for c in range(col):
            if ovrly[r][c][3] == 0:
                continue
            
            a = float(ovrly[r][c][3] / 255.0)
            img[r][c] = a * ovrly[r][c] + (1 - a) * img[r][c]

    return img

def create(data):
    img = None
    for layer, item in data:
        path = "assets/" + str(layer) + "/" + item + ".png"

        if layer == 0:
            img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
            continue
        if item == "None":
            continue
        
        ovrly = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        img = overlay(img, ovrly)

    return img

def main():
    # parse arguments
    parser = argparse.ArgumentParser(description='options for NFT generation.')
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
            config.append((int(layer), random.choices(v, weights=w, k=1)[0]))
        config.sort(key=lambda x: x[0])

        # write image result
        nft = create(config)
        path = "result/" + str(datetime.now()) + ".png"
        cv2.imwrite(path, nft)

if __name__ == "__main__":
    main()
