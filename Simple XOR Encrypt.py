#!/usr/bin/env python3
""" encrypt-string.py - Encode string by XOR """
# Copyright (c) 2016-2018 ArdeshirV@protonmail.com, Licensed under GPLv3+
import sys
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog


def main(args):
    err_code = 0
    try:
        default_code = 82
        if len(args) >= 2:
            default_code = args[1]
        if len(args) <= 2:
            print_title()
            encode_string(default_code)
        else:
            for s in args[2:]:
                print(Encode(default_code, s))
    except Exception as exp:
        print('\033[0;31m{0}\033[0m'.format(exp), file=sys.stderr)
        raise exp  # err_code = -1
    return err_code


rol = lambda val, r_bits, max_bits: \
        (val << r_bits%max_bits) & (2**max_bits-1) | \
        ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))


ror = lambda val, r_bits, max_bits: \
        ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
        (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))


def Encode(strPassword, stringInput, key_bits=8):
    encoded = ''
    password = abs(int(strPassword))
    max_val = 2**key_bits - 1
    code = password if password <= max_val else password % max_val
    num_bytes = key_bits // 8
    key_bytes = [(code >> (8 * (num_bytes - 1 - i))) & 0xFF for i in range(num_bytes)]
    for i, c in enumerate(stringInput):
        # m = ord(c)
        # n = ror(m, 4, 8)
        # print('{}-{}'.format(bin(m), bin(n)))
        encoded += chr(ord(c) ^ key_bytes[i % num_bytes])
    return encoded


class encode_string(object):
    def __init__(self, default_code, default_key_bits=8):
        self.default_code = default_code
        self.default_key_bits = default_key_bits
        self.root = tk.Tk()
        #self.root.withdraw()
        #self.root.eval('tk::PlaceWindow %s center' %
        #               self.root.winfo_pathname(self.root.winfo_id()))
        self.root.title('Encrypt String')
        self.frame = tk.Frame(self.root)
        self.frame2 = tk.Frame(self.root, padx=10, pady=10)
        self.frame.pack()
        self.frame2.pack()
        self.initialization()
        self.root.mainloop()

    def initialization(self):
        r = self.frame
        self.Code = tk.StringVar()
        k_a = tk.Label(r, text='Password: ')
        k_a.grid(row=0, column=0, sticky=tk.E)
        self.txtCode = tk.Entry(r,  text=self.Code)
        self.txtCode.grid(row=0, column=1, sticky=tk.W)
        self.txtCode.focus_set()
        self.Code.set(self.default_code)
        self.KeyBits = tk.StringVar()
        k_kb = tk.Label(r, text='Key Bits: ')
        k_kb.grid(row=1, column=0, sticky=tk.E)
        self.cmbKeyBits = ttk.Combobox(r, textvariable=self.KeyBits,
                                       values=['8', '16', '32', '64', '128', '256'],
                                       state='readonly', width=17)
        self.cmbKeyBits.grid(row=1, column=1, sticky=tk.W)
        self.KeyBits.set(str(self.default_key_bits))
        self.String = tk.StringVar()
        k_b = tk.Label(r, text='String: ')
        k_b.grid(row=2, column=0, sticky=tk.E)
        self.txtString = tk.Entry(r, text=self.String)
        self.txtString.grid(row=2, column=1)
        self.txtString.focus_set()
        b = tk.Button(r, text='Load ...', command=self.Load)
        b.grid(row=2, column=2)
        self.Encrypted = tk.StringVar()
        k_b = tk.Label(r, text='Encrypted: ')
        k_b.grid(row=3, column=0, sticky=tk.E)
        self.txtOutput = tk.Entry(r, text=self.Encrypted, state="readonly")
        self.txtOutput.grid(row=3, column=1)
        # self.txtOutput.focus_set()
        b = tk.Button(r, text='Save ...', command=self.SaveAs)
        b.grid(row=3, column=2)
        r2 = self.frame2
        b = tk.Button(r2, text='Paste String', command=self.PasteFromClipboard)
        b.pack(side='left')
        b = tk.Button(r2, text='Encode', command=self.Encrypt)
        b.pack(side='left')
        b = tk.Button(r2, text='Copy Encoded', command=self.Copy2Clipboard)
        b.pack(side='left')
        b = tk.Button(r2, text='Exit', command=self.close)
        b.pack(side='left')

    def Load(self):
        input_file_name = tkinter.filedialog.askopenfilename(
            defaultextension=".code", filetypes=[("All Files", "*.*")])
        if input_file_name:
            self.String.set(open(input_file_name, 'r').read())

    def SaveAs(self):
        input_file_name = tkinter.filedialog.asksaveasfilename(
            defaultextension=".code", filetypes=[("All Files", "*.*")])
        if input_file_name:
            open(input_file_name, 'w').write(self.txtOutput.get())

    def PasteFromClipboard(self):
        try:
            self.String.set(self.root.clipboard_get())
        except Exception as exp:
            print('\033[0;31m{0}\033[0m'.format(exp), file=sys.stderr)

    def Copy2Clipboard(self):
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.txtOutput.get())
        except Exception as exp:
            print('\033[0;31m{0}\033[0m'.format(exp), file=sys.stderr)

    def Encrypt(self):
        code = self.txtCode.get()
        data = self.txtString.get()
        key_bits = int(self.KeyBits.get())
        possible_keys = 2 ** key_bits
        brute_force_time = possible_keys / (10**9)
        print('키 길이: {}비트'.format(key_bits))
        print('가능한 키 개수: {:,}'.format(possible_keys))
        print('무차별 대입 복호화 시간: {}초 (10^9 시도/초 기준)'.format(brute_force_time))
        self.Encrypted.set(Encode(code, data, key_bits))

    def close(self):
        quit()


def print_title():
    strAppName = "encrypt-string"
    strAppYear = "2016-2018"
    strAppDescription = "Encode string by XOR"
    strVersion = "1.0"
    strLicense = "GPLv3+"
    strCopyright = "ArdeshirV@protonmail.com"
    from platform import system
    if system() == 'Windows':
        from colorama import init
        init()
    blnColor = True  # False if (system() == 'Windows') else True
    print(FormatTitle(strAppName, strAppDescription, strVersion, blnColor))
    print(FormatCopyright(strAppYear, strCopyright, strLicense, blnColor))


def FormatTitle(strAppName, strAppDescription, strVersion, blnColor):
    NoneColored = "{} - {}, Version {}\n"
    Colored = "\033[1;33m{}\033[0;33m - {}, \033[1;33mVersion {}\033[0m"
    strFormat = Colored if blnColor else NoneColored
    return strFormat.format(strAppName, strAppDescription, strVersion)


def FormatCopyright(strAppYear, strCopyright, strLicense, blnColor):
    NoneColored = "Copyright (c) {} {}, Licensed under {}\n\n"
    Colored = ("\033[0;33mCopyright (c) \033[1;33m{} \033[1;34m{}" +
               "\033[0;33m, Licensed under \033[1;33m{}\033[0m\n")
    strFormat = Colored if blnColor else NoneColored
    return strFormat.format(strAppYear, strCopyright, strLicense)


if __name__ == "__main__":
    exit(main(sys.argv))