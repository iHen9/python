# -*- coding: utf-8 -*-


def get_json_value(key, json, is_all=False, result_list=None):
    """
    Get the associated value according to the given key
    :return:None、value:str or result_list:list
    """
    if not result_list:
        result_list = []
    if type(json) == dict:
        for k, v in json.items():
            if k == key:
                if not is_all:
                    return v
                else:
                    result_list.append(v)
            else:
                value = get_json_value(key, v, is_all=is_all, result_list=result_list)
                if value is not None:
                    if not is_all:
                        return value
                    else:
                        result_list = value
    if type(json) == list:
        for i in json:
            value = get_json_value(key, i, is_all=is_all, result_list=result_list)
            if value is not None:
                if not is_all:
                    return value
                else:
                    result_list = value
    if is_all:
        return result_list


def execute():
    t1 = {'a': 13}
    t2 = {'b': 32}
    t3 = [t1]
    t4 = [t2, t1]
    t5 = [{'b': [t1, t2, t1]},t1]
    for i in (t1, t2, t3, t4, t5):
        print(get_json_value('a', i), get_json_value('a', i, True))


if __name__ == '__main__':
    execute()
