#importing all necessary libraries
import telebot
import os
import requests
from bs4 import BeautifulSoup
from telebot import types

#accessing website
response = f"company name   |   Trending Price   |   Revenue   |    Market Cap \n"
req = requests.get('https://www.businesstoday.in/indices/nifty-50')
with open("htmlcode.html",'w+',encoding='utf-8-sig') as htmlfile:
    htmlfile.write(req.text)
    htmlfile.seek(0)
    content = htmlfile.read()
    soup = BeautifulSoup(content,'html5lib')
    table = soup.find('div',id='sensexComponentsId')
    inform = {}
    
    if table:
        print("found")
        rows = table.find_all('a',class_='stk_tbl_tr')
        for row in rows:
            company_name = ""
            information = []
            elements = row.find_all('span',class_='stk_tbl_td')
            for element in elements:
                if element == elements[0]:
                    
                    company_name = element.find('strong').text
                    response += f"\n* {company_name}"
                elif element == elements[1]:
                    information.append(element.find('strong').text)
                    response += f"  |  {element.find('strong').text}"
                else:
                    information.append(element.text)
                    response += f"  |  {element.text}"
            inform[company_name] = information
            

    else:
        print("not found")

#super secret api key
API_KEY = '6902495965:AAEFPPVkMVE2IcrbAgf3k9XhLIvso28e3wY'
#assign bot to api key
bot = telebot.TeleBot(API_KEY)
#greeting command 
@bot.message_handler(commands = ['start'])
def start(message):
    bot.reply_to(message, "Commands : /fiftystocks or /sector.")

@bot.message_handler(commands=['fiftystocks'])
def fiftystocks(message):
    bot.send_message(message.chat.id,response)

