from optparse import OptionParser
import os
import CommentDB

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
        # the basename
        self.basename = os.path.basename(filename)
        # the abslute path name 
        self.abspath = os.path.abspath(filename)
        # the abslute path name of parient folder
        self.dirname = os.path.dirname(self.abspath)
                    
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
            commentDB = CommentDB.CommentDB(commentFile.dirname)
            print "show comment of file "+ args[0]
            if options.showFullHistory:
                print "showing full history"
                print commentDB.getAllComment(commentFile.basename)
            else:
                print "showing latest comment"
                print commentDB.getLatestComment(commentFile.basename)
        elif len(args)==2:
            commentFile = CFile(args[0])
            commentDB = CommentDB.CommentDB(commentFile.dirname)
            print "add comment: \""+args[1]+"\" on file "+args[0]
            commentDB.addComment(commentFile.basename,args[1])
        else:
            print "error"
    except InvalidFileException:
        print "File does not exist"

            

