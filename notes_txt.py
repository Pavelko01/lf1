#для начала скопируй сюда интерфейс "Умных заметок" и проверь его работу
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout)


app = QApplication ([])

notes = []


window = QWidget ()
window.setWindowTitle('Очень умные заметки')
window.resize(900,600)
list_notest=QListWidget ()
list_notest_lable = QLabel ('Список заметок')
button_note_create=QPushButton('Создать заметку')
button_note_del=QPushButton('Удалить заметку')
button_note_save=QPushButton('Сохранить заметку')
field_tag =QLineEdit('')
field_tag.setPlaceholderText('Введите тег...')
field_text=QTextEdit()
button_teg_add=QPushButton('Добавить к заметки')
button_teg_del=QPushButton('Открепить от заметки')
button_teg_search = QPushButton ('Искать заметку по тегу')
list_tags=QListWidget()
list_tags_label= QLabel('Список тегов')

# линии
layout_notes=QHBoxLayout()
col_1=QVBoxLayout()
col_1.addWidget(field_text)
col_2=QVBoxLayout()
col_2.addWidget(list_notest_lable)
col_2.addWidget(list_notest)
row_1=QHBoxLayout()
row_2=QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)
col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)

row_3=QHBoxLayout()
row_4=QHBoxLayout()
row_3.addWidget(button_teg_add)
row_3.addWidget(button_teg_del)
row_4.addWidget(button_teg_search)
col_2.addLayout(row_3)
col_2.addLayout(row_4)
layout_notes.addLayout(col_1, stretch=2)
layout_notes.addLayout(col_2, stretch=1)
window.setLayout(layout_notes)



def add_note():
    note_name, ok = QInputDialog.getText(window, "Добавить заметку", "Название заметки")
    if ok and note_name != "":
        note = list()
        note = [note_name, "", []]
        notes.append(note)
        list_notest.addItem(note[0])
        list_tags.addItems(note[2])
        print(notes)
        with open(str(len(notes)-1)+".txt", "w") as file:
            file.write(note[0]+"\n")
    
        

def show_note():
    key= list_notest.selectedItems()[0].text()
    print(key)
    for note in notes:
        if note[0] == key:
            field_text.setText(note[1])
            list_tags.clear()
            list_tags.addItems(note[2])



def save_note():
    if list_notest.selectedItems():
        key = list_notest.selectedItems()[0].text()
        index = 0
        for note in notes:
            if note[0] == key:
                note[1] = field_text.toPlainText()
                with open(str(index)+".txt", "w") as file:
                    file.write(note[0]+"\n")
                    file.write(note[1]+"\n")
                    for tag in note[2]:
                        file.write(tag+" ")
                    file.write("\n")
            index+=1
        print(notes)
    else:
        print("Заметка для сохранения не выбрана")


button_note_create.clicked.connect(add_note)
button_note_save.clicked.connect(save_note)



list_notest.itemClicked.connect(show_note)
window.show()

name = 0
note = []
while True:
    filename = str(name)+".txt"
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.replace("\n", "")
                note.append(line)
        tags = note[2].split(" ")
        note[2] = tags

        notes.append(note)
        note = []
        name +=1

    except IOError:
        break

print(notes)
for note in notes:
    list_notest.addItem(note[0])

        
    


app.exec_()
#затем запрограммируй демо-версию функционала
