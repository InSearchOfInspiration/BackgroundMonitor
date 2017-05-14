from singleton import Singleton
import os


class SharedApplications(metaclass=Singleton):
    __APPLICATIONS = None
    __PATH = '/usr/share/applications'
    __USER_PATH = os.path.expanduser('~')+'/.local/share/applications'
    __DESKTOP_EXTENSIONS_FILE_NAME = 'Name='
    __DESKTOP_EXTENSIONS_EXEC = 'Exec='

    @classmethod
    def shared_applications(cls):
        if cls.__APPLICATIONS is None:
            f = []
            f.extend(cls.__get_shared_application(cls.__PATH))
            f.extend(cls.__get_shared_application(cls.__USER_PATH))

            cls.__APPLICATIONS = f

        return cls.__APPLICATIONS

    @classmethod
    def __get_shared_application(cls, path):
        result = []
        for (dirpath, dir, filenames) in os.walk(path):
            for filename in filenames:
                if filename.endswith('.desktop'):
                    file_info = {}
                    file = open(os.path.join(dirpath, filename), 'r')
                    for line in file:
                        number = line.find(cls.__DESKTOP_EXTENSIONS_FILE_NAME)
                        if number is not -1:
                            file_info['name'] = line[number + len(cls.__DESKTOP_EXTENSIONS_FILE_NAME):].replace('\n', '')

                        number = line.find(cls.__DESKTOP_EXTENSIONS_EXEC)
                        if number is not -1:
                            file_info['exec'] = line[number + len(cls.__DESKTOP_EXTENSIONS_EXEC):].replace('\n', '')
                    file.close()
                    result.append(file_info)
            break

        return result
