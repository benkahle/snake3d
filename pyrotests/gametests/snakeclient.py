from visual import *
import time
import Pyro4

def main():
    border = curve(pos=[(-100,-100),(100,-100),(100,100),(-100,100),(-100,-100)])
    Pyro4.config.HOST=('192.168.134.147')
    daemon=Pyro4.Daemon()
    ns=Pyro4.locateNS()
    player = Pyro4.Proxy("PYRONAME:Snake3d.player1.snake")
    player.check_dir()
    daemon.requestLoop()


main()