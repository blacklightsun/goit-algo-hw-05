# goit-algo-hw-05
Алгоритми пошуку (ДЗ 5)

## Завдання 2

Характеристика текстів для пошуку:
Текст1 - довжина 12658 символів,
Текст2 - довжина 18400 символів.

Характеристика підрядка пошуку:
Довжина для всіх типів - 500 символів.

Неіснуючий підрядок формується рандомно з ASCII-символів з діапазону кодів символів 48-122.

Гіпотези для перевірки:
1. Чим далі в тексті розташований підрядок пошуку, тим довше буде пошук.
2. Час пошуку неіснуючого підрядку буде менше, ніж час існуючого підрядка, через те, що коли алгоритм не знаходить початкові символи підрядка, він не перевіряє залишок підрядку на входження.

### Експеримент 1
Стартова позиція розташування існуючого підрядка = 3000.

Час 1000 пошуків (text1, real_substring1) по методу 'kmp_search          ' склав 0.57009 секунд.

Час 1000 пошуків (text1, real_substring1) по методу 'boyer_moore_search  ' склав 0.1356 секунд.

Час 1000 пошуків (text1, real_substring1) по методу 'rabin_karp_search   ' склав 3.43711 секунд.

******************************************************************************************************
Час 1000 пошуків (text1, fake_substring) по методу 'kmp_search          ' склав 1.51676 секунд.

Час 1000 пошуків (text1, fake_substring) по методу 'boyer_moore_search  ' склав 0.05929 секунд.

Час 1000 пошуків (text1, fake_substring) по методу 'rabin_karp_search   ' склав 6.85973 секунд.

******************************************************************************************************
Час 1000 пошуків (text2, real_substring2) по методу 'kmp_search          ' склав 0.55923 секунд.

Час 1000 пошуків (text2, real_substring2) по методу 'boyer_moore_search  ' склав 0.14102 секунд.

Час 1000 пошуків (text2, real_substring2) по методу 'rabin_karp_search   ' склав 3.43295 секунд.

******************************************************************************************************
Час 1000 пошуків (text2, fake_substring) по методу 'kmp_search          ' склав 2.12428 секунд.

Час 1000 пошуків (text2, fake_substring) по методу 'boyer_moore_search  ' склав 0.06439 секунд.

Час 1000 пошуків (text2, fake_substring) по методу 'rabin_karp_search   ' склав 9.1061 секунд.

******************************************************************************************************

### Експеримент 2
Стартова позиція розташування існуючого підрядка = 11000.

Час 1000 пошуків (text1, real_substring1) по методу 'kmp_search          ' склав 1.60982 секунд.

Час 1000 пошуків (text1, real_substring1) по методу 'boyer_moore_search  ' склав 0.20506 секунд.

Час 1000 пошуків (text1, real_substring1) по методу 'rabin_karp_search   ' склав 6.37855 секунд.

******************************************************************************************************
Час 1000 пошуків (text1, fake_substring) по методу 'kmp_search          ' склав 1.487 секунд.

Час 1000 пошуків (text1, fake_substring) по методу 'boyer_moore_search  ' склав 0.05188 секунд.

Час 1000 пошуків (text1, fake_substring) по методу 'rabin_karp_search   ' склав 6.79637 секунд.

******************************************************************************************************
Час 1000 пошуків (text2, real_substring2) по методу 'kmp_search          ' склав 1.72539 секунд.

Час 1000 пошуків (text2, real_substring2) по методу 'boyer_moore_search  ' склав 0.21429 секунд.

Час 1000 пошуків (text2, real_substring2) по методу 'rabin_karp_search   ' склав 6.52329 секунд.

******************************************************************************************************
Час 1000 пошуків (text2, fake_substring) по методу 'kmp_search          ' склав 2.14717 секунд.

Час 1000 пошуків (text2, fake_substring) по методу 'boyer_moore_search  ' склав 0.06084 секунд.

Час 1000 пошуків (text2, fake_substring) по методу 'rabin_karp_search   ' склав 8.98172 секунд.

******************************************************************************************************

## Висновки
1. Дійсно, чим далі в тексті розташований підрядок пошуку, тим довше буде пошук. Гіпотеза підтверждення для всіх алгоритмів. При цьому час пошуку алгоритма Боєра-Мура зростає менше ніж в два рази (десь +30-50%), алгоритма КМП - зростає майже в три рази, а Рабіна-Карпа - зростає майже в два рази. При цьому існуючий підрядок у дрегому експерименті розташований далі у 3,67 рази далі ніж в першому експерименті.
2. Час пошуку неіснуючого підрядка дійсно менше, ніж існуючого (в рази), але тільки для алгоритму Боєра-Мура (при цьому скас скоротився трохи більше ніж в два рази). Для двох інших алгоритмів час пошуку неіснуючого підрядка співставний з часом пошуку підрядка, розташованого в кінці тексту. Емпірчно це підтверджує теоретичну складність алгоритму Боєра-Мура = O(n), що коли коли жоден символ підрядка не збігається з символами тексту, змушуючи алгоритм робити максимальний можливий зсув при кожній невдалій спробі знаходження збігу.
3. Найменший час пошуку показав алгоритм Боєра-Мура як для існуючого підрядка, так і для неіснуючого. Найбільший час пошуку показав алгоритм Рабіна-Карпа. Такі результати відповідають теоретичним оцінкам часової складності: Боєра-Мура - в найкращому випадку часова складність = О(𝑛) (в найгіршому O(n⋅m)), КМП - завжди O(n+m), Рабіна-Карпа - У середньому випадку та в найкращому випадку O(n+m) (в найгіршому O(n⋅m)).
4. Також треба відзначити суутєву відміннсть часу пошуку. На прикладі тексту1 в умовах експерименту 1: алгоритм КМП - в 4-25 раз, а алгоритм Рабіна-Карпа - в 25-114 раз повільнише ніж алгоритм Боєра-Мура.
