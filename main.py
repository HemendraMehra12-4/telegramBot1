from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN: Final = '6337708022:AAGb953a-pZ9EaRszlKezFvIgjvAAU7jvbk'
BOT_USERNAME: Final= '@ech_em_bot'

#Commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting with me! I am botOfEchhem')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a bot created to answer your quesries of HM. Please ask away whatever you want to ask!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom Command!')


#Responses

def handle_response(text: str)->str:
    processed: str =text.lower()
    
    if 'hello' in processed:
        return 'Hey There!'
    
    if 'how are you' in processed:
        return 'I am good'
    
    if 'i love python' in processed:
        return 'me as well! same-pinch'
    
    return 'unable to process what you wrote'

async def handle_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type=='group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response:str = handle_response(text)
    
    
    print('Bot:',response)
    await update.message.reply_text(response)
    
    
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')



if __name__=='___main__':
    print('Welcome to the botOfEchem...') 
    
    app= Application.builder().token(TOKEN).build()
    
    #commands
    
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))

    #Messages
    
    app.add_handler(MessageHandler(filters.TEXT,handle_message))
    
    #errors
    
    app.add_error_handler(error)
    
    #polls the bot
    print('polling')
    app.run_polling(poll_interval=3)    



