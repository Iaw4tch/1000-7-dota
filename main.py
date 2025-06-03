import tkinter as tk
from tkinter import ttk
import os
import ctypes
import sys
from threading import Thread, Event
from keyboard import *
import themes
from time import sleep


class bEntry(ttk.Button):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.configure(command=self.read_button)
    self.is_reading_key = False
    self.button = self.config('text')[-1]

  def read_button(self):
    if self.is_reading_key:
      self.is_reading_key = False
      self.config(text=self.button)
    else:
      self.is_reading_key = True
      if not all(bentry.is_reading_key for bentry in (start_bentry, stop_bentry)):
        self.config(state="normal", text="___")
        return
      self.is_reading_key = False


def validate_digit_input(new_value):
  if new_value in ("", '-') or new_value.isdigit() or ('-' in new_value and new_value[1:].isdigit()):
    return True
  return False


def key_pressed(event):
  for bentry in (start_bentry, stop_bentry):
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


def action(i, mode):
  press_and_release('shift+enter')
  sleep(0.1)
  write(f"{i}-7={i-7}\n" if mode == '-' else f"{i}+7={i+7}\n")


def do():
  if input_data['start'] == 'f9':
    for i in range(3, 0, -1):
      print(i)
      sleep(1)

  def loop():
    if input_data['end'] <= 1000:
      step = -7
      end = input_data['end']+7-1
      mode = '-'
    else:
      step = 7
      end = input_data['end']-7+1
      mode = '+'
    for i in range(1000, end, step):
      if flag.is_set():
        flag.clear()
        break
      action(i, mode)
  Thread(target=loop, daemon=True).start()


def start():
  global flag
  flag = Event()
  add_hotkey(input_data['start'], do)
  add_hotkey(input_data['stop'], lambda: flag.set())


def insert():
  global input_data
  if end_entry.get() != '':
    warning_label.pack_forget()
    input_data.update(
        {'start': start_bentry.config('text')[-1], 'stop': stop_bentry.config('text')[-1], 'end': int(end_entry.get())})
    phrases = ('Запуск:', 'Остановка:')
    for phrase, label, bentry in zip(phrases,
                                     (start_label, stop_label),
                                     (start_bentry, stop_bentry)):
      label.config(text=phrase)
      bentry.config(state='disabled')
    end_label.config(text='Порог окончания:')
    end_entry.config(state='disabled', style='Finished.TEntry')
    button_insert.pack_forget()
    Thread(target=start, daemon=True).start()
  else:
    warning_label.pack(side='left')


def is_admin():
  try:
    return ctypes.windll.shell32.IsUserAnAdmin()
  except:
    return False


def give_warning():
  kernel32 = ctypes.windll.kernel32
  kernel32.FreeConsole()
  kernel32.AllocConsole()
  sys.stdout = open("CONOUT$", "w")
  sys.stdin = open("CONIN$", "r")
  print("ОШИБКА: Программа требует прав администратора!")
  print("Запустите её от имени администратора.")
  input("Нажмите Enter для выхода...")


if __name__ == "__main__":
  if not is_admin():
    give_warning()
  else:
    root = tk.Tk()
    root.title("1000-7")

    # Установка минимального и максимального размеров окна
    root.minsize(360, 340)  # Минимальный размер
    root.maxsize(490, 365)   # Максимальный размер
    root.geometry("360x340")

    # иконка
    icon_path = os.path.join(os.path.dirname(__file__), 'app_icon.ico')
    root.iconbitmap(icon_path)

    input_data = {}
    VERSION = "v0.0.1a 2025"

    # Настройка темной темы
    style = themes.style()

    style.theme_use('dark')

    # Основной фрейм
    main_frame = ttk.Frame(root, padding=20)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Создание валидатора
    validate_digit_command = main_frame.register(validate_digit_input)

    # Заголовок приложения
    title_label = ttk.Label(
        main_frame, text="ZXC flooder", style='Title.TLabel')
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    # Поля ввода
    start_label = ttk.Label(main_frame, text="Кнопка запуска:")
    start_label.grid(row=1, column=0, sticky='nse', pady=(0, 5))
    start_bentry = bEntry(main_frame, text="i", style='TButton')
    start_bentry.grid(row=1, column=1, sticky='nsew', pady=(0, 5))

    stop_label = ttk.Label(main_frame, text="Кнопка остановки:")
    stop_label.grid(row=2, column=0, sticky='nse', pady=(10, 10))
    stop_bentry = bEntry(main_frame, text="o", style='TButton')
    stop_bentry.grid(row=2, column=1, sticky='nsew', pady=(10, 10))

    end_label = ttk.Label(main_frame, text="Окончание после:")
    end_label.grid(row=3, column=0, sticky='nse', pady=(0, 5))
    end_entry = ttk.Entry(main_frame, validate="key",
                          validatecommand=(validate_digit_command, '%P'), justify='center', font=('Helvetica', 14, 'bold'))
    end_entry.grid(row=3, column=1, sticky='nsew', pady=(0, 5))

    # Добавляем кнопки в следующей строке (row=4)
    button_frame = ttk.Frame(main_frame)
    button_frame.grid(row=4, column=0, columnspan=2,
                      pady=(10, 0), sticky='nsew')

    button_insert = ttk.Button(button_frame, text="Insert", command=insert)
    button_insert.pack(side=tk.RIGHT, padx=(5, 0))

    warning_label = ttk.Label(
        button_frame, text="Заполните поле", style='Warning.TLabel')

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

    root.mainloop()
