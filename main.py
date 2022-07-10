import class_vk
import class_ya

if __name__ == '__main__':
    user_id = input('Введите id пользователя Vkontakte: ')
    YATOKEN = input('Введите токен Яндекс.Диска: ')
    VKTOKEN = input('Введите токен VK: ')
    directory = input('Введите название для создания загрузочной папки: ')

    vk = class_vk.Vk(VKTOKEN, user_id, '5.131')
    ya = class_ya.Yandex(token=YATOKEN)

    dir_name = ya.create_directory(directory) #создаем папку на Яндекс.Диске
    files_list = vk.save_info('filelist.txt') #формируем список файлов
    ya.upload_file(dir_name, files_list) #загружаем файлы на Яндекс.Диск, формируем файл info.json с информацией о загруженных файлах
