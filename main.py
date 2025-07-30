import tkinter as tk
from tkinter import Event as tkEvent
from tkinter import ttk, messagebox
import os
import ctypes
from threading import Thread, Event
from keyboard import press_and_release, write, add_hotkey, unhook_all_hotkeys
import themes
from time import sleep
from typing import Any, TypedDict, ClassVar, Protocol, Hashable, TypeVar

T: dict[str, dict[str, str]] = {
    'русский': {
        'start_button': 'Кнопка запуска:',
        'stop_button': 'Кнопка остановки:',
        'begin_number': 'Начальное число:',
        'step': 'Шаг:',
        'end_number': 'Число окончания:',
        'end': 'ОКОНЧАНИЕ',
        'begin': 'НАЧАЛО',
        'step_show': 'ШАГ',
        'cancel': 'Отмена',
        'insert': 'Запуск',
        'theme': 'Тема:',
        'fill_fields': 'Заполните поля:'
    },
    'english': {
        'start_button': 'Start Button:',
        'stop_button': 'Stop Button:',
        'begin_number': 'Begin Number:',
        'step': 'Step:',
        'end_number': 'End Number:',
        'end': 'END',
        'begin': 'BEGIN',
        'step_show': 'STEP',
        'cancel': 'Cancel',
        'insert': 'Insert',
        'theme': 'Theme:',
        'fill_fields': 'Fill fields:'
    },
}

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


class InputData(TypedDict):
  start: str
  stop: str
  begin: int
  step: int
  end: int


class BEntry(ttk.Button):
  bentrys: ClassVar[list['BEntry']] = []

  def __init__(self, master: ttk.Widget, *args: Hashable, **kwargs: Hashable):
    super().__init__(master, *args, **kwargs)
    self.configure(command=self.read_button)
    self.is_reading_key: bool = False
    self.button: str = self.cget('text')
    BEntry.bentrys.append(self)

  def read_button(self):
    if pressing:
      if self.is_reading_key:
        self.is_reading_key = False
        self.config(text=self.button)
      else:
        self.is_reading_key = True
        if not all(bentry.is_reading_key for bentry in BEntry.bentrys):
          self.config(text="___")
          return
        self.is_reading_key = False


class Packable(Protocol):
  def pack(self, **whole_config: Any) -> None: ...
  def pack_forget(self) -> None: ...


class Packer:
  objects: list[tuple[Packable, dict[str, Hashable]]] = []

  @classmethod
  def pack(cls, widget: Packable, **kwargs: Hashable):
    widget.pack(**kwargs)
    cls.objects.append((widget, kwargs))

  @classmethod
  def repack(cls):
    for object in cls.objects:
      object[0].pack_forget()
    for object in cls.objects:
      object[0].pack(**object[1])


class ThemeSelector:
  def __init__(self, parent: ttk.Frame, options: list[str], options_config: dict[str, Any]):
    self.main_frame = ttk.Frame(parent)
    self.button_frame = ttk.Frame(self.main_frame)
    self.button = ttk.Button(
        self.button_frame, text=f"{T[lng]['theme']} dark", command=self.toggle_list, style='Selectors.TButton')
    self.button.pack(fill='x')

    self.list_frame = ttk.Frame(self.main_frame)
    for option in options:
      btn = ttk.Button(self.list_frame, text=option,
                       command=lambda o=option: self.select_option(o), style='Selectors.TButton')
      btn.pack(**options_config)

    self.button_frame.pack(fill='x')
    self.visible_list = False

  def toggle_list(self):
    if self.visible_list:
      self.list_frame.pack_forget()
      self.button_frame.pack()
    else:
      self.button_frame.pack_forget()
      self.list_frame.pack()

    self.visible_list = not self.visible_list
    Packer.repack()

  def select_option(self, option: str):
    style.theme_use(option)

    self.button.config(
        text=f"{T[lng]['theme']} {option}")
    self.button_frame.pack()

    self.list_frame.pack_forget()
    self.visible_list = False

  def pack(self, **whole_config: Any):
    self.main_frame.pack(**whole_config)

  def pack_forget(self):
    self.main_frame.pack_forget()


