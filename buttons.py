
# from telebot.types import ReplyKeyboardMarkup,KeyboardButton 

# def contact_button():
#     kb = ReplyKeyboardMarkup(resize_keyboard=True)
    
#     button = KeyboardButton('Share contact',request_contact=True)
#     kb.add(button)
    
#     return kb

# def translete_button():
#     kb = ReplyKeyboardMarkup(resize_keyboard=True)
    
#     button = KeyboardButton('Translate')
#     kb.add(button)
    
#     return kb

# def languages_button():
#     kb = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    
#     ru = KeyboardButton('RU')
#     uz = KeyboardButton('UZ')
#     en = KeyboardButton('EN')
#     es = KeyboardButton('ES')
#     fa = KeyboardButton('FA')
    
#     kb.add(ru, uz, en, es, fa)
    
#     return kb


from telebot.types import ReplyKeyboardMarkup,KeyboardButton


def buttons():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    share_contact = KeyboardButton('Поделиться номером',request_contact=True)

    kb.add(share_contact)

    return kb






    


def start_button():

    kb = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)

    ru = KeyboardButton('Russain 🇷🇺')
    uz = KeyboardButton('Uzbek 🇺🇿')
    us = KeyboardButton('English 🇬🇧🇺🇸')
    cn = KeyboardButton('Chinese 🇨🇳')
    kr = KeyboardButton('Korean 🇰🇷')  
    kz = KeyboardButton('Kazakh 🇰🇿')  

    kb.row(ru,uz)
    kb.add(us)
    kb.row(kz,cn)
    kb.add(kr)

   


    return kb