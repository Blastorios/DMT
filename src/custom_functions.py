#!/usr/bin/python
'''Basic Helper Functions
Created on 13/04/2021'''

import json
import sys
from typing import *
from pathlib import Path

import numpy as np
import pandas as pd
import sklearn as sk

####################

def store_json(data: Dict, path: Union[str, Path]) -> None:
    with open(Path(path), "w") as json_upload:
        json.dump(data, json_upload)
    
    return

def load_json(path: Union[str, Path]) -> Dict:
    with open(Path(path), "r") as json_down:
        data = json.load(json_down)
    
    return data