class LanguageSelector:
  def __init__(self, parent: ttk.Frame, languages: tuple[str, ...], options_config: dict[str, Any]):
    self.main_frame = ttk.Frame(parent)
    self.button_frame = ttk.Frame(self.main_frame)
    self.button = ttk.Button(
        self.button_frame, text=f"{languages[0]}", command=self.toggle_list, style='Selectors.TButton')
    self.button.pack(fill='x')

    self.list_frame = ttk.Frame(self.main_frame)
    for language in languages:
      btn = ttk.Button(self.list_frame, text=language,
                       command=lambda l=language: self.select_language(l), style='Selectors.TButton')
      btn.pack(**options_config)

    self.button_frame.pack(fill='x')
    self.visible_list = False

  def toggle_list(self):
    if self.visible_list:
      self.list_frame.pack_forget()
      self.button_frame.pack()
    else:
      self.button_frame.pack_forget()
      self.list_frame.pack()

    self.visible_list = not self.visible_list
    Packer.repack()

  def select_language(self, language: str):
    update_widgets(language)
    self.button.config(text=language)
    self.button_frame.pack()

    self.list_frame.pack_forget()
    self.visible_list = False

  def pack(self, **whole_config: Any):
    self.main_frame.pack(**whole_config)

  def pack_forget(self):
    self.main_frame.pack_forget()


class LabeledEntry:
  def __init__(self, master: ttk.Widget, label: str, text: str, validator: str):
    self.label = ttk.Label(master, text=label)
    self.entry = ttk.Entry(master, validate="key",
                           validatecommand=(validator, '%P'), justify='center', font=('Helvetica', 14, 'bold'))
    self.entry.insert(0, text)

  def grid(self, row: int, column: int, label_kwargs: dict[str, Any]={}, entry_kwargs: dict[str, Any]={}):
    self.label.grid(row=row, column=column, **label_kwargs)
    self.entry.grid(row=row, column=column+1, **entry_kwargs)


class LabeledBEntry:
  def __init__(self, master: ttk.Widget, label: str, button: str):
    self.label = ttk.Label(master, text=label)
    self.entry = BEntry(master, text=button, style='TButton')
    self.button = button

  def grid(self, row: int, column: int, label_kwargs: dict[str, Any] = {}, entry_kwargs: dict[str, Any] = {}):
    self.label.grid(row=row, column=column, **label_kwargs)
    self.entry.grid(row=row, column=column+1, **entry_kwargs)


def update_widgets(language: str):
  global lng
  lng = language
  for info in widget_registry:
    widget = info[0]
    subscription = info[1]
    if isinstance(widget, (LabeledBEntry, LabeledEntry)):
      widget.label.config(text=T[lng][subscription])
    elif isinstance(widget, ThemeSelector):
      widget.button.config(text=f"{T[lng][subscription]} {style.theme_use()}")
    elif isinstance(widget, LanguageSelector):
      widget.button.config(text=f"{lng}")
    elif isinstance(widget, ttk.Label):
      if warning_list:
        if len(warning_list) == 3 and lng == 'english':
          root.minsize(390, MIN_SIZE[1])
          root.maxsize(*MAX_SIZE)
        elif lng == 'русский':
          root.minsize(*MIN_SIZE)
          root.maxsize(600, MAX_SIZE[1])
        else:
          root.minsize(*MIN_SIZE)
          root.maxsize(*MAX_SIZE)
        warning.config(
            text=f'{T[lng]['fill_fields']} {','.join(dict[lng] for dict in warning_list)}')
        warning.pack(side='left')
    else:
      widget.config(text=T[lng][subscription])


def validate_digit_input(new_value: str) -> bool:
  if new_value in ("", '-') or new_value.isdigit() or (new_value.startswith('-') and new_value[1:].isdigit()):
    return True
  return False


