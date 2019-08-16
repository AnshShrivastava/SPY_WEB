import os


def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating Project ' + directory)
        os.makedirs(directory)



#create quere and crawled files
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name +'/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')



#Create a new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)
    #f.close()


#Add data onto an existing file
def append_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# Clean file
def clear_file(path):
    with open(path, 'w'):
        pass

# Read File and Convert into Set Items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

# Iterate through a set, each item will be new line in file
def set_to_file(links, file_name):
    with open(file_name, "w") as f:
        for l in sorted(links):
            f.write(l + "\n")


