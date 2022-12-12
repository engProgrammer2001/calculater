
# we are going to make calculater by using python language
# this is amazing to calculate some operation By using GUI.

# this is used to make GUI and this perform operation.
from tkinter import  *

first_number=second_number=operator=None

# display digit when you will click number.
def get_digit(digit):
    current = result_label['text'] # hmm pta kar rahe hai ki anhi screen me kya hai
    new = current + str(digit)
    result_label.config(text=new)

# click Button functionality in this function
def clear():
    result_label.config(text='')

# this function is related to all operations
def get_operator(op):
    global  first_number,operator
    first_number = int(result_label['text'])
    operator = op
    result_label.config(text='')

# this is ue to get result after complete operation
def get_result():
    global first_number,second_number,operator

    second_number = int(result_label['text'])
    if operator=='+':
        result_label.config(text=str(first_number + second_number))
    elif operator=='-':
        result_label.config(text=str(first_number - second_number))
    elif operator=='*':
        result_label.config(text=str(first_number * second_number))
    else:
        if second_number==0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(round(first_number / second_number,3)))

root = Tk()
root.title('Apna Calculator..')
root.geometry('400x525')
root.resizable(0,0)      # this line make fix our page.
root.configure(bg='#DDA0DD')
root.iconbitmap('favicon.ico')

# This is related to result page.
result_label = Label(root,text='',fg='white',bg='#DDA0DD')
result_label.grid(row=0,column=0,columnspan=10,pady=(100,25),sticky='w')
result_label.config(font=('verdana',30,'bold'))

# this are related to btn .
btn7 = Button(root,text='7',fg='white',bg='#87CEEB',width=7,height=3,command=lambda:get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',14,'bold'))

btn8 = Button(root,text='8',fg='white',bg='#87CEEB',width=7,height=3,command=lambda:get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',14,'bold'))

btn9 = Button(root,text='9',fg='white',bg='#87CEEB',width=7,height=3,command=lambda:get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',14,'bold'))

btn_add = Button(root,text='+',fg='white',bg='#CD853F',width=7,height=3,command=lambda:get_operator('+'))
btn_add.grid(row=1,column=3)
btn_add.config(font=('verdana',14,'bold'))

btn4 = Button(root,text='4',fg='white',bg='#87CEEB',width=7,height=3,command=lambda:get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',14,'bold'))

btn5 = Button(root,text='5',fg='white',bg='#87CEEB',width=7,height=3,command=lambda:get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',14,'bold'))

btn6 = Button(root,text='6',fg='white',bg='#87CEEB',width=7,height=3,command=lambda:get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',14,'bold'))

btn_sub = Button(root,text='-',fg='white',bg='#CD853F',width=7,height=3,command=lambda:get_operator('-'))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=('verdana',14,'bold'))

btn1 = Button(root,text='1',fg='white',bg='#87CEEB',width=7,height=3,command=lambda:get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',14,'bold'))

btn2 = Button(root,text='2',fg='white',bg='#87CEEB',width=7,height=3,command=lambda:get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',14,'bold'))

btn3 = Button(root,text='3',fg='white',bg='#87CEEB',width=7,height=3,command=lambda:get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',14,'bold'))

btn_mult = Button(root,text='*',fg='white',bg='#CD853F',width=7,height=3,command=lambda:get_operator('*'))
btn_mult.grid(row=3,column=3)
btn_mult.config(font=('verdana',14,'bold'))

btn_clear = Button(root,text='clear',fg='white',bg='red',width=7,height=3,command=lambda:clear())
btn_clear.grid(row=4,column=0)
btn_clear.config(font=('verdana',14,'bold'))

btn0 = Button(root,text='0',fg='white',bg='#87CEEB',width=7,height=3,command=lambda:get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=('verdana',14,'bold'))

btn_equals = Button(root,text='=',fg='white',bg='#98FB98',width=7,height=3,command=get_result)
btn_equals.grid(row=4,column=2)
btn_equals.config(font=('verdana',14,'bold'))

btn_div = Button(root,text='/',fg='white',bg='#CD853F',width=7,height=3,command=lambda:get_operator('/'))
btn_div.grid(row=4,column=3)
btn_div.config(font=('verdana',14,'bold'))

root.mainloop()  #this is use to hold the screen.



