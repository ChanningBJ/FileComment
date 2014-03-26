from optparse import OptionParser
import os

class InvalidFileException(Exception):
    """
    """
    pass
        
        


class CFile(object):
    """
    """
    File = 0
    Folder = 1
    
    def __init__(self, filename):
        """
        """
        if os.path.exists(filename)==False:
            raise InvalidFileException
        if os.path.isfile(filename):
            self._type = CFile.File
        else:
            self._type = CFile.Folder
                    
    def isFolder(self, ):
        return self._type==CFile.Folder

    def isFile(self,):
        return self._type==CFile.File



if __name__ == '__main__':
    parser = OptionParser(usage="Usage: %prog [options] [file name] [comment message]", version="%prog v1.0")
    parser.add_option("-f", "--full", action="store_true", dest="showFullHistory", default=False, help="Display all comments history")

    (options, args) = parser.parse_args()
    try:
        if len(args)==1:
            commentFile = CFile(args[0])
            print "show comment of file "+ args[0]
            if options.showFullHistory:
                print "showing full history"
            else:
                print "showing latest comment"
        elif len(args)==2:
            commentFile = CFile(args[0])
            print "add comment: \""+args[1]+"\" on file "+args[0]
        else:
            print "error"
    except InvalidFileException:
        print "File does not exist"

            

