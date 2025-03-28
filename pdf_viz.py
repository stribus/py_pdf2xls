import os
import camelot
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


file_name = "Redrex - Fatura (1)"
path = os.path.join(os.getcwd(), f"downloads/pdf/{file_name}.pdf")

tables = camelot.read_pdf(path, pages='all',flavor='stream')

print(tables[0].parsing_report)

camelot.plot(tables[0], kind='text').show()

print("press any key to continue")
input()