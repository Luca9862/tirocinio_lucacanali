'''
TIROCINIO 2023 - CORSO DI LAUREA DI INFORMATICA TRIENNALE
Luca Canali 744802
This code is a simple implementation of a graphical interface based on the pgn_manager library, created by me.
You can run the program from the graphical interface (Windows and Mac) or you can directly run this file.
Remember to run the command: pip install pgn_manager
'''
#! DON'T USE THIS SCRIPT
import os
from pgn_manager import _createID
from pgn_manager.pfilter import filter_player, _readPGN
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
from games_manager import on_button_search_file
from games_manager import on_button_search_path

def filter_white(pgn, player):
    """
    Filters a PGN file to only include games where the specified player plays as White.

    Args:
        pgn: The filename of the PGN file to filter.
        player: The name of the player to filter for.

    Returns:
        A list of games where the specified player plays as White.
    """
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player == game.headers.get('White'):
            games_filtered.append(game)
    return games_filtered 

def export_pgn(games, destination_path):
    with open(os.path.join(destination_path, 'pgn_exported' + ".pgn"), "a") as f:
        for game in games:
            f.append(str(game))

def on_button_filter_player():
    export_pgn(filter_player(str(text_box_pgn_filter_player.get(1.0, 'end-1c')), str(text_box_player_name_fplayer.get(1.0))), text_box_destination_filter_player.get(1.0))

def on_button_filter_white(pgn, path):
    games = _readPGN(pgn)
    games_filtered = filter_white(pgn, str(text_box_destination_filter_player.get(1.0, 'end-1c')))
    with open(os.path.join(path, 'pgn_exported.pgn'), 'w') as f:
        for game in games_filtered:
            f.write(str(game))
# ---------- GUI ---------- #
root_filter = tk.Tk()
root_filter.title('pgn_filter')
root_filter.geometry("580x280")

notebook = ttk.Notebook(root_filter)
notebook.pack(pady=10, expand=True)

style = Style()
style.configure('W.TButton', font =
               ('calibri', 10, 'bold', 'underline'),
                foreground = 'red')

#menu "filter_player"
frame_filter_player = ttk.Frame(notebook, width=400, height=280)
button_pgn_filter_player = ttk.Button(frame_filter_player, text='pgn', 
                                         command=lambda: on_button_search_file(text_box_pgn_filter_player))
button_destination_filter_player = ttk.Button(frame_filter_player, text='Path', 
                                                 command=lambda: on_button_search_path(text_box_destination_filter_player))
button_digit_player = ttk.Button(frame_filter_player, text='insert_player_name', command=lambda: messagebox.showinfo('inutile!' , 'inutile'))
button_filter_player = ttk.Button(frame_filter_player, text='FILTER', style= 'W.TButton',
                                  command=lambda:on_button_filter_player())
button_filter_white = ttk.Button(frame_filter_player, text='FILTER WHITE PLAYER', style= 'W.TButton',
                                 command=lambda: on_button_filter_white(str(text_box_pgn_filter_player.get(1.0, 'end-1c')), str(text_box_destination_filter_player.get(1.0, 'end-1c'))))
button_filter_black = ttk.Button(frame_filter_player, text='FILTER BLACK PLAYER', style= 'W.TButton',
                                 command=lambda:messagebox.showinfo('TO IMPLEMENT!'))
text_box_player_name_fplayer = tk.Text(frame_filter_player, width=50, height=1)
text_box_pgn_filter_player = tk.Text(frame_filter_player, width=50, height=1)
text_box_destination_filter_player = tk.Text(frame_filter_player, width=50, height=1)
# positioning button
button_pgn_filter_player.grid(row=0, column=0, padx=10, pady=10)
button_destination_filter_player.grid(row=1, column=0, padx=10, pady=10)
button_digit_player.grid(row=2, column=0, padx=10, pady=10)
button_filter_player.grid(row=3, column=0, padx=10, pady=10)
button_filter_white.grid(row=3, column=1, padx=10, pady=10)
button_filter_black.grid(row=3, column=2, padx=10, pady=10)
text_box_player_name_fplayer.grid(row=2, column=1, padx=10, pady=10, sticky='ew')
text_box_pgn_filter_player.grid(row=0, column=1,padx=10, pady=10, sticky='ew')
text_box_destination_filter_player.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

# menu 'filter_player_win'
frame_filter_player_win = ttk.Frame(notebook, width=400, height=280)
button_pgn_filter_pwin = ttk.Button(frame_filter_player_win, text='PGN',
                                    command=lambda: on_button_search_file(text_box_pgn_filter_pwin))
text_box_pgn_filter_pwin = tk.Text(frame_filter_player_win, width=50, height=1)
button_destination_pwin = ttk.Button(frame_filter_player_win, text='path',
                                    command=lambda: on_button_search_path(text_box_pgn_filter_pwin_path))
text_box_pgn_filter_pwin_path = tk.Text(frame_filter_player_win, width=50, height=1)
button_player_name_pwin = ttk.Button(frame_filter_player_win, text='player_name')
text_box_player_name_pwin = tk.Text(frame_filter_player_win, width=50, height=1)
button_filter_pwin = ttk.Button(frame_filter_player_win, text='FILTER PLAYER', style= 'W.TButton',
                                command=lambda: messagebox.showinfo('TO IMPLEMENT!'))
button_filter_wwin = ttk.Button(frame_filter_player_win, text='FILTER WIN PLAYER WHITE', style= 'W.TButton',
                                command=lambda: messagebox.showinfo('TO IMPLEMENT!'))
button_filter_bwin = ttk.Button(frame_filter_player_win, text='FILTER WIN PLAYER BLACK', style= 'W.TButton',
                                command=lambda: messagebox.showinfo('TO IMPLEMENT!'))
# positioning button
button_pgn_filter_pwin.grid(row=0, column=0, padx=10, pady=10)
text_box_pgn_filter_pwin.grid(row=0, column=1, padx=10, pady=10, sticky='ew')
button_destination_pwin.grid(row=1, column=0, padx=10, pady=10)
text_box_pgn_filter_pwin_path.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
button_player_name_pwin.grid(row=2, column=0, padx=10, pady=10)
text_box_player_name_pwin.grid(row=2, column=1, padx=10, pady=10, sticky='ew')
button_filter_pwin.grid(row=3 , column=0, padx=10, pady=10)
button_filter_wwin.grid(row=3, column=1, padx=10, pady=10)
button_filter_bwin.grid(row=3, column=2, padx=10, pady=10)

#menu 'filter_player_lose'
frame_filter_player_lose = ttk.Frame(notebook, width=400, height=280)

#menu 'filter_player_draws'
frame_filter_player_draw = ttk.Frame(notebook, width=400, height=280)

notebook.add(frame_filter_player, text='filter_for_player')
notebook.add(frame_filter_player_win, text='filter_player_win')
notebook.add(frame_filter_player_lose, text='filter_player_lose')
notebook.add(frame_filter_player_draw, text='filter_player_draw')

root_filter.mainloop()