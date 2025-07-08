from tkinter import ttk


def style():
  st = ttk.Style()
  st.theme_create(  # type: ignore
      'dark',
      parent='clam',
      settings={
          '.': {
              'configure': {
                  'background': '#313131',
                  'foreground': 'white',
                  'selectbackground': '#a0a0a0',
                  'selectforeground': 'black',
                  'insertcolor': 'white',
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
                  'fieldbackground': "#444444",
                  'foreground': 'white',
                  'padding': 6,
                  'font': ('Helvetica', 14, 'bold'),
                  'borderwidth': 1,
                  'lightcolor': '#f0f0f0',
                  'bordercolor': '#c7c7c7',
                  'relief': 'sunken'
              }
          },
          'TLabel': {
              'configure': {
                  'foreground': 'white',
                  'padding': 5,
                  'font': ('Arial', 15)
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
          },
          'ThemeSelector.TButton': {
              'configure': {
                  'anchor': 'c',
                  'background': "#444444",
                  'foreground': 'white',
                  'padding': 6,
                  'font': ('Helvetica', 10),
                  'borderwidth': 1,
                  'lightcolor': '#f0f0f0',
                  'bordercolor': '#c7c7c7',
                  'relief': 'sunken'
              },
              'map': {
                  'background': [('active', '#666666'), ('pressed', '#444444')]
              }
          },
      }
  )

  st.theme_create(  # type: ignore
      'light',
      parent='clam',
      settings={
          '.': {
              'configure': {
                  'background': '#dfdfdf',
                  'foreground': 'black',
                  'insertcolor': 'black',
                  
              }
          },
          'TButton': {
              'configure': {
                  'anchor': 'c',
                  'background': "#e0e0e0",
                  'foreground': 'black',
                  'padding': 6,
                  'font': ('Helvetica', 14, 'bold'),
                  'borderwidth': 1,
                  'lightcolor': '#ffffff',
                  'bordercolor': '#a0a0a0',
                  'relief': 'raised'
              },
              'map': {
                  'background': [('active', '#d0d0d0'), ('pressed', '#b0b0b0')]
              }
          },
          'TEntry': {
              'configure': {
                  'fieldbackground': '#e0e0e0',
                  'foreground': 'black',
                  'padding': 6,
                  'font': ('Helvetica', 14, 'bold'),
                  'borderwidth': 1,
                  'lightcolor': '#ffffff',
                  'bordercolor': '#a0a0a0',
                  'relief': 'raised'
              }
          },
          'TLabel': {
              'configure': {
                  'foreground': 'black',
                  'padding': 5,
                  'font': ('Arial', 15)
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
                  'foreground': '#555555'
              }
          },
          'Finished.TEntry': {
              'configure': {
                  'fieldbackground': '#e0e0e0',
                  'foreground': 'black',
                  'lightcolor': '#ffffff',
                  'bordercolor': '#a0a0a0',
              }
          },
          'Warning.TLabel': {
              'configure': {
                  'foreground': 'red',
                  'font': ('Arial', 15),
                  'padding': 5
              }
          },
          'ThemeSelector.TButton': {
              'configure': {
                  'anchor': 'c',
                  'background': "#e0e0e0",
                  'foreground': 'black',
                  'padding': 6,
                  'font': ('Helvetica', 10),
                  'borderwidth': 1,
                  'lightcolor': '#ffffff',
                  'bordercolor': '#a0a0a0',
                  'relief': 'raised'
              },
              'map': {
                  'background': [('active', '#d0d0d0'), ('pressed', '#b0b0b0')]
              }
          },
      }
  )

  st.theme_create(  # type: ignore
      'contrast',
      parent='clam',
      settings={
          '.': {
              'configure': {
                  'background': '#121212',
                  'foreground': '#ffffff',
                  'selectbackground': '#4a98cf',
                  'selectforeground': 'white',
                  'insertcolor':'yellow'
              }
          },
          'TButton': {
              'configure': {
                  'anchor': 'c',
                  'background': "#000000",
                  'foreground': '#ffff00',
                  'padding': 6,
                  'font': ('Helvetica', 14, 'bold'),
                  'borderwidth': 2,
                  'lightcolor': '#ff0000',
                  'bordercolor': '#ffff00',
                  'relief': 'raised'
              },
              'map': {
                  'background': [('active', '#222222'), ('pressed', '#000000')],
                  'foreground': [('active', '#ffffff')]
              }
          },
          'TEntry': {
              'configure': {
                  'fieldbackground': "#000000",
                  'foreground': '#ffff00',
                  'padding': 6,
                  'font': ('Helvetica', 14, 'bold'),
                  'borderwidth': 2,
                  'lightcolor': '#ff0000',
                  'bordercolor': '#ffff00',
                  'relief': 'raised'
              }
          },
          'TLabel': {
              'configure': {
                  'foreground': '#ffff00',
                  'padding': 5,
                  'font': ('Arial', 15)
              }
          },
          'Title.TLabel': {
              'configure': {
                  'font': ('Helvetica', 20, 'bold'),
                  'foreground': '#ff0000'
              }
          },
          'Version.TLabel': {
              'configure': {
                  'font': ('Helvetica', 8),
                  'foreground': '#ff8800'
              }
          },
          'Finished.TEntry': {
              'configure': {
                  'fieldbackground': '#000000',
                  'foreground': '#ffff00',
                  'lightcolor': '#ff0000',
                  'bordercolor': '#ffff00',
              }
          },
          'Warning.TLabel': {
              'configure': {
                  'foreground': '#ff0000',
                  'font': ('Arial', 15, 'bold'),
                  'padding': 5
              }
          },
          'ThemeSelector.TButton': {
              'configure': {
                  'anchor': 'c',
                  'background': "#000000",
                  'foreground': '#ffff00',
                  'padding': 6,
                  'font': ('Helvetica', 10),
                  'borderwidth': 2,
                  'lightcolor': '#ff0000',
                  'bordercolor': '#ffff00',
                  'relief': 'raised'
              },
              'map': {
                  'background': [('active', '#222222'), ('pressed', '#000000')],
                  'foreground': [('active', '#ffffff')]
              }
          },
      }
  )

  return st
