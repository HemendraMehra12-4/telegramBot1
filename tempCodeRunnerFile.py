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
