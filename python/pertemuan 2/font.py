import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
                    layout=[[sg.Text("NPM   : 2210010419")],
                            [sg.Text("Nama  : Akbar Kemal Mahendra")],
                            [sg.Text("Kelas : 5P Reguler Banjatmasin")],
                            [sg.Text("Matkul: Pemrograman Visual 3")]
                            ],
                            size=(400,200),
                            font=("Times", 18))
window()
window.close()