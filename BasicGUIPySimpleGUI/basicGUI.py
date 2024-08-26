#Image Viewer

import PySimpleGUI as sg #sg is the alias for PySimpleGUI
import os.path #in python standard lib with functions to manipulate and interact with files and dir

file_list = [
	[
		sg.Text("Image Folder"),
		sg.In(size=(25,1), enable_events=True, key="-FOLDER-"), #sg.In is the input with id of FOlDER
		sg.FolderBrowse(),
	],
	[
		sg.Listbox(
			values=[], enable_events=True, size=(40,20),key="-FILE LIST-"
		)
	], #trailing comma not necessary but some say its a standard of how to write lists and tuples
	]

image_viewer = [
	[sg.Text("Choose an image from list on left:")],
	[sg.Text(size=(40,1), key="-TOUT-")],
	[sg.Image(key="-IMAGE-")],
	]

#full layout
layout = [
	[
		sg.Column(file_list),
		sg.VSeparator(),
		sg.Column(image_viewer),
	]
	]

# Create the window
window = sg.Window("Image Viewer", layout, resizable=True)

# Create an event loop to properly kill the window when certain conditions are met
while True:
	event, values = window.read()
	# End program if user closes window or
	# presses the OK button
	if event == "Exit" or event == sg.WIN_CLOSED:
		break
	if event == "-FOLDER-":
		folder = values["-FOLDER-"]
		try:
			file_list = os.listdir(folder) #use os.listdir() to get file listing
		except:
			file_list = []
		# filter file listing to just .png and .gif
		fnames = [
			f
			for f in file_list
			if os.path.isfile(os.path.join(folder,f))
			and f.lower().endswith((".png", ".gif"))
		]
		window["-FILE LIST-"].update(fnames)
	elif event == "-FILE LIST-": #you choose a file
		try:
			filename = os.path.join(
				values["-FOLDER-"], values["-FILE LIST-"][0]
			)
			window["-TOUT-"].update(filename) #update the text element to show the filename
			window["-IMAGE-"].update(filename=filename) #update img ele to show image
		except:
			pass

window.close()
