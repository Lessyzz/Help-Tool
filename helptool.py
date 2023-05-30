class HelpTool():
    def __init__(self):
        self.tools = """
1) Port scan
2) Directory search
3) SSH Login
4) Search explit
5) Exit
"""

        self.portScan = """
Port scan tools: nmap 
nmap usage: nmap <paramaters> <website address or ip address>  |  nmap -sS -sV 127.0.0.1
"""

        self.directorySearch = """
Directory search tools: dirb, gobuster, dirsearcher (https://github.com/Lessyzz/Directory-Searcher)

dirb usage: dirb <ip address> <wordlist>  |  dirb http://127.0.0.1/ /usr/share/wordlists/dirb/common.txt

gobuster usage: gobuster -e -u http://127.0.0.1/ -w /usr/share/wordlists/dirb/common.txt

dirsearcher usage: dirsearcher.py -u <url> -t <threads> -w <wordlist>
"""

        self.sshLogin = """
SSH Login tools: ssh
ssh usage: ssh <Username>@<Server IP>  |  ssh lessy@127.0.0.1
"""

        self.searchExploit = """
Search exploit tools: searchsploit 
searchsploit usage: searchsploit apache 2.4.49
Also you need to update searchsploit, for update > searchsploit -u
"""

        self.run()

    def getInput(self):
        number = input("> ")

        match number:
            case "1":
                print(self.portScan)
            case "2":
                print(self.directorySearch)
            case "3":
                print(self.sshLogin)
            case "4":
                print(self.searchExploit)
            case "5":  
                exit()


    def run(self):
        while True:
            print(self.tools)
            self.getInput()


HelpToolRun = HelpTool()
