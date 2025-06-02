import tkinter as tk
from tkinter import ttk
from random import randint as rand
import os
import ctypes
import sys


class bEntry(ttk.Button):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.configure(command=self.read_button)
    self.is_reading_key = False
    self.button = ''

  def read_button(self):
    global bentrys
    if self.is_reading_key:
      self.is_reading_key = False
      self.config(text=self.button)
    else:
      self.is_reading_key = True
      if not all(bentry.is_reading_key for bentry in bentrys):
        self.config(state="normal", text="___")
        return
      self.is_reading_key = False


def validate_digit_input(new_value):
  if new_value in ("", '-') or new_value.isdigit() or ('-' in new_value and new_value[1:].isdigit()):
    return True
  return False


def key_pressed(event):
  global is_reading_key, bentrys
  for bentry in bentrys:
    if bentry.is_reading_key:
      if str(event.char) == '':
        key = str(event.keysym)
      elif str(event.keysym) == '??':
        key = str(event.char)
      else:
        key = str(event.char)
      print(f"Key Pressed on {bentry}: " + key)
      bentry.button = key
      bentry.config(text=bentry.button)
      bentry.is_reading_key = False


def insert():
  global input_data, bentrys, entrys, labels
  input_data.update(
      {'key': bentrys[0].config('text')[-1], 'end': int(entrys[0].get()), 'stop': bentrys[1].config('text')[-1]})
  phrases = ['Запуск:', 'Остановка:']
  for phrase, label, bentry in zip(phrases, labels[:-1], bentrys):
    label.config(text=phrase)
    bentry.config(state='disabled')
  labels[2].config(text='Порог окончания:')
  labels[2].configure(style='Finished.Entry')

  # Thread(target=starting).start()


