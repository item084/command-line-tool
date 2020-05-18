"""Command Line Tool"""

import sys

################# colors #################
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
RED = '\033[1;31m'

RED_BG = '\033[1;77m\033[41m'

CLOSE_COLOR = '\033[m'
##########################################

print(f'''{GREEN}
     _______. _______ .______     ____    ____  _______ .______       __  
    /       ||   ____||   _  \    \   \  /   / |   ____||   _  \     |  | 
   |   (----`|  |__   |  |_)  |    \   \/   /  |  |__   |  |_)  |    |  | 
    \   \    |   __|  |      /      \      /   |   __|  |      /     |  | 
.----)   |   |  |____ |  |\  \----.  \    /    |  |____ |  |\  \----.|__| 
|_______/    |_______|| _| `._____|   \__/     |_______|| _| `._____|(__) 
                                                                     
 {RED_BG}      Server Command Line Tool  v1.0,  Author:  @item084  (GitHub)     {CLOSE_COLOR}\n
''')


def back_line(num=1):
    for _ in range(num):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[2K")


def cursor(mode):
    return input(
        '{} {} > {}'
        .format(YELLOW, mode, CLOSE_COLOR))


def cmd_view():
    mode = "VIEW"

    seen = 0
    total = 25
    print(
        '\n{} [#] There are {}{}{} records in the database:{}'
        .format(GREEN, BLUE, total, GREEN, CLOSE_COLOR))
    print("\n{} aaa bbb ccc ddd{}".format(BLUE, CLOSE_COLOR))
    
    mode = "VIEW {}{}/{}{}".format(BLUE, seen, total, YELLOW)
    print(
        "\n{} Press <{}ENTER{}> to see next {}10{} items, <{}q{}> to quit{}"
        .format(GREEN, CLOSE_COLOR, GREEN, BLUE, GREEN, CLOSE_COLOR, GREEN, CLOSE_COLOR))
    opt = cursor(mode)

    while seen < total:
        if opt == 'q':
            break
        back_line(3)
        print(' fake fake fake fake\033[K'.format())
        print(' fake fake fake fake\033[K'.format())
        print(' fake fake fake fake\033[K'.format())
        print(' fake fake fake fake\033[K'.format())
        print(' fake fake fake fake\033[K'.format())
        seen = total if total < seen + 10 else seen + 10
        mode = "VIEW {}{}/{}{}".format(BLUE, seen, total, YELLOW)
        print(
            "\n{} Press <{}ENTER{}> to see next {}10{} items, <{}q{}> to quit{}"
            .format(GREEN, CLOSE_COLOR, GREEN, BLUE, GREEN, CLOSE_COLOR, GREEN, CLOSE_COLOR))
        opt = cursor(mode)
    back_line(3)
    print('{} - END -{}'.format(BLUE, CLOSE_COLOR))
    
    pass


def cmd_add():
    mode = "ADD"
    pass


def cmd_edit():
    mode = "EDIT"
    pass


def cmd_delete():
    mode = "DEL"
    pass

        
def continue_statement():
    statement = input(
        '\n{} [*] Have you any other requests? ([Y]es or [N]):\n'
        '{} Y or N > {}'.format(GREEN, YELLOW, CLOSE_COLOR))
    if statement.lower() == 'yes' or statement.lower() == 'y':
        return True
    elif statement.lower() == 'no' or statement.lower() == 'n':
        return False
    else:
        return continue_statement()


def main():
    err = False
    mode = 'OPT'
    while True:
        # input = input(f'{GREEN} [*] Enter a \"Google Play URL\" or \"APP Code\":\n {YELLOW}> {CLOSE_COLOR}')
        if err:
            service_number = cursor(mode)
        else:
            service_number = input(
                '\n{} [*] Enter a number:\n'
                '       1. View database\n'
                '       2. Add an item\n'
                '       3. Edit an item\n'
                '       4. Delete an item\n'
                '       5. Exit\n{} {} > {}'.format(GREEN, YELLOW, mode, CLOSE_COLOR))
        if service_number is '1':
            cmd_view()
        elif service_number is '2':
            cmd_add()
        elif service_number is '3':
            cmd_edit()
        elif service_number is '4':
            cmd_delete()
        elif service_number is '5':
            break
        else:
            back_line()
            print('{} [!] Please choose among one of the options!{}'.format(RED, CLOSE_COLOR))
            err = True
            continue

        err = False

        if True:
            # print(f'\n{GREEN} [*] The download successfully performed and stored in the "file" folder. Enjoy :){CLOSE_COLOR}')
            statement = continue_statement()
            if statement: continue
            else: break
        else:
            print('\n{} [!] There is a problem for download.{}'.format(GREEN, CLOSE_COLOR))
            statement = continue_statement()
            if statement: continue
            else: break
    
    print('\n{} [*] Safely exited :){}\n'.format(GREEN, CLOSE_COLOR))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\n\n{} [!] Force exited :< {}\n'.format(RED, CLOSE_COLOR))


"""
except requests.exceptions.ConnectionError:
    print(f'\n{RED} [!] No Connection.{CLOSE_COLOR}')
except TypeError:
    print(f'\n{RED} [!] App/Game not found.\n [!] Try again later.{CLOSE_COLOR}')
except:
    print(f'\n{RED} [!] There\'s a problem.\n [!] Try another website.{CLOSE_COLOR}')
"""
