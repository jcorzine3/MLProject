import csv

with open('player_data.csv','r') as player_csv_file:
    player_csv_reader = csv.DictReader(player_csv_file)

    with open('2010-2018_player_data.csv','w') as recent_player_data_file:
        fieldnames = ['name','year_end','position','height','weight','birth_date']
        player_csv_writer = csv.DictWriter(recent_player_data_file, fieldnames=fieldnames, delimiter=',')

        player_csv_writer.writeheader()


        for line in player_csv_reader:
            if 2010 <= int(line['year_end']):
                del line['year_start']
                del line['college']
                line['birth_date'] = line['birth_date'][-4:]
                player_csv_writer.writerow(line)