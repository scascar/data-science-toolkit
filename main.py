from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
import os
import pandas as pd
from sys import exit

commands_completer = WordCompleter(['ls','open','head','columns','renamecol','deletecol','setindex','save','types','valuecount','whichhasnan'])

session = PromptSession()
df = None

while 1 == 1:
    command = session.prompt('>',completer=commands_completer)

    if command == 'ls':
        files = [f for f in os.listdir('.')]
        print('FILE \t\tSIZE')
        for f in files:
            print(str(f) + '\t\t'+ str(os.stat(f).st_size/1000)+'KB')

    elif command == 'open':
        name = session.prompt('Name of csv: ')
        df = pd.read_csv(name)
        
    elif command == 'head':
        if df is not None:
            print(df.shape)
            print(df.head())
        else:
            print('No File loaded')

    elif command == 'columns':
        print(df.columns.values)

    elif command == 'renamecol':
        col1 = session.prompt('Column to rename: ')
        col2 = session.prompt('new name: ')
        df = df.rename(columns ={col1:col2})
    elif command == 'deletecol':
        col = session.prompt('Column to drop: ')
        df = df.drop([col],axis=1)
    elif command == 'setindex':
        ind = session.prompt('Column to index on: ')
        df = df.set_index(ind)
        print(df.head())

    elif command == 'quit' or command == 'exit':
        exit(0)
    elif command == 'save':
        name = session.prompt('Name for file: ')
        df.to_csv(name,index=False)
        print(name +' Saved!')
    elif command == 'types':
        print(df.dtypes)
    elif command == 'valuecount':
        col = session.prompt('Columns: ')
        print(df[col].value_counts())
    elif command == 'whichhasnan':
        print('Columns containing NaN values:')
        print(df.isna().sum())


