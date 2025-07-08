import tkinter as tk
from tkinter import Event as tkEvent
from tkinter import ttk, messagebox, StringVar
import os
import ctypes
from threading import Thread, Event
from keyboard import press_and_release, write, add_hotkey, unhook_all_hotkeys
import themes
from time import sleep
from typing import Any, TypedDict

key_dict: dict[str | tuple[str, ...], str] = {
    ('Shift_L', 'Shift_R'): 'shift',
    ('Control_L', 'Control_R'): 'ctrl',
    ('Alt_L', 'Alt_R'): 'alt',
    ('Win_L', 'Win_R'): 'win',
    'Prior': 'pgup',
    'Next': 'pgdown',
    'minus': '-',
    'equal': '=',
}


class bEntry(ttk.Button):
  def __init__(self, *args: Any, **kwargs: Any):
    super().__init__(*args, **kwargs)
    self.configure(command=self.read_button)
    self.is_reading_key = False
    self.button = self.config('text')[-1]

  def read_button(self):
    if pressing:
      if self.is_reading_key:
        self.is_reading_key = False
        self.config(text=self.button)
      else:
        self.is_reading_key = True
        if not all(bentry.is_reading_key for bentry in (start_bentry, stop_bentry)):
          self.config(state="normal", text="___")
          return
        self.is_reading_key = False


class ThemeSelector:
  def __init__(self, parent: ttk.Frame, options: list[str]):
    self.button_frame = ttk.Frame(parent)
    self.var = 'dark'
    self.button = ttk.Button(
        self.button_frame, text=f"theme: {self.var}", command=self.toggle_list, style='ThemeSelector.TButton')
    self.list_frame = ttk.Frame(parent)

    self.visible_list = False
    self.options = options

  def toggle_list(self):
    if self.visible_list:
      self.list_frame.pack_forget()
      self.button_frame.pack()
    else:
      self.button_frame.pack_forget()
      self.list_frame.pack(fill="x")

      for widget in self.list_frame.winfo_children():
        widget.destroy()

      for option in self.options:
        btn = ttk.Button(self.list_frame, text=option,
                         command=lambda o=option: self.select_option(o), style='ThemeSelector.TButton')
        btn.pack(padx=2, *self.args, **self.kwargs)

    self.visible_list = not self.visible_list

  def select_option(self, option: str):
    self.var = option
    self.list_frame.pack_forget()
    self.visible_list = False
    style.theme_use(self.var)
    self.button_frame.pack(*self.args, **self.kwargs)
    self.button.config(
        text=f"theme: {self.var}")

  def pack(self, *args: Any, **kwargs: Any):
    self.button_frame.pack(*args, **kwargs)
    self.button.pack(*args, **kwargs)
    self.args = args
    self.kwargs = kwargs


class InputData(TypedDict):
  start: str
  stop: str
  end: int


def validate_digit_input(new_value: str) -> bool:
  if new_value in ("", '-') or new_value.isdigit() or (new_value.startswith('-') and new_value[1:].isdigit()):
    return True
  return False


def pressed(event: tkEvent):
  global pressing
  pressing = True


def released(event: tkEvent):
  global pressing
  pressing = False


def key_pressed(event: tkEvent):
  for bentry in (start_bentry, stop_bentry):
    if bentry.is_reading_key:
      if str(event.char) == '':
        key = str(event.keysym)
      elif str(event.keysym) == '??':
        key = str(event.char)
      else:
        key = str(event.keysym)
      for k in key_dict:
        if isinstance(k, str):
          if key == k:
            key = key_dict[k]
            break
        else:
          if key in k:
            key = key_dict[k]
            break
      bentry.button = key
      bentry.config(text=bentry.button)
      bentry.is_reading_key = False


def action(i: int, mode: str):
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
  global flag, stop_start_def
  flag = Event()
  add_hotkey(input_data['start'], do)
  add_hotkey(input_data['stop'], lambda: flag.set())
  while not stop_start_def:
    sleep(0.5)
  stop_start_def = False
  unhook_all_hotkeys()


def switch():
  global input_data, inserting, stop_start_def
  if inserting:
    if end_entry.get() != '':
      inserting = False
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
      switch_button.config(text='Cancel')
      Thread(target=start, daemon=True).start()
    else:
      warning_label.pack(side='left')
  else:
    stop_start_def = True
    inserting = True
    phrases = ('Кнопка запуска:', 'Кнопка остановки:')
    for phrase, label, bentry in zip(phrases,
                                     (start_label, stop_label),
                                     (start_bentry, stop_bentry)):
      label.config(text=phrase)
      bentry.config(state='enabled')
    end_label.config(text='Окончание после:')
    end_entry.config(state='enabled', style='TEntry')
    switch_button.config(text='Insert')


def is_admin():
  try:
    return ctypes.windll.shell32.IsUserAnAdmin()
  except:
    return False



if __name__ == "__main__":
  root = tk.Tk()
  root.title("1000-7")

  # Установка минимального и максимального размеров окна
  root.minsize(340, 350)  # Минимальный размер
  root.maxsize(390, 400)   # Максимальный размер
  root.geometry("360x350")

  # иконка
  icon_path = os.path.join(os.path.dirname(__file__), 'app_icon.ico')
  root.iconbitmap(icon_path)  # type: ignore
  input_data: InputData = {'start': 'i', 'stop': 'o', 'end': 0}
  pressing = False
  VERSION = "v2.0 2025"
  stop_start_def = False

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

  end_text = StringVar(value='0')
  end_label = ttk.Label(main_frame, text="Окончание после:")
  end_label.grid(row=3, column=0, sticky='nse', pady=(0, 5))
  end_entry = ttk.Entry(main_frame, textvariable=end_text, validate="key",
                        validatecommand=(validate_digit_command, '%P'), justify='center', font=('Helvetica', 14, 'bold'))
  end_entry.grid(row=3, column=1, sticky='nsew', pady=(0, 5))

  # Добавляем кнопки в следующей строке (row=4)
  switch_frame = ttk.Frame(main_frame)
  switch_frame.grid(row=4, column=0, columnspan=2,
                    pady=(10, 0), sticky='nsew')
  inserting = True
  switch_button = ttk.Button(switch_frame, text="Insert", command=switch)
  switch_button.pack(side=tk.RIGHT, padx=(5, 0))

  warning_label = ttk.Label(
      switch_frame, text="Заполните поле", style='Warning.TLabel')\

  # Подпись версии
  version_frame = ttk.Frame(main_frame)
  version_frame.grid(row=5, column=0, columnspan=2,
                     sticky='wse', pady=(20, 0))
  version_label = ttk.Label(
      version_frame, text=VERSION, style='Version.TLabel')
  version_label.pack(side='right')
  theme_selector = ThemeSelector(
      version_frame, options=["light", "dark", "contrast"])
  theme_selector.pack(side='left')

  # Настройка растягивания
  main_frame.columnconfigure(1, weight=1)
  main_frame.rowconfigure(5, weight=1)
  root.bind("<Button-1>", pressed)
  root.bind("<ButtonRelease-1>", released)
  root.bind("<Key>", key_pressed)

  if not is_admin():
    messagebox.showwarning(  # type: ignore
        "Предупреждение", "Программа запущена без прав администратора!\nВозможны проблемы с печатью текста")

  root.mainloop()
