from ohmysportsfeedspy import MySportsFeeds

Data_query = MySportsFeeds('1.2', verbose=True)
Data_query.authenticate('830a6f7f-dbb9-4aaa-abce-c2feab', 'SportsSkills123!')
Output = Data_query.msf_get_data(league='nba', season='2016-2017-regular',
                                 feed='player_gamelogs', format='json', player='stephen-curry', force='true')

print(Output)
