import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
                    layout=[[sg.Text("Selamat Datang Di Kelas", font=("Arial",25,"italic","bold","underline"))],
                            [sg.Text("NPM   : 2210010419")],
                            [sg.Text("Nama  : Akbar Kemal Mahendra")],
                            [sg.Text("Kelas : 5P Reguler Banjatmasin")],
                            [sg.Text("Matkul: Pemrograman Visual 3")]
                            ],
                            size=(500,200),
                            font=("Times", 18))
window()
window.close()