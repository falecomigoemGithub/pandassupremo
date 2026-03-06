import pandas as pd
import numpy as np
from IPython.display import display

def main():
    df_vendas = pd.read_csv("vendas_tech.csv")
    display(df_vendas)


if __name__ == "__main__":
    main()
