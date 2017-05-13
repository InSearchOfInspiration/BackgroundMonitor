from singleton import Singleton
import os


class SharedApplications(metaclass=Singleton):
    __APPLICATIONS = None
    __PATH = '/usr/share/applications'
    __DESKTOP_EXTENSIONS_FILE_NAME = 'Name='
    __DESKTOP_EXTENSIONS_EXEC = 'Exec='

    @classmethod
    def shared_applications(cls):
        if cls.__APPLICATIONS is None:
            f = []
            for (dirpath, dir, filenames) in os.walk(cls.__PATH):
                for filename in filenames:
                    if filename.endswith('.desktop'):
                        file_info = {}
                        file = open(os.path.join(dirpath, filename), 'r')
                        for line in file:
                            number = line.find(cls.__DESKTOP_EXTENSIONS_FILE_NAME)
                            if number is not -1:
                                file_info['name'] = line[number+len(cls.__DESKTOP_EXTENSIONS_FILE_NAME):].replace('\n', '')

                            number = line.find(cls.__DESKTOP_EXTENSIONS_EXEC)
                            if number is not -1:
                                file_info['exec'] = line[number+len(cls.__DESKTOP_EXTENSIONS_EXEC):].replace('\n', '')
                        file.close()
                        f.append(file_info)
                break
            cls.__APPLICATIONS = f

        return cls.__APPLICATIONS
