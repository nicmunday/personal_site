#!/usr/bin/env python3
import requests
import json
import sys
import pathlib

user_input = []
URL = "https://api.freecurrencyapi.com/v1/latest"

current_path = pathlib.Path(__file__).parent
currency_file = current_path.joinpath("imports",
                                      "json",
                                      "currency_api_user_data.json")
with currency_file.open() as reader:
     headers = json.load(reader)

parameters = {
     "base_currency" : "GBP",
     "currencies" : "USD,EUR"
}

response = requests.get(URL, headers=headers, params=parameters)
return_json = response.json()
data = return_json["data"]

def get_currency():
    currency = input(f"Which currency would you like to convert? "
                     f"('EUR' / 'USD') :").upper().strip()

    if currency != "USD" and currency != "EUR":
        currency = get_currency()
    return currency
    
def get_fromTo(currency):
    fromTo = input(f"Do you want to convert to {currency} or from "
                   f"{currency}? 'from'/'to': ").lower().strip()

    if fromTo != "from" and fromTo != "to":
        fromTo = get_fromTo(currency)
        
    return fromTo

def get_amount():    
    try:
        amount = float(input("How much do you want to convert? (no "
                             "currency symbols, just a number): ").strip())
    except ValueError:
        amount = get_amount()
    return amount
    

def get_user_input():

    currency = get_currency()
    fromTo = get_fromTo(currency)
    amount = get_amount()
        
        
    return [fromTo, currency, amount]

def command_line_input():
    if sys.argv[1].lower().strip() == "from" or \
            sys.argv[1].lower().strip() == "to":
          fromTo = sys.argv[1].lower().strip()
    else:
        user_input = get_user_input()
        return user_input
        
    if sys.argv[2].upper().strip() == "USD"or \
            sys.argv[2].upper().strip() == "EUR":
        currency = sys.argv[2].upper().strip()
    else:
        user_input = get_user_input()
        return user_input
    try:
        amount = float(sys.argv[3].strip())

    except ValueError as error:
        user_input = get_user_input()
        return user_input
        
    return [fromTo, currency, amount]
         


if len(sys.argv) == 4:
    user_input = command_line_input()
else:
    user_input = get_user_input()
    
if len(user_input) == 3:
    fromTo, currency, amount = \
        [item for item in user_input]

if fromTo == "from":
     result_amount = amount/data[f"{currency}"]
     print(f"\n\n                      "
           f"{amount} {currency} is currently "
           f"{round(result_amount, 2)} GBP\n\n")

elif fromTo == "to":
     result_amount = amount*data[f"{currency}"]
     print(f"\n\n                            "
           f"{amount} GBP is currently "
           f"{round(result_amount, 2)} {currency} \n\n")
else:
    user_input = get_user_input()
