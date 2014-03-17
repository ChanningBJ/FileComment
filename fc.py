from optparse import OptionParser
import os

class InvalidFileException(Exception):
    """
    """
    pass
        
        


class File(object):
    """
    """
    File = 0
    Folder = 1
    
    def __init__(self, filename):
        """
        """
        if os.path.exists(filename)==False:
            raise InvalidFileException
        self._path
        if os.path.isfile(filename):
            self._type = FileType.File
        else:
            self._type = FileType.Folder
                    
    def isFolder(self, ):
        return self._type==FileType.Folder

    def isFile(self,):
        return self._type==FileType.File


def checkFolderOrFile(path):
    """
    Return "File"/"Folder", will return None if the path is not valid
    """
    pass


if __name__ == '__main__':
    parser = OptionParser(usage="Usage: %prog [options] [file name] [comment message]", version="%prog v1.0")
    parser.add_option("-f", "--full", action="store_true", dest="showFullHistory", default=False, help="Display all comments history")

    (options, args) = parser.parse_args()
    try:
        if len(args)==1:
            print "show comment of file "+ args[0]
        elif len(args)==2:
            print "add comment: \""+args[1]+"\" on file "+args[0]
        else:
            print "error"
    except InvalidFileException:
        print "File does not exist"

            

