from tkinter import ttk


def style():
    st = ttk.Style()
    st.theme_create(
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
    st.theme_create(
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

    st.theme_create(
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

    return st