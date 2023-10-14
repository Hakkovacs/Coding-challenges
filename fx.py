from forex_python.converter import CurrencyCodes, CurrencyRates

cc = CurrencyCodes()
cr = CurrencyRates()

#test

print ("\n\n |EUR - Euro Member Countries |IDR - Indonesia Rupiah |BGN - Bulgaria Lev |ILS - Israel Shekel |GBP - United Kingdom Pound |DKK - Denmark Krone |CAD - Canada Dollar |JPY - Japan Yen |HUF - Hungary Forint |RON - Romania New Leu |MYR - Malaysia Ringgit |SEK - Sweden Krona |SGD - Singapore Dollar |HKD - Hong Kong Dollar |AUD - Australia Dollar |CHF - Switzerland Franc |KRW - Korea (South) Won |CNY - China Yuan Renminbi |TRY - Turkey Lira |HRK - Croatia Kuna |NZD - New Zealand Dollar |THB - Thailand Baht |USD - United States Dollar |NOK - Norway Krone |RUB - Russia Ruble |INR - India Rupee |MXN - Mexico Peso |CZK - Czech Republic Koruna |BRL - Brazil Real |PLN - Poland Zloty |PHP - Philippines Peso |ZAR - South Africa Rand \n\n" )

amount = int(input("Please enter the amount you want to convert: "))

from_currency = input("Please enter the currency code that has to be converted: ").upper()

to_currency = input("Please enter the currency code to convert: ").upper()

output = cr.convert(from_currency, to_currency, amount)
er = cr.get_rate(from_currency, to_currency)
formatted_er = f"{er:.4f}"
formatted_output = f"{output:.2f}"


print("\n\nYou are converting", amount, cc.get_symbol(from_currency), "to", cc.get_symbol(to_currency),".")
print("The exchange rate is:", formatted_er)
print("The converted amount is:", formatted_output)



