from mininet.topo import Topo

class MyTopo(Topo):

    def build(self):
        leftHost = self.addHost('h1')
        rightHost = self.addHost('h2')
        leftSwitch = self.addSwitch('s3')
        rightSwitch = self.addSwitch('s4')

        self.addLink(leftHost, leftSwitch)
        self.addLink(leftSwitch, rightSwitch)
        self.addLink(rightHost, rightSwitch)

topos = {'mytopo': (lambda: MyTopo())}