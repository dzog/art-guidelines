import csv
import os
import shlex
import subprocess

with open('grants.csv', 'rb') as input_file:
    grant_info = csv.reader(input_file)

    for row in grant_info:
        with open('contract_template.tex', 'r') as output:
            data = output.read()
            data = data.replace('GRANT', row[2])
            data = data.replace('PROJECT', row[1])
            data = data.replace('ARTIST', row[0])
            data = data.replace('AMOUNT', row[3].replace('$','\$').replace(',',''))

            filename = row[1].replace(' ', '_')
            filename = filename.lower()
            filename += '.tex'

            with open(filename, 'w') as output:
                output.write(data)

            proc = subprocess.Popen(shlex.split('pdflatex %s' % filename))
            proc.communicate()
    
            os.unlink(filename)
            os.unlink(filename.replace('.tex', '.log'))
            os.unlink(filename.replace('.tex', '.aux'))
            os.unlink(filename.replace('.tex', '.out'))
            os.rename(filename.replace('.tex', '.pdf'), 'contracts/' + filename.replace('.tex', '.pdf'))