def validate_step_input(new_value: str) -> bool:
  if new_value == '' or new_value.isdigit():
    return True
  return False


def pressed(event: tkEvent):
  global pressing
  pressing = True


def released(event: tkEvent):
  global pressing
  pressing = False


def key_pressed(event: tkEvent):
  for bentry in BEntry.bentrys:
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
  write(f"{i}-{input_data['step']}={i-input_data['step']}\n" if mode == '-'
        else f"{i}+{input_data['step']}={i+input_data['step']}\n")


def do():
  if input_data['start'] == 'F9':
    for _ in range(3, 0, -1):
      sleep(1)

  def loop():
    if input_data['end'] <= input_data['begin']:
      step = -input_data['step']
      end = input_data['end']+input_data['step']-1
      mode = '-'
    else:
      step = input_data['step']
      end = input_data['end']-input_data['step']+1
      mode = '+'
    for i in range(input_data['begin'], end, step):
      if flag.is_set():
        flag.clear()
        break
      action(i, mode)
  Thread(target=loop, daemon=True).start()


def run():
  global flag
  flag = Event()
  add_hotkey(input_data['start'], do)
  add_hotkey(input_data['stop'], lambda: flag.set())
  while running:
    sleep(0.5)
  unhook_all_hotkeys()


def switch():
  global input_data, inserting, running
  if inserting:
    warning_list.clear()
    if end.entry.get() == '':
      warning_list.append(
          {'русский': T['русский']['end'], 'english': T['english']['end']})
    if begin.entry.get() == '':
      warning_list.append(
          {'русский': T['русский']['begin'], 'english': T['english']['begin']})
    if step.entry.get() == '':
      warning_list.append(
          {'русский': T['русский']['step_show'], 'english': T['english']['step_show']})
    if warning_list:
      if len(warning_list) == 3 and lng == 'english':
        root.minsize(390, MIN_SIZE[1])
        root.maxsize(*MAX_SIZE)
      elif lng == 'русский':
        root.minsize(*MIN_SIZE)
        root.maxsize(600, MAX_SIZE[1])
      else:
        root.minsize(*MIN_SIZE)
        root.maxsize(*MAX_SIZE)
      warning.config(
          text=f'{T[lng]['fill_fields']} {','.join(dict[lng] for dict in warning_list)}')
      warning.pack(side='left')
    else:
      inserting = False
      running = True
      warning.pack_forget()
      input_data.update(
          {'start': start.entry.cget('text'),
           'stop': stop.entry.cget('text'),
           'begin': int(begin.entry.get()),
           'step': int(step.entry.get()),
           'end': int(end.entry.get())})
      for field in (start, stop, begin, step, end):
        field.entry.config(state='disabled')
      switch_button.config(text=T[lng]['cancel'])
      Thread(target=run, daemon=True).start()
  else:
    running = False
    inserting = True
    for field in (start, stop, begin, step, end):
      field.entry.config(state='enabled')
    switch_button.config(text=T[lng]['insert'])


def is_admin() -> bool:
  try:
    return os.getuid() == 0  # type: ignore
  except AttributeError:
    try:
      return ctypes.windll.shell32.IsUserAnAdmin()
    except:
      return False


W = TypeVar('W', bound=ttk.Label | ttk.Button | LabeledBEntry |
            LabeledEntry | ThemeSelector | LanguageSelector)


def register(widget: W, subscription: str) -> W:
  widget_registry.append((widget, subscription))
  return widget


