keys = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-+={}[]\|,.?>''"";:<1234567890/ '
values = '!@#$%^&*()_+=-[]\{}|,./`<''"";:>?AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr0123456789SsTtUuVvWwXxYyZz'
encrypt = dict(zip(keys,values))
decrypt = dict(zip(values,keys))
jo = ''

mode = input('Encode(E) or Decode(D) : ' )
modes = mode.upper()
if modes == 'E':
    encodemessage = input("Enter the message : ")
    for letter in encodemessage:
        jo = jo + encrypt[letter]
    print(jo)
elif modes == 'D':
    decodemessage = input("Enter the encrypted code : ")
    for letter in decodemessage:
        jo = jo + decrypt[letter]
    print(jo)
    
else:
    print('Enter the correct word')
        
        