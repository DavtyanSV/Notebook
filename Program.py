import datetime
import csv

def show_menu() -> int:
    print("\nВыберите необходимое действие\n"
          "1. Отобразить все заметки\n"
          "2. Создать заметку\n"
          "3. Редактировать заметку\n"
          "4. Удалить заметку\n"
          "5. Завершить работу\n")
    choice = int(input())
    return choice

def creat_notebook(notebook, title, text):
    new_id = len(notebook)+1
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_note = {
        'ID': str(new_id),
        'Заголовок': title,
        'Текст заметки': text,
        'Дата внесения': current_time
    }
    notebook.append(new_note)
    return notebook

def save_notebook(filename, notes):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['ID', 'Заголовок', 'Текст заметки', 'Дата внесения']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(notes)

def show_notebook(notebook):
    if not notebook:
        print("Нет заметок.")
    else:
        for note in notebook:
            print(f"ID: {note['ID']}")
            print(f"Заголовок: {note['Заголовок']}")
            print(f"Текст заметки: {note['Текст заметки']}")
            print(f"Дата внесения: {note['Дата внесения']}")
            print("=" * 30)

def edit_notebook(notebook, note_id, new_title, new_text):
    for note in notebook:
        if note['ID'] == note_id:
            note['Заголовок'] = new_title
            note['Текст заметки'] = new_text
            note['Дата внесения'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return notebook
    return None

def delete_notebook(notebook, note_id):
    for note in notebook:
        if note['ID'] == note_id:
            notebook.remove(note)
            return notebook
    return None

def work_with_notebook():
    notebook = []
    choice = show_menu()

    while True:
        match choice:
            case 1:
                show_notebook(notebook)
                choice = show_menu()
            case 2:
                title = input("Введите заголовок заметки: ")
                text = input("Введите текст заметки: ")
                notebook = creat_notebook(notebook, title, text)
                save_notebook("Заметки.csv", notebook)
                print("Заметка создана")
                choice = show_menu()
            case 3:
                note_id = input("Введите ID заметки для редактирования: ")
                new_title = input("Введите новый заголовок заметки: ")
                new_text = input("Введите новый текст заметки: ")
                updated_notebook = edit_note(notebook, note_id, new_title, new_text)
                if updated_notebook is not None:
                    notes = updated_notebook
                    save_notebook("Заметки.csv", notebook)
                    print("Заметка отредактирована.")
                else:
                    print("Заметка с указанным ID не найдена.")
                choice = show_menu()
            case 4:
                note_id = input("Введите ID заметки для удаления: ")
                deleted_notebook = delete_notebook(notebook, note_id)
                if deleted_notebook is not None:
                    notebook = deleted_notebook
                    save_notebook("Заметки.csv", notebook)
                    print("Заметка удалена.")
                else:
                    print("Заметка с указанным ID не найдена.")
                choice = show_menu()
            case 5:
                break
            case _:
                print("Неверный выбор команды. Попробуйте еще раз.")          
        
           
work_with_notebook()

