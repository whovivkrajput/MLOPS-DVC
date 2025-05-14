import pandas as pd
import os
from pathlib import Path

def main(): 
    clubData = {"Name":['Real Madrid','Bayern07', 'Milan'],
                "Country": ["Spain", "Germany", "Dutch"],
                "UCL" :[15, 6, 7]}

    df = pd.DataFrame(clubData)

    new_row_loc = {"Name": "Liverpool", "Country": "England", "UCL": 5}
    df.loc[len(df)] = new_row_loc
    
    new_row_loc_3 = {"Name": "Ajax", "Country": "Dutch", "UCL": 2}
    df.loc[len(df)] = new_row_loc_3
    
    dataDir = Path("data")
    # dataDir.makedirs(exist_ok=True)
    os.makedirs(dataDir,exist_ok=True)

    filePath = dataDir/"samplefile.csv"

    df.to_csv(filePath ,index=False)
    print(f'Csv file saved - {filePath}')

if __name__ == "__main__":
    main()