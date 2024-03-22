import customtkinter as ctk
import os
import pickle
from pygame import mixer
from PIL import Image, ImageTk
from tkinter import filedialog

class Data:
    def __init__(self):
        diretorio_atual = os.path.dirname(os.path.realpath(__file__))
        self.musics = [
            Music("Can't Stop", "Red Hot Chili Peppers", "C:\\Users\\vcarvalho\\OneDrive - CORSB RADIOTERAPIA E MEGAVOLTAGEM LTDA\\Apps\\StagePlayer\\assets\\Example_musics\\red_hot.jpg", "C:\\Users\\vcarvalho\\OneDrive - CORSB RADIOTERAPIA E MEGAVOLTAGEM LTDA\\Apps\\StagePlayer\\assets\\Example_musics\\RED HOT CHILI PEPPERS - Can't Stop.mp3"),
            Music("Stop Crying Your Heart Out", "Oasis", "C:\\Users\\vcarvalho\\OneDrive - CORSB RADIOTERAPIA E MEGAVOLTAGEM LTDA\\Apps\\StagePlayer\\assets\\Example_musics\\oasis_cover.jpg", "C:\\Users\\vcarvalho\\OneDrive - CORSB RADIOTERAPIA E MEGAVOLTAGEM LTDA\\Apps\\StagePlayer\\assets\\Example_musics\\Oasis - Stop Crying Your Heart Out (Official Video).mp3"),
            Music("I Miss You", "Blink-182", "C:\\Users\\vcarvalho\\OneDrive - CORSB RADIOTERAPIA E MEGAVOLTAGEM LTDA\\Apps\\StagePlayer\\assets\\Example_musics\\blink_cover.png", "C:\\Users\\vcarvalho\\OneDrive - CORSB RADIOTERAPIA E MEGAVOLTAGEM LTDA\\Apps\\StagePlayer\\assets\\Example_musics\\Blink 182 - I Miss You.mp3"),
            Music("Song 3", "Artist 3", "C:\\Users\\vcarvalho\\OneDrive - CORSB RADIOTERAPIA E MEGAVOLTAGEM LTDA\\Apps\\StagePlayer\\assets\\unknown_cover.jpg", "C:\\Users\\vcarvalho\\OneDrive - CORSB RADIOTERAPIA E MEGAVOLTAGEM LTDA\\Apps\\StagePlayer\\assets\\Example_musics\\RED HOT CHILI PEPPERS - Can't Stop.mp3"),
            Music("Song 4", "Artist 4", "C:\\Users\\vcarvalho\\OneDrive - CORSB RADIOTERAPIA E MEGAVOLTAGEM LTDA\\Apps\\StagePlayer\\assets\\unknown_cover.jpg", "C:\\Users\\vcarvalho\\OneDrive - CORSB RADIOTERAPIA E MEGAVOLTAGEM LTDA\\Apps\\StagePlayer\\assets\\Example_musics\\Oasis - Stop Crying Your Heart Out (Official Video).mp3"),
            Music("Song 5", "Artist 5", "C:\\Users\\vcarvalho\\OneDrive - CORSB RADIOTERAPIA E MEGAVOLTAGEM LTDA\\Apps\\StagePlayer\\assets\\unknown_cover.jpg", "C:\\Users\\vcarvalho\\OneDrive - CORSB RADIOTERAPIA E MEGAVOLTAGEM LTDA\\Apps\\StagePlayer\\assets\\Example_musics\\Blink 182 - I Miss You.mp3"),
        ]
        self.playlists = [
            Playlist("Rock", "C:\\Users\\vcarvalho\\OneDrive - CORSB RADIOTERAPIA E MEGAVOLTAGEM LTDA\\Apps\\StagePlayer\\assets\\unknown_cover.jpg", [self.musics[0], self.musics[1], self.musics[3], self.musics[2]]),
            Playlist("Show 22/03", "C:\\Users\\vcarvalho\\OneDrive - CORSB RADIOTERAPIA E MEGAVOLTAGEM LTDA\\Apps\\StagePlayer\\assets\\unknown_cover.jpg", [self.musics[2], self.musics[3]]),
            Playlist("Playlist 3", "C:\\Users\\vcarvalho\\OneDrive - CORSB RADIOTERAPIA E MEGAVOLTAGEM LTDA\\Apps\\StagePlayer\\assets\\unknown_cover.jpg", [self.musics[5], self.musics[4], self.musics[3], self.musics[2]]),
            Playlist("Playlist 4", "C:\\Users\\vcarvalho\\OneDrive - CORSB RADIOTERAPIA E MEGAVOLTAGEM LTDA\\Apps\\StagePlayer\\assets\\unknown_cover.jpg", [self.musics[2], self.musics[1], self.musics[3]]),
            Playlist("Playlist 5", "C:\\Users\\vcarvalho\\OneDrive - CORSB RADIOTERAPIA E MEGAVOLTAGEM LTDA\\Apps\\StagePlayer\\assets\\unknown_cover.jpg", [self.musics[4], self.musics[3], self.musics[2]]), ]

    def save(self):
        with open('stage_player_data.pkl', 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load(cls):
        try:
            with open('stage_player_data.pkl', 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return cls()

class NewMusic(ctk.CTkToplevel):
    def __init__(self, add_music_callback, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("Stage Player - Add Music")
        self.grid_columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.folder_icon_image = ctk.CTkImage(Image.open((os.path.dirname(os.path.realpath(__file__))) + "/assets/folder_icone.png"), size=(30, 30))
        self.create_new_music_widgets()
        self.add_music_callback = add_music_callback
        self.music_name = ""
        self.music_artist = ""
        self.music_cover = ""
        self.music_file = ""

    def create_new_music_widgets(self):
        self.main_frame = ctk.CTkScrollableFrame(self)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=0)
        self.main_frame.grid_columnconfigure(2, weight=1)
        self.main_frame.grid_columnconfigure(3, weight=0)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        self.new_music_label = ctk.CTkLabel(self.main_frame, text="Adicione uma Música", font=ctk.CTkFont(family='Kollektif', size=22, weight="bold"))
        self.new_music_label.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=20, pady=(10, 5))

        self.music_name_label = ctk.CTkLabel(self.main_frame, text="Nome da Música", font=ctk.CTkFont(family='Kollektif', size=16, weight="normal"))
        self.music_name_label.grid(row=1, column=0, columnspan=4, sticky="w", padx=20, pady=(10, 0))
        self.music_name_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Nome da Música", font=ctk.CTkFont(family='Kollektif', size=16, weight="normal"))
        self.music_name_entry.grid(row=2, column=0, columnspan=4, sticky="nsew", padx=20, pady=(0, 10))

        self.music_artist_label = ctk.CTkLabel(self.main_frame, text="Adicione o Autor", font=ctk.CTkFont(family='Kollektif', size=16, weight="normal"))
        self.music_artist_label.grid(row=3, column=0, columnspan=4, sticky="w", padx=20, pady=(10, 0))
        self.music_artist_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Autor da Música", font=ctk.CTkFont(family='Kollektif', size=16, weight="normal"))
        self.music_artist_entry.grid(row=4, column=0, columnspan=4, sticky="nsew", padx=20, pady=(0, 10))

        self.music_cover_label = ctk.CTkLabel(self.main_frame, text="Adicione uma Capa", font=ctk.CTkFont(family='Kollektif', size=16, weight="normal"))
        self.music_cover_label.grid(row=5, column=0, columnspan=4, sticky="w", padx=20, pady=(10, 0))
        self.music_cover_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Adicione um arquivo", font=ctk.CTkFont(family='Kollektif', size=16, weight="normal"))
        self.music_cover_entry.grid(row=6, column=0, columnspan=3, sticky="nsew", padx=(20, 5), pady=(0, 10))
        self.music_cover_browser_button = ctk.CTkButton(self.main_frame, text="", command=lambda: self.browse_files(self.music_cover_entry, "image"), hover_color=("gray70", "gray30"), fg_color="transparent", image=self.folder_icon_image, width=30)
        self.music_cover_browser_button.grid(row=6, column=3, columnspan=1, sticky="ew", padx=(0, 20), pady=(0, 10))

        self.music_file_label = ctk.CTkLabel(self.main_frame, text="Adicione o Arquivo da Música", font=ctk.CTkFont(family='Kollektif', size=16, weight="normal"))
        self.music_file_label.grid(row=7, column=0, columnspan=4, sticky="w", padx=20, pady=(10, 0))
        self.music_file_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Adicione um arquivo", font=ctk.CTkFont(family='Kollektif', size=16, weight="normal"))
        self.music_file_entry.grid(row=8, column=0, columnspan=3, sticky="nsew", padx=(20, 5), pady=(0, 10))
        self.music_file_browser_button = ctk.CTkButton(self.main_frame, text="", command=lambda: self.browse_files(self.music_file_entry, "music"), hover_color=("gray70", "gray30"), fg_color="transparent", image=self.folder_icon_image, width=30)
        self.music_file_browser_button.grid(row=8, column=3, columnspan=1, sticky="nsew", padx=(0, 20), pady=(0, 10))

        self.music_save_button = ctk.CTkButton(self.main_frame, text="Salvar", command=self.save_music, font=ctk.CTkFont(family='Kollektif', size=16, weight="normal"))
        self.music_save_button.grid(row=9, column=0, columnspan=2, sticky="nsew", padx=(20, 10), pady=(10, 10))

        self.music_clear_button = ctk.CTkButton(self.main_frame, text="Limpar", command=self.clear_entries, font=ctk.CTkFont(family='Kollektif', size=16, weight="normal"))
        self.music_clear_button.grid(row=9, column=2, columnspan=2, sticky="nsew", padx=(20, 10), pady=(10, 10))

    def clear_entries(self):
        self.music_name_entry.delete(0, "end")
        self.music_artist_entry.delete(0, "end")
        self.music_cover_entry.delete(0, "end")
        self.music_file_entry.delete(0, "end")

    def get_entries(self):
        music_name = self.music_name_entry.get()
        music_artist = self.music_artist_entry.get()
        music_cover = self.music_cover_entry.get()
        music_file = self.music_file_entry.get()
        return music_name, music_artist, music_cover, music_file

    def save_music(self):
        self.music_name, self.music_artist, self.music_cover, self.music_file = self.get_entries()
        self.add_music_callback(self.music_name, self.music_artist, self.music_cover, self.music_file)
        self.destroy()

    def browse_files(self, entry, file_type):
        if file_type == "music":
            filename = filedialog.askopenfilename(filetypes=(("Arquivos de Música", ("*.mp3")),))
        elif file_type == "image":
            filename = filedialog.askopenfilename(filetypes=(("Imagens", ("*.jpeg", "*.jpg", "*.png")),))

        if filename:
            entry.configure(state="normal")
            entry.delete(first_index=0, last_index=500)
            entry.insert(0, filename)
            entry.configure(state="normal")
            entry.configure(state="readonly")
        else:
            pass

class NewPlaylist(ctk.CTkToplevel):
    def __init__(self, musics, add_playlist_callback, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("Stage Player - Add Playlist")
        self.grid_columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.folder_icon_image = ctk.CTkImage(Image.open((os.path.dirname(os.path.realpath(__file__))) + "/assets/folder_icone.png"), size=(30, 30))
        self.create_new_playlist_widgets(musics)
        self.add_playlist_callback = add_playlist_callback
        self.playlist_name = ""
        self.playlist_cover = ""
        self.selected_musics = []

    def create_new_playlist_widgets(self, musics):
        self.main_frame = ctk.CTkScrollableFrame(self)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=0)
        self.main_frame.grid_columnconfigure(2, weight=1)
        self.main_frame.grid_columnconfigure(3, weight=0)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=0)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        self.new_playlist_label = ctk.CTkLabel(self.main_frame, text="Adicione uma Playlist", font=ctk.CTkFont(family='Kollektif', size=22, weight="bold"))
        self.new_playlist_label.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=20, pady=(10, 5))

        self.playlist_name_label = ctk.CTkLabel(self.main_frame, text="Nome da Playlist", font=ctk.CTkFont(family='Kollektif', size=16, weight="normal"))
        self.playlist_name_label.grid(row=1, column=0, columnspan=4, sticky="w", padx=20, pady=(10, 0))
        self.playlist_name_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Nome da Playlist", font=ctk.CTkFont(family='Kollektif', size=16, weight="normal"))
        self.playlist_name_entry.grid(row=2, column=0, columnspan=4, sticky="nsew", padx=20, pady=(0, 10))

        self.playlist_cover_label = ctk.CTkLabel(self.main_frame, text="Adicione uma Capa", font=ctk.CTkFont(family='Kollektif', size=16, weight="normal"))
        self.playlist_cover_label.grid(row=3, column=0, columnspan=4, sticky="w", padx=20, pady=(10, 0))
        self.playlist_cover_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Adicione um arquivo", font=ctk.CTkFont(family='Kollektif', size=16, weight="normal"))
        self.playlist_cover_entry.grid(row=4, column=0, columnspan=3, sticky="nsew", padx=(20, 5), pady=(0, 10))
        self.playlist_cover_browser_button = ctk.CTkButton(self.main_frame, text="", command=lambda: self.browse_files(self.playlist_cover_entry), hover_color=("gray70", "gray30"), fg_color="transparent", image=self.folder_icon_image, width=30)
        self.playlist_cover_browser_button.grid(row=4, column=3, columnspan=1, sticky="ew", padx=(0, 20), pady=(0, 10))

        self.playlist_musics_label = ctk.CTkLabel(self.main_frame, text="Adicione Músicas à Playlist", font=ctk.CTkFont(family='Kollektif', size=16, weight="normal"))
        self.playlist_musics_label.grid(row=5, column=0, columnspan=4, sticky="w", padx=20, pady=(10, 0))

        self.music_checkboxes = []
        for index, music in enumerate(musics):
            checkbox = ctk.CTkCheckBox(self.main_frame, text=music.name, font=ctk.CTkFont(family='Kollektif', size=16, weight="normal"))
            checkbox.grid(row=6 + index, column=0, columnspan=4, sticky="w", padx=20, pady=(10, 0))
            self.music_checkboxes.append(checkbox)

        self.main_frame_bottom = ctk.CTkFrame(self)
        self.main_frame_bottom.grid_columnconfigure(0, weight=1)
        self.main_frame_bottom.grid_columnconfigure(1, weight=1)
        self.main_frame_bottom.grid(row=1, column=0, sticky="nsew")

        self.playlist_save_button = ctk.CTkButton(self.main_frame_bottom, text="Salvar", command=self.save_playlist, font=ctk.CTkFont(family='Kollektif', size=16, weight="normal"))
        self.playlist_save_button.grid(row=0, column=0, columnspan=1, sticky="nsew", padx=(20, 10), pady=(10, 10))

        self.playlist_clear_button = ctk.CTkButton(self.main_frame_bottom, text="Limpar", command=self.clear_entries, font=ctk.CTkFont(family='Kollektif', size=16, weight="normal"))
        self.playlist_clear_button.grid(row=0, column=1, columnspan=1, sticky="nsew", padx=(10, 20), pady=(10, 10))

    def clear_entries(self):
        self.playlist_name_entry.delete(0, "end")
        self.playlist_cover_entry.delete(0, "end")
        # Limpeza adicional de entradas, se necessário

    def get_entries(self):
        playlist_name = self.playlist_name_entry.get()
        playlist_cover = self.playlist_cover_entry.get()
        playlist_musics = []
        for music in self.music_checkboxes:
            if music.get() == 1:
                playlist_musics.append(music.cget("text"))
        return playlist_name, playlist_cover, playlist_musics

    def save_playlist(self):
        self.playlist_name, self.playlist_cover, self.playlist_musics = self.get_entries()
        self.add_playlist_callback(self.playlist_name, self.playlist_cover, self.playlist_musics)
        self.destroy()

    def browse_files(self, entry):
        filename = filedialog.askopenfilename(filetypes=(("Imagens", ("*.jpeg", "*.jpg", "*.png")),))

        if filename:
            entry.configure(state="normal")
            entry.delete(first_index=0, last_index=500)
            entry.insert(0, filename)
            entry.configure(state="normal")
            entry.configure(state="readonly")
        else:
            pass

