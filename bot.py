import openai
import telebot

# write tg bot which will send asnwers to questions via chatgpt

bot = telebot.TeleBot("6211084422:AAHKwyFCKhiQVTD7c3ovvnxJlEkvEsJx0QM")
# insert chatgpt api key
openai.api_key = "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"

# write tg bot which will send asnwers to questions via chatgpt
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello, write me a question')


@bot.message_handler(content_types=['text'])
def send_text(message):
    text = message.text
    print(text)
    if text.lower() == 'hi':
        bot.send_message(message.chat.id, 'Hello, write me a question')
    else:
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": text}])
        print(response)
        bot.send_message(message.chat.id, response.choices[0].message.content)


bot.polling()
