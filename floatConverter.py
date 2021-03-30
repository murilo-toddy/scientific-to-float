import pathlib

for path in pathlib.Path('/mnt/161EAC0D1249AD81/Codes/Tupã/Diferencial Eletrônico/PreController/TextFiles').iterdir():
    
    if path.is_file():

        numbers = open(path, 'r').read()
        newpath = str(path)

        if newpath.find('floatConverter.py') == -1:
            newpath = newpath[0:(len(newpath) - 4)] + '_float.txt'
            newfile = open(newpath, 'w')
        
            floats = numbers.split(',')

            for item in floats:
                try:
                    newfile.write(str(format(float(item), '.20f')) + ',')
                except:
                    continue

        