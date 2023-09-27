import wave
import Levenshtein
import vosk
import os
import re

path_list_audio = os.path.join(os.getcwd(), 'processed_audio')

# Словарь всех эталонных фраз
dict_for_levenstein = ['белая пелена лежала на полях', 'белый пар расстилается над лужами',
        'экипаж танка понял задачу', 'этот блок работает хорошо', 'начинаются степные пожары',
        'ученики поливают огород', 'тяжелый подъем закончился', 'тропинка уперлась в глинистый уступ',
        'солнце поднялось над лесом', 'в подъезде стояли санитары', 'стало известно место встречи',
        'на участке ведется наблюдение', 'в класс вошел преподаватель', 'полено раскололось надвое',
        'надо зарядить ружье', 'мать отвела ребенка в сад', 'ребята сидели на берегу',
        'в магазине продаются яблоки', 'директор сравнил доход с расходом', 'высокая рожь колыхалась',
        'цветы пестрели в долине', 'чудный запах леса освежает', 'день был удивительно хорош'
        ]

def recognize_vosk():

    # Загрузка модели локально, модель инициализируется при каждом запуске цикла, ускоряет работу
    model_path = os.path.join(os.getcwd(), 'vosk-model-ru-0.22')
    model = vosk.Model(model_path)
    recognizer = vosk.KaldiRecognizer(model, 16000)

    # Распознавания каждого файла директории, запись в отдельные файлы результаты распознавания
    for filename in os.listdir(path_list_audio):
        #Проходим по всем файлам в пути
        wf = wave.open(fr"{path_list_audio}/{filename}", "rb")
        data = wf.readframes(240000)
        while data:
            recognizer.AcceptWaveform(data)
            data = wf.readframes(240000)
        result_recognition = recognizer.FinalResult()
        result_recognition = result_recognition.replace('\\n', ' ')
        result_recognition = re.sub("[^А-Яа-я]", " ", result_recognition)
        result_recognition = ' '.join(result_recognition.split())

        return result_recognition


def levenstein(result):
    #Здесь рассчитывается расстояние Левенштейна и затем точность, но обращение происходит только к первому эталону
    # со словаря, хз, как у вас тут будет происходить обращение к серваку, просто цикл если что сделаешь
    levenstein_distance = Levenshtein.distance(str(result), dict_for_levenstein[0])
    recognition_accuracy = round((levenstein_distance/len(dict_for_levenstein[0])*100), 2)
    return recognition_accuracy
