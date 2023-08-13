from string import ascii_lowercase
from glob import glob

legal = list((ascii_lowercase+' '))
for path in [path.replace('binary\\', '').replace('\\', '').replace('-negative', '') for path in glob('binary/*/')]:
    print(path)
    for c in list(path):
        if not c in legal:
            print(f'Found illegal char: {c}')