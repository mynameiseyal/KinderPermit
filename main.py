from sel import Selenium

sel = Selenium()

if __name__ == '__main__':
    sel.launch_chrome()
    sel.go_to_decleration_page()
    sel.login(username='', password='')
    a = 'wait'