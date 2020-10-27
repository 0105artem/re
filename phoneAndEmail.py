#! python3
# phoneAndEmail.py - Finds phone numbers (russian form) and emails from clipboard, 
# then copies it into the clipboard using re and pyperclip modules.

import pyperclip
import re


# Making regular exprassion for phone nuumbers.
phoneRegex = re.compile(r'''(
    (\d|\+\d)?          # +7 или 8
    (\s|-|\.)?          # Разделитель
    (\d{3}|\(\d{3,5}\)) # Территориальный код
    (\s|-|\.)?          # Разделитель
    (\d{3})             # Первые 3 цифры после терр. кода
    (\s|-|\.)?          # Разделитель
    (\d{2})             # 2 цифры
    (\s|-|\.)?          # Разделитель
    (\d{2})?            # Последние 2 цифры
    (\s*(доб|д|доб.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

# Making regular expression for emails.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+     # Имя пользователя 
    @                     # Символ @
    [a-zA-Z0-9.-]+        # Имя домена
    (\.[a-zA-Z]{2,4})     # Домен верхнего уровня
    )''', re.VERBOSE)

# Searching for matches in the clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = ''
    if groups[1] != '':
        phoneNum += groups[1] + ' '
    if groups[9] != '':
        phoneNum += '-'.join([groups[3], groups[5], groups[7], groups[9]])
    else:
        phoneNum += '-'.join([groups[3], groups[5], groups[7]])
    
    if groups[12] != '':
        phoneNum += ' доб. ' + groups[12]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    print(groups)
    matches.append(groups[0])

# Copies results into the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Скопировано в буфер обмена:')
    print('\n'.join(matches))
else:
    print('Телефонные номера и адреса электронной почты не найдены.')

