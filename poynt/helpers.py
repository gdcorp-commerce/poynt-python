def json_patch(from_obj, to_obj, ignore_keys=None, only_keys=None, no_remove=False):
    """
    Creates a JSON patch diff between two objects.

    Arguments:
    from_obj (dict): from object, usually the existing object returned by API
    to_obj (dict): to object, usually the new object to return

    Keyword arguments:
    ignore_keys (list of str, optional): whether to ignore any keys (e.g. not patch them)
    only_keys (list of str, optional): only patch keys from this whitelist
    no_remove (bool, optional): don't remove any keys when patching (in case you forgot
                                to specify certain keys in the object)
    """

    ops = []

    for key in to_obj:
        # filter keys based on ignore_keys, only_keys
        if ignore_keys is not None and key in ignore_keys:
            continue
        if only_keys is not None and key not in only_keys:
            continue

        # when key is not in from but in to, use add op
        if key not in from_obj or from_obj[key] is None:
            ops.append({
                'op': 'add',
                'path': '/%s' % key,
                'value': to_obj[key]
            })
        elif from_obj[key] != to_obj[key]:
            ops.append({
                'op': 'replace',
                'path': '/%s' % key,
                'value': to_obj[key]
            })

    if no_remove is False:
        for key in from_obj:
            # filter keys based on ignore_keys, only_keys
            if ignore_keys is not None and key in ignore_keys:
                continue
            if only_keys is not None and key not in only_keys:
                continue

            # when key is in from and not in to, use remove op
            if key not in to_obj or to_obj[key] is None:
                ops.append({
                    'op': 'remove',
                    'path': '/%s' % key
                })

    return ops
