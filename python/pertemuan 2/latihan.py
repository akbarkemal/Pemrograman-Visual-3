import PySimpleGUI as sg
window = sg.Window(title="Profile",
                    layout=[[sg.Text("NPM   : 2210010419")],
                            [sg.Text("Nama  : Akbar Kemal Mahendra")],
                            [sg.Text("Kelas : 5P Reguler Banjatmasin")],
                            [sg.Text("Matkul: Pemrograman Visual 3")]
                            ],
                            size=(400,200))
window()
window.close()