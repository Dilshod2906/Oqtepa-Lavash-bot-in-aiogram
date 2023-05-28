from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove

uz = InlineKeyboardButton(text="O'zbek tili ",callback_data="uz")
ru = InlineKeyboardButton(text="Rus tili ",callback_data="ru")


manzil = KeyboardButton(text="manzilni kirting 🕹 ",request_location=True)
languages = InlineKeyboardMarkup().add(uz,ru)

shahar = KeyboardButton(text="🌆 Shaharni tanlang")
kontakt = KeyboardButton(text="☎️ kontaktni yuboring",request_contact=True)
qaytish = KeyboardButton(text="⬅️Ortga")
back = ReplyKeyboardMarkup(resize_keyboard=True).add(qaytish)



set6 = ReplyKeyboardMarkup(resize_keyboard=True).add(manzil).add(kontakt)

menyu = KeyboardButton(text="⬅️ asosiy menu")

btn1 = InlineKeyboardButton(text="🛒Buyurtma berish",callback_data="Bu")
btn2 = InlineKeyboardButton(text="📄Biz haqimizda",callback_data="bi")
btn3 = InlineKeyboardButton(text="🛍 Buyurtmalarim",callback_data="By")
btn4 = InlineKeyboardButton(text="🏘 Fliallarimiz",callback_data="Fl")
btn5 = InlineKeyboardButton(text="✍️ Fikr Bildirish",callback_data="Fi")
btn6 = InlineKeyboardButton(text="⚙️ Sozlamalar",callback_data="So")








str1 = InlineKeyboardButton(text="🧈 Lavash",callback_data="L")
str2 = InlineKeyboardButton(text="🍔 Burger",callback_data="B")
str3 = InlineKeyboardButton(text="🍔🍔 Big Burger",callback_data="B B")
str4 = InlineKeyboardButton(text="🥖 Xaggi",callback_data="X")
str5 = InlineKeyboardButton(text="🍕 Pitsa",callback_data="P")
str6 = InlineKeyboardButton(text="🧇 Sendvich",callback_data="S")
str7 = InlineKeyboardButton(text="🥞 Danar",callback_data="D")
str8 = InlineKeyboardButton(text="🥞 🥞Big Danar",callback_data="B D")
str9 = InlineKeyboardButton(text="🌮 SHourma",callback_data="SH")
str10 = InlineKeyboardButton(text="🍟 Fri",callback_data="F")
str11 = InlineKeyboardButton(text="🍗 Strips",callback_data="S")
str12 = InlineKeyboardButton(text="🌯 Monster",callback_data="M")
btn7 = InlineKeyboardButton(text="Coca cola 🥤",callback_data="cc")
btn8 = InlineKeyboardButton(text="Qahva ☕️",callback_data="p")
btn9 = InlineKeyboardButton(text="Dinay 🧃",callback_data="Dinay")

set5 = InlineKeyboardMarkup().add(str1,str2,str3,str4,str5,str6,str7,str8,str9,str10,str11,str12,btn7,btn8,btn9)






son1 = KeyboardButton(text="Toshkent 🏙")
son2 = KeyboardButton(text="Namangan 🌃")
son3 = KeyboardButton(text="Buxoro 🕍")
son4 = KeyboardButton(text="Samarqand 🕌")

citys = ReplyKeyboardMarkup(resize_keyboard=True).add(son1).add(son2).add(son3).add(son4)
# son1 = ReplyKeyboardMarkup(resize_keyboard=True).add(menyu)

main_manyu = InlineKeyboardMarkup().add(btn1,btn2,btn3,btn4,btn5,btn6)


nomer = ReplyKeyboardMarkup(resize_keyboard=True).add(kontakt).add(menyu)
