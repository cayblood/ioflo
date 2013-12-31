""" cloning.py framer cloning behaviors


"""
#print "module %s" % __name__

from collections import deque
from ....base.globaling import *

from ....base import aiding
from ....base import storing 
from ....base import deeding
from ....base import framing

from ....base.consoling import getConsole
console = getConsole()


def CreateInstances(store):
    """ Create action instances. Recreate with each new house after clear registry
        
        init protocol:  inode  and (ipath, ival, iown)
    """
    ClonerFramer(name='clonerFramer', store=store).ioinit.update(
        index=('index', 0, True))
    
    ClonerFramer(name='framerCloner', store=store).ioinit.update(
        index=('index', 0, True))
    
class ClonerFramer(deeding.ParamDeed):
    """ CloneDeed creates a new aux framer as clone of given framer and adds
        it to the auxes of a given frame. Default is current frame.
        
        Since it is a ParamDeed is does not create instance variables for its
        ioinits
        
        inherited attributes
            .name is actor name string
            .store is data store ref
            .ioinit is dict of ioinit data for initio
            ._parametric is flag for initio to not create attributes

    """
    def __init__(self, **kw):
        """Initialize Instance """
        if 'preface' not in kw:
            kw['preface'] = 'ClonerFramer'

        #call super class method
        super(ClonerFramer,self).__init__(**kw)
    
    def cloneParms(self, parms, cloneds, **kw):
        """ Returns parms fixed up for framing cloning. This includes:
            Reverting any Frame links to name strings,
            Reverting non cloned Framer links into name strings
            Replacing any cloned framer links with the cloned name strings from cloneds
            Replacing any parms that are acts, in this case the needs with clones.
        """
        parms = super(ClonerFramer,self).cloneParms(parms, cloneds, **kw)
        
        framer = parms.get('framer')
        frame = parms.get('frame')
        
        if isinstance(framer, framing.Framer):
            if framer.name in cloneds:
                parms['framer'] = cloneds[framer.name]
            else:
                parms['framer'] = framer.name # revert to name
        elif framer: # assume namestring
            if framer in cloneds:
                parms['framer'] = cloneds[framer]

        if isinstance(frame, framing.Frame):
            parms['frame'] = frame.name # revert to name        
        
        return parms
           
    def resolveLinks(self, framer, frame, **kw):
        """ Resolves value (tasker) link that is passed in as parm
            resolved link is passed back to act to store in parms
            since framer may not be current framer at build time
        """
        parms = {}
        parms['framer'] = framing.resolveFramer(framer, who=self.name)
        parms['frame'] = framing.resolveFrame(frame, who=self.name)
        
        return parms
        
    def action(self, framer, frame, name='', index=None, **kw):
        """ Clone framer onto new aux framer named name and assign to frame frame
            If name is empty then create name from framer.name + suffix counter
        """
        if not name and index:
            name = "{0}_{1:d}".format(framer.name, index.value)
            index.value += 1
        
        # if name is empty then a unique name will be created by the registry
        clone = self.store.house.cloneFramer(framer, name)
        frame.addAux(clone)
        
        return None    

def Test():
    """Module Common self test

    """
    pass


if __name__ == "__main__":
    Test()
