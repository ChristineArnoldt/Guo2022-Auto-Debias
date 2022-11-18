import pandas as pd

df = pd.read_csv('data/dewiki-2022-08-29.txt', sep=" ", names=['word', 'count'])
df.sort_values(by=['count'], ascending=False, inplace=True)
print(len(df))
df = df.head(5000)
print(len(df))

print('writing')
df.to_csv(r'data/wiki_words_5000_de.txt', header=None, index=None, sep=' ', mode='a')