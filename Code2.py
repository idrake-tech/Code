
from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        Topo.__init__( self )
	# add host
        h1 = self.addHost('h1')
	h2 = self.addHost('h2')
	h3 = self.addHost('h3')

	# add switch
        s1 = self.addSwitch('s1')
	s2 = self.addSwitch('s2')
	s3 = self.addSwitch('s3')

	# add connection
        self.addLink(s1, s2)
        self.addLink(s3, s2)
	self.addLink(s3, s1)
	
	self.addLink(s1, h1)
	self.addLink(s2, h2)
	self.addLink(s3, h3)


	# sudo mn --controller=remote,ip=127.0.0.1,port=6653 --custom code2.py --topo tp

topos = { 'tp': ( lambda: MyTopo() ) }