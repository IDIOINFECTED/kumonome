# kumonome
Простенький скрипт для поиска случайных видео с Youtube
![intro](https://github.com/IDIOINFECTED/kumonome/assets/161202764/d3d81ebb-a0a1-4375-9a99-65f6c07534dd)

Писался изначально just4lulz за один вечер. Тем не менее, вроде как работает, так что пускай будет и здесь.

Из-за того, что мне приспичило поиграться с asciimatics, нормально запускается только через командную строку:

  >python kumonome.py (--ql --docx --maxviews)
>

Работает путём парсинга поискового запроса с тегом "inurl:" и переданным в него некоторым количеством рандомных символов(задаётся с помощью --ql, значение по умолчанию равно 5). С json я работать не особо умею, да и API с моими потрясающими навыками написания кода порой начинает глючить, так что вытаскиваются данные напрямую из текста страницы поисковой выдачи. "Собирает" только видео, где меньше 2000 просмотров(можно задать своё значение флажком --maxviews). Изначальная задумка - поиск малоизвестного рандомного контента. В планах добавить режимы для поиска каналов и плейлистов, а также изучить другие видеохостинги вроде Vimeo и возможность написания подобного алгоритма к ним(если не заброшу, конечно).

Остановка "классическим" Ctrl+C, анимированное "интро" можно пропустить пробелом.

Записывает найденное в txt файл. Может записывать в .docx вытаскивая превьюшки, однако работает данная штука не очень стабильно. Запись в .docx включается с помощью --docx=1  при вызове скрипта.
![Screenshot_1](https://github.com/IDIOINFECTED/kumonome/assets/161202764/6e32aece-12c7-43f0-905b-4e359f3459b9)
