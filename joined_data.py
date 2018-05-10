# pulling datas together into single file

import pandas as pd


def compile_data(input_csv):
    dataTicker = pd.read_csv(input_csv, header=None)
    dataTicker = dataTicker[0]
    main_df = pd.DataFrame()
    #reading each ticker's file and merge their close price into single file, called main_df and save as joined_data.csv
    for count, ticker in enumerate(dataTicker):
        try:
            df = pd.read_csv('stock_dfs1/{}.csv'.format(ticker))
            df.set_index('Date', inplace=True)
            df.rename(columns={'Close': ticker}, inplace=True)
            df.drop(["Open", "High", "Low", "Volume", "Symbol"], 1, inplace=True)

            # joining all dfs together
            if main_df.empty:
                main_df = df
            else:
                main_df = main_df.join(df, how='outer')
        except:
            pass
        main_df.to_csv("joined_data.csv")