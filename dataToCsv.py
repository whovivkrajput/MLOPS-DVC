import pandas as pd
import os
from pathlib import Path

def main(): 
    clubData = {"Name":['Real Madrid','Bayern07', 'Milan'],
                "Country": ["Spain", "Germany", "Dutch"],
                "UCL" :[15, 6, 7]}

    df = pd.DataFrame(clubData)

    dataDir = Path("data")
    dataDir.makedir(exist_ok=True)
    filePath = dataDir/"samplefile.csv"

    df.to_csv(filePath ,index=False)
    print(f'Csv file saved - {filePath}')

if __name__ == "__main__":
    main()