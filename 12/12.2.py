import requests
import json
import tkinter as tk


def get_github_info():
    rep_name = entry.get()
    url = f"https://api.github.com/users/{rep_name}"
    response = requests.get(url)
    if response.status_code == 200:
        item = response.json()
        obj = {
            'company': item['company'],
            'created_at': item['created_at'],
            'email': item['email'],
            'id': item['id'],
            'name': item['login'],
            'url': item['url']
        }
        with open("github_info.json", "w") as file:
            json.dump(obj, file, sort_keys=True, indent=4)
            result_label.config(text="Файл готов")
    else:
        result_label.config(text="Ошибка")


window = tk.Tk()
window.geometry("200x100")
window.title("Поиск по имени")
label = tk.Label(window, text="Введите имя:")
label.pack()
entry = tk.Entry(window)
entry.pack()
button = tk.Button(window, text="Найти", command=get_github_info)
button.pack()
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()