from work23 import words
from random import choice

"""
sana: 12-mart 2021-yil soat=23:23
tavsif: So'z topish o'yini krill alifbosida
tuzuvchi: Haydarov Akbar
"""

def suz_ober(words):
    word = choice(words)
    while "-" in word or " " in word:
        word = choice(words)
    return word

def suzni_tekshir(word,user_letters):
    user_letter = ""
    for item in word:
        if item in user_letters:
            user_letter += item
        else:
            user_letter += "-"
    return user_letter

def play_function():
    """Bu funcksiya orqali o'yinning asosiy qismini bajarashimiz mumkin!"""
    komp_word = suz_ober(words)
    #Bu kompyuter tanlagan ixtiyoriy so'z
    set_word  = set(komp_word)
    count = camedy = 0
    # 'count' orqali biz o'yin o'ynashlar sonini aniqlashimiz mumkin
    print(f"Man {len(komp_word)} xonali so'z o'yladim. Topa olasinmi ?")
    user_letters = ""
    while set_word:
        print(suzni_tekshir(komp_word,user_letters))
        if len(user_letters) > 0:
            print(f"Hozircha kiritgan harflaringiz {user_letters}")

        count += 1
        user_letter = input("\nSo'z Kiriting ").lower()
        if user_letter in user_letters:
            print(f"'{user_letter}' bu harfni kiritgansiz, Yana urinib ko'ring")
            camedy += 1
            if camedy >5:
                print("\nNima xotirangiz shanchali pastmi :)")
            continue
        if user_letter in set_word:
            print(f"'{user_letter}' bu harf to'g'ri")
            set_word.remove(user_letter)
        else:
            print(f"Afsuski bu harf yuq")
        user_letters += user_letter
    if count <= 10:
        print(f"\nTabriklayman super o'yin {count} tada '''{komp_word}''' so'zni topdinzgiz qoyilman lekin!!!")
    elif 50 >count > 10:
        print(f"\nTabriklaymiz '''{komp_word}''' so'zni {count} ta urinishda topdinzgiz!")
    else:
        print(f"\nTabriklaymi yoki yo'qmi bilmay qoldim (Sabringizga qoyil)'''{komp_word}''' mana o'sha mashhur so'z {count} shuncha urinish bo'ldi")
play_function()