def app_create():
  root = tk.Tk()
  root.title("1000-7")

  # Установка минимального и максимального размеров окна
  root.minsize(360, 320)  # Минимальный размер
  root.maxsize(490, 365)   # Максимальный размер
  root.geometry("360x320")

  # иконка
  icon_path = os.path.join(os.path.dirname(__file__), 'app_icon.ico')
  root.iconbitmap(icon_path)

  # Настройка темной темы
  style = ttk.Style()
  style.theme_create(
      'dark',
      parent='clam',
      settings={
          '.': {
              'configure': {
                  'background': '#313131',
                  'foreground': 'white',
              }
          },
          'TButton': {
              'configure': {
                  'anchor': 'c',
                  'background': "#444444",
                  'foreground': 'white',
                  'padding': 6,
                  'font': ('Helvetica', 14, 'bold')
              },
              'map': {
                  'background': [('active', '#666666'), ('pressed', '#444444')]
              }
          },
          'TEntry': {
              'configure': {
                  'fieldbackground': '#444444',
                  'foreground': 'white',
                  'insertcolor': 'white',
                  'font': ('Helvetica', 28, 'bold')
              }
          },
          'TLabel': {
              'configure': {
                  'background': '#313131',
                  'foreground': 'white',
                  'padding': 5,
                  'font': ('Arial', 15)
              }
          },
          'Title.Label': {
              'configure': {
                  'font': ('Helvetica', 20, 'bold'),
              }
          },
          'Version.Label': {
              'configure': {
                  'font': ('Helvetica', 8),
                  'foreground': '#aaaaaa'
              }
          },
          'Finished.Entry': {
              'configure': {
                  'foreground':  '#313131'
              }
          }
      }
  )

  style.theme_create(
      'black',
      parent='clam',
      settings={
          '.': {
              'configure': {
                  'background': '',
                  'foreground': '',
              }
          },
          'TButton': {
              'configure': {
                  'background': "#444444",
                  'foreground': 'white',
                  'padding': 6,
                  'font': ('Helvetica', 14, 'bold')
              },
              'map': {
                  'background': [('active', '#666666'), ('pressed', '#444444')]
              }
          },
          'TEntry': {
              'configure': {
                  'fieldground': '#444444',
                  'foreground': 'white',
                  'insertcolor': 'white'
              }
          },
          'TLabel': {
              'configure': {
                  'background': '#333333',
                  'foreground': 'white',
                  'padding': 5,
                  'font': ('Arial', 15)
              }
          },
          'Title.Label': {
              'configure': {
                  'font': ('Helvetica', 14, 'bold')
              }
          },
          'Version.Label': {
              'configure': {
                  'font': ('Helvetica', 8),
                  'foreground': '#aaaaaa'
              }
          }
      }
  )

  style.theme_create(
      'white',
      parent='clam',
      settings={
          '.': {
              'configure': {
                  'background': '',
                  'foreground': '',
              }
          },
          'TButton': {
              'configure': {
                  'background': "#444444",
                  'foreground': 'white',
                  'padding': 6,
                  'font': ('Helvetica', 14, 'bold')
              },
              'map': {
                  'background': [('active', '#666666'), ('pressed', '#444444')]
              }
          },
          'TEntry': {
              'configure': {
                  'fieldground': '#444444',
                  'foreground': 'white',
                  'insertcolor': 'white'
              }
          },
          'TLabel': {
              'configure': {
                  'background': '#333333',
                  'foreground': 'white',
                  'padding': 5,
                  'font': ('Arial', 15)
              }
          },
          'Title.Label': {
              'configure': {
                  'font': ('Helvetica', 14, 'bold')
              }
          },
          'Version.Label': {
              'configure': {
                  'font': ('Helvetica', 8),
                  'foreground': '#aaaaaa'
              }
          }
      }
  )

  style.theme_use('dark')

  # Основной фрейм
  main_frame = ttk.Frame(root, padding="20")
  main_frame.pack(fill=tk.BOTH, expand=True)

  bentrys = []
  entrys = []
  labels = []

  # Создание валидатора
  validate_digit_command = main_frame.register(validate_digit_input)

  # Заголовок приложения
  title_label = ttk.Label(
      main_frame, text="ZXC flooder", style='Title.Label')
  title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

  # Поля ввода
  label1 = ttk.Label(main_frame, text="Кнопка запуска:")
  labels.append(label1)
  label1.grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
  global is_reading_key
  is_reading_key = False
  bentry1 = bEntry(main_frame, text="i", style='TButton')
  bentry1.button = 'i'
  bentrys.append(bentry1)
  bentry1.grid(row=1, column=1, sticky=tk.EW, pady=(0, 5))

  label2 = ttk.Label(main_frame, text="Кнопка остановки:")
  labels.append(label2)
  label2.grid(row=2, column=0, sticky=tk.W, pady=(10, 10))
  bentry2 = bEntry(main_frame, text="o", style='TButton')
  bentry2.button = 'o'
  bentrys.append(bentry2)
  bentry2.grid(row=2, column=1, sticky=tk.EW, pady=(10, 10))

  label3 = ttk.Label(main_frame, text="Окончание после:")
  labels.append(label3)
  label3.grid(row=3, column=0, sticky=tk.W, pady=(0, 5))
  entry1 = ttk.Entry(main_frame, validate="key",
                     validatecommand=(validate_digit_command, '%P'), font=('Helvetica', 14))
  entry1.grid(row=3, column=1, sticky=tk.EW, pady=(0, 5))
  entrys.append(entry1)

  # Добавляем кнопки в следующей строке (row=4)
  button_frame = ttk.Frame(main_frame)
  button_frame.grid(row=4, column=0, columnspan=2, pady=(10, 0), sticky=tk.E)

  btn_ok = ttk.Button(button_frame, text="Cancel")
  btn_ok.pack(side=tk.RIGHT, padx=(5, 0))

  btn_cancel = ttk.Button(button_frame, text="OK", command=insert)
  btn_cancel.pack(side=tk.RIGHT)

  # Подпись версии
  version_frame = ttk.Frame(main_frame)
  version_frame.grid(row=5, column=0, columnspan=2,
                     sticky=tk.SE, pady=(20, 0))

  version_label = ttk.Label(
      version_frame, text=VERSION, style='Version.TLabel')
  version_label.pack()

  # Настройка растягивания
  main_frame.columnconfigure(1, weight=1)
  main_frame.rowconfigure(4, weight=1)

  root.bind("<Key>", key_pressed)

  return root, bentrys, labels, entrys


# def check_admin():


def main():
  global bentrys, labels, entrys, input_data
  # try:
  #   is_admin = ctypes.windll.shell32.IsUserAnAdmin()
  # except:
  #   is_admin = False
  # if is_admin:
  app, bentrys, labels, entrys = app_create()
  input_data = {}
  app.mainloop()
  # else:
  #   kernel32 = ctypes.windll.kernel32
  #   kernel32.FreeConsole()
  #   kernel32.AllocConsole()
  #   sys.stdout = open("CONOUT$", "w")
  #   sys.stdin = open("CONIN$", "r")
  #   print("ОШИБКА: Программа требует прав администратора!")
  #   print("Запустите её от имени администратора.")
  #   input("Нажмите Enter для выхода...")


VERSION = "v0.0.1a 2025"

if __name__ == "__main__":
  main()
