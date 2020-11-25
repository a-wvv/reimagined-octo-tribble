class FirstPageLocators():
    CHECKBOX_VALUE = '[data-answer-value="Check this"]'
    MONTH_FIELD = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input'
    MOUNTH_NAME_FIELD = 'div.quantumWizTextinputPaperinputEl:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)'
    NEXT_BUTTON = '.appsMaterialWizButtonPaperbuttonLabel.quantumWizButtonPaperbuttonLabel'


class SecondPageLocators():
    MOVIE_FIELD = '.quantumWizTextinputPapertextareaInput'
    COLOR_LIST = 'div.quantumWizMenuPaperselectOption:nth-child(1)'
    NEXT_BUTTON = 'div.appsMaterialWizButtonEl:nth-child(2) > span:nth-child(3) > span:nth-child(1)'
    PREV_BUTTON = 'div.appsMaterialWizButtonEl:nth-child(1) > span:nth-child(3) > span:nth-child(1)'


class ThridPageLocators():
    RADIOBOX = '#i5 > div:nth-child(3) > div:nth-child(1)'
    SUBMIT = 'div.appsMaterialWizButtonEl:nth-child(2) > span:nth-child(3) > span:nth-child(1)'
