from Y_data import y_scap

with y_scap() as bot:
    bot.get_home_page()
    bot.search_channel()
