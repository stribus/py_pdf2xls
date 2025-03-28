import os
import camelot
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt



def extractRedrex(file_name):
    path = os.path.join(os.getcwd(), f"downloads/pdf/{file_name}.pdf")

    tables = camelot.read_pdf(path
                            , pages='all'
                            ,flavor='stream'
                            #,flavor='lattice'                        
                            ,table_areas=['65, 558, 518, 300']
                            ,columns=['107,156,212,280,336,383,450']
                            )

    df = tables[0].df
    pddf = pd.DataFrame(df)
    if not os.path.exists("downloads/excel"):
        os.makedirs("downloads/excel")
    pddf.to_excel(f"downloads/excel/{file_name}.xlsx", index=False)
    
dir = os.path.join(os.getcwd(), "downloads/pdf")
for file in os.listdir(dir):
    if file.startswith('Redrex') and file.endswith(".pdf"):
        #print(file[:-4])
        extractRedrex(file[:-4])