import os
import requests
import json

api_address = '127.0.0.1'
api_port = 8000

# requête m1
rm1 = requests.get(
    url='http://{address}:{port}/select_model'.format(address=api_address, port=api_port),
    params= {
        "model": "Logistic regression",
        "test_data": "sample 1",
        "username":"bob"
    }
)

output_m1 = '''
============================
    Model test
============================

request done at "/select_model"
| model="Logistic regression"
| test_data="sample 1"

expected result = 200
actual result = {status_code_m1}

==>  {test_status_m1}
'''
status_code_m1 = rm1.status_code
if status_code_m1 == 200:
    test_status_m1 = 'SUCCESS'
else:
    test_status_m1 = 'FAILURE'
print(output_m1.format(status_code_m1=status_code_m1, test_status_m1=test_status_m1))

# impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output_m1)
######

# requête m2
rm2 = requests.get(
    url='http://{address}:{port}/select_model'.format(address=api_address, port=api_port),
    params= {
        'model': 'KNN',
        'test_data': 'sample 1',
        "username":"bob"
    }
)

output_m2 = '''
============================
    Model test
============================

request done at "/select_model"
| model="Random Forest"
| test_data="sample 1"

expected result = 200
actual result = {status_code_m2}

==>  {test_status_m2}
'''
status_code_m2 = rm2.status_code
if status_code_m2 == 200:
    test_status_m2 = 'SUCCESS'
else:
    test_status_m2 = 'FAILURE'
print(output_m2.format(status_code_m2=status_code_m2, test_status_m2=test_status_m2))

# impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output_m2)
######

# requête m3
rm3 = requests.get(
    url='http://{address}:{port}/select_model'.format(address=api_address, port=api_port),
    params= {
        'model': 'Random Fox Terrier',
        'test_data': 'sample 1',
        "username":"bob"
    }
)

output_m3 = '''
============================
    Model test
============================

request done at "/select_model"
| model="Random Fox Terrier"
| test_data="sample 1"

expected result = 404
actual result = {status_code_m3}

==>  {test_status_m3}
'''
status_code_m3 = rm3.status_code
if status_code_m3 == 404:
    test_status_m3 = 'SUCCESS'
else:
    test_status_m3 = 'FAILURE'
print(output_m3.format(status_code_m3=status_code_m3, test_status_m3=test_status_m3))

# impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output_m3)
######

# requête m4
rm4 = requests.get(
    url='http://{address}:{port}/select_model'.format(address=api_address, port=api_port),
    params= {
        'model': 'KNN',
        'test_data': 'sample 3',
        "username":"bob"
    }
)
print(rm4.url)
output_m4 = '''
============================
    Model test
============================

request done at "/select_model"
| model="KNN"
| test_data="sample 3"

expected result = 405
actual result = {status_code_m4}

==>  {test_status_m4}
'''
status_code_m4 = rm4.status_code
if status_code_m4 == 405:
    test_status_m4 = 'SUCCESS'
else:
    test_status_m4 = 'FAILURE'
print(output_m4.format(status_code_m4=status_code_m4, test_status_m4=test_status_m4))

# impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output_m4)
######