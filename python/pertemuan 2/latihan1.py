import PySimpleGUI as sg
sg.theme("DarkRed1")
sg.theme_text_color("#1C1CEC")
window = sg.Window(title="Profile",
                    layout=[[sg.Text("NPM   : 2210010419")],
                            [sg.Text("Nama  : Akbar Kemal Mahendra")],
                            [sg.Text("Kelas : 5P Reguler Banjatmasin")],
                            [sg.Text("Matkul: Pemrograman Visual 3")]
                            ],
                            size=(400,200))
window()
window.close()