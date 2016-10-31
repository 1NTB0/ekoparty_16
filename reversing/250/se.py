import angr

get_flag_func = 0x403a23
goodbye_func = 0x4051f1

b = angr.Project('./FUck_binary')
state = b.factory.entry_state()
path_group = b.factory.path_group(state)
path_group.explore(find=get_flag_func, avoid=goodbye_func)

# get all paths that're stored at the <found> stash
for path in path_group.found:
    num_constraints = len(path.state.se.constraints)
    print "num constraints to solve in this path: " + str(num_constraints)
    print "input: ",
    print repr(path.state.posix.dumps(0))
    print "output: ",
    print repr(path.state.posix.dumps(1))
    
    # used when there's a specific filter in the results that you want to apply in angr's path state
    #print repr(path.state.se.any_str())
