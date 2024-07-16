import telebot
from PIL import Image
import io
from telebot import types


TOKEN = "7131166100:AAFE6iXmjs8o7FfU60o3A8KeN-C6UGrh7-w"
# bot: https://t.me/imgreziserbot


class ImageResizerBot(telebot.TeleBot):
    def __init__(self, token):
        super().__init__(token)
        self.__token = token
        self.__admin_chat_id = '5547740249'
        self.user_data = {}

        @self.message_handler(commands=['start'])
        def send_welcome(message):
            self.send_message(self.__admin_chat_id,
                              f"Start bosildi: @{message.from_user.username} ({message.chat.id})")
            self.send_message(message.chat.id, "Salom! Rasmni yuboring va men uning o'lchamini o'zgartirib qaytaraman.")

        @self.message_handler(content_types=['photo'])
        def handle_image(message):
            file_id = message.photo[-1].file_id
            file_info = self.get_file(file_id)
            file = self.download_file(file_info.file_path)

            self.user_data[message.chat.id] = {'file': file}

            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('3x4', '9:16', '16:9')
            self.send_message(message.chat.id, "O'lchamni tanlang:", reply_markup=markup)

        @self.message_handler(content_types=['text'])
        def handle_text(message):
            chat_id = message.chat.id
            if chat_id in self.user_data:
                if 'file' in self.user_data[chat_id]:
                    file = self.user_data[chat_id]['file']
                    if message.text == '3x4':
                        new_size = (300, 400)
                    elif message.text == '9:16':
                        new_size = (90, 160)
                    elif message.text == '16:9':
                        new_size = (160, 90)
                    else:
                        self.send_message(chat_id, "Noto'g'ri o'lcham tanlandi.")
                        return

                    image = Image.open(io.BytesIO(file))

                    resized_image = image.resize(new_size)

                    byte_io = io.BytesIO()
                    resized_image.save(byte_io, 'PNG')
                    byte_io.seek(0)

                    self.send_photo(chat_id, byte_io)
                    self.send_message(chat_id, "Bizning botdan foydalanganingiz uchun raxmat!")

                    del self.user_data[chat_id]

    def run(self):
        self.polling(none_stop=True)


bot = ImageResizerBot(TOKEN)
bot.run()
