#####
# for the quillnote / quillpad android app
# iterate a backup file
# create files for each note relative to its notebook
#####

import json
import os

# create a directory if it doesnt already exist
def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

# create a file for a note under its notebook dir
def create_note(work_dir, notebooks_by_id, note):
    # if the note doesnt have a notebook put it in generic dir
    if "notebookId" in note:
        path = f'{work_dir}/{notebooks_by_id[note["notebookId"]]}'
    else:
        path = f'{work_dir}/other'

    # make sure have a file name
    if "title" in note:
        # make sure no illegal chars in filename
        file_name = note["title"]
        if "/" in file_name:
            file_name = file_name.replace("/", "-")
        file_path = f'{path}/{file_name}.md'

        # write note content to its file if it doesnt exist already
        if not os.path.exists(file_path):
            #print(file_path)
            with open(file_path, 'w') as file:
                if "content" in note:
                    file.write(note["content"])
    else:
        print("no title")
        print(note)

# open backup and load it
f = open('quilnote_backup.json')
data = json.load(f)

# create dirs for each notebook
notebooks = data["notebooks"]

work_dir = "outputs"

# create workspace dir
create_dir(work_dir)

# create dir for notes with no notebook
create_dir(f'{work_dir}/other')

# create dir for each notebook
for nb in notebooks:
    #print(nb)
    #print(f'{work_dir}{nb["name"]}')
    create_dir(f'{work_dir}/{nb["name"]}')

# order notebooks by id for later access
notebooks_by_id = {}
for nb in notebooks:
    notebooks_by_id[nb["id"]] = nb["name"]
print(notebooks_by_id)

# create files for notes
notes = data["notes"]
for note in notes:
    create_note(work_dir, notebooks_by_id, note)

# closing file
f.close()
