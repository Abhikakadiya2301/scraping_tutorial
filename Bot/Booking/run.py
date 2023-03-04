from booking import Booking

with Booking() as bot:
    bot.land_first_page()
    #bot.currency_change()
    bot.select_place_to_go('VRINDAVAN')
    #bot.select_date()

