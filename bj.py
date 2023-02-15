import random
random.seed()


class BlackJack:
    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'] * 4
        self.score = 0
        self.bot_score = 0

    """
        Функция выводит сообщение какая карта вам попалась и у дилера, а также количесвто очков
    """
    def print_card(self, current, score, bot):
        if not bot:
            print(f'Вам попалась карта {current}. У вас {score} очков.')
        else:
            print(f'У дилера попалась карта {current}. У дилера {score} очков')

    """
        Функция раздает карты для игрока и дилера, и добавляет очки з зависимости от карты
    """
    def random_card(self, score, bot):
        current = self.deck.pop()
        if type(current) is int:
            score += current
        elif current == 'Ace':
            if score <= 10:
                score += 11
            else:
                score += 1
        else:
            score += 10
        self.print_card(current, score, bot)
        return score

    """
        Функция рассчета победителя
        Сначала вычитывает кол очков у игрока и дилера в функции random_card
    """
    def choice(self):
        score = self.random_card(self.score, False)
        bot_score = self.random_card(self.bot_score, True)
        while True:
            print('Будете брать карту? y/n')
            choice = input()

            """
            Если вы взяли карту то:
                Если у дилера меньше 19 очков и у игрока меньше или ранвяеться 21 то он берет карту
                Если у вас больше 21 очков или у дилера равняеться 21 то вы проиграли
                Если у вас и у дилера 21 очка то ничья
                Если у вас ровно 21 очка или у дилера больше 21 то вы победили
            """

            if choice == 'y':
                score = self.random_card(score, False)
                if bot_score < 19 and score <= 21:
                    bot_score = self.random_card(bot_score, True)
                if score > 21 or bot_score == 21:
                    print('Вы проиграли')
                    break
                elif score == 21 and bot_score == 21:
                    print('ничья')
                elif score == 21 or bot_score > 21:
                    print('Вы победили!')
                    break

                """
                    Если вы отказались брать карту то дилер продолжит играть
                    Если у вас меньше очков чем у дилера и при этом у него меньше или ранво 21 то он победил, в противном случае вы победили
                """

            elif choice == 'n':
                if score > bot_score and bot_score < 19:
                    while bot_score < 19:
                        bot_score = self.random_card(bot_score, True)
                if score < bot_score <= 21:
                    print(f'Вы проиграли, у вас {score} очков, у дилера {bot_score} очков ')
                else:
                    print(f'Вы победили, у вас {score} очков, у дилера {bot_score} очков ')

                break

    """
        Фунция старта игры, где пишеться что игра началсь, и разьяснение о кол очков карт
    """
    def start(self):
        random.shuffle(self.deck)
        print('Игра в BlackJack началась')
        print('В блэкджеке десятки, валеты, дамы и короли стоят по 10 очков.')
        print('Туз может стоить 1 или 11 очков.')
        print('----------------------------------')
        self.choice()


if __name__ == "__main__":
    game = BlackJack()
    game.start()
