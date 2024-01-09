
import customtkinter
import tkinter

class MyCheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.values = values
        self.checkboxes = []

        self.title_label = customtkinter.CTkLabel(self, text=self.title, fg_color="gray50", corner_radius=6)
        self.title_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")


        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)
        
    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            checked_checkboxes.append(checkbox.get())
        return checked_checkboxes

class MyRadiobuttonFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = customtkinter.StringVar(value="")

        self.title_label = customtkinter.CTkLabel(self, text=self.title, fg_color="gray50", corner_radius=6)
        self.title_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            radiobutton = customtkinter.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)


class MyScrollableCheckboxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.values = values
        self.checkboxes = []

        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            checked_checkboxes.append(checkbox.get())
        return checked_checkboxes


class ReportPackageFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, number_of_columns, report_frames):
        super().__init__(master, label_text=title)
        self.title = title
        self.report_frames = report_frames

        for i in range(10):
            new_frame = customtkinter.CTkFrame(self, border_width=1)
            new_frame.grid(row=i, column=0, padx=(0, 20), pady=10, sticky="nsew", columnspan=number_of_columns)

            label1 = customtkinter.CTkLabel(new_frame, text=i, fg_color="grey50")
            label1.grid(row=0, column=0, padx=20, pady=0, sticky="nwes", columnspan=number_of_columns)

            label2 = customtkinter.CTkLabel(new_frame, text=i, fg_color="grey50")
            label2.grid(row=1, column=0, padx=20, pady=0, sticky="nw")

            label3 = customtkinter.CTkLabel(new_frame, text=i, fg_color="grey50")
            label3.grid(row=1, column=1, padx=20, pady=0, sticky="nw")






class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Report Package Creator")
        self.geometry("800x500")
        customtkinter.set_appearance_mode("dark")

        #Only Works for Even Numbers
        self.number_of_columns = 8
        self.columns = [int(x) for x in range(self.number_of_columns)]
        self.middle = int(round(self.number_of_columns/2))

        self.grid_columnconfigure(self.columns, weight=1)

        self.grid_rowconfigure((0), weight=5)
        self.grid_rowconfigure((1, 2, 3, 4), weight=1)


        self.write_row = 0

        #Row 0
        self.prelim_reporting_button = customtkinter.CTkButton(self, text="Prelim Reporting", command=self.Prelim_Reporting)
        self.prelim_reporting_button.grid(row=self.write_row, column=0, padx=(20, 10), sticky="ew", columnspan=self.middle)

        self.final_reporting_button = customtkinter.CTkButton(self, text="Final Reporting", command=self.Final_Reporting)
        self.final_reporting_button.grid(row=self.write_row, column=self.middle, padx=(10, 20), sticky="ew", columnspan=self.middle)

        #Row 1
        self.write_row += 1
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Save Location")
        self.entry.grid(row=self.write_row, column=0, padx=20, pady=0, sticky="new", columnspan=self.number_of_columns)

        #Row 2
        self.write_row += 1
        self.browse_button = customtkinter.CTkButton(self, text="Browse", command=self.Browse)
        self.browse_button.grid(row=self.write_row, column=0, padx=(20, 0), pady=0, sticky="nw", columnspan=self.number_of_columns)

        #Row 3
        self.write_row += 1
        self.report_package_frame = ReportPackageFrame(self, "Reports", self.number_of_columns, [])
        self.report_package_frame.grid(row=self.write_row, column=0, padx=20, pady=0, sticky="new", columnspan=self.number_of_columns)
        
        #Row 4
        self.write_row += 1
        self.finalize_reports = customtkinter.CTkButton(self, text="Finalize Repots", command=self.Finalize_Reports)
        self.finalize_reports.grid(row=self.write_row, column=0, padx=20, pady=0, sticky="new", columnspan=self.number_of_columns)

    def Prelim_Reporting(self):
        pass

    def Final_Reporting(self):
        pass

    def Browse(self):
        pass
    
    def Finalize_Reports(self):
        pass
        

app = App()
app.mainloop()