if __name__ == "__main__":
  root = tk.Tk()
  root.title("1000-7")

  MIN_SIZE = 350, 445
  MAX_SIZE = 405, 500

  root.minsize(*MIN_SIZE)
  root.maxsize(*MAX_SIZE)
  root.geometry('x'.join(map(str, MIN_SIZE)))

  icon_path = os.path.join(os.path.dirname(__file__), 'app_icon.ico')
  root.iconbitmap(icon_path)  # type: ignore
  input_data: InputData = {'start': 'i',
                           'stop': 'o',
                           'begin': 1000,
                           'step': 7,
                           'end': 0}
  pressing: bool = False
  VERSION: str = "v3.0 2025"
  running = False
  lng: str = 'english'
  inserting: bool = True
  warning_list: list[dict[str, str]] = []
  widget_registry: list[tuple[ttk.Label | ttk.Button | LabeledBEntry |
                              LabeledEntry | ThemeSelector | LanguageSelector, str]] = []

  style = themes.style()
  style.theme_use('dark')

  main_frame = ttk.Frame(root, padding=20)
  main_frame.pack(fill=tk.BOTH, expand=True)

  validate_digit = main_frame.register(validate_digit_input)
  validate_step = main_frame.register(validate_step_input)

  title_label = ttk.Label(
      main_frame, text="Dota range flooder", style='Title.TLabel')
  title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

  start = register(LabeledBEntry(
      main_frame, label=T[lng]['start_button'], button='i'), 'start_button')
  start.grid(row=1, column=0, label_kwargs={'sticky':'nse', 'pady':(0,7)}, entry_kwargs={'sticky':'nswe', 'pady':(0,7)})

  stop = register(LabeledBEntry(
      main_frame, label=T[lng]['stop_button'], button='o'), 'stop_button')
  stop.grid(row=2, column=0, label_kwargs={
            'sticky': 'nse', 'pady':(0,7)}, entry_kwargs={'sticky': 'nswe', 'pady':(0,7)})

  begin = register(LabeledEntry(
      main_frame, label=T[lng]['begin_number'], text='1000', validator=validate_digit), 'begin_number')
  begin.grid(row=3, column=0, label_kwargs={
             'sticky': 'nse', 'pady':(0,7)}, entry_kwargs={'sticky': 'nswe', 'pady':(0,7)})

  step = register(LabeledEntry(
      main_frame, label=T[lng]['step'], text='7', validator=validate_step), 'step')
  step.grid(row=4, column=0, label_kwargs={
            'sticky': 'nse', 'pady':(0,7)}, entry_kwargs={'sticky': 'nswe', 'pady':(0,7)})

  end = register(LabeledEntry(
      main_frame, label=T[lng]['end_number'], text='0', validator=validate_digit), 'end_number')
  end.grid(row=5, column=0, label_kwargs={
           'sticky': 'nse', 'pady':(0,7)}, entry_kwargs={'sticky': 'nswe', 'pady':(0,7)})

  switch_frame = ttk.Frame(main_frame)
  switch_frame.grid(row=6, column=0, columnspan=2,
                    pady=(10, 0), sticky='nsew')

  switch_button = register(ttk.Button(
      switch_frame, text=T[lng]['insert'], command=switch), 'insert')
  switch_button.pack(side=tk.RIGHT, padx=(5, 0))

  warning = register(ttk.Label(
      switch_frame, style='Warning.TLabel'), 'fill_fields')

  version_frame = ttk.Frame(main_frame)
  version_frame.grid(row=7, column=0, columnspan=2,
                     sticky='nwse', pady=(20, 0))

  version_label = ttk.Label(
      version_frame, text=VERSION, style='Version.TLabel')
  version_label.pack(side='right')

  theme_selector = register(ThemeSelector(
      version_frame, options=["light", "dark", "contrast"], options_config={'padx': (0, 2), 'side': 'left'}), 'theme')
  Packer.pack(theme_selector, side='left', padx=(0, 7))

  language_selector = LanguageSelector(
      version_frame, languages=('english', 'русский'), options_config={'padx': (0, 2), 'side': 'left'})
  Packer.pack(language_selector, side='left')

  main_frame.columnconfigure(1, weight=1)
  main_frame.rowconfigure(6, weight=1)
  root.bind("<Button-1>", pressed)
  root.bind("<ButtonRelease-1>", released)
  root.bind("<Key>", key_pressed)

  if not is_admin():
    messagebox.showwarning(  # type: ignore
        "Warning", "If the text doesn't write try opening program with admin rights")

  root.mainloop()
