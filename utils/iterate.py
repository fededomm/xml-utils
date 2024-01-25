def iterate_n_check(parent_tags, child_tag, multiple_child_count, num_of_requested_child) -> int:
    for parent in parent_tags:
        child_tags = parent.find_all(child_tag)
        if len(child_tags) > num_of_requested_child:
            multiple_child_count += 1
    return multiple_child_count

def iterate_n_check_equals(parent_tags, child_tag, multiple_child_count, num_of_requested_child) -> int:
    for parent in parent_tags:
        child_tags = parent.find_all(child_tag)
        if len(child_tags) == num_of_requested_child:
            multiple_child_count += 1
    return multiple_child_count