class Music:
    def __init__(self, name, artist, cover, file):
        self.name = name
        self.artist = artist
        self.cover = cover
        self.file = file

class Playlist:
    def __init__(self, name, cover, musics):
        self.name = name
        self.cover = cover
        self.musics = musics

class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Music Player")
        self.geometry("1000x700")
        self.resizable(True, True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.data = Data.load()
        mixer.init()
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.new_music = None
        self.new_playlist = None
        self.current_playlist = None
        self.current_music_index = 0
        self.current_music_playing = None
        self.musics = self.data.musics
        self.playlists = self.data.playlists
        self.create_navigation_frame()
        self.create_main_frame()
        self.create_playlists_frame()
        self.create_musics_frame()
        #self.create_config_frame()
        self.create_player_frame()
        self.select_frame("main_frame")

    def create_player_frame(self):
        self.player_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="black")
        self.player_frame.grid(row=4, column=1, sticky="sew", rowspan=1)
        self.player_frame.grid_rowconfigure(0, weight=1)
        self.player_frame.grid_rowconfigure(1, weight=1)
        self.player_frame.grid_rowconfigure(2, weight=1)
        self.player_frame.grid_columnconfigure(0, weight=1)
        self.player_frame.grid_columnconfigure(1, weight=1)
        self.player_frame.grid_columnconfigure(2, weight=1)
        self.player_frame.grid_columnconfigure(3, weight=1)
        self.player_frame.grid_columnconfigure(4, weight=1)

        self.player_music_name_label = ctk.CTkLabel(self.player_frame, text="", font=ctk.CTkFont(family='Kollektif', size=18, weight="bold"))
        self.player_music_name_label.grid(row=0, column=0, columnspan=5, padx=20, pady=(20, 0), sticky="nsew")

        self.player_music_time_running_label = ctk.CTkLabel(self.player_frame, text="00:00", font=ctk.CTkFont(family='Kollektif', size=16, weight="normal"))
        self.player_music_time_running_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="nsew")

        self.player_music_time_left_label = ctk.CTkLabel(self.player_frame, text="00:00", font=ctk.CTkFont(family='Kollektif', size=16, weight="normal"))
        self.player_music_time_left_label.grid(row=0, column=4, padx=20, pady=(20, 0), sticky="nsew")

        self.player_progress_bar = ctk.CTkProgressBar(self.player_frame, fg_color="yellow", progress_color="red", width=(self.player_frame.cget("width") / 2))
        # self.player_progress_bar.grid(row=1, column=0, columnspan=5, padx=20, pady=20, sticky="nsew")

        self.player_status_slider = ctk.CTkSlider(self.player_frame, fg_color="yellow", progress_color="red", width=(self.player_frame.cget("width") / 2), command=self.set_music_position)
        self.player_status_slider.grid(row=1, column=0, columnspan=5, padx=20, pady=20, sticky="nsew")

        self.player_previous_button = ctk.CTkButton(self.player_frame, corner_radius=25, height=40, border_spacing=10, fg_color="blue", hover_color=("gray70", "gray30"), command=self.previous_music, text="⏪")
        self.player_previous_button.grid(row=2, column=1, padx=10, pady=(0, 20))

        self.player_play_button = ctk.CTkButton(self.player_frame, corner_radius=25, height=40, border_spacing=10, fg_color="blue", hover_color=("gray70", "gray30"), command=self.play_pause_music, text="⏯️")
        self.player_play_button.grid(row=2, column=2, padx=10, pady=(0, 20))

        self.player_next_button = ctk.CTkButton(self.player_frame, corner_radius=25, height=40, border_spacing=10, fg_color="blue", hover_color=("gray70", "gray30"), command=self.next_music, text="⏩")
        self.player_next_button.grid(row=2, column=3, padx=10, pady=(0, 20))

    def create_navigation_frame(self):
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="black")
        self.navigation_frame.grid(row=0, column=0, sticky="ns", rowspan=5)
        self.navigation_frame.grid_rowconfigure(6, weight=1)
        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="Music Player", font=ctk.CTkFont(family='Kollektif', size=20, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.main_frame_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Tela Inicial", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=lambda: self.select_frame("main_frame"), font=ctk.CTkFont(family='Kollektif', size=18, weight="bold"))
        self.main_frame_button.grid(row=1, column=0, sticky="ew")

        self.playlists_frame_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Playlistss", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=lambda: self.select_frame("playlists_frame"), font=ctk.CTkFont(family='Kollektif', size=18, weight="bold"))
        self.playlists_frame_button.grid(row=2, column=0, sticky="ew")

        self.musics_frame_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Músicas", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=lambda: self.select_frame("musics_frame"), font=ctk.CTkFont(family='Kollektif', size=18, weight="bold"))
        self.musics_frame_button.grid(row=3, column=0, sticky="ew")

        # self.config_frame_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Configurações", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=lambda: self.select_frame("config_frame"), font=ctk.CTkFont(family='Kollektif', size=18, weight="bold"))
        # self.config_frame_button.grid(row=4, column=0, sticky="ew")

    def select_frame(self, name):
        self.main_frame_button.configure(fg_color=("gray75", "gray25") if name == "main_frame" else "transparent")
        self.playlists_frame_button.configure(fg_color=("gray75", "gray25") if name == "playlists_frame" else "transparent")
        self.musics_frame_button.configure(fg_color=("gray75", "gray25") if name == "musics_frame" else "transparent")
        #self.config_frame_button.configure(fg_color=("gray75", "gray25") if name == "config_frame" else "transparent")
        if name == "main_frame":
            self.main_frame.grid(row=0, column=1, columnspan=2, sticky="nsew", rowspan=5)
        else:
            self.main_frame.grid_forget()
        if name == "playlists_frame":
            self.playlists_frame.grid(row=0, column=1, columnspan=2, sticky="nsew", rowspan=5)
        else:
            self.playlists_frame.grid_forget()
        if name == "musics_frame":
            self.musics_frame.grid(row=0, column=1, columnspan=2, sticky="nsew", rowspan=5)
        else:
            self.musics_frame.grid_forget()
        # if name == "config_frame":
        #     self.config_frame.grid(row=0, column=1, columnspan=2, sticky="nsew", rowspan=5)
        # else:
        #     self.config_frame.grid_forget()


#----------------MainFrame-----------------
    def create_main_frame(self):
        self.main_frame = ctk.CTkScrollableFrame(self, corner_radius=0, fg_color="gray30")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=1)
        self.main_frame.grid_columnconfigure(3, weight=1)

        self.main_frame_label = ctk.CTkLabel(self.main_frame, text="Tocando Agora", font=ctk.CTkFont(family='Kollektif', size=20, weight="bold"))
        self.main_frame_label.grid(row=0, column=0, padx=(20), pady=(20), sticky="w", columnspan=4)

        self.playlist_names = [playlist.name for playlist in self.playlists]

        self.playlist_combobox = ctk.CTkComboBox(self.main_frame, values=self.playlist_names, height=50, font=ctk.CTkFont(family="Kollektif", size=20, weight="bold"), width=200, state="readonly", command=self.update_main_frame)
        self.playlist_combobox.grid(row=0, column=0, padx=(20, 20), pady=(20), sticky="e", columnspan=4)
        self.playlist_combobox.set(self.playlist_names[0])
        self.selected_playlist_name = self.playlist_combobox.get()

        for playlist in self.playlists:
            if playlist.name == self.selected_playlist_name:
                selected_playlist = playlist

        frame_width = self.main_frame.cget("width")
        row = 1
        col = 0
        for music_index, music in enumerate(selected_playlist.musics):
            music_label = ctk.CTkLabel(self.main_frame, text=music.name, font=ctk.CTkFont(family="Kollektif", size=18, weight="bold"))
            music_label.grid(row=row, column=col, padx=(12, 0), pady=(0, 3), sticky="w")
            music_button = ctk.CTkButton(self.main_frame, text="", command=lambda m=music, i=music_index: self.play_music_from_playlist(self.selected_playlist_name, i), height=frame_width, width=frame_width, image=ctk.CTkImage(Image.open(music.cover), size=(frame_width, frame_width)), anchor="center")
            music_button.grid(row=row + 1, column=col, padx=(10, 0), pady=(0, 25))
            col += 1
            if col == 4:
                row += 2
                col = 0

    def update_main_frame(self, selected_playlist_name):

        for widget in self.main_frame.winfo_children():
            widget.destroy()

        for playlist in self.playlists:
            if playlist.name == selected_playlist_name:
                selected_playlist = playlist

        print(selected_playlist.name)

        self.playlist_names = [playlist.name for playlist in self.playlists]
        self.playlist_combobox = ctk.CTkComboBox(self.main_frame, values=self.playlist_names, height=50, font=ctk.CTkFont(family="Kollektif", size=20, weight="bold"), width=200, state="readonly", command=self.update_main_frame)
        self.playlist_combobox.grid(row=0, column=0, padx=(20, 20), pady=(20), sticky="e", columnspan=4)
        self.playlist_combobox.set(selected_playlist.name)

        self.main_frame_label = ctk.CTkLabel(self.main_frame, text="Tocando Agora", font=ctk.CTkFont(family='Kollektif', size=20, weight="bold"))
        self.main_frame_label.grid(row=0, column=0, padx=(20), pady=(20), sticky="w", columnspan=4)

        frame_width = self.main_frame.cget("width")
        # number_of_musics = enumerate(self.musics)

        # Exibindo as playlists
        row = 1
        col = 0
        for music_index, music in enumerate(selected_playlist.musics):
            music_label = ctk.CTkLabel(self.main_frame, text=music.name, font=ctk.CTkFont(family="Kollektif", size=18, weight="bold"))
            music_label.grid(row=row, column=col, padx=(12, 0), pady=(0, 3), sticky="w")
            music_button = ctk.CTkButton(self.main_frame, text="", command=lambda m=music, i=music_index: self.play_music_from_playlist(self.selected_playlist_name, i), height=frame_width, width=frame_width, image=ctk.CTkImage(Image.open(music.cover), size=(frame_width, frame_width)), anchor="center")
            music_button.grid(row=row + 1, column=col, padx=(10, 0), pady=(0, 25))
            col += 1
            if col == 4:
                row += 2
                col = 0


