from index_module import *
import os
import json

my_token = "EAACEdEose0cBANqlDZAay99cXa8oJv7R2PFovGOM3ZAzb060MS7lSIRH5cF8kK8AF92rEfJMN1V5ASUB381ypyrNdAiVQyh2trAn1KmeVhL2ZCsU2bjZAZBRoQQmAIZAW0ygvBQ6LGfY2YpHsW0DFqY879YW012StPmMdvp4Cz7ZArNZCD3zXZBRUSwNvW2lyuMgZD"
user = ['thathinhdaitoi', 'DesignerVietnam', 'BKConfessions']

index(my_token, user[2], os.path.join(os.path.dirname(__file__),'data'), 'project2_test',1)