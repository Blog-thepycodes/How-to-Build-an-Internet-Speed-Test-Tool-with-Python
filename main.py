from tkinter import *
from tkinter import messagebox
import speedtest
 
 
 
def measure_speed():
   st = speedtest.Speedtest()
 
 
 
   def start_speed_test():
       choice = choice_var.get()
 
 
 
       if choice == '1':
           download_speed = st.download() / (1024 * 1024) # Convert to Mbps
           result_label.config(text=f"Download Speed: {download_speed:.2f} Mbps")
       elif choice == '2':
            upload_speed = st.upload() / (1024 * 1024) # Convert to Mbps
            result_label.config(text=f"Upload Speed: {upload_speed:.2f} Mbps")
       elif choice == '3':
            server = st.get_best_server()
            ping = server["latency"]
            result_label.config(text=f"Ping: {ping} ms")
       else:
           messagebox.showerror("Error", "Invalid choice. Please select 1, 2, or 3.")
 
 
 
 
   root = Tk()
   root.title("Internet Speed Test - The Pycodes")
   root.geometry("500x200")
 
 
 
 
   choice_var = StringVar()
   choice_var.set('1')
 
 
 
 
   label = Label(root, text="Select the type of speed measurement :",font="arial 16 bold")
   label.pack()
 
 
 
 
   download_radio = Radiobutton(root, text="Download Speed", variable=choice_var, value='1',font="arial 12")
   download_radio.pack()
   upload_radio = Radiobutton(root, text="Upload Speed", variable=choice_var, value='2',font="arial 12")
   upload_radio.pack()
   ping_radio = Radiobutton(root, text="Ping", variable=choice_var, value='3',font="arial 12")
   ping_radio.pack()
 
 
 
 
   start_button = Button(root, text="Start Speed Test",font="arial 12", command=start_speed_test)
   start_button.pack()
 
 
 
   result_label = Label(root, text="",font="arial 12")
   result_label.pack()
 
 
 
   root.mainloop()
 
 
 
if __name__ == "__main__":
   measure_speed()