#--------------PlaylistsFrame----------------
    def create_playlists_frame(self):
        self.playlists_frame = ctk.CTkScrollableFrame(self, corner_radius=0, fg_color="gray30")
        self.playlists_frame.grid_columnconfigure(0, weight=1)
        self.playlists_frame.grid_columnconfigure(1, weight=1)
        self.playlists_frame.grid_columnconfigure(2, weight=1)
        self.playlists_frame.grid_columnconfigure(3, weight=1)
        self.playlists_frame.grid()

        self.playlist_frame_label = ctk.CTkLabel(self.playlists_frame, text="Playlists", font=ctk.CTkFont(family='Kollektif', size=20, weight="bold"))
        self.playlist_frame_label.grid(row=0, column=0, padx=(20), pady=(20), sticky="w", columnspan=4)
        self.add_playlist_button = ctk.CTkButton(self.playlists_frame, text="Adicionar Playlist", command=self.open_add_playlist_screen)
        self.add_playlist_button.grid(row=0, column=0, padx=(20), pady=(20), sticky="e", columnspan=4)

        frame_width = self.playlists_frame.cget("width")
        number_of_playlists = enumerate(self.playlists)

        # Exibindo as playlists
        row = 1
        col = 0
        for playlist in self.playlists:
            playlist_label = ctk.CTkLabel(self.playlists_frame, text=playlist.name, font=ctk.CTkFont(family="Kollektif", size=18, weight="bold"))
            playlist_label.grid(row=row, column=col, padx=(12, 0), pady=(0, 3), sticky="w")
            playlist_button = ctk.CTkButton(self.playlists_frame, text="", command=lambda name=playlist.name: self.select_playlist(name), height=frame_width, width=frame_width, image=ctk.CTkImage(Image.open(playlist.cover), size=(frame_width, frame_width)), anchor="center")
            playlist_button.grid(row=row + 1, column=col, padx=(10, 0), pady=(0, 25))
            col += 1
            if col == 4:
                row += 2
                col = 0

    def update_playlists_frame(self):
        # Atualiza a exibição das playlists
        for widget in self.playlists_frame.winfo_children():
            widget.destroy()

        self.playlist_frame_label = ctk.CTkLabel(self.playlists_frame, text="Playlists", font=ctk.CTkFont(family='Kollektif', size=20, weight="bold"))
        self.playlist_frame_label.grid(row=0, column=0, padx=(20), pady=(20), sticky="w", columnspan=4)
        self.add_playlist_button = ctk.CTkButton(self.playlists_frame, text="Adicionar Playlist", command=self.open_add_playlist_screen)
        self.add_playlist_button.grid(row=0, column=0, padx=(20), pady=(20), sticky="e", columnspan=4)

        frame_width = self.playlists_frame.cget("width")
        number_of_playlists = enumerate(self.playlists)

        # Exibindo as playlists
        row = 1
        col = 0
        for playlist in self.playlists:
            playlist_label = ctk.CTkLabel(self.playlists_frame, text=playlist.name, font=ctk.CTkFont(family="Kollektif", size=18, weight="bold"))
            playlist_label.grid(row=row, column=col, padx=(12, 0), pady=(0, 3), sticky="w")
            playlist_button = ctk.CTkButton(self.playlists_frame, text="", command=lambda name=playlist.name: self.select_playlist(name), height=frame_width, width=frame_width, image=ctk.CTkImage(Image.open(playlist.cover), size=(frame_width, frame_width)), anchor="center")
            playlist_button.grid(row=row + 1, column=col, padx=(10, 0), pady=(0, 25))
            col += 1
            if col == 4:
                row += 2
                col = 0

    def select_playlist(self, playlist_name):
        self.update_main_frame(playlist_name)
        self.select_frame("main_frame")

        #----------------MusicsFrame----------------

    def open_add_playlist_screen(self):
        if self.new_playlist is None or not self.new_playlist.winfo_exists():
            self.new_playlist = NewPlaylist(self.musics, add_playlist_callback=self.add_playlist)  # create window if its None or destroyed
        else:
            self.new_playlist.focus()

    def add_playlist(self, name, cover, musics_names):
        added_musics = []
        for music_name in musics_names:
            for music in self.musics:
                if music.name == music_name:
                    added_musics.append(music)
                    break

        new_loaded_playlist = Playlist(name, cover, added_musics)
        self.playlists.append(new_loaded_playlist)
        self.data.playlists = self.playlists
        self.data.save()
        self.update_playlists_frame()


