from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
from io import BytesIO
import os
import encryption


class Stegno:

    art = '''¯\STAGENO/¯'''
    art2 = '''@(\ ENCODE TEXT IN IMAGE/)@'''
    output_image_size = 0

    def main(self, root):
        root.title('AES-IMAGE STEGA')
        root.geometry('500x600')
        root.resizable(width=False, height=False)
        f = Frame(root)

        title = Label(f, text='AES-IMAGE STEGANO')
        title.config(font=('courier', 33))
        title.grid(pady=10)

        btn_encode = Button(f, text="Encode",
                            command=lambda: self.frame_one_enoder(f), padx=14)
        btn_encode.config(font=('courier', 14))
        btn_decode = Button(f, text="Decode", padx=14,
                            command=lambda: self.framer_decoder(f))
        btn_decode.config(font=('courier', 14))
        btn_decode.grid(pady=12)

        design_art = Label(f, text=self.art)
        design_art.config(font=('courier', 60))

        design_art2 = Label(f, text=self.art2)
        design_art2.config(font=('courier', 12, 'bold'))

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        f.grid()
        title.grid(row=1)
        btn_encode.grid(row=2)
        btn_decode.grid(row=3)
        design_art.grid(row=4, pady=10)
        design_art2.grid(row=5, pady=5)

    def home(self, frame):
        frame.destroy()
        self.main(root)

    def framer_decoder(self, f):
        f.destroy()
        frm = Frame(root)
        label_art = Label(frm, text='Decode Image')
        label_art.config(font=('courier', 90))
        label_art.grid(row=1, pady=50)
        label_one = Label(frm, text='select the image to decode the text')
        label_one.config(font=('courier', 18))
        label_one.grid()
        btn_decoder = Button(frm, text='Select',
                             command=lambda: self.framer_decoder_click(frm))
        btn_decoder.config(font=('courier', 18))
        btn_decoder.grid()
        btn_back = Button(frm, text='Cancel',
                          command=lambda: Stegno.home(self, frm))
        btn_back.config(font=('courier', 18))
        btn_back.grid(pady=15)
        btn_back.grid()
        frm.grid()

    def framer_decoder_click(self, d_f2):
        d_f3 = Frame(root)
        image_file = tkinter.filedialog.askopenfilename(filetypes=(
            [('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'), ('All Files', '*.*')]))
        if not image_file:
            messagebox.showerror("Error", "Please Select an Image")
        else:
            selected_image = Image.open(image_file, 'r')
            myimage = selected_image.resize((300, 200))
            img = ImageTk.PhotoImage(myimage)
            l4 = Label(d_f3, text='Selected Image :')
            l4.config(font=('courier', 18))
            l4.grid()
            panel = Label(d_f3, image=img)
            panel.image = img
            panel.grid()
            hidden_data = self.decode(selected_image)
            lab_2 = Label(d_f3, text='Hidden data is :')
            lab_2.config(font=('courier', 18))
            lab_2.grid(pady=10)
            text_area = Text(d_f3, width=50, height=10)
            text_area.insert(INSERT, hidden_data)
            text_area.configure(state='disabled')
            text_area.grid()
            back_button = Button(d_f3, text='Cancel',
                                 command=lambda: self.page_three(d_f3))
            back_button.config(font=('courier', 11))
            back_button.grid(pady=15)
            back_button.grid()
            show_info = Button(d_f3, text='More Info', command=self.info)
            show_info.config(font=('courier', 11))
            show_info.grid()
            d_f3.grid(row=1)
            d_f2.destroy()

    def decode(self, image):
        data = ''
        imgdata = iter(image.getdata())

        while (True):
            pixels = [value for value in imgdata.__next__()[:3] +
                      imgdata.__next__()[:3] +
                      imgdata.__next__()[:3]]
            binstr = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binstr += '0'
                else:
                    binstr += '1'

            data += chr(int(binstr, 2))
            if pixels[-1] % 2 != 0:
                return data

    def frame_one_enoder(self, f):
        f.destroy()
        f2 = Frame(root)
        label_art = Label(f2, text='\'\(OO)/\'')
        label_art.config(font=('courier', 70))
        label_art.grid(row=1, pady=50)
        label_one = Label(
            f2, text='Select the Image \n you want to hide text :')
        label_one.config(font=('courier', 18))
        label_one.grid()

        btn_encode = Button(f2, text='Select',
                            command=lambda: self.frame_two_decoder(f2))
        btn_encode.config(font=('courier', 18))
        btn_encode.grid()
        btn_back = Button(f2, text='Cancel',
                          command=lambda: Stegno.home(self, f2))
        btn_back.config(font=('courier', 18))
        btn_back.grid(pady=15)
        btn_back.grid()
        f2.grid()

    def frame_two_decoder(self, f2):
        ep = Frame(root)
        image_file = tkinter.filedialog.askopenfilename(filetypes=(
            [('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'), ('All Files', '*.*')]))
        if not image_file:
            messagebox.showerror("Error", "Please select an image!!!")
        else:
            selected_image = Image.open(image_file)
            myimage = selected_image.resize((300, 200))
            img = ImageTk.PhotoImage(myimage)
            lab_3 = Label(ep, text='Selected Image')
            lab_3.config(font=('courier', 18))
            lab_3.grid()
            panel = Label(ep, image=img)
            panel.image = img
            self.output_image_size = os.stat(image_file)
            self.o_image_w, self.o_image_h = selected_image.size
            panel.grid()
            lab_2 = Label(ep, text='Enter the message')
            lab_2.config(font=('courier', 18))
            lab_2.grid(pady=15)
            text_area = Text(ep, width=50, height=10)
            text_area.grid()
            encode_button = Button(
                ep, text='Cancel', command=lambda: Stegno.home(self, ep))
            encode_button.config(font=('courier', 11))
            data = text_area.get("1.0", "end-1c")
            back_button = Button(ep, text='Encode', command=lambda: [
                                 self.enc_fun(text_area, selected_image), Stegno.home(self, ep)])
            back_button.config(font=('courier', 11))
            back_button.grid(pady=15)
            encode_button.grid()
            ep.grid(row=1)
            f2.destroy()

    def info(self):
        try:
            str = 'original image:-\nsize of original image:{}mb\nwidth: {}\nheight: {}\n\n' \
                  'decoded image:-\nsize of decoded image: {}mb\nwidth: {}' \
                '\nheight: {}'.format(self.output_image_size.st_size/1000000,
                                      self.o_image_w, self.o_image_h,
                                      self.d_image_size/1000000,
                                      self.d_image_w, self.d_image_h)
            messagebox.showinfo('info', str)
        except:
            messagebox.showinfo('Info', 'Unable to get the information')

    def genData(self, data):
        newd = []

        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd

    def modify_pixel(self, pix, data):
        datalist = self.genData(data)
        lendata = len(datalist)
        image_data = iter(pix)
        for i in range(lendata):
            pix = [value for value in image_data.__next__()[:3] +
                   image_data.__next__()[:3] +
                   image_data.__next__()[:3]]
            for j in range(0, 8):
                if (datalist[i][j] == '0') and (pix[j] % 2 != 0):

                    if (pix[j] % 2 != 0):
                        pix[j] -= 1

                elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1
            # The eigth pixel of every set tells determines whether to read further or not
            # 0 means keep reading; 1 means the
            # message is over.
            if (i == lendata - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]

    def encode_enc(self, newimg, data):
        w = newimg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modify_pixel(newimg.getdata(), data):

            # Putting modified pixels in the new image
            newimg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    def enc_fun(self, text_area, selected_image):
        data = text_area.get("1.0", "end-1c")
        if (len(data) == 0):
            messagebox.showinfo(
                "Alert", "Please enter the text in the TextBox")
        else:
            newimg = selected_image.copy()
            # self.encode_enc(newimg, encryption.encryption(data))
            self.encode_enc(newimg, data)
            my_file = BytesIO()
            temp = os.path.splitext(
                os.path.basename(selected_image.filename))[0]
            newimg.save(tkinter.filedialog.asksaveasfilename(
                initialfile=temp, filetypes=([('png', '*.png')]), defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w, self.d_image_h = newimg.size
            messagebox.showinfo(
                "Success", "Encoding Successful\n File is saved as Image_with_hiddentext.png in the same directory")

    def page_three(self, frame):
        frame.destroy()
        self.main(root)


root = Tk()

st = Stegno()
st.main(root)

root.mainloop()
