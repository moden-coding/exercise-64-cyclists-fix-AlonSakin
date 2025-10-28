#!/usr/bin/env python3

import pandas as pd

def cyclists():
    tb = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")

    return tb.dropna(how="all").dropna(axis=1, how="all")


def main():
    cyclists()
    
if __name__ == "__main__":
    main()
