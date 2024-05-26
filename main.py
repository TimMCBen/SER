import pandas as pd

filename = 'iemocap_6way_label.csv'
df = pd.read_csv(filename)
print(f'表头: {df.columns.tolist()} ')
paths = []
for session in df['id']:
    parts = session.rsplit('_',1)
    path = f'Session{parts[0][4]}/sentences/wav/{parts[0]}/{session}.wav'
    paths.append(path)
print(paths[0])
