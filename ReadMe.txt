Привет, пользователь бота BinanceImpulseViewer!

Чтобы включить бота, нужно два раза кликнуть на файл Run.bat

У бота две функции: поиск импульсов и добавление пар в черный список.
Поиск импульсов может осуществляться в любое время с одной команды - фильтра поиска формата (5% 2% 5m)



Где первое значение - искомый импульс,
Второе значение - задаваемый Вами процент продажи/покупки актива,
Третье значение - ТаймФрейм, на котором бот будет искать импульсы (обратите внимание, время указывается английским символом m/h/s/d, как и на самой бирже)
Существующие ТФ для бота: 1s 1m 3m 5m 10m 15m 20m 25m 30m 1h 2h 4h 6h 8h 12h 1d (при вводе пользовательского таймфрейма, произойдет исключение-ошибка)

Бот не следит за таймфреймами на Бинансе, но задает свой таймфрейм с начала поискаъ
В результате бот выдает информацию о цене закрытия предыдущей свечи, цене открытия на текущей свече, текущей цене актива, название пары и процент продажи/покупки
Блэк-лист работает по такой же схеме - нужно написать простым сообщением название пары (регистр неважен) и сообщения об импульсах этой пары больше не будут Вам приходить.
Возможные ошибки (исключения):
1. Если некорректно ввести данные фильтра поиска, то сработает исключение, бот продолжит работу, но попросит ввести корректные данные
2. Если некорректно ввести данные о паре, которую вы хотите добавить в черный список, просто напишите название пары заново и правильно, исключений и ошибок не произойдет, но от некорректного ввода в черный список добавится другое значение.
3. При отказе бота от работы или другого рода возникающих ошибках пишите в телеграм - @mikebelly

Удачного пользования и удачной проверки стратегий!
