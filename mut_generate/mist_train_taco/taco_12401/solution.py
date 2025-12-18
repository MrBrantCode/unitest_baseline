"""
QUESTION:
You are currently in the United States of America. The main currency here is known as the United States Dollar (USD). You are planning to travel to another country for vacation, so you make it today's goal to convert your USD (all bills, no cents) into the appropriate currency. This will help you be more prepared for when you arrive in the country you will be vacationing in.

Given an integer (`usd`) representing the amount of dollars you have and a string (`currency`) representing the name of the currency used in another country, it is your task to determine the amount of foreign currency you will receive when you exchange your United States Dollars.

However, there is one minor issue to deal with first. The screens and monitors at the Exchange are messed up. Some conversion rates are correctly presented, but other conversion rates are incorrectly presented. For some countries, they are temporarily displaying the standard conversion rate in the form of a number's binary representation! 

You make some observations. If a country's currency begins with a vowel, then the conversion rate is unaffected by the technical difficulties. If a country's currency begins with a consonant, then the conversion rate has been tampered with.

Normally, the display would show 1 USD converting to 111 Japanese Yen. Instead, the display is showing 1 USD converts to 1101111 Japanese Yen. You take it upon yourself to sort this out. By doing so, your 250 USD rightfully becomes 27750 Japanese Yen.

`
function(250, "Japanese Yen") => "You now have 27750 of Japanese Yen."
`

Normally, the display would show 1 USD converting to 21 Czech Koruna. Instead, the display is showing 1 USD converts to 10101 Czech Koruna. You take it upon yourself to sort this out. By doing so, your 325 USD rightfully becomes 6825 Czech Koruna.

`
function(325, "Czech Koruna") => "You now have 6825 of Czech Koruna."
`

Using your understanding of converting currencies in conjunction with the preloaded conversion-rates table, properly convert your dollars into the correct amount of foreign currency.

```if:javascript,ruby
Note: `CONVERSION_RATES` is frozen.
```
"""

def convert_currency(usd, currency):
    # Conversion rates dictionary
    CONVERSION_RATES = {
        'Ar': 478, 'Ba': 82, 'Cr': 6, 'Cz': 21, 'Do': 48, 'Ph': 50, 'Uz': 10000, 
        'Ha': 64, 'Gu': 7, 'Ta': 32, 'Ro': 4, 'Eg': 18, 'Vi': 22573, 'In': 63, 
        'Ni': 31, 'Ve': 10, 'No': 8, 'Ja': 111, 'Sa': 3, 'Th': 32, 'Ke': 102, 'So': 1059
    }
    
    # Check if the currency name starts with a vowel or consonant
    first_letter = currency[0].lower()
    is_vowel = first_letter in 'aeiou'
    
    # Get the conversion rate based on the first two letters of the currency name
    rate_key = currency[:2]
    conversion_rate = CONVERSION_RATES.get(rate_key, 0)
    
    # If the currency starts with a consonant, convert the binary rate to decimal
    if not is_vowel:
        conversion_rate = int(str(conversion_rate), 2)
    
    # Calculate the converted amount
    converted_amount = usd * conversion_rate
    
    # Return the formatted string
    return f'You now have {converted_amount} of {currency}.'