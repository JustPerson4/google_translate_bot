
import telebot 

import db

import buttons

from googletrans import Translator
 

 

token = '6535978716:AAFmIqvI3omH9MDqL5s8ZsppTi4kmEDTNAA'


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    
    user = db.check_user(message.from_user.id)
    
    if user:
        bot.send_message(message.from_user.id, 'To translete,user the button', reply_markup=buttons.start_button())
        
    else:
        bot.send_message(message.from_user.id, 'To start the using the bot,share contact!', reply_markup=buttons.buttons    )
    
    bot.send_message(message.from_user.id, 'To start the using the bot,share contact!', reply_markup=buttons.buttons())
    bot.register_next_step_handler(message,get_contact)  
    
def get_contact(message):
    if message.contact:
        user_phone = message.contact.phone_number
        first_name = message.contact.first_name
        telegram_id = message.from_user.id
        
        db.register_user(telegram_id, first_name,user_phone)
        
        bot.send_message(message.from_user.id, 'To translete,user the button', reply_markup=buttons.start_button())
        
    else:
        bot.send_message(message.from_user.id, 'Place to share your contact use the button', reply_markup=buttons.buttons()) 
        bot.register_next_step_handler(message, get_language)









    




@bot.message_handler(content_types=['text'])
def get_language(message):

    def ru(message):
        
        trans = Translator()

        result = trans.translate(message.text,dest='ru').text

        print(result)
        bot.send_message(message.from_user.id, f'Вот перевод:  "{result}"')

        db.add_user_word(message.from_user.id,message.text,result)




    
    def uz(message):
        
        trans = Translator()

        result = trans.translate(message.text,dest='uz').text

        print(result)
        bot.send_message(message.from_user.id, f'Вот перевод:  "{result}"')
        db.add_user_word(message.from_user.id,message.text,result)

    def us(message):
        
        trans = Translator()

        result = trans.translate(message.text,dest='en').text

        print(result)
        bot.send_message(message.from_user.id, f'Вот перевод:  "{result}"')
        db.add_user_word(message.from_user.id,message.text,result)
    def cn(message):
        
        trans = Translator()

        result = trans.translate(message.text,dest='zh-CN').text

        print(result)
        bot.send_message(message.from_user.id, f'Вот перевод:  "{result}"')
        db.add_user_word(message.from_user.id,message.text,result)

    def kr(message):

        trans = Translator()
        
        result = trans.translate(message.text,dest='ko').text
        print(result)
        bot.send_message(message.from_user.id, f'Вот перевод:  "{result}"')
        db.add_user_word(message.from_user.id,message.text,result)

    def kz(message):

        trans = Translator()
        
        result = trans.translate(message.text,dest='kk').text
        print(result)
        bot.send_message(message.from_user.id, f'Вот перевод:  "{result}"')
        db.add_user_word(message.from_user.id,message.text,result)





    if message.text == 'Russain 🇷🇺':
        bot.send_message(message.from_user.id, 'Write text:')
        bot.register_next_step_handler(message,ru)



    elif message.text == 'Uzbek 🇺🇿':
        
            if message.text =='Uzbek 🇺🇿' :
                bot.send_message(message.from_user.id, 'Write text:')
                bot.register_next_step_handler(message,uz)

                
                
    

    elif message.text =='English 🇬🇧🇺🇸' :
        bot.send_message(message.from_user.id, 'Write text:')
        bot.register_next_step_handler(message,us)
    

    elif message.text == 'Chinese 🇨🇳':
        bot.send_message(message.from_user.id, 'Write text:')
        bot.register_next_step_handler(message,cn)



    elif message.text == 'Korean 🇰🇷':
        bot.send_message(message.from_user.id, 'Write text:')
        bot.register_next_step_handler(message,kr)


    elif message.text == 'Kazakh 🇰🇿':
        bot.send_message(message.from_user.id, 'Write text:')
        bot.register_next_step_handler(message,kz)




    else:
        bot.send_message(message.from_user.id, 'Down choice buttons!')    
         



bot.polling()