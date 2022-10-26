import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import font
from tkinter import ttk
from datetime import datetime
from datetime import timedelta

mhc = tk.Tk()
mhc.title('App đếm ngày tiêm vắc-xin Covid-19')
app_width = 1000
app_height = 850
screen_width = mhc.winfo_screenwidth()
screen_height = mhc.winfo_screenheight()
x = (screen_width//2) - (app_width//2)
y = (screen_height//2) - (app_height//2)
mhc.geometry(f'{app_width}x{app_height}+{x}+{y}')
mhc.config(bg='#4fe3a5')

alert = tk.Label(mhc, bg = '#4fe3a5', text = '')
alert.pack( pady = 10)

dong_tieu_de = tk.Label(mhc, text = 'TÍNH NGÀY TIÊM MŨI KẾ TIẾP VẮC-XIN COVID-19 TRONG NĂM 2022', font = ('Times', 18, 'bold'), bg = 'pink')
dong_tieu_de.pack(pady = 10)

dong_bao_nhap_thang_tiem = tk.Label(mhc, bg='light green', text = 'Mời bạn nhập tháng tiêm: ', font = ('',15,'bold'))
dong_bao_nhap_thang_tiem.pack()

nhap_thang_tiem = tk.Entry(mhc)
nhap_thang_tiem.pack(pady = 10)

dong_bao_nhap_ngay_tiem = tk.Label(mhc,bg='light green', text = 'Mời bạn nhập ngày tiêm: ', font = ('', 15, 'bold'))
dong_bao_nhap_ngay_tiem.pack()


nhap_ngay_tiem = tk.Entry(mhc)
nhap_ngay_tiem.pack(pady = 10)

def cal(event):
    if int(nhap_ngay_tiem.get()) <= 0 or int(nhap_ngay_tiem.get()) > 31 or int(nhap_thang_tiem.get()) <= 0 or int(nhap_thang_tiem.get()) > 12:
        alert.configure(bg = 'red', text = 'Bạn đã nhập sai ngày hoặc tháng!')
    else:
        if int(nhap_thang_tiem.get()) == 1 or int(nhap_thang_tiem.get()) == 3 or int(nhap_thang_tiem.get()) == 5 or int(nhap_thang_tiem.get()) == 7 or int(nhap_thang_tiem.get()) == 8 or int(nhap_thang_tiem.get()) == 10 or int(nhap_thang_tiem.get()) == 12:
            if int(nhap_ngay_tiem.get()) > 31:
                alert.configure(bg = 'red', text = 'Bạn đã nhập sai ngày hoặc tháng!')
            else: 
                alert.configure(bg = '#4fe3a5', text = '')
        elif int(nhap_thang_tiem.get()) == 2:
            if int(nhap_ngay_tiem.get()) >28:
                alert.configure(bg = 'red', text = 'Bạn đã nhập sai ngày hoặc tháng!')
            else: 
                alert.configure(bg = '#4fe3a5', text = '')
        else:
            if int(nhap_ngay_tiem.get()) > 30:
                alert.configure(bg = 'red', text = 'Bạn đã nhập sai ngày hoặc tháng!')
            else: 
                alert.configure(bg = '#4fe3a5', text = '')
    ngay_tiem_mui_1 = f'2022-{nhap_thang_tiem.get()}-{nhap_ngay_tiem.get()}'
    ngay_tiem_mui_1 = datetime.strptime(ngay_tiem_mui_1, "%Y-%m-%d")
    if ten_cac_loai_vaccine.get() == 'Pfizer BioNTech':
        ngay_tiem_mui_2 = ngay_tiem_mui_1 + timedelta(days = 21)
    elif ten_cac_loai_vaccine.get() == 'Moderna':
        ngay_tiem_mui_2 = ngay_tiem_mui_1 + timedelta(days = 28)
    else:
        ngay_tiem_mui_2 = ngay_tiem_mui_1 + timedelta(days = (9*28))
    t = f'Ngày tiêm mũi 2 của liều vắc-xin {ten_cac_loai_vaccine.get()} là vào ngày {ngay_tiem_mui_2.strftime("%d")} tháng {ngay_tiem_mui_2.strftime("%m")} năm {ngay_tiem_mui_2.strftime("%Y")}.'
    dong_thong_bao_ngay_tiem_mui_2.config(text = t, bg="#cd950c", font=('Times', 20, 'bold'))
    

thong_bao_chon_vaccine = tk.Label(mhc, bg = 'light green', text = 'Chọn loại vắc-xin bạn muốn', font = ('', 15, 'bold'))
thong_bao_chon_vaccine.pack()
ten_cac_loai_vaccine = tk.StringVar()
tap_hop_cac_loai_vaccine = ttk.Combobox(mhc, textvariable=ten_cac_loai_vaccine)
tap_hop_cac_loai_vaccine['values'] = ['Pfizer BioNTech', 'Moderna', 'AstraZeneca']
tap_hop_cac_loai_vaccine['state'] = 'readonly'
tap_hop_cac_loai_vaccine.pack(fill=tk.X, padx=5, pady=5)

nut_dong_y = tk.Button(mhc, text = 'Nhập')
nut_dong_y.pack(pady = 20)
nut_dong_y.bind('<Button - 1>', cal)


dong_thong_bao_ngay_tiem_mui_2 = tk.Label(mhc, bg='#4fe3a5') 
dong_thong_bao_ngay_tiem_mui_2.pack(pady = 10)



mhc.mainloop()
