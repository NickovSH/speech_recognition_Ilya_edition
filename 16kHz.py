import os

path_list_input = os.path.join(os.getcwd(), 'audio')
path_list_output = os.path.join(os.getcwd(), 'processed_audio')

# Проходим по указанному пути и меняем частоту дискретизации на 16 кГц
for filename in os.listdir(path_list_input):
    print(path_list_input)
    os.system(fr'ffmpeg -i {path_list_input}/{filename} -ar 16000 {path_list_output}/{filename}.wav')