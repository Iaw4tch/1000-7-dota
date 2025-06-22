from tkinter import ttk


def style():
  st = ttk.Style()
  st.theme_create( # type: ignore
      'dark',
      parent='clam',
      settings={
          '.': {
              'configure': {
                  'background': '#313131',
                  'foreground': 'white'
              }
          },
          'TButton': {
              'configure': {
                  'anchor': 'c',
                  'background': "#444444",
                  'foreground': 'white',
                  'padding': 6,
                  'font': ('Helvetica', 14, 'bold'),
                  'borderwidth': 1,
                  'lightcolor': '#f0f0f0',
                  'bordercolor': '#c7c7c7',
                  'relief': 'sunken'
              },
              'map': {
                  'background': [('active', '#666666'), ('pressed', '#444444')]
              }
          },
          'TEntry': {
              'configure': {
                  'fieldbackground': '#444444',
                  'foreground': 'white',
                  'insertcolor': 'white'
              }
          },
          'TLabel': {
              'configure': {
                  'foreground': 'white',
                  'padding': 5,
                  'font': ('Arial', 15)
              }
          },
          'TCombobox': {
              'configure': {
                  'background': '#444444',
                  'fieldbackground': '#444444',
                  'selectbackground': "#444444"
              },
              'map': {
                  'fieldbackground': [("readonly", "#444444"), ("focus", "#444444")],
                  'selectbackground': [("focus", "#444444")]
              }
          },
          'Title.TLabel': {
              'configure': {
                  'font': ('Helvetica', 20, 'bold'),
              }
          },
          'Version.TLabel': {
              'configure': {
                  'font': ('Helvetica', 8),
                  'foreground': '#aaaaaa'
              }
          },
          'Finished.TEntry': {
              'configure': {
                  'fieldbackground': '#444444',
                  'foreground': 'white',
                  'lightcolor': '#f0f0f0',
                  'bordercolor': '#c7c7c7',
              }
          },
          'Warning.TLabel': {
              'configure': {
                  'foreground': 'red',
                  'font': ('Arial', 15),
                  'padding': 5
              }
          }
      }
  )

  st.theme_create(  # type: ignore
      'light',
      parent='clam',
      settings={
          '.': {
              'configure': {
                  'background': '#313131',
                  'foreground': 'white'
              }
          },
          'TButton': {
              'configure': {
                  'anchor': 'c',
                  'background': "#444444",
                  'foreground': 'white',
                  'padding': 6,
                  'font': ('Helvetica', 14, 'bold'),
                  'borderwidth': 1,
                  'lightcolor': '#f0f0f0',
                  'bordercolor': '#c7c7c7',
                  'relief': 'sunken'
              },
              'map': {
                  'background': [('active', '#666666'), ('pressed', '#444444')]
              }
          },
          'TEntry': {
              'configure': {
                  'fieldbackground': '#444444',
                  'foreground': 'white',
                  'insertcolor': 'white'
              }
          },
          'TLabel': {
              'configure': {
                  'foreground': 'white',
                  'padding': 5,
                  'font': ('Arial', 15)
              }
          },
          'TCombobox': {
              'configure': {
                  'background': '#444444',
                  'fieldbackground': '#444444',
                  'selectbackground': "#444444"
              },
              'map': {
                  'fieldbackground': [("readonly", "#444444"), ("focus", "#444444")],
                  'selectbackground': [("focus", "#444444")]
              }
          },
          'Title.TLabel': {
              'configure': {
                  'font': ('Helvetica', 20, 'bold'),
              }
          },
          'Version.TLabel': {
              'configure': {
                  'font': ('Helvetica', 8),
                  'foreground': '#aaaaaa'
              }
          },
          'Finished.TEntry': {
              'configure': {
                  'fieldbackground': '#444444',
                  'foreground': 'white',
                  'lightcolor': '#f0f0f0',
                  'bordercolor': '#c7c7c7',
              }
          },
          'Warning.TLabel': {
              'configure': {
                  'foreground': 'red',
                  'font': ('Arial', 15),
                  'padding': 5
              }
          }
      }
  )

  st.theme_create(  # type: ignore
      'black',
      parent='clam',
      settings={
          '.': {
              'configure': {
                  'background': '#313131',
                  'foreground': 'white'
              }
          },
          'TButton': {
              'configure': {
                  'anchor': 'c',
                  'background': "#444444",
                  'foreground': 'white',
                  'padding': 6,
                  'font': ('Helvetica', 14, 'bold'),
                  'borderwidth': 1,
                  'lightcolor': '#f0f0f0',
                  'bordercolor': '#c7c7c7',
                  'relief': 'sunken'
              },
              'map': {
                  'background': [('active', '#666666'), ('pressed', '#444444')]
              }
          },
          'TEntry': {
              'configure': {
                  'fieldbackground': '#444444',
                  'foreground': 'white',
                  'insertcolor': 'white'
              }
          },
          'TLabel': {
              'configure': {
                  'foreground': 'white',
                  'padding': 5,
                  'font': ('Arial', 15)
              }
          },
          'TCombobox': {
              'configure': {
                  'background': '#444444',
                  'fieldbackground': '#444444',
                  'selectbackground': "#444444"
              },
              'map': {
                  'fieldbackground': [("readonly", "#444444"), ("focus", "#444444")],
                  'selectbackground': [("focus", "#444444")]
              }
          },
          'Title.TLabel': {
              'configure': {
                  'font': ('Helvetica', 20, 'bold'),
              }
          },
          'Version.TLabel': {
              'configure': {
                  'font': ('Helvetica', 8),
                  'foreground': '#aaaaaa'
              }
          },
          'Finished.TEntry': {
              'configure': {
                  'fieldbackground': '#444444',
                  'foreground': 'white',
                  'lightcolor': '#f0f0f0',
                  'bordercolor': '#c7c7c7',
              }
          },
          'Warning.TLabel': {
              'configure': {
                  'foreground': 'red',
                  'font': ('Arial', 15),
                  'padding': 5
              }
          }
      }
  )

  return st
