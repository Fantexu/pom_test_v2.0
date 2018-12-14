import os
from base.baseYaml import get_tuple

dirpath = os.path.dirname(__file__)
LOGIN_ELEMENT = get_tuple(dirpath+'/loginElement.yaml')
HOME_ELEMENT = get_tuple(dirpath+'/homeElement.yaml')


HH_ELEMENT = get_tuple(dirpath+'/hhElement.yaml')