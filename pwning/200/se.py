import angr

get_flag_func = 0x403a23
goodbye_func = 0x4051f1

b = angr.Project('./FUck_binary')
state = b.factory.entry_state()
path_group = b.factory.path_group(state)
path_group.explore(find=get_flag_func, avoid=goodbye_func)

# get all paths that're stored at the <found> stash
for path in path_group.found:
    #'''
    num_constraints = len(path.state.se.constraints)
    for i in range(0, num_constraints):
        print "input: ",
        print repr(path.state.posix.dumps(i))
    #'''
    #print repr(path.state.se.any_str())
