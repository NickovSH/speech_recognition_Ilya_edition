import recognition

if __name__ == "__main__":
    result = recognition.recognize_vosk()
    print('Результат распознавания: ', result)
    recognition_accuracy = recognition.levenstein(result)
    print('Точность распознавания: ', recognition_accuracy)