import csv

with open('2010-2018_player_data.csv','r') as player_csv_file:
    player_csv_reader = csv.DictReader(player_csv_file)

    with open('injury_data.csv','r') as injury_csv_file:
        injury_csv_reader = csv.DictReader(injury_csv_file)

        with open('combined_data.csv','w') as combined_csv_file:
            fieldnames = ['name','injury date','return date','days missed','injury type','age', 'height', 'weight',
                'times previously injured', 'reinjured']
            combined_csv_writer = csv.DictWriter(combined_csv_file, fieldnames=fieldnames, delimiter=',')

            combined_csv_writer.writeheader()

            player_list = list(player_csv_reader)
            injury_list = list(injury_csv_reader)

            month_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7,
                'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
            
            injury_dict = {'Sprained Left Ankle': 0, 'Sprained Right Ankle': 1, 'Sore Left Knee': 2, 'Sore Right Knee': 3,
                'Concussion': 5, 'Sore Left Ankle': 6, 'Left Knee Injury': 7}

            for iline in injury_list:
                for p in player_list:
                    if iline['PLAYER'] == p['name']:
                        injury = iline['INJURY TYPE']
                        player_name = iline['PLAYER']

                        return_date = iline['RETURNED']
                        if return_date[1].isnumeric():
                            return_month = month_dict[return_date[3:-5]]
                        else:
                            return_month = month_dict[return_date[2:-5]]
                        return_year = int(return_date[-4:])
                        return_day = int(return_date[0:2])
                        reinjured = 0
                        num_prev_injuries = 0
                        if injury != 'Illness' and injury != 'For Rest' and injury != 'NBA Health and Safety Protocols':
                            for i in injury_list:
                                if player_name == i['PLAYER'] and injury == i['INJURY TYPE']:
                                    injury_date = i['INJURED ON']
                                    injury_year = int(injury_date[-4:])
                                    if injury_date[1].isnumeric():
                                        injury_month = month_dict[injury_date[3:-5]]
                                    else:
                                        injury_month = month_dict[injury_date[2:-5]]
                                    injury_day = int(injury_date[0:2])

                                    next_return_date = i['RETURNED']
                                    if next_return_date[1].isnumeric():
                                        next_return_month = month_dict[next_return_date[3:-5]]
                                    else:
                                        next_return_month = month_dict[next_return_date[2:-5]]
                                    next_return_year = int(next_return_date[-4:])
                                    next_return_day = int(next_return_date[0:2])

                                    if return_year <= injury_year:
                                        monthes_between_injuries = 12 * (injury_year - return_year)
                                        monthes_between_injuries = monthes_between_injuries + (injury_month - return_month)

                                        #reinjured
                                        if monthes_between_injuries <= 12 and monthes_between_injuries >= 1:
                                            reinjured = 1
                                        if monthes_between_injuries == 0 and return_day < injury_day:
                                            reinjured = 1

                                        #previous injuries
                                        if next_return_year < return_year:
                                            num_prev_injuries = num_prev_injuries + 1
                                        if next_return_year == return_year:
                                            if next_return_month < return_month:
                                                num_prev_injuries = num_prev_injuries + 1
                                            if next_return_month == return_month:
                                                if next_return_day < return_day:
                                                    num_prev_injuries = num_prev_injuries + 1


                            age = int(iline['INJURED ON'][-4:]) - int(p['birth_date'])
                            height = p['height']
                            feet = int(height[0])
                            inches = int(height[2:])
                            total_inches = feet*12 + inches
                            player_entry = {'name': iline['PLAYER'], 'injury date': iline['INJURED ON'], 'return date': iline['RETURNED'],
                                'days missed': iline['DAYS MISSED'], 'injury type': injury_dict[iline['INJURY TYPE']], 'age': age,'height': total_inches,
                                'weight': p['weight'], 'times previously injured': num_prev_injuries, 'reinjured': reinjured}
                            combined_csv_writer.writerow(player_entry)
