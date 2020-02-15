import telebot
import random
import time
from telebot import types
from pymongo import MongoClient
import os



#MONGODB
client = MongoClient(os.environ["MongoDB"])
db = client.UserDB
coll = db.AllINFO

bot=telebot.TeleBot(os.environ["token"])

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(commands=['help'])
def lsHelp_message(message):
    bot.send_message(message.chat.id, 'Существуют команды:\n/start - Начальная команда\n/myinfo - Твоя информация\n/info - Чья либо информация(Отвечать на чье-либо сообщение)')


'''
@bot.message_handler(commands=['random'])
def choice_random(message):
	random1=["@dimagorovtsov","@Atik_8D"]##########################
	choice=random.choice(random1)
	bot.send_message(message.chat.id, 'Рандом выбрал '+str(choice))
''' 
'''
@bot.message_handler(commands=['randommygroup'])
def choice_random(message):
	random1=["@Atik_8D","@KinG_Of_DeatCh","@iamdior","@schastyee_15_06","@Moy_ray_14"]##########################
	choice=random.choice(random1)
	bot.send_message(message.chat.id, 'Рандом выбрал '+str(choice))
'''
@bot.message_handler(commands=['info'])
def give_me_info(message):
	if message.reply_to_message!=None:
		bot.send_message(message.chat.id, "Айди: "+str(message.reply_to_message.from_user.id)+"\nИмя: "+str(message.reply_to_message.from_user.first_name)+"\nUserName: "+"@" +str(message.reply_to_message.from_user.username))
		print(message)
	else:
		bot.send_message(message.chat.id, "Отвечай на чьё либо сообщение!!!")

@bot.message_handler(commands=['chatinfo'])
def give_me_chatinfo(message):
	bot.send_message(message.chat.id, "Айди: "+str(message.chat.id)+"\nИмя: "+str(message.chat.title)+"\nUserName: "+"@" +str(message.chat.username))
	print(message)

@bot.message_handler(commands=['myinfo'])
def give_me_myinfo(message):
	bot.send_message(message.chat.id, "Айди: "+str(message.from_user.id)+"\nИмя: "+str(message.from_user.first_name)+"\nUserName: "+"@" +str(message.from_user.username))
'''
@bot.message_handler(commands=['addrandom'])
def add_for_random(message):
	bot.send_message(message.reply_to_message.chat.id,"В ближайшее время вы будете добавлены в Рандом")
	bot.send_message(512177277,"@"+str(message.from_user.username))
'''


@bot.message_handler(commands=["shipping"])
def shipping(message):
	random2=["@dimagorovtsov","@Atik_8D","@KinG_Of_DeatCh","@iamdior","@schastyee_15_06","@Moy_ray_14"]#####################
	chsh1=random.choice(random2)
	random3=["@dimagorovtsov","@Atik_8D","@KinG_Of_DeatCh","@iamdior","@schastyee_15_06","@Moy_ray_14"]###################
	chsh2=random.choice(random3)
	bot.send_message(message.chat.id, "Пара выбрана\n"+str(chsh1)+" + "+str(chsh2)+"\nМожет быть рандом выберет одного и тогоже человека.Это в разработке")


@bot.message_handler(commands=['donate'])
def choice_random(message):
	bot.send_message(message.chat.id, 'Хочешь много монет?Задонать! 1р=5💰Писать @Atik_8D')




slovar={ 
'p1':0,
'p2':2
}

@bot.message_handler(commands=['switch'])
def switch_slovar(message):
	if slovar['p1']==1:
		slovar['p1']=0
	else:
		slovar['p1']=1
	bot.send_message(message.chat.id, 'Сейчас переменная = '+str(slovar['p1']))





@bot.message_handler(commands=['haveidb'])
def have_i_db(message):
	haveidb=coll.find_one({"_id": message.from_user.id})
	if haveidb==None:
		bot.send_message(message.chat.id,"Вас нет в моей базе!")
	else:
		bot.send_message(message.chat.id,"Вы есть в моей базе!")

@bot.message_handler(commands=['me'])
def money_(message):
	gmoney = coll.find_one({'_id':message.from_user.id})
	if gmoney!=None:
		bot.send_message(message.chat.id, 'Ваши монеты: '+str(gmoney['money'])+"💰")
		bot.send_message(message.chat.id,'EXP: "В РАЗРАБОТКЕ"')
		bot.send_message(message.chat.id, "Уровень кирки:"+str(gmoney["Kirka"]))


@bot.message_handler(commands=['find'])
def find_user(message):
	if message.reply_to_message!=None:
		if message.from_user.id==512177277:
			find_user_=coll.find_one({"_id": message.reply_to_message.from_user.id})
			if find_user_!=None:
				bot.send_message(message.chat.id,"Вот данные:\nМонеты: "+str(find_user_['money'])+"💰")
		else:
			bot.send_message(message.chat.id,"Вы - не админ бота!!")
	else:
		bot.send_message(message.chat.id, "Отвечай на чьё либо сообщение!!!")



@bot.message_handler(commands=['staff'])
def choice_random(message):
	gstaff=requests.post("https://api.telegram.org/bot<TOKEN>/getChatAdministrators?chat_id="+str(message.chat.id))
	print(gstaff.url)
	qwe=bot.get_chat_administrators(message.chat.id)
	bot.send_message(message.chat.id,"Администраторы чата \n"+ str(qwe))

