import tkinter as tk
from threading import Thread
import voice_manager

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Anime kızı Nasibe")

# Pencere boyutunu arttır
root.geometry("300x150")

# Pencereyi sağ alt köşeye yerleştir
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = screen_width - window_width - 100
y_coordinate = screen_height - window_height - 23
root.geometry("+{}+{}".format(x_coordinate, y_coordinate))

label = tk.Label(root, text="Nasibe burada")
label.pack()
voice_manager.speak("Selam Emirhan sana nasıl yardımcı olabilirm.")

# start_nasibe fonksiyonunu bir iş parçacığında başlatmak için bir fonksiyon tanımlayın
def start_nasibe_thread():
    while True:
        voice_manager.start_nasibe()

# Tkinter ana döngüsünü bloke etmeden start_nasibe_thread fonksiyonunu bir iş parçacığında başlat
thread_nasibe = Thread(target=start_nasibe_thread)
thread_nasibe.start()
# Pencereyi göster
root.mainloop()