# Command to start a filer
@bot.message_handler(commands=['sector'])
def title(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    Automobile = types.InlineKeyboardButton('Automobile', callback_data='answer_a')
    Cement = types.InlineKeyboardButton('Cement', callback_data='answer_b')
    Cigarettes = types.InlineKeyboardButton('Cigarettes', callback_data='answer_c')
    Consumer_Goods = types.InlineKeyboardButton('Consumer Goods', callback_data='answer_d')
    Energy = types.InlineKeyboardButton('Energy', callback_data='answer_e')
    Engineering = types.InlineKeyboardButton('Engineering', callback_data='answer_f')
    
    Financial_Services = types.InlineKeyboardButton('Financial Services', callback_data='answer_h')
    Information_Technology = types.InlineKeyboardButton('Information Technology', callback_data='answer_i')

    Metals_and_Mining = types.InlineKeyboardButton('Metals & Mining', callback_data='answer_k')
    Pharma = types.InlineKeyboardButton('Pharma', callback_data='answer_l')
    Shipping = types.InlineKeyboardButton('Shipping', callback_data='answer_m')
    Telecom = types.InlineKeyboardButton('Telecom', callback_data='answer_n')
    
    markup.add(Automobile,Cement,Cigarettes,Consumer_Goods,Energy,Engineering,Financial_Services,Information_Technology,
                Metals_and_Mining,Pharma,Shipping,Telecom)

    bot.send_message(message.chat.id, 'Which sector? ', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def info(callback):
    if callback.message:
        
        if callback.data == 'answer_a':
            markup = types.InlineKeyboardMarkup(row_width=1)
            Bajaj_Auto_Ltd = types.InlineKeyboardButton('Bajaj Auto Ltd.', callback_data='Bajaj Auto')
            Hero_MotoCorp_Ltd= types.InlineKeyboardButton('Hero MotoCorp Ltd.', callback_data='Hero MotoCorp')
            Eicher_Motors_Ltd= types.InlineKeyboardButton('Eicher Motors Ltd.', callback_data='Eicher Motors')
            Maruti_Suzuki_India_Ltd= types.InlineKeyboardButton('Maruti Suzuki India Ltd.', callback_data='Maruti Suzuki')
            Tata_Motors_Ltd= types.InlineKeyboardButton('Tata Motors Ltd.', callback_data='Tata Motors')
            markup.add(Bajaj_Auto_Ltd,Hero_MotoCorp_Ltd,Eicher_Motors_Ltd,Maruti_Suzuki_India_Ltd,Tata_Motors_Ltd)
            bot.send_message(callback.message.chat.id, 'Automobile', reply_markup=markup)
            
        elif callback.data == 'answer_b':
            markup = types.InlineKeyboardMarkup(row_width=1)
            Grasim_Industries_Ltd= types.InlineKeyboardButton('Grasim Industries Ltd.', callback_data='Grasim Inds')
            UltraTech_Cement_Ltd= types.InlineKeyboardButton('UltraTech Cement Ltd.', callback_data='UltraTech Cem.')
            markup.add(Grasim_Industries_Ltd,UltraTech_Cement_Ltd)
            bot.send_message(callback.message.chat.id,'Cement', reply_markup=markup)
        
        elif callback.data == 'answer_c':
            markup = types.InlineKeyboardMarkup(row_width=1)
            ITC_Ltd = types.InlineKeyboardButton('ITC Ltd.', callback_data='ITC')
            markup.add(ITC_Ltd)
            bot.send_message(callback.message.chat.id, 'Cigarettes', reply_markup=markup)
            
        elif callback.data == 'answer_d':
            markup = types.InlineKeyboardMarkup(row_width=1)
            Hindustan_Unilever_Ltd = types.InlineKeyboardButton('Hindustan Unilever Ltd.', callback_data='Hind. Unilever')
            Britannia_Industries_Ltd= types.InlineKeyboardButton('Britannia Industries Ltd.', callback_data='Britannia Inds.')
            Nestle_India_Ltd= types.InlineKeyboardButton('Nestle India Ltd.', callback_data='Nestle India')
            Titan_Company_Ltd= types.InlineKeyboardButton('Titan Company Ltd.', callback_data='Titan Company')
            Asian_Paints_Ltd= types.InlineKeyboardButton('Asian Paints Ltd.', callback_data='Asian Paints')
            markup.add(Hindustan_Unilever_Ltd,Britannia_Industries_Ltd,Nestle_India_Ltd,Titan_Company_Ltd,Asian_Paints_Ltd)
            bot.send_message(callback.message.chat.id, 'Consumer Goods', reply_markup=markup)
            
        elif callback.data == 'answer_e':
            markup = types.InlineKeyboardMarkup(row_width=1)
            Oil_and_Natural_Gas_Corporation_Ltd= types.InlineKeyboardButton('Oil & Natural Gas Corporation Ltd.', callback_data='O N G C')
            NTPC_Ltd= types.InlineKeyboardButton('NTPC Ltd.', callback_data='NTPC')
            Power_Grid_Corporation_of_India_Ltd= types.InlineKeyboardButton('Power Grid Corporation of India Ltd.', callback_data='Power Grid Corpn')
            Bharat_Petroleum_Corporation_Ltd= types.InlineKeyboardButton('Bharat Petroleum Corporation Ltd.', callback_data='B P C L')
            Reliance_Industries_Ltd= types.InlineKeyboardButton('Reliance Industries Ltd.', callback_data='Reliance Industr')
            markup.add(Oil_and_Natural_Gas_Corporation_Ltd,NTPC_Ltd,Power_Grid_Corporation_of_India_Ltd,Bharat_Petroleum_Corporation_Ltd,Reliance_Industries_Ltd)
            bot.send_message(callback.message.chat.id, 'Energy', reply_markup=markup)
            
        elif callback.data == 'answer_f':
            markup = types.InlineKeyboardMarkup(row_width=1)
            Larsen_and_Toubro_Ltd= types.InlineKeyboardButton('Larsen & Toubro Ltd.', callback_data='Larsen & Toubro')
            markup.add(Larsen_and_Toubro_Ltd)
            bot.send_message(callback.message.chat.id, 'Engineering', reply_markup=markup)
            
        elif callback.data == 'answer_h':
            markup = types.InlineKeyboardMarkup(row_width=1)
            Axis_Bank_Ltd= types.InlineKeyboardButton('Axis Bank Ltd.', callback_data='Axis Bank')
            HDFC_Bank_Ltd= types.InlineKeyboardButton('HDFC Bank Ltd.', callback_data='HDFC Bank')
            ICICI_Bank_Ltd= types.InlineKeyboardButton('ICICI Bank Ltd.', callback_data='ICICI Bank')
            IndusInd_Bank_Ltd= types.InlineKeyboardButton('IndusInd Bank Ltd.', callback_data='Fin4')
            Kotak_Mahindra_Bank_Ltd= types.InlineKeyboardButton('Kotak Mahindra Bank Ltd.' ,callback_data='Kotak Mah. Bank')
            State_Bank_of_India= types.InlineKeyboardButton('State Bank of India', callback_data='St Bk of India')
            Bajaj_Finance_Ltd= types.InlineKeyboardButton('Bajaj Finance Ltd.', callback_data='Bajaj Finance')
            Bajaj_Finserv_Ltd= types.InlineKeyboardButton('Bajaj Finserv Ltd.', callback_data='Bajaj Finserv')
            Housing_Development_Finance_Corporation_Ltd= types.InlineKeyboardButton('Housing Development Finance Corporation Ltd.', callback_data='Fin7')
            markup.add(Axis_Bank_Ltd,HDFC_Bank_Ltd,ICICI_Bank_Ltd,IndusInd_Bank_Ltd,Kotak_Mahindra_Bank_Ltd,State_Bank_of_India,Bajaj_Finance_Ltd,Bajaj_Finserv_Ltd,Housing_Development_Finance_Corporation_Ltd)
            bot.send_message(callback.message.chat.id, 'Financial Services', reply_markup=markup)
            
        elif callback.data == 'answer_i':
            markup = types.InlineKeyboardMarkup(row_width=1)
            HCL_Technologies_Ltd= types.InlineKeyboardButton('HCL Technologies Ltd.', callback_data='HCL Technologies')
            Infosys_Ltd= types.InlineKeyboardButton('Infosys Ltd.', callback_data='Infosys')
            Tata_Consultancy_Services_Ltd= types.InlineKeyboardButton('Tata Consultancy Services Ltd.', callback_data='TCS')
            Tech_Mahindra_Ltd= types.InlineKeyboardButton('Tech Mahindra Ltd.', callback_data='Tech Mahindra')
            Wipro_Ltd= types.InlineKeyboardButton('Wipro Ltd.', callback_data='Wipro')
            markup.add(HCL_Technologies_Ltd,Infosys_Ltd,Tata_Consultancy_Services_Ltd,Tech_Mahindra_Ltd,Wipro_Ltd)
            bot.send_message(callback.message.chat.id,'Information Technology', reply_markup=markup)
            
            
            
        elif callback.data == 'answer_k':
            markup = types.InlineKeyboardMarkup(row_width=1)
            Hindalco_Industries_Ltd=types.InlineKeyboardButton('Hindalco Industries Ltd.', callback_data='Hindalco Inds.')
            JSW_Steel_Ltd= types.InlineKeyboardButton('JSW Steel Ltd.', callback_data='JSW Steel')
            Tata_Steel_Ltd= types.InlineKeyboardButton('Tata Steel Ltd.', callback_data='Tata Steel')
            Coal_India_Ltd= types.InlineKeyboardButton('Coal India Ltd.', callback_data='Coal India')
            markup.add(Hindalco_Industries_Ltd,JSW_Steel_Ltd,Tata_Steel_Ltd,Coal_India_Ltd)
            bot.send_message(callback.message.chat.id, 'Metals & Mining', reply_markup=markup)
            
        elif callback.data == 'answer_l':
            markup = types.InlineKeyboardMarkup(row_width=1)
            Cipla_Ltd= types.InlineKeyboardButton('Cipla Ltd.', callback_data='Cipla')
            Dr_Reddys_Laboratories_Ltd= types.InlineKeyboardButton('Dr. Reddy’s Laboratories Ltd.', callback_data='Dr Reddy\'s Labs')
            Sun_Pharmaceutical_Industries_Ltd= types.InlineKeyboardButton('Sun Pharmaceutical Industries Ltd.', callback_data='Sun Pharma.Inds.')
            markup.add(Cipla_Ltd,Dr_Reddys_Laboratories_Ltd,Sun_Pharmaceutical_Industries_Ltd)
            bot.send_message(callback.message.chat.id, 'Pharma', reply_markup=markup)
            
        elif callback.data == 'answer_m':
            markup = types.InlineKeyboardMarkup(row_width=1)
            Adani_Ports_and_Special_Economic_Zone_Ltd= types.InlineKeyboardButton('Adani Ports and Special Economic Zone Ltd.', callback_data='Adani Enterp.')
            markup.add(Adani_Ports_and_Special_Economic_Zone_Ltd)
            bot.send_message(callback.message.chat.id, 'Shipping', reply_markup=markup)
            
        elif callback.data == 'answer_n':
            markup = types.InlineKeyboardMarkup(row_width=1)
            Bharti_Airtel_Ltd= types.InlineKeyboardButton('Bharti Airtel Ltd.', callback_data='Bharti Airtel')
            markup.add(Bharti_Airtel_Ltd)
            bot.send_message(callback.message.chat.id, 'Telecom', reply_markup=markup)
        if callback.data in inform:
            s = str(callback.data)
            x = inform[s]
            ans = f"Company name :- {s} \n"
            ans += f"Price :- {x[0]} \n"
            ans += f"Revenue :- {x[1]} \n"
            ans += f"Market Cap :- {x[2]} \n"
            bot.send_message(callback.message.chat.id,ans)
            
            
bot.polling()
