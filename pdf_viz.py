import os
import camelot
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


file_name = "Redrex - Fatura (1)"
path = os.path.join(os.getcwd(), f"downloads/pdf/{file_name}.pdf")

tables = camelot.read_pdf(path
                        , pages='all'
                        ,flavor='stream'
                        #,flavor='lattice'                        
                        ,table_areas=['65, 558, 518, 300']
                        ,columns=['107,156,212,280,336,383,450']
                        )

print(tables[0].parsing_report)

camelot.plot(tables[0]
            #, kind='text'
            , kind='contour'
            #, kind='grid'
            ).show()

df = tables[0].df

print(df)

print("press any key to continue")
input()