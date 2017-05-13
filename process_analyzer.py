import psutil
from shared_applications import SharedApplications


class ProcessAnalyzer:

    @classmethod
    def analyze(cls, pid):
        process = psutil.Process(pid)
        result = None

        for shared_application in SharedApplications().shared_applications():
            if shared_application['exec'].find(process.cmdline()[0]) is not -1\
                    or shared_application['exec'] is process.cmdline()[0]\
                    or shared_application['exec'] == process.cmdline()[0]:
                result = shared_application
                break

        return result
