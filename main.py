import time
import pickle

notebookList = []
t = 0

try:
	opFile = open("notebook.dat", "rb")
	t = 1

except Exception:
	opFile = open("notebook.dat", "wb")
	print("No default notebook was found, created one.")

if (t == 1):
	justread = pickle.load(opFile)
	notebookList.append(justread)

while True:

	print("(1) Read the notebook\n(2) Add note\n(3) Edit a note\n(4) Delete a note\n(5) Save and quit\n")

	selec = int(input("Please select one: "))
	if selec == 1:
		for i in notebookList:
			print(i)
	elif selec == 2:
		newNote = str(input("Write a new note: "))
		nowTime = str(time.strftime("%X %x"))
		result = newNote + ":::" + nowTime
		notebookList.append(str(result))
	elif selec == 3:
		print("The list has",len(notebookList) ,"notes.")
		chanItem = int(input("Which of them will be changed?: "))
		chanNote = notebookList[chanItem]
		notebookList.pop(chanItem)
		print(chanNote)
		newwNote = str(input("Give the new note: "))
		nowTime = str(time.strftime("%X %x"))
		newwNote = newwNote + ":::" + nowTime
		notebookList.insert(chanItem, str(newwNote))
	elif selec == 4:
		print("The list has", len(notebookList), "notes.")
		delItem = int(input("Which of them will be deleted?: "))
		dellItem = notebookList[delItem-1]
		notebookList.pop(delItem-1)
		print("Deleted note", dellItem)
	elif selec == 5:
		opFile = open("notebook.dat", "ab")
		pickle.dump(notebookList, opFile)
		opFile.close()
		print("Notebook shutting down, thank you.")
		break


#opFile = open("notebook.dat", "rb")
#justread = pickle.load(opFile)
#print(justread)
#opFile.close()