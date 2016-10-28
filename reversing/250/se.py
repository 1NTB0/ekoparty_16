import angr, simuvex

b = angr.Project('./PFUck_binary', load_options={"auto_load_libs": False})
state = b.factory.blank_state(addr=0x0400c05)
#'''
states = [state]
while len(states) > 0:
    successors = []
    for state in states:
        successors.extend(b.factory.sim_run(state).all_successors)
    states = successors
    print states
#'''

print "Done"
