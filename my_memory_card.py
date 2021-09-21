#создай приложение для запоминания информации
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import *

class Question():
    def __init__(self, q, r, w1, w2, w3):
        self.question = q
        self.right_answer = r
        self.wrong1 = w1
        self.wrong2 = w2
        self.wrong3 = w3

question_list = []
q1 = Question("Когда день Победы", "9 мая", "22 июня", "13 октября", "1 января")
q2 = Question("В какой день празднуется день России", "22 июня", "9 мая", "13 октября", "1 января")
q3 = Question("Самое дождливое время года?", "Осень", "Зима", "Лето", "Весна")
q4 = Question("Какой город столица в Белоруси", "Минск", "вапрол", "hjjj", "sdfghjk")
q5 = Question("Когда день Победы", "9 мая", "22 июня", "13 октября", "1 января")
q6 = Question("Когда день Победы", "9 мая", "22 июня", "13 октября", "1 января")
q7 = Question("Когда день Победы", "9 мая", "22 июня", "13 октября", "1 января")

question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
question_list.append(q5)
question_list.append(q6)
question_list.append(q7)





app = QApplication([])
window = QWidget()
window.setWindowTitle("Memory Card")

#--------------ИНТЕРФЕЙС ПРИЛОЖЕНИЯ --------------------
btn_OK = QPushButton("Ответить")
lb_Question = QLabel("В каком году была основана Москва")

#создаем панель результата
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel("прав ты или нет?")
lb_Correct = QLabel("ответ будет тут!")
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

#группа на экране для переключателей с ответами
RadioGroupBox = QGroupBox("Варианты ответа")
rbtn1 = QRadioButton("1147")
rbtn2 = QRadioButton("1861")
rbtn3 = QRadioButton("2021")
rbtn4 = QRadioButton("1242")

#группа кнопок 
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

#Размещаем все виджеты в окне
layout_line1 = QHBoxLayout() #вопрос
layout_line2 = QHBoxLayout() #варианты ответов и результат 
layout_line3 = QHBoxLayout() #кнопка ответить
layout_line1.addWidget(lb_Question,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_line3.addWidget(btn_OK, stretch=2)
main_layout = QVBoxLayout() #создаю главный вертикальный лейаут
main_layout.addLayout(layout_line1, stretch=2)
main_layout.addLayout(layout_line2, stretch=8)
main_layout.addLayout(layout_line3, stretch=1)
window.setLayout(main_layout)

def show_result():
    AnsGroupBox.show()
    RadioGroupBox.hide()
    btn_OK.setText("Следующий вопрос")
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText("Ответить")


def ask (q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()


def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct("ok!")
    else:
        show_correct("ne ok1")

#счётчик вопросов
cur_question = -1 
total = 0 
score = 0

def next_question():
    global car_question, total
    total += 1
    car_question = randint(0, len(question_list))
    if car_question == len(question_list):
        car_question = 0
    z = question_list[car_question]
    ask(z)
    print("Процент правильных ответов", score/total*100)


def click_OK():
    if btn_OK.text() == "Ответить":
        check_answer()
    else:
        next_question()



btn_OK.clicked.connect(click_OK)

window.show()
app.exec()