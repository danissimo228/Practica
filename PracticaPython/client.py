import requests

print(
    "1 - GET => /api/notifications \n" +
    "2 - DELETE => /api/notifications/id \n" +
    "3 - POST => /api/notifications \n" +
    "4 - PUT => /api/notifications/id \n" +
    "5 - POST => /api/notifications/id/send \n" +
    "q - exit"
)

n=""
while n != "q":
    n = str(input("Input number of operation: "))

    if n == "1":
        res = requests.get("http://127.0.0.1:3001/api/notifications")
        print(res.json())

    elif n == "2":
        id = int(input("Input id: "))
        res = requests.delete(f"http://127.0.0.1:3001/api/notifications/{id}")
        print(res.json())

    elif n == "3":
        res = requests.post("http://127.0.0.1:3001/api/notifications")
        print(res.json())

    elif n == "4":
        id = int(input("Input id: "))
        res = requests.put(f"http://127.0.0.1:3001/api/notifications/{id}")
        print(res.json())

    elif n == "5":
        try:
            id = int(input("Input id: "))
            res = requests.post(f"http://127.0.0.1:3001/api/notifications/{id}/send")
            print(res.json())
        except:
            print("try again")

    elif n == "q":
        print("exit")
        break

    else:
        print("Не верный символ, попробуйте еще")