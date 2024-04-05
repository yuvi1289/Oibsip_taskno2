from tkinter import *
import customtkinter
from tkinter import messagebox

app = customtkinter.CTk()
app.geometry("345x500")
app.title("BMI CALCUALTOR")
app.config(bg="#020414")
image_icon=PhotoImage(file="icon.png")
app.iconphoto(False,image_icon)

top=Label(app,text="BMI CALCULAOR",font=('Arial',18,'bold'),fg="#FFFFFF",bg="#181935",width=28,height=1)
top.pack()


height_label=Label(app,font=('Arial',18,'bold'),fg="#FFFFFF",bg="#181935",width=20,height=4)
height_label.place(x=40,y=60)

height_text=Label(app,text="HEIGHT CM",font=('Arial',18,'bold'),fg="#FFFFFF",bg="#181935",width=18,height=1)
height_text.place(x=55,y=60)

weight_label=Label(app,font=('Arial',18,'bold'),fg="#FFFFFF",bg="#181935",width=20,height=4)
weight_label.place(x=40,y=210)


weight_text=Label(app,text=" WEIGHT KG",font=('Arial',18,'bold'),fg="#FFFFFF",bg="#181935",width=18,height=1)
weight_text.place(x=55,y=210)


height=StringVar()
weight=StringVar()


height_value=IntVar()
weight_value=IntVar()

txt = StringVar()

def get_height_value():
    return height_value.get()


def slider1(event):
    return height.set(get_height_value())


def get_weight_value():
    return weight_value.get()


def slider2(event):
    return weight.set(get_weight_value())

heigh_entry= customtkinter.CTkEntry(app,textvariable=height,bg_color="#181935",fg_color="#181935",border_width=0,font=('Arial',23,'bold'))
heigh_entry.place(x=150,y=100)

weigh_entry= customtkinter.CTkEntry(app,textvariable=weight,bg_color="#181935",fg_color="#181935",border_width=0,font=('Arial',23,'bold'))
weigh_entry.place(x=150,y=250)


height_slider=customtkinter.CTkSlider(app,variable=height_value,from_=0,to=300,width=265,bg_color="#181935",fg_color="#ffffff",button_color="#bf0d87",command=slider1)
height_slider.place(x=40,y=155)

weight_slider=customtkinter.CTkSlider(app,variable=weight_value,from_=0,to=500,width=265,bg_color="#181935",fg_color="#ffffff",button_color="#bf0d87",command=slider2 )
weight_slider.place(x=40,y=300)





def BMI():
    try:
        cm=int(heigh_entry.get())
        m=(cm/100)*(cm/100)
        w=int(weigh_entry.get())
        bmi=float(format(w/m,".2f"))
        if(bmi<=18.5):
            txt.set('Underweight')
        elif(bmi<=24.5):
            txt.set('Normal')
        elif(bmi<=29.9):
            txt.set('Overweight')
        elif(bmi<=34.9):
            txt.set('Obese I')
        elif(bmi<=39.9):
            txt.set('Obese II')
        elif (bmi>44):
            messagebox.showerror(title="Error",message="your not a human......")
        else:
            txt.set('Obese III')

        result1_label=customtkinter.CTkLabel(app,text=f'BMI:{bmi}',font=('Arial',18,'bold'))
        result1_label.place(x=135,y=410)

        result2_label=customtkinter.CTkLabel(app,textvariable=txt,font=('Arial',18,'bold'))
        result2_label.place(x=135,y=440)

    except:
        messagebox.showerror(title="Error",message="height or weight cannot be zero. Please enter a valid number.")
  

    result1_label=customtkinter.CTkLabel(app,text=f'BMI:{bmi}',font=('Arial',18,'bold'))
    result1_label.place(x=135,y=410)

    result2_label=customtkinter.CTkLabel(app,textvariable=txt,font=('Arial',18,'bold'))
    result2_label.place(x=135,y=440)
    


calc_button=customtkinter.CTkButton(app,text="CALCULATOR",command=BMI,width=170,height=50,font=('Arial',18,'bold'),fg_color="#ff00ff",hover_color="#ff00ff")
calc_button.place(x=90,y=350) 
 


app.mainloop()