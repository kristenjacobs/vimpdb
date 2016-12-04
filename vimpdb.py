import os
import commands


g_checked = False
g_enabled = False
g_last_linenumber = -1
g_last_filename = ""


def enabled():
    global g_checked
    global g_enabled
    if not g_checked:
        _, output = commands.getstatusoutput('vim --serverlist')
        for line in output.split("\n"):
            if line == "VIMPDB":
                g_enabled = True
        g_checked = True
    return g_enabled


def sendCommand(command):
    os.system("vim --servername VIMPDB --remote-send " +
              "'<Esc>:windo if winnr() == 1 | " + command +
              " | endif | startinsert<Enter>'")


def update_file(filename):
    global g_last_filename
    if filename != g_last_filename:
        sendCommand("e " + filename)
        g_last_filename = filename
        g_last_linenumber = -1


def update_line(linenumber):
    global g_last_linenumber
    if linenumber != g_last_linenumber:
        sendCommand(str(linenumber))
        g_last_linenumber = linenumber


def update(self):
    if enabled():
        frame, linenumber = self.stack[self.curindex]
        filename = self.canonic(frame.f_code.co_filename)
        update_file(filename)
        update_line(linenumber)


def preloop(self):
    update(self)


def precmd(self, line):
    update(self)
    return line


def postcmd(self, stop, line):
    if self.lastcmd == "quit" or \
       self.lastcmd == "q" or \
       self.lastcmd == "exit":
        if enabled():
            sendCommand("x")
    return True
