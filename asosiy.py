import logging
from config import API_TOKEN
from aiogram import Bot,Dispatcher,executor,types
from buttans import languages,nomer,citys,main_manyu,set5,set6,back


logging.basicConfig(level=logging.INFO)

bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f"Assalomu aleykum  {message.from_user.first_name} \n Botimizga xush kelibsiz!\n Kerakli tilni tanlang",reply_markup=languages)
    
@dp.message_handler()
async def buttons(message: types.Message):
    if message.text == "Toshkent 🏙":
        await message.answer("siz Toshkent shakrini tanladingiz\n kontaktingizni yuboring",reply_markup=nomer)
    elif message.text == "Namangan 🌃":
        await message.answer("siz Namangan shakrini tanladingiz\n kontaktingizni yuboring",reply_markup=nomer)
    elif message.text == "Buxoro 🕍":
        await message.answer("siz Buxoro shakrini tanladingiz\n kontaktingizni yuboring",reply_markup=nomer)
    elif message.text == "Samarqand 🕌":
        await message.answer("siz Samarqand shakrini tanladingiz\n kontaktingizni yuboring",reply_markup=nomer)
    
    elif message.text == "⬅️ asosiy menu":
        await message.answer("Kerakli joyni tanlang",reply_markup=main_manyu)
    elif message.text == "⬅️Ortga":
        await message.answer("menyuga qaytdingiz",reply_markup=nomer)
       



@dp.callback_query_handler(lambda a: a.data)
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    surov = callback_query.data
    if surov == "uz":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, "Siz o'zbek tilini tanladingiz.",reply_markup=citys)
    elif surov == "Bu":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,"Buyutmangizni tanlang",reply_markup=set5)
    elif surov == "bi":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,"Biz O‘zbekiston bozorida 12 yildan beri faoliyat yuritamiz va bugungi kunda butun mamlakat bo‘ylab 50 dan ortiq filiallarimizmavjud. Mazali va to‘yimli taomlar, qulay narxlar, tez yetkazib berish xizmatidan mamnun mijozlar yana va yana bizni tanlamoqda.",reply_markup=main_manyu)
    elif surov == "Fl":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,"Bizni Filiallarimiz",reply_markup=citys)
    elif surov == "So":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,"Malumotlaringizni korib chiqish uchun bo'lim !",reply_markup=set6)
    elif surov =="By":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,"Sizda hozircha buyurtmaklaringiz yoq \n Buyurtma tanlasangiz qoshib qoyamiz 🤗",reply_markup=back)
    elif surov == "L":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(callback_query.from_user.id, "https://yukber.uz/image/cache/catalog/lavash-700x700.jpg", caption="Oddiy lavash")
        await bot.send_message(callback_query.from_user.id,"Buyurtmangiz qabul qilindi [🧈 Lavash]",reply_markup=back)
    elif surov == "B":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,"Buyurtmangiz qabul qilindi [🍔 Burger]",reply_markup=back)
    elif surov == "B B":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,"Buyurtmangiz qabul qilindi [🍔🍔 Big Burger]",reply_markup=back)
    elif surov == "X":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,"Buyurtmangiz qabul qilindi [🥖 Xaggi]",reply_markup=back)
    elif surov == "P":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,"Buyurtmangiz qabul qilindi [🍕 Pitsa]",reply_markup=back)
    elif surov == "S":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,"Buyurtmangiz qabul qilindi [🧇 Sendvich]",reply_markup=back)
    elif surov == "D":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,"Buyurtmangiz qabul qilindi [🥞 Danar]",reply_markup=back)
    elif surov == "B D":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,"Buyurtmangiz qabul qilindi [🥞 🥞Big Danar]",reply_markup=back)
    elif surov == "SH":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,"Buyurtmangiz qabul qilindi [🌮 SHourma]",reply_markup=back)
    elif surov == "F":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,"Buyurtmangiz qabul qilindi [🍟 Fri]",reply_markup=back)
    elif surov == "S":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,"Buyurtmangiz qabul qilindi [🍗 Strips]",reply_markup=back)
    elif surov == "M":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,"Buyurtmangiz qabul qilindi [🌯 Monster]",reply_markup=back)
    elif surov == "cc":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,"Buyurtmangiz qabul qilindi [Coca cola 🥤]",reply_markup=back)
    elif surov == "p":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,"Buyurtmangiz qabul qilindi [Qahva ☕️]",reply_markup=back)
    elif surov == "Dinay":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,"Buyurtmangiz qabul qilindi [Dinay 🧃]",reply_markup=back)
        
        
        

    
    
    
    
    
    
        
    
    
    
if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)    

