import socket
from tkinter import *

def ClientChat():
    host = '127.0.0.1'#socket.gethostname()  # as both code is running on same pc
    port = 8001  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    print("se ejecuto ClientChat")
    # GUI
    root = Tk()
    root.title("Network UPTC chat service")

    BG_GRAY = "#ABB2B9"
    BG_COLOR = "#D4AC0D"
    TEXT_COLOR = "#EAECEE"

    FONT = "Helvetica 14"
    FONT_BOLD = "Helvetica 13 bold"

    # Send function
    def send():
        send = "You -> " + e.get()
        txt.insert(END, "\n" + send)
        user = e.get().lower()
        print("send " + user)
        message = user  # take input

        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        print('Received from server: ' + data)  # show in terminal
        txt.insert(END, "\n" + "Operator -> " + data)
        e.delete(0, END)

    #se lanza la interfaz
    lable1 = Label(root, bg=BG_GRAY, fg=TEXT_COLOR, text="Welcome to chat UPTC", font=FONT_BOLD, pady=10, width=20, height=1).grid(
        row=0)

    txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
    txt.grid(row=1, column=0, columnspan=2)

    scrollbar = Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.974)

    e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
    e.grid(row=2, column=0)
  
    send = Button(root, text="SEND", font=FONT_BOLD, bg=BG_GRAY,
                command=send).grid(row=2, column=1)
     #queda a la espera de nuevos envios   
    root.mainloop()
if __name__ == '__main__':
    ClientChat()