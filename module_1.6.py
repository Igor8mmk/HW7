my_dict = {'Igor' : '10.03.1986', 'Katia' : '07.05.1990', 'Nika' : '23.08.2021', 'Roma' : '11.09.2023'}
print(my_dict)
print (my_dict.get('Igor'))
print (my_dict.get('Boris'))
my_dict.update({'Tom' : '10.10.1901',
                'Boris' : '20.07.2011'})
print(my_dict)
igor = my_dict.pop('Igor')
print(igor)
print(my_dict)
my_set = {11, 12, 13, 14, 78, 55, 12, 11}
print(my_set)
my_set.update ({58, 65})
print(my_set)
my_set.discard(11)
print(my_set)
