import csv
import numpy as np

with open('2010-2018_player_data.csv','r') as player_csv_file:
    player_csv_reader = csv.DictReader(player_csv_file)

    with open('injury_data.csv','r') as injury_csv_file:
        injury_csv_reader = csv.DictReader(injury_csv_file)

        with open('combined_data.csv','w') as combined_csv_file:
            fieldnames = ['name','injury date','return date','days missed','injury type','age', 'height', 'weight']
            combined_csv_writer = csv.DictWriter(combined_csv_file, fieldnames=fieldnames, delimiter=',')

            combined_csv_writer.writeheader()

            player_list = list(player_csv_reader)

            print(player_list)

            for iline in injury_csv_reader:
                for p in player_list:
                    if iline['PLAYER'] == p['name']:
                        age = int(iline['INJURED ON'][-4:]) - int(p['birth_date'])
                        print(p['name'] + ' ' + str(age))
                        player_entry = {'name': iline['PLAYER'], 'injury date': iline['INJURED ON'], 'return date': iline['RETURNED'],
                            'days missed': iline['DAYS MISSED'], 'injury type': iline['INJURY TYPE'], 'age': age,'height': p['height'],
                            'weight': p['weight']}
                        combined_csv_writer.writerow(player_entry)
