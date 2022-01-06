"""
# line ve g_list'te herhangi bir sıkıntı yok aynı uyumlu

# Ana kaynak dosya all_gods.txt'den yazan millet ismine göre ayrılacak ve üç ayrı dosyaya gidecek

# g_list[1] Greek God ve Greek Goddess ise greek_gods.txt'e gidecek
# g_list[1] Egyptian God ve Egyptian Goddess ise egyptian_gods.txt'e gidecek
# g_list[1] Norse God ve Norse Goddess ise norse_gods.txt'e gidecek
"""

print("""********************************************************************************************
Subject: File Operations

Instruction: Free to choose any topic that is available to split into min. three groups.
# Create main source file and its elements needs to be randomly ordered.
# If you want to use mine you can find it in this repository:
https://github.com/acarismet/Python_Begginer_Projects_For_Exercise
# Elements of main source file will be split into three groups like Greek Gods and Goddesses,
Egyptian Gods and Goddesses, Norse Gods and Goddesses.
*************************************************************
What stages were accomplished? 
# Reading main source file
# Append and filtering all None elements under reading
# Creating/Writing three different files

But what was the problem and how I solved it?
# I couldn't figure out how I return the if else statement.
Solution: the list of line under the each def function 

# Başlık etmek istedim şu yöntemleri şöyle çözdüm 
*************************************************************
********************************************************************************************
""")



def greek(line):

    line = line[:-1]
    g_list = line.split(",")

    if (g_list[1] == "Greek God"):
        g_list[1] = "God"

    elif (g_list[1] == "Greek Goddess"):
        g_list[1] = "Goddess"
    else:
        return None

    return g_list[0] + "------>" + g_list[1] + "\n"


def egyptian(line):
    line = line[:-1]
    g_list = line.split(",")

    if (g_list[1] == "Egyptian God"):
        g_list[1] = "God"

    elif (g_list[1] == "Egyptian Goddess"):
        g_list[1] = "Goddess"
    else:
        return None

    return g_list[0] + "------>" + g_list[1] + "\n"


def norse(line):
    line = line[:-1]
    g_list = line.split(",")

    if (g_list[1] == "Norse God"):
        g_list[1] = "God"

    elif (g_list[1] == "Norse Goddess"):
        g_list[1] = "Goddess"
    else:
        return None

    return g_list[0] + "------>" + g_list[1] + "\n"


with open("all_gods.txt", "r")as file:

    greek_list = []
    for i in file:

        greek_list.append(greek(i))

    print("greek_list\n", greek_list)
    greek_list = filter(None, greek_list)
    print("new_greek_list:\n", greek_list)

    with open("greek_gods.txt", "w") as file2:

        for i in greek_list:
            file2.write(i)

    with open("greek_gods.txt","r+") as file5:
        g_title = file5.read()
        g_title = "All Greek Gods and Goddess\n" + g_title
        file5.seek(0)
        file5.write(g_title)

with open("all_gods.txt", "r")as file:

    egypt_list = []
    for i in file:

        egypt_list.append(egyptian(i))

    print("egypt_list\n", egypt_list)
    egypt_list = filter(None, egypt_list)
    print("new_egypt_list:\n", egypt_list)

    with open("egyptian_gods.txt", "w") as file3:

        for i in egypt_list:
            file3.write(i)

    with open("egyptian_gods.txt","r+") as file6:
        e_title = file6.read()
        e_title = "All Egyptian Gods and Goddess\n" + e_title
        file6.seek(0)
        file6.write(e_title)

with open("all_gods.txt", "r")as file:

    norse_list = []
    for i in file:

        norse_list.append(norse(i))

    print("norse_list\n", norse_list)
    norse_list = filter(None, norse_list)
    print("new_norse_list:\n", norse_list)

    with open("norse_gods.txt", "w") as file4:

        for i in norse_list:
            file4.write(i)

    with open("norse_gods.txt","r+") as file7:
        n_title = file7.read()
        n_title = "All Norse Gods and Goddess\n" + n_title
        file7.seek(0)
        file7.write(n_title)