# ------------MusicsFrames----------------
    def create_musics_frame(self):
        self.musics_frame = ctk.CTkScrollableFrame(self, corner_radius=0, fg_color="gray30")
        self.musics_frame.grid_columnconfigure(0, weight=1)
        self.musics_frame.grid_columnconfigure(1, weight=1)
        self.musics_frame.grid_columnconfigure(2, weight=1)
        self.musics_frame.grid_columnconfigure(3, weight=1)
        self.musics_frame.grid()

        self.musics_frame_label = ctk.CTkLabel(self.musics_frame, text="Músicas", font=ctk.CTkFont(family='Kollektif', size=20, weight="bold"))
        self.musics_frame_label.grid(row=0, column=0, padx=(20), pady=(20), sticky="w", columnspan=4)

        self.add_playlist_button = ctk.CTkButton(self.musics_frame, text="Adicionar Música", command=self.open_add_music_screen)
        self.add_playlist_button.grid(row=0, column=0, padx=(20), pady=(20), sticky="e", columnspan=4)

        frame_width = self.musics_frame.cget("width")
        number_of_musics = enumerate(self.musics)

        # Exibindo as playlists
        row = 1
        col = 0
        for music in self.musics:
            music_label = ctk.CTkLabel(self.musics_frame, text=music.name, font=ctk.CTkFont(family="Kollektif", size=18, weight="bold"))
            music_label.grid(row=row, column=col, padx=(12, 0), pady=(0, 0), sticky="w")
            music_artist_label = ctk.CTkLabel(self.musics_frame, text=music.artist, font=ctk.CTkFont(family="Kollektif", size=12, weight="normal"))
            music_artist_label.grid(row=row + 1, column=col, padx=(12, 0), pady=(0, 3), sticky="w")
            music_button = ctk.CTkButton(self.musics_frame, text="", command=lambda: self.play_music(music), height=frame_width, width=frame_width, image=ctk.CTkImage(Image.open(music.cover), size=(frame_width, frame_width)), anchor="center")
            music_button.grid(row=row + 2, column=col, padx=(10, 0), pady=(0, 25))
            col += 1
            if col == 4:
                row += 3
                col = 0

    def update_musics_frames(self):
        for widget in self.musics_frame.winfo_children():
            widget.destroy()

        self.musics_frame_label = ctk.CTkLabel(self.musics_frame, text="Músicas", font=ctk.CTkFont(family='Kollektif', size=20, weight="bold"))
        self.musics_frame_label.grid(row=0, column=0, padx=(20), pady=(20), sticky="w", columnspan=4)

        self.add_playlist_button = ctk.CTkButton(self.musics_frame, text="Adicionar Música", command=self.open_add_music_screen)
        self.add_playlist_button.grid(row=0, column=0, padx=(20), pady=(20), sticky="e", columnspan=4)

        frame_width = self.musics_frame.cget("width")
        number_of_musics = enumerate(self.musics)

        # Exibindo as playlists
        row = 1
        col = 0
        for music in self.musics:
            music_label = ctk.CTkLabel(self.musics_frame, text=music.name, font=ctk.CTkFont(family="Kollektif", size=18, weight="bold"))
            music_label.grid(row=row, column=col, padx=(12, 0), pady=(0, 0), sticky="w")
            music_artist_label = ctk.CTkLabel(self.musics_frame, text=music.artist, font=ctk.CTkFont(family="Kollektif", size=12, weight="normal"))
            music_artist_label.grid(row=row + 1, column=col, padx=(12, 0), pady=(0, 3), sticky="w")
            music_button = ctk.CTkButton(self.musics_frame, text="", command=lambda: self.play_music(music), height=frame_width, width=frame_width, image=ctk.CTkImage(Image.open(music.cover), size=(frame_width, frame_width)), anchor="center")
            music_button.grid(row=row + 2, column=col, padx=(10, 0), pady=(0, 25))
            col += 1
            if col == 4:
                row += 3
                col = 0

    def open_add_music_screen(self):
        if self.new_music is None or not self.new_music.winfo_exists():
            self.new_music = NewMusic(add_music_callback=self.add_music)  # create window if its None or destroyed
        else:
            self.new_music.focus()

    def add_music(self, music_name, music_artist, music_cover, music_file):
        new_loaded_music = Music(music_name, music_artist, music_cover, music_file)
        self.musics.append(new_loaded_music)
        self.data.musics = self.musics
        self.data.save()
        self.update_musics_frames()


    #----------------Player Functions-------------
    def play_music_from_playlist(self, playlist_name, music_index=0):
        for playlist in self.playlists:
            if playlist.name == playlist_name:
                self.current_playlist = playlist
                self.current_music_index = music_index
                self.play_music(self.current_playlist.musics[self.current_music_index])

    def play_music(self, music):
        self.current_music_playing = music
        current_music = music.file
        mixer.music.load(current_music)
        mixer.music.play()
        current_music_length = round(mixer.Sound(current_music).get_length())

        self.player_music_name_label.configure(text=music.name)
        self.player_status_slider.configure(number_of_steps=current_music_length, to=current_music_length)
        self.update_slider(0)
        self.update_time_left_label(current_music_length)
        self.update_time_running_label()

    def play_pause_music(self):
        if mixer.music.get_busy():
            mixer.music.pause()
        else:
            mixer.music.unpause()

    def next_music(self):
        self.current_music_playing = None
        if self.current_playlist:
            self.current_music_index += 1
            if self.current_music_index >= len(self.current_playlist.musics):
                self.current_music_index = 0
            next_music = self.current_playlist.musics[self.current_music_index]
            next_music_length = round(mixer.Sound(next_music.file).get_length())
            self.play_music(next_music)

    def previous_music(self):
        self.current_music_playing = None
        if self.current_playlist:
            if mixer.music.get_pos() > 3000:
                current_music = self.current_playlist.musics[self.current_music_index]
                current_music_length = round(mixer.Sound(current_music.file).get_length())
                self.play_music(current_music)
            else:
                self.current_music_index -= 1
                if self.current_music_index < 0:
                    self.current_music_index = len(self.current_playlist.musics) - 1
                previous_music = self.current_playlist.musics[self.current_music_index]
                previous_music_length = round(mixer.Sound(previous_music.file).get_length())
                self.play_music(previous_music)

    def select_playlist_and_play_music(self, playlist_name):
        self.current_playlist = None
        for playlist in self.playlists:
            if playlist.name == playlist_name:
                self.current_playlist = playlist
                break
        if self.current_playlist:
            self.play_music_from_playlist(self.current_playlist.name)

    #---------------WidgetsFunctions-----------
    def update_slider(self, current_position):
        current_time = mixer.music.get_pos() / 1000
        if current_position < current_time:
            current_position += 1
            self.player_status_slider.set(current_position)
        self.after(1000, self.update_slider, current_position)

    def set_music_position(self, slider_value):
        current_time = (mixer.music.get_pos())
        slider_value = round(slider_value)
        self.update_slider(slider_value)
        mixer.music.rewind()
        mixer.music.set_pos(slider_value)

    def update_time_running_label(self):
        current_time = mixer.music.get_pos() / 1000
        minutes, seconds = divmod(int(current_time), 60)
        self.player_music_time_running_label.configure(text="{:02d}:{:02d}".format(minutes, seconds))
        self.after(1000, self.update_time_running_label)

    def update_time_left_label(self, total_time):
        current_time = round(mixer.music.get_pos() / 1000)
        remaining_time = total_time - current_time
        minutes, seconds = divmod(int(remaining_time), 60)
        self.player_music_time_left_label.configure(text="{:02d}:{:02d}".format(minutes, seconds))
        if remaining_time > 0:
            self.after(1000, self.update_time_left_label, total_time)
        else:
            self.player_music_time_left_label.configure(text="00:00")

#----------------ConfigFrame----------------
    # def create_config_frame(self):
    #     self.config_frame = ctk.CTkScrollableFrame(self, corner_radius=0, fg_color="blue")
    #     self.config_frame.grid_columnconfigure(0, weight=1)
    #     self.config_frame.grid_rowconfigure(0, weight=1)
if __name__ == '__main__':
    app = Main()
    app.mainloop()