pizza_menu = {'margherita': 0,
             'marinara': 0,
             'napoletana': 0}
print('pizza menu: margherita at S$15.5, marinara at S$17.5 and napoletana at S$18')
cont = 1
while cont == 1:
  pizza_type = input('What do you want to eat: ')
  if(pizza_type!='margherita' and pizza_type!='marinara' and pizza_type!='napoletana'):
    print('May an cai deo gi vay')
    continue
  pizza_num = input('How many (please type in a number): ')
  pizza_num = int(pizza_num)
  
  if(pizza_num >=3): 
    print('May beo nhu mot con lon')
  if(pizza_num <1):
    print('May dua thang bo may a')
    pizza_num =0
  
  if pizza_type == 'margherita': 
    pizza_menu['margherita'] += pizza_num
  elif pizza_type == 'marinara':
    pizza_menu['marinara'] += pizza_num
  elif pizza_type == 'napoletana':
    pizza_menu['napoletana'] += pizza_num

  print('Do you want to eat more? Continue press 1, Stop press 0')
  cont = input()
  cont = int(cont)

pizza_price = pizza_menu['margherita']*15.5 + pizza_menu['marinara']*17.5 + pizza_menu['napoletana']*18 
print('Pizza price: ', pizza_price)