@bot.message_handler(commands=['give'])
def give_money(message):
	if message.reply_to_message!=None:
		if message.from_user.id==512177277:
			coll.update({"_id": message.reply_to_message.from_user.id}, {"$inc": {"money": int(message.text.split(' ')[1])}} )
			bot.send_message(message.chat.id,'Монеты выданы!')
		else:
			bot.send_message(message.chat.id,"Вы - не админ бота!!")
	else:
		bot.send_message(message.chat.id, "Отвечай на чьё либо сообщение!!!")

@bot.message_handler(commands=['konkurs'])
def give_money(message):
	if message.reply_to_message!=None:
		if message.from_user.id==512177277:
			bot.send_message(message.chat.id, "Открыт конкурс на 10000💰!!!")
		
	else:
		bot.send_message(message.chat.id, "Отвечай на чьё либо сообщение!!!")



@bot.message_handler(commands=['testqwer'])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
    keyboard.add(callback_button)
    bot.send_message(message.chat.id, "Я – сообщение из обычного режима", reply_markup=keyboard)


@bot.message_handler(commands=['removeDB'])
def give_money(message):
	if message.from_user.id==512177277:
		coll.remove({})
		bot.send_message(message.chat.id,"База данных удалена!!!(Все монеты и т.д. удалены)")
	else:
		bot.send_message(message.chat.id,"Вы - не админ бота!!")

@bot.message_handler(commands=['removeK'])
def give_money(message):
	qw = coll.find_one({'_id':message.from_user.id})
	if qw['Kirka']==2:
		coll.update({"_id": message.from_user.id}, {"$inc": {"Kirka":-1}} )
		bot.send_message(message.chat.id,"Уровень кирки сброшен!")

@bot.message_handler(commands=['mining'])
def mining(message):
	miningme=coll.find_one({'_id':message.from_user.id})
	if miningme!=None:
		if miningme['Kirka']==1:
			coll.update({"_id": message.from_user.id}, {"$inc": {"money":1}} )
			bot.send_message(message.chat.id,"Вы накопали 1 монету!")
		if miningme['Kirka']==2:
			coll.update({"_id": message.from_user.id}, {"$inc": {"money":5}} )
			bot.send_message(message.chat.id,"Вы накопали 5 монет!")

@bot.message_handler(commands=['upgrade'])
def upgrade_(message):
	upgrade__=coll.find_one({'_id':message.from_user.id})
	if upgrade__!=None:
		if upgrade__['Kirka']==1:
			if upgrade__['money']>=100:
				coll.update({"_id": message.from_user.id}, {"$inc": {"money":-100}} )
				coll.update({"_id": message.from_user.id}, {"$inc": {"Kirka":1}} )
				qw = coll.find_one({'_id':message.from_user.id})
				bot.send_message(message.chat.id , "Уровень вашей кирки повышен до "+str(qw["Kirka"]))
			else:
				bot.send_message(message.chat.id,"У Вас должно быть 100💰")

		else:
			bot.send_message(message.chat.id, "У Вас на данный момент максимальный уровень кирки!")

@bot.message_handler(commands=['present'])
def give_money(message):
	if message.reply_to_message!=None:
		coll.update({"_id": message.from_user.id}, {"$inc": {"money":-int(message.text.split(' ')[1])}} )
		coll.update({"_id": message.reply_to_message.from_user.id}, {"$inc": {"money": int(message.text.split(' ')[1])}} )

	else:
		bot.send_message(message.chat.id, "Отвечай на чьё либо сообщение!!!")

@bot.message_handler(commands=['dm'])
def deletem_message(message):
	if message.reply_to_message!=None:
		bot.delete_message(message.chat.id, message.reply_to_message.message_id)

@bot.message_handler(commands=['pin'])
def deletem_message(message):
	if message.reply_to_message!=None:
		bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)

@bot.message_handler(commands=['unpin'])
def deletem_message(message):
		bot.unpin_chat_message(message.chat.id)

@bot.message_handler(commands=['staff'])
def deletem_message(message):
	x = bot.get_chat_administrators(message.chat.id)
	text = " "
	for elem in x:
		text += elem.first_name
		bot.send_message(message.chat.id, text)

'''
@bot.message_handler(commands=['pin'])
def pin(message):
	if message.reply_to_message!=None:
		bot.send_message(message.reply_to_message.chat.id, message.pinned_message.chat.id)
		print(message)
	else:
		bot.send_message(message.chat.id, "Отвечай на чьё либо сообщение!!!")horror stories
'''

'''
@bot.message_handler(commands=['find'])
def choice_random(message):
	find=coll.find({"name": "Петр"})
	if 
	bot.send_message(message.chat.id,"Дата:"+ str(date))
'''
####################################################################




################################################################

@bot.message_handler(content_types=['text'])
def text_content(message):
	user=coll.find_one({'_id':message.from_user.id})
	if user==None:
		bot.send_message(message.chat.id,("Вижу Вас впервые!Добавляю в свою базу!\n Даю 10 монет\nКирку 1 уровня(Чтоб монеты копать)!"))
		reg = { "_id": message.from_user.id, "name":message.from_user.first_name, "username":"@"+str(message.from_user.username), "money":10 ,"Kirka":1}
		coll.insert_one(reg)
	if message.reply_to_message!=None:
		if message.text.lower() == "бить":
			bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, time.time()+60)
			bot.send_message(message.chat.id, str(message.from_user.first_name)+" избил "+str(message.reply_to_message.from_user.first_name)+"\nМут на 1 минуту.")




####################################################################





bot.polling(none_stop=True)
