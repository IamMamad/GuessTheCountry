import random


class countryG:

    def randomCountry(self):
        countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Anguilla", "Antarctica", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahrain", "Bahamas", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bonaire", "Botswana", "Brazil", "Bulgaria", "Burundi", "Cambodia", "Cameroon", "Canada", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Congo", "Croatia", "Cuba", "Cyprus", "Denmark", "Djibouti", "Dominica", "Ecuador", "Egypt", "Eritrea", "Estonia", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guernsey", "Guinea", "Guyana", "Haiti", "Vatican", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jersey", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea", "Kuwait", "Kyrgyzstan", "Lao", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macao", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "Nicaragua", "Niger", "Nigeria", "Niue", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Samoa", "Arabia", "Senegal", "Serbia", "Seychelles", "Singapore", "Slovakia", "Slovenia", "Somalia", "Spain", "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tokelau", "Tonga", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "Emirates", "England", "America", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Yemen", "Zambia", "Zimbabwe"]
        country = random.choice(countries)
        country = country.lower()
        return country

    def setRight(self):
        rightGuesses = ""
        for letter in self.country:
            rightGuesses += "-"
        return rightGuesses

    def __init__(self):
        self.country = self.randomCountry()
        self.rightGuesses = self.setRight()
        self.wrongGuesses = ""

    def isGameOver(self):
        gameOver = False
        countryLen = len(self.country)
        wrongLen = len(self.wrongGuesses)
        print(countryLen,wrongLen)
        if self.rightGuesses == self.country or countryLen <= wrongLen:
            gameOver = True
        return gameOver

    def check(self, guess):
        i = 0
        isAGoodGuess = False
        while i < len(self.country):
            if self.country[i] == guess:
                isAGoodGuess = True
                rg = list(self.rightGuesses)
                rg[i] = self.country[i]
                self.rightGuesses = "".join(rg)
            i += 1
        if not isAGoodGuess: 
            self.wrongGuesses += guess

    def hint(self):
        self.wrongGuesses += "**"
        i = 0   # counter
        possibleHelps = []
        while i < len(self.country):
            if self.country[i] != self.rightGuesses[i]:
                possibleHelps.append(i)
            i += 1
        i = random.choice(possibleHelps)
        return self.country[i]