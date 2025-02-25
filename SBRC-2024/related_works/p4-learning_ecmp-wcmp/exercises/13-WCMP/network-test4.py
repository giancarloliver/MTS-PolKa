from p4utils.mininetlib.network_API import NetworkAPI
from mininet.log import setLogLevel
from mininet.cli import CLI
from time import sleep

net = NetworkAPI()

edges = []
hosts = []

BW = 10
BWE = 100

# Network general options
net.setLogLevel('info')

# Network definition
net.addP4Switch('s1_0', cli_input='sw-commands/s1_0-commands.txt')
net.addP4Switch('s2_0', cli_input='sw-commands/s2_0-commands.txt')
net.addP4Switch('s2_1', cli_input='sw-commands/s2_1-commands.txt')
net.addP4Switch('s2_2', cli_input='sw-commands/s2_2-commands.txt')
net.addP4Switch('s2_3', cli_input='sw-commands/s2_3-commands.txt')
net.addP4Switch('s2_4', cli_input='sw-commands/s2_4-commands.txt')
net.addP4Switch('s1_1', cli_input='sw-commands/s1_1-commands.txt')
net.addP4Switch('e1', cli_input='sw-commands/e1-commands.txt')
net.addP4Switch('e2', cli_input='sw-commands/e2-commands.txt')
net.addP4Switch('e3', cli_input='sw-commands/e3-commands.txt')
net.addP4Switch('e4', cli_input='sw-commands/e4-commands.txt')
net.addP4Switch('e5', cli_input='sw-commands/e5-commands.txt')
net.setP4SourceAll('p4src/wcmp.p4')


net.addHost('h1')
net.addHost('h2')
net.addHost('h3')
net.addHost('h4')
net.addHost('h5')

# Conexões entre switches e hosts
net.addLink("h1", "e1", port2=1, bw=BWE)
net.addLink("e1", "s1_0", port1=2, bw=BWE)
net.addLink("h3", "e3", port2=1, bw=BWE)
net.addLink("e3", "s1_0", port1=2, bw=BWE)

net.addLink("h2", "e2", port2=1, bw=BWE)
net.addLink("e2", "s1_1", port1=2, bw=BWE)
net.addLink("h4", "e4", port2=1, bw=BWE)
net.addLink("e4", "s1_1", port1=2, bw=BWE)
net.addLink("h5", "e5", port2=1, bw=BWE)
net.addLink("e5", "s1_1", port1=2, bw=BWE)


# Conexões entre switches s1_0 e s2_0
net.addLink("s1_0", "s2_0", port1=3, bw=BW)
net.addLink("s1_0", "s2_0", port1=4, bw=BW)

# Conexões entre switches
net.addLink("s1_0", "s2_1", bw=BW)
net.addLink("s1_0", "s2_2", bw=BW)
net.addLink("s1_0", "s2_3", bw=BW)
net.addLink("s1_0", "s2_4", bw=BW)
net.addLink("s2_0", "s1_1", bw=BW)
net.addLink("s2_1", "s1_1", bw=BW)
net.addLink("s2_2", "s1_1", bw=BW)
net.addLink("s2_3", "s1_1", bw=BW)
net.addLink("s2_4", "s1_1", bw=BW)

# Assignment strategy
net.mixed()

# Nodes general options
net.enablePcapDumpAll()
net.enableLogAll()
net.enableCli()
net.startNetwork()

    