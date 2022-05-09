import os
import requests
import json


api_address = '127.0.0.1'
api_port = 8000

ra = requests.get(
    url='http://{address}:{port}/Login'.format(address=api_address, port=api_port),
    params= {
        'credentials.username': 'alice',
        'credentials.password': 'wonderland'
    }
)
print(ra)

output_a = '''
============================
    Authorization test
============================

request done at "/Login"
| username="alice"
| password="wonderland"

expected result = 200
actual result = {status_code_a}

==>  {test_status_a}
'''

status_code_a = ra.status_code

if status_code_a == 200:
    test_status_a = 'SUCCESS'
else:
    test_status_a = 'FAILURE'
#print(output_a.format(status_code_a=status_code_a, test_status_a=test_status_a))

# impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output_a)
######

# requête
rb = requests.get(
    url='http://{address}:{port}/Login'.format(address=api_address, port=api_port),
    params= {
        'username': 'bob',
        'password': 'builder'
    }
)


output_b = '''
============================
    Authorization test
============================

request done at "/Login"
| username="bob"
| password="builder"

expected result = 200
actual restult = {status_code_b}

==>  {test_status_b}

'''


# statut de la requête
status_code_b = rb.status_code

# affichage des résultats
if status_code_b == 200:
    test_status_b = 'SUCCESS'
else:
    test_status_b = 'FAILURE'
#print(output_b.format(status_code_b=status_code_b, test_status_b=test_status_b))

# impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output_b)
######

# requête
rc = requests.get(
    url='http://{address}:{port}/Login'.format(address=api_address, port=api_port),
    params= {
        'username': 'Jean-Marcel',
        'password': 'Hello'
    }
)

output_c = '''
============================
    Authorization test
============================

request done at "/Login"
| username="Jean-Marcel"
| password="Hello"

expected result = 403
actual restult = {status_code_c}

==>  {test_status_c}
'''

# statut de la requête
status_code_c = rc.status_code

# affichage des résultats
if status_code_c == 403:
    test_status_c = 'SUCCESS'
else:
    test_status_c = 'FAILURE'
#print(output_c.format(status_code_c=status_code_c, test_status_c=test_status_c))

# impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output_c)
######

# requête
rd = requests.get(
    url='http://{address}:{port}/Login'.format(address=api_address, port=api_port),
    params= {
        'username': 'Alice',
        'password': 'Hello'
    }
)

output_d = '''
============================
    Authorization test
============================

request done at "/Login"
| username="Alice"
| password="Hello"

expected result = 403
actual restult = {status_code_d}

==>  {test_status_d}
'''

# statut de la requête
status_code_d = rd.status_code

# affichage des résultats
if status_code_d == 403:
    test_status_d = 'SUCCESS'
else:
    test_status_d = 'FAILURE'
#print(output_d.format(status_code_d=status_code_d, test_status_d=test_status_d))

# impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output_d)
######