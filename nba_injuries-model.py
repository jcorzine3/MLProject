import csv

with open('player_data.csv','r') as player_csv_file:
    player_csv_reader = csv.reader(player_csv_file)

    with open('2010-2018_player_data.csv','w') as recent_player_data_file:
        player_csv_writer = csv.writer(recent_player_data_file)

    next(player_csv_reader)

    for line in player_csv_reader:
        if 
        print(line)