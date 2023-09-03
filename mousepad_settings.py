from tendo import singleton
from os import environ
from tkinter import *
import customtkinter as ctk
import importlib
from PIL import Image
from functools import partial
from win10toast_click import ToastNotifier
import constants
from constants import *
from mapping import *
from controller import retrieve_controllers

environ["PBR_VERSION"] = "4.0.2"

mousepad = singleton.SingleInstance()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class MappingManagementFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.controller_frame = ctk.CTkFrame(
            self, fg_color=self.cget("fg_color"))
        self.controller_frame.grid(row=1, column=1, padx=5, pady=2)
        self.controller_img = ctk.CTkImage(
            dark_image=Image.open("controller.png"), size=(568, 665))
        self.central_img = ctk.CTkLabel(
            self.controller_frame, image=self.controller_img, text="")
        self.central_img.pack(side=TOP, expand=YES)

        self.left_frame = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        self.left_frame.grid(row=1, column=0, padx=5, pady=2)

        self.right_frame = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        self.right_frame.grid(row=1, column=2, padx=5, pady=2)

        self.top_frame = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        self.top_frame.grid(row=0, column=1, padx=5, pady=2)
        self.menu_label = ctk.CTkLabel(self.top_frame, text="Menu")
        self.menu_label.grid(row=0, column=0, padx=5, pady=5)
        self.menu_dropdown = ctk.CTkOptionMenu(self.top_frame, values=list(
            COMMAND_DICT.keys()), variable=ctk.StringVar(value=BUTTON_DICT['Menu']))
        self.menu_dropdown.grid(row=1, column=0, padx=5, pady=5)

        self.save_frame = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        self.save_frame.grid(row=2, column=1, padx=5, pady=2)
        self.save_button = ctk.CTkButton(
            self.save_frame, text="Save", command=self.save_cmd, font=("Helvetica", 14, "bold"))
        self.save_button.pack(side=TOP, expand=YES)

        self.left_stick_label = ctk.CTkLabel(
            self.left_frame, text="Left Stick")
        self.left_stick_label.grid(row=0, column=0, padx=5, pady=5)
        self.left_stick_dropdown = ctk.CTkOptionMenu(self.left_frame, values=list(
            MOVEMENT_DICT.keys()), variable=ctk.StringVar(value=STICK_DICT['Left Stick']))
        self.left_stick_dropdown.grid(row=1, column=0, padx=5, pady=5)

        self.l3_label = ctk.CTkLabel(self.left_frame, text="L3")
        self.l3_label.grid(row=2, column=0, padx=5, pady=5)
        self.l3_dropdown = ctk.CTkOptionMenu(self.left_frame, values=list(
            COMMAND_DICT.keys()), variable=ctk.StringVar(value=BUTTON_DICT['L3']))
        self.l3_dropdown.grid(row=3, column=0, padx=5, pady=5)

        self.up_label = ctk.CTkLabel(self.left_frame, text="Up")
        self.up_label.grid(row=4, column=0, padx=5, pady=5)
        self.up_dropdown = ctk.CTkOptionMenu(self.left_frame, values=list(
            COMMAND_DICT.keys()), variable=ctk.StringVar(value=BUTTON_DICT['Up']))
        self.up_dropdown.grid(row=5, column=0, padx=5, pady=5)

        self.left_label = ctk.CTkLabel(self.left_frame, text="Left")
        self.left_label.grid(row=6, column=0, padx=5, pady=5)
        self.left_dropdown = ctk.CTkOptionMenu(self.left_frame, values=list(
            COMMAND_DICT.keys()), variable=ctk.StringVar(value=BUTTON_DICT['Left']))
        self.left_dropdown.grid(row=7, column=0, padx=5, pady=5)

        self.right_label = ctk.CTkLabel(self.left_frame, text="Right")
        self.right_label.grid(row=8, column=0, padx=5, pady=5)
        self.right_dropdown = ctk.CTkOptionMenu(self.left_frame, values=list(
            COMMAND_DICT.keys()), variable=ctk.StringVar(value=BUTTON_DICT['Right']))
        self.right_dropdown.grid(row=9, column=0, padx=5, pady=5)

        self.down_label = ctk.CTkLabel(self.left_frame, text="Down")
        self.down_label.grid(row=10, column=0, padx=5, pady=5)
        self.down_dropdown = ctk.CTkOptionMenu(self.left_frame, values=list(
            COMMAND_DICT.keys()), variable=ctk.StringVar(value=BUTTON_DICT['Down']))
        self.down_dropdown.grid(row=11, column=0, padx=5, pady=5)

        self.l1_label = ctk.CTkLabel(self.left_frame, text="L1")
        self.l1_label.grid(row=12, column=0, padx=5, pady=5)
        self.l1_dropdown = ctk.CTkOptionMenu(self.left_frame, values=list(
            COMMAND_DICT.keys()), variable=ctk.StringVar(value=BUTTON_DICT['L1']))
        self.l1_dropdown.grid(row=13, column=0, padx=5, pady=5)

        self.l2_label = ctk.CTkLabel(self.left_frame, text="L2")
        self.l2_label.grid(row=14, column=0, padx=5, pady=5)
        self.l2_dropdown = ctk.CTkOptionMenu(self.left_frame, values=list(
            COMMAND_DICT.keys()), variable=ctk.StringVar(value=BUTTON_DICT['L2']))
        self.l2_dropdown.grid(row=15, column=0, padx=5, pady=5)

        self.y_label = ctk.CTkLabel(self.right_frame, text="Y")
        self.y_label.grid(row=0, column=0, padx=5, pady=5)
        self.y_dropdown = ctk.CTkOptionMenu(self.right_frame, values=list(
            COMMAND_DICT.keys()), variable=ctk.StringVar(value=BUTTON_DICT['Y']))
        self.y_dropdown.grid(row=1, column=0, padx=5, pady=5)

        self.x_label = ctk.CTkLabel(self.right_frame, text="X")
        self.x_label.grid(row=2, column=0, padx=5, pady=5)
        self.x_dropdown = ctk.CTkOptionMenu(self.right_frame, values=list(
            COMMAND_DICT.keys()), variable=ctk.StringVar(value=BUTTON_DICT['X']))
        self.x_dropdown.grid(row=3, column=0, padx=5, pady=5)

        self.b_label = ctk.CTkLabel(self.right_frame, text="B")
        self.b_label.grid(row=4, column=0, padx=5, pady=5)
        self.b_dropdown = ctk.CTkOptionMenu(self.right_frame, values=list(
            COMMAND_DICT.keys()), variable=ctk.StringVar(value=BUTTON_DICT['B']))
        self.b_dropdown.grid(row=5, column=0, padx=5, pady=5)

        self.a_label = ctk.CTkLabel(self.right_frame, text="A")
        self.a_label.grid(row=6, column=0, padx=5, pady=5)
        self.a_dropdown = ctk.CTkOptionMenu(self.right_frame, values=list(
            COMMAND_DICT.keys()), variable=ctk.StringVar(value=BUTTON_DICT['A']))
        self.a_dropdown.grid(row=7, column=0, padx=5, pady=5)

        self.right_stick_label = ctk.CTkLabel(
            self.right_frame, text="Right Stick")
        self.right_stick_label.grid(row=8, column=0, padx=5, pady=5)
        self.right_stick_dropdown = ctk.CTkOptionMenu(self.right_frame, values=list(
            MOVEMENT_DICT.keys()), variable=ctk.StringVar(value=STICK_DICT['Right Stick']))
        self.right_stick_dropdown.grid(row=9, column=0, padx=5, pady=5)

        self.r3_label = ctk.CTkLabel(self.right_frame, text="R3")
        self.r3_label.grid(row=10, column=0, padx=5, pady=5)
        self.r3_dropdown = ctk.CTkOptionMenu(self.right_frame, values=list(
            COMMAND_DICT.keys()), variable=ctk.StringVar(value=BUTTON_DICT['R3']))
        self.r3_dropdown.grid(row=11, column=0, padx=5, pady=5)

        self.r1_label = ctk.CTkLabel(self.right_frame, text="R1")
        self.r1_label.grid(row=12, column=0, padx=5, pady=5)
        self.r1_dropdown = ctk.CTkOptionMenu(self.right_frame, values=list(
            COMMAND_DICT.keys()), variable=ctk.StringVar(value=BUTTON_DICT['R1']))
        self.r1_dropdown.grid(row=13, column=0, padx=5, pady=5)

        self.r2_label = ctk.CTkLabel(self.right_frame, text="R2")
        self.r2_label.grid(row=14, column=0, padx=5, pady=5)
        self.r2_dropdown = ctk.CTkOptionMenu(self.right_frame, values=list(
            COMMAND_DICT.keys()), variable=ctk.StringVar(value=BUTTON_DICT['R2']))
        self.r2_dropdown.grid(row=15, column=0, padx=5, pady=5)

    def save_cmd(self):
        new_button_dict = {
            'L1': self.l1_dropdown._current_value,
            'L2': self.l2_dropdown._current_value,
            'L3': self.l3_dropdown._current_value,
            'R1': self.r1_dropdown._current_value,
            'R2': self.r2_dropdown._current_value,
            'R3': self.r3_dropdown._current_value,
            'Menu': self.menu_dropdown._current_value,
            'Left': self.left_dropdown._current_value,
            'Right': self.right_dropdown._current_value,
            'Up': self.up_dropdown._current_value,
            'Down': self.down_dropdown._current_value,
            'A': self.a_dropdown._current_value,
            'B': self.b_dropdown._current_value,
            'Y': self.y_dropdown._current_value,
            'X': self.x_dropdown._current_value
        }

        new_stick_dict = {
            'Left Stick': self.left_stick_dropdown._current_value,
            'Right Stick': self.right_stick_dropdown._current_value
        }

        save_settings(CONTROLLER_ID, LEFT_SPEED, RIGHT_SPEED, VIBRATE_BUTTON_TIME,
                      VIBRATE_TRIGGER_TIME, MOVE_SPEED, SCROLL_SPEED, new_button_dict, new_stick_dict)
        importlib.reload(constants)

        notify.show_toast("Settings Saved", "Your changes to the button mapping have been saved.",
                          icon_path="mouse_pad.ico", duration=5, threaded=True)


class SettingsManagementFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        id_ls = [str(i) for i in retrieve_controllers()]

        self.left_frame = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        self.left_frame.grid(row=1, column=0, padx=5, pady=2)

        self.right_frame = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        self.right_frame.grid(row=1, column=2, padx=5, pady=2)

        self.top_frame = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        self.top_frame.grid(row=0, column=1, padx=5, pady=2)
        self.id_label = ctk.CTkLabel(self.top_frame, text="Controller ID")
        self.id_label.grid(row=0, column=0, padx=5, pady=5)
        self.id_dropdown = ctk.CTkOptionMenu(
            self.top_frame, values=id_ls, variable=ctk.StringVar(value=str(CONTROLLER_ID)))
        self.id_dropdown.grid(row=1, column=0, padx=5, pady=5)

        self.save_frame = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        self.save_frame.grid(row=2, column=1, padx=5, pady=2)
        self.save_button = ctk.CTkButton(
            self.save_frame, text="Save", command=self.save_cmd, font=("Helvetica", 14, "bold"))
        self.save_button.pack(side=TOP, expand=YES)

        self.left_vibration_label = ctk.CTkLabel(
            self.left_frame, text="Left Vibration Sensitivity")
        self.left_vibration_label.grid(row=0, column=0, padx=5, pady=5)
        self.left_vibration_slider = ctk.CTkSlider(
            self.left_frame, from_=0, to=1, number_of_steps=20, variable=ctk.DoubleVar(value=LEFT_SPEED))
        self.left_vibration_slider.grid(row=1, column=0, padx=5, pady=5)

        self.cursor_label = ctk.CTkLabel(
            self.left_frame, text="Cursor Sensitivity")
        self.cursor_label.grid(row=2, column=0, padx=5, pady=5)
        self.cursor_slider = ctk.CTkSlider(
            self.left_frame, from_=0, to=50, number_of_steps=50, variable=ctk.DoubleVar(value=MOVE_SPEED))
        self.cursor_slider.grid(row=3, column=0, padx=5, pady=5)

        self.button_vibrate_label = ctk.CTkLabel(
            self.left_frame, text="Button Vibration Time")
        self.button_vibrate_label.grid(row=4, column=0, padx=5, pady=5)
        self.button_vibrate_slider = ctk.CTkSlider(
            self.left_frame, from_=0, to=1, number_of_steps=20, variable=ctk.DoubleVar(value=VIBRATE_BUTTON_TIME))
        self.button_vibrate_slider.grid(row=5, column=0, padx=5, pady=5)

        self.right_vibration_label = ctk.CTkLabel(
            self.right_frame, text="Right Vibration Sensitivity")
        self.right_vibration_label.grid(row=0, column=0, padx=5, pady=5)
        self.right_vibration_slider = ctk.CTkSlider(
            self.right_frame, from_=0, to=1, number_of_steps=20, variable=ctk.DoubleVar(value=RIGHT_SPEED))
        self.right_vibration_slider.grid(row=1, column=0, padx=5, pady=5)

        self.scroll_label = ctk.CTkLabel(
            self.right_frame, text="Scroll Sensitivity")
        self.scroll_label.grid(row=2, column=0, padx=5, pady=5)
        self.scroll_slider = ctk.CTkSlider(
            self.right_frame, from_=0, to=1, number_of_steps=20, variable=ctk.DoubleVar(value=SCROLL_SPEED))
        self.scroll_slider.grid(row=3, column=0, padx=5, pady=5)

        self.trigger_vibrate_label = ctk.CTkLabel(
            self.right_frame, text="Trigger Vibration Time")
        self.trigger_vibrate_label.grid(row=4, column=0, padx=5, pady=5)
        self.trigger_vibrate_slider = ctk.CTkSlider(
            self.right_frame, from_=0, to=1, number_of_steps=20, variable=ctk.DoubleVar(value=VIBRATE_TRIGGER_TIME))
        self.trigger_vibrate_slider.grid(row=5, column=0, padx=5, pady=5)

    def save_cmd(self):
        save_settings(int(self.id_dropdown._current_value), round(self.left_vibration_slider._value, 2), round(self.right_vibration_slider._value, 2), round(
            self.button_vibrate_slider._value, 2), round(self.trigger_vibrate_slider._value, 2), round(self.cursor_slider._value, 2), round(self.scroll_slider._value, 2), BUTTON_DICT, STICK_DICT)
        importlib.reload(constants)

        notify.show_toast("Settings Saved", "Your changes to the button mapping have been saved.",
                          icon_path="mouse_pad.ico", duration=5, threaded=True)


class RestoreSettingsFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.text_frame = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        self.text_frame.grid(row=0, column=0, padx=5, pady=150)
        self.text_label = ctk.CTkLabel(self.text_frame, text="Clicking the button below will restore all settings to the defaults. Are you sure you want to reset all settings?", font=(
            "Helvetica", 24, "bold"), wraplength=900)
        self.text_label.pack(side=TOP, expand=YES)

        self.restore_frame = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        self.restore_frame.grid(row=1, column=0, padx=5, pady=30)
        self.restore_button = ctk.CTkButton(
            self.restore_frame, text="Restore Settings", height=40, command=self.restore_cmd, font=("Helvetica", 16, "bold"))
        self.restore_button.pack(side=TOP, expand=YES)

    def restore_cmd(self):
        save_settings(DEFAULT_CONTROLLER_ID, DEFAULT_LEFT_SPEED, DEFAULT_RIGHT_SPEED, DEFAULT_VIBRATE_BUTTON_TIME,
                      DEFAULT_VIBRATE_TRIGGER_TIME, DEFAULT_MOVE_SPEED, DEFAULT_SCROLL_SPEED, DEFAULT_BUTTON_DICT, DEFAULT_STICK_DICT)
        importlib.reload(constants)

        notify.show_toast("All Settings Restored", "All settings have now been restored to the defaults.",
                          icon_path="mouse_pad.ico", duration=5, threaded=True)


class AboutFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.text_frame = ctk.CTkFrame(self, fg_color=self.cget("fg_color"))
        self.text_frame.grid(row=0, column=0, padx=5, pady=150)
        self.text_label = ctk.CTkLabel(self.text_frame, text="MousePad v1.0, Fireball Innovations\n\n\nThis software is meant as a supplement to make using the computer with a controller easier, but in some instances you will still need your keyboard such as when using task manager or the Ctrl+Alt+Del Menu.\n\nThe software is intended to help those with limited mobility use a computer, but it would also work for those playing games with a controller who also want to control their PC in a similar fashion.\n\nIntended for use with the Fireball Innovations Phoenix Controller System.\n\n\nThe Team:\nFrank, Ibrahim, Shyavan, & Soham\n\n\nCopyright 2022.", font=("Helvetica", 18, "bold"), wraplength=900)
        self.text_label.pack(side=TOP, expand=YES)


class App(ctk.CTk):
    frames = {}
    current = None
    bg = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bg = self.cget("fg_color")
        self.num_of_frames = 0
        self.geometry("920x820")
        self.minsize(920, 820)
        self.maxsize(920, 820)
        self.iconbitmap("mouse_pad.ico")
        self.title("MousePad Settings")

        main_frame = ctk.CTkFrame(self, fg_color=self.bg)
        main_frame.pack(side=TOP, fill=Y, expand=YES, padx=2, pady=5)

        self.selector_frame = ctk.CTkFrame(main_frame, fg_color=self.bg)
        self.selector_frame.grid(row=0, column=1, padx=5, pady=2)

        self.content_frame = ctk.CTkFrame(main_frame, fg_color=self.bg)
        self.content_frame.grid(row=1, column=1, padx=2, pady=2)

        self.create_nav(self.selector_frame, "Mappings")
        self.create_nav(self.selector_frame, "Settings")
        self.create_nav(self.selector_frame, "Reset")
        self.create_nav(self.selector_frame, "About")

        App.current = App.frames["Mappings"]
        App.current.pack(in_=self.content_frame, side=TOP,
                         fill=BOTH, expand=YES, padx=0, pady=0)

    def frame_selector_button(self, parent, frame_id):
        button_frame = ctk.CTkButton(parent)
        button_frame.configure(height=20)
        button_frame.configure(text=frame_id, font=("Helvetica", 14, "bold"))
        button_frame.configure(command=partial(
            self.toggle_frame_by_id, frame_id))
        button_frame.grid(padx=5, row=0, column=self.num_of_frames)
        self.num_of_frames = self.num_of_frames + 1

    def create_frame(self, frame_id):
        if frame_id == "Mappings":
            App.frames[frame_id] = MappingManagementFrame(
                master=self, fg_color=self.cget("fg_color"))
        elif frame_id == "Settings":
            App.frames[frame_id] = SettingsManagementFrame(
                master=self, fg_color=self.cget("fg_color"))
        elif frame_id == "Reset":
            App.frames[frame_id] = RestoreSettingsFrame(
                master=self, fg_color=self.cget("fg_color"))
        elif frame_id == "About":
            App.frames[frame_id] = AboutFrame(
                master=self, fg_color=self.cget("fg_color"))

        App.frames[frame_id].padx = 8

    def toggle_frame_by_id(self, frame_id):
        if App.frames[frame_id] is not None:
            if App.current is App.frames[frame_id]:
                App.current.pack_forget()
                App.current = App.frames[frame_id]
                App.current.pack(in_=self.content_frame, side=TOP,
                                 fill=BOTH, expand=YES, padx=0, pady=0)
            elif App.current is not None:
                App.current.pack_forget()
                App.current = App.frames[frame_id]
                App.current.pack(in_=self.content_frame, side=TOP,
                                 fill=BOTH, expand=YES, padx=0, pady=0)
            else:
                App.current = App.frames[frame_id]
                App.current.pack(in_=self.content_frame, side=TOP,
                                 fill=BOTH, expand=YES, padx=0, pady=0)

    def create_nav(self, parent, frame_id):
        self.frame_selector_button(parent, frame_id)
        self.create_frame(frame_id)


def main():
    root = App()
    root.mainloop()


if __name__ == "__main__":
    notify = ToastNotifier()
    main()
else:
    raise ImportError(
        "This is not meant to be imported as a module, it is the main program for MousePad Settings.")
