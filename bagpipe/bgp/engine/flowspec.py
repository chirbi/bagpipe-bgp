from exabgp.bgp.message.update.nlri.flow import Flow as ExaBGPFlow
from exabgp.bgp.message.update.nlri.nlri import NLRI

from exabgp.reactor.protocol import AFI
from exabgp.reactor.protocol import SAFI


@NLRI.register(AFI.ipv4, SAFI.flow_vpn, force=True)
@NLRI.register(AFI.ipv6, SAFI.flow_vpn, force=True)
class Flow(ExaBGPFlow):
    '''This wraps an ExaBGP Flow so that __eq__ and __hash__
    meet the criteria for RouteTableManager (in particular,
    not look at actions and nexthop)
    '''

    def __eq__(self, other):
        return self.pack() == other.pack()

    def __hash__(self):
        return hash(self.pack())

    def __repr__(self):
        return str(self)


def FlowRouteFactory(afi, rd):
    flow_route = Flow(afi, safi=SAFI.flow_vpn)
    flow_route.rd = rd
    return flow_route