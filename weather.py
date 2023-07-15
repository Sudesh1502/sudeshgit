from tkinter import *
from tkinter import ttk

import requests


def data_get():
    city=city_name.get()

    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=24eba57fa206b4f82e78a6fe6f025190").json()
    w_label1.config(text=data["weather"][0]["main"])
    
    wb_label2.config(text=data["weather"][0]["description"])
    
    temp_label3.config(text=str(int(data["main"]["temp"]-273.15)))
    
    per_label4.config(text=data["main"]["pressure"])








win = Tk()

win.title("My first Project")
win.config(bg="sky blue")
win.geometry("600x600")


name_label=Label(win,text="Weather App",
                 font=("Time New Roman",40,"bold"))
name_label.place(x=25,y=50,height=50,width=450)


city_name=StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com=ttk.Combobox(win,text="Weather App",values=list_name,
                 font=("Time New Roman",20,"bold"),textvariable=city_name)

com.place(x=25,y=120,height=50,width=450)





w_label=Label(win,text="Weather Climate",
                 font=("Time New Roman",20))
w_label.place(x=25,y=260,height=50,width=210)

w_label1=Label(win,text="",
                 font=("Time New Roman",20))
w_label1.place(x=250,y=260,height=50,width=210)





wb_label=Label(win,text="Weather Description",
                 font=("Time New Roman",16))
wb_label.place(x=25,y=330,height=50,width=210)

wb_label2=Label(win,text="",
                 font=("Time New Roman",17))
wb_label2.place(x=250,y=330,height=50,width=210)




temp_label=Label(win,text="Temperature",
                 font=("Time New Roman",20))
temp_label.place(x=25,y=400,height=50,width=210)

temp_label3=Label(win,text="",
                 font=("Time New Roman",20))
temp_label3.place(x=250,y=400,height=50,width=210)




per_label=Label(win,text="Pressure",
                 font=("Time New Roman",20))
per_label.place(x=25,y=470,height=50,width=210)

per_label4=Label(win,text="",
                 font=("Time New Roman",20))
per_label4.place(x=250,y=470,height=50,width=210)




done_button=Button(win,text="Done",
                 font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(x=200,y=190,height=50,width=100)







win.mainloop()