
import os
import sys
from HTMLParser import HTMLParser
import cPickle
import zipfile

def yes_i_am_working():
    """Check the the eskytester app is installed and available."""
    assert True

def yes_my_deps_are_working():
    """Check that dependencies have been correctly sucked in."""
    TestHTMLParser()

def yes_my_data_is_installed():
    """Check that datafiles have been correctly copied over."""
    if hasattr(sys,"frozen"):
        mydir = os.path.join(os.path.dirname(sys.executable))
        assert os.path.exists(os.path.join(mydir,"data","datafile.txt"))
        lib = zipfile.ZipFile(os.path.join(mydir,"library.zip"))
        assert "eskytester/pkgdata.txt" in lib.namelist()
    else:
        mydir = os.path.dirname(__file__)
        assert os.path.exists(os.path.join(mydir,"datafile.txt"))
        assert os.path.exists(os.path.join(mydir,"pkgdata.txt"))
    

class TestHTMLParser(HTMLParser):
   def __init__(self):
       HTMLParser.__init__(self)
       self.expecting = ["html","body","p","p"]
       self.feed("<html><body><p>hi</p><p>world</p></body></html>")
   def handle_starttag(self,tag,attrs):
       assert tag == self.expecting.pop(0)


