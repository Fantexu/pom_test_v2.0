import os
from base.baseYaml import *
from base.baseTxt import get_txt

LOGIN_URL = 'http://localhost/index.php/Home/user/login.html'
LOGIN_DATA = get_testdata(os.path.dirname(__file__)+'/loginData.yaml', 'phone', 'password', 'code')
HOME_URL = 'http://localhost/index.php'


LOGIN_DATA_TXT = get_txt(os.path.dirname(__file__)+'/data